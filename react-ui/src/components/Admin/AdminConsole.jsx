import React, { useState, useEffect } from 'react';
import { fetchScenarios, fetchCards, fetchNews, fetchBills, fetchFactions, apiPost, apiPut, apiDelete } from '../../api/apiClient';

export default function AdminConsole() {
  const [activeTab, setActiveTab] = useState('SCENARIOS');
  
  const [data, setData] = useState([]);
  const [filterKey, setFilterKey] = useState('west_bengal_2000');
  const [loading, setLoading] = useState(false);
  const [expandedItemId, setExpandedItemId] = useState(null);

  // Draft states for inline editing
  const [editJson, setEditJson] = useState('');

  useEffect(() => {
    loadData();
  }, [activeTab, filterKey]);

  const loadData = async () => {
    setLoading(true);
    setExpandedItemId(null);
    try {
      let resData = [];
      if (activeTab === 'SCENARIOS') resData = await fetchScenarios();
      if (activeTab === 'CARDS') resData = await fetchCards(filterKey);
      if (activeTab === 'NEWS') resData = await fetchNews(filterKey);
      if (activeTab === 'BILLS') resData = await fetchBills(filterKey);
      if (activeTab === 'FACTIONS') resData = await fetchFactions();
      setData(resData);
    } catch (err) {
      console.error(err);
      alert('Failed to fetch data for ' + activeTab);
    } finally {
      setLoading(false);
    }
  };

  const getPath = () => {
    if (activeTab === 'SCENARIOS') return '/api/admin/scenarios';
    if (activeTab === 'CARDS') return '/api/admin/cards';
    if (activeTab === 'NEWS') return '/api/admin/news';
    if (activeTab === 'BILLS') return '/api/admin/bills';
    if (activeTab === 'FACTIONS') return '/api/admin/factions';
    return '';
  };

  const handleSaveEdit = async (item) => {
    try {
      const parsed = JSON.parse(editJson);
      await apiPut(`${getPath()}/${item.id}`, parsed);
      alert('Successfully saved!');
      loadData();
    } catch (err) {
      alert('Invalid JSON or Server Error: ' + err.message);
    }
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Are you sure you want to permanently delete this item?')) return;
    try {
      await apiDelete(`${getPath()}/${id}`);
      alert('Deleted.');
      loadData();
    } catch (err) {
      alert('Delete failed: ' + err.message);
    }
  };

  const handleReloadCache = async () => {
    setLoading(true);
    try {
      await apiPost('/api/admin/cache/reload', {});
      alert('Backend static caches reloaded successfully!');
    } catch (err) {
      console.error(err);
      alert('Failed to reload cache: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  const renderTabs = () => (
    <div style={{ display: 'flex', justifyContent: 'space-between', gap: '15px', marginBottom: '20px', flexWrap: 'wrap' }}>
      <div style={{ display: 'flex', gap: '10px', flex: '1 1 auto' }}>
        {['SCENARIOS', 'CARDS', 'NEWS', 'BILLS', 'FACTIONS'].map(tab => (
          <button
            key={tab}
            className={activeTab === tab ? 'selected' : ''}
            onClick={() => setActiveTab(tab)}
            style={{ padding: '10px 20px', fontWeight: 'bold' }}
          >
            {tab}
          </button>
        ))}
      </div>
      <button 
        onClick={handleReloadCache} 
        disabled={loading}
        style={{ backgroundColor: '#10b981', borderColor: '#10b981', color: '#fff', fontWeight: 'bold', padding: '10px 20px' }}
      >
        {loading ? 'Reloading...' : '🔄 Reload Static Caches'}
      </button>
    </div>
  );

  const renderJsonMaintenanceList = () => {
    if (loading) return <p>Loading...</p>;
    if (data.length === 0) return <p>No items found.</p>;

    return data.map(item => {
      const label = item.name || item.title || item.scenarioKey || item.id;
      const isExpanded = expandedItemId === item.id;

      return (
        <div key={item.id} style={{ border: '1px solid var(--primary-border)', padding: '15px', borderRadius: '8px', marginBottom: '10px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', cursor: 'pointer' }} onClick={() => {
            if (isExpanded) {
              setExpandedItemId(null);
            } else {
              setExpandedItemId(item.id);
              setEditJson(JSON.stringify(item, null, 2));
            }
          }}>
            <h4 style={{ margin: 0 }}>{label} | <span style={{ fontSize: '10px', color: 'gray' }}>{item.id}</span></h4>
            <span>{isExpanded ? '▼' : '▶'}</span>
          </div>
          
          {isExpanded && (
            <div style={{ marginTop: '15px' }}>
              <textarea 
                style={{ width: '100%', height: '300px', backgroundColor: 'var(--primary-dark)', color: '#ffffff', border: '1.5px solid var(--primary-border)', borderRadius: '4px', padding: '10px', fontFamily: 'monospace' }}
                value={editJson}
                onChange={(e) => setEditJson(e.target.value)}
              />
              <div style={{ display: 'flex', gap: '10px', marginTop: '10px' }}>
                <button onClick={() => handleSaveEdit(item)}>Save Changes</button>
                <button onClick={() => handleDelete(item.id)} style={{ backgroundColor: '#be123c', borderColor: '#be123c' }}>Delete</button>
              </div>
            </div>
          )}
        </div>
      );
    });
  };

  const renderFilterInput = () => {
    if (activeTab === 'SCENARIOS' || activeTab === 'FACTIONS') return null;
    return (
      <div style={{ marginBottom: '20px' }}>
        <label style={{ fontWeight: 'bold', display: 'block', marginBottom: '5px' }}>Filter by Scenario Key</label>
        <div style={{ display: 'flex', gap: '10px' }}>
          <input 
            type="text" 
            value={filterKey} 
            onChange={(e) => setFilterKey(e.target.value)} 
          />
        </div>
      </div>
    );
  };

  // For this MVP port, the create forms just provide a raw blank JSON template to post.
  // This avoids building massive multi-field forms and relies on the exact JSON schema.
  const CreateTemplate = ({ defaultJson }) => {
    const [createJson, setCreateJson] = useState(JSON.stringify(defaultJson, null, 2));

    const handleCreate = async () => {
      try {
        const parsed = JSON.parse(createJson);
        await apiPost(getPath(), parsed);
        alert('Created successfully!');
        loadData();
      } catch (err) {
        alert('Invalid JSON or Server Error: ' + err.message);
      }
    };

    return (
      <div className="unified-card" style={{ marginBottom: '30px' }}>
        <h3 style={{ marginTop: 0 }}>Create New {activeTab.toLowerCase()} (JSON)</h3>
        <textarea 
          style={{ width: '100%', height: '250px', backgroundColor: 'var(--primary-dark)', color: '#ffffff', border: '1.5px solid var(--primary-border)', borderRadius: '4px', padding: '10px', fontFamily: 'monospace' }}
          value={createJson}
          onChange={(e) => setCreateJson(e.target.value)}
        />
        <button style={{ marginTop: '10px' }} onClick={handleCreate}>Submit POST</button>
      </div>
    );
  };

  return (
    <div>
      <div style={{
        background: 'var(--primary-border)',
        padding: '30px',
        borderRadius: '16px',
        border: '2px solid var(--primary-dark)',
        marginBottom: '25px',
        textAlign: 'center',
        color: '#ffffff',
        boxShadow: '0 10px 30px rgba(33,60,81,0.1)'
      }}>
        <h1 style={{ fontSize: '36px', fontWeight: 900, margin: 0, letterSpacing: '-0.02em', color: '#ffffff' }}>
          Admin Rule Editor
        </h1>
        <p style={{ fontSize: '15px', marginTop: '8px', opacity: 0.95, color: '#ffffff' }}>
          Maintain scenario rules, cards, news, and legislative bills directly in JSON format.
        </p>
      </div>

      {renderTabs()}
      
      {activeTab === 'SCENARIOS' && <CreateTemplate defaultJson={{ scenarioKey: 'new_scenario', active: true }} />}
      {activeTab === 'CARDS' && <CreateTemplate defaultJson={{ scenarioKey: filterKey, cardKey: 'new_card', cost: 1, active: true }} />}
      {activeTab === 'NEWS' && <CreateTemplate defaultJson={{ scenarioKey: filterKey, newsKey: 'new_news', active: true }} />}
      {activeTab === 'BILLS' && <CreateTemplate defaultJson={{ scenarioKey: filterKey, billKey: 'new_bill', proposingRole: 'GOVERNMENT', pointsPassed: 10, pointsFailed: -5, effectsPassed: {}, effectsFailed: {}, active: true }} />}
      {activeTab === 'FACTIONS' && <CreateTemplate defaultJson={{ scenarioKey: 'default', factionKey: 'new_faction', name: 'New Faction Name', startingLoyalty: 70, startingInfluence: 30, satisfiedEffects: {}, rebelliousEffects: {} }} />}

      <hr style={{ margin: '30px 0', borderColor: 'var(--primary-border)', opacity: 0.3 }} />
      
      <h3 style={{ marginTop: 0 }}>Existing {activeTab.toLowerCase()}</h3>
      {renderFilterInput()}
      {renderJsonMaintenanceList()}
    </div>
  );
}
