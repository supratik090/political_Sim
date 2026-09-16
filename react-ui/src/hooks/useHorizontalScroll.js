import { useRef, useEffect } from 'react';

/**
 * Reusable hook to enable mouse click-and-drag horizontal scrolling
 * as well as mouse wheel vertical-to-horizontal scrolling for web users.
 */
export function useHorizontalScroll() {
  const elRef = useRef(null);

  useEffect(() => {
    const el = elRef.current;
    if (!el) return;

    let isDown = false;
    let startX = 0;
    let scrollLeft = 0;
    let isDraggingMoved = false;

    const handleMouseDown = (e) => {
      if (e.button !== 0) return;
      isDown = true;
      isDraggingMoved = false;
      startX = e.pageX - el.offsetLeft;
      scrollLeft = el.scrollLeft;
      el.style.cursor = 'grabbing';
      el.style.userSelect = 'none';
    };

    const handleMouseLeave = () => {
      if (!isDown) return;
      isDown = false;
      el.style.cursor = '';
      el.style.userSelect = '';
    };

    const handleMouseUp = () => {
      if (!isDown) return;
      isDown = false;
      el.style.cursor = '';
      el.style.userSelect = '';
    };

    const handleMouseMove = (e) => {
      if (!isDown) return;
      const x = e.pageX - el.offsetLeft;
      const walk = (x - startX) * 1.5;
      if (Math.abs(walk) > 4) {
        isDraggingMoved = true;
      }
      el.scrollLeft = scrollLeft - walk;
    };

    const handleWheel = (e) => {
      if (e.deltaY !== 0 && el.scrollWidth > el.clientWidth) {
        // Translate vertical wheel scroll into horizontal container scroll
        e.preventDefault();
        el.scrollLeft += e.deltaY;
      }
    };

    const handleClickCapture = (e) => {
      if (isDraggingMoved) {
        e.stopPropagation();
        e.preventDefault();
        isDraggingMoved = false;
      }
    };

    el.addEventListener('mousedown', handleMouseDown);
    el.addEventListener('mouseleave', handleMouseLeave);
    el.addEventListener('mouseup', handleMouseUp);
    el.addEventListener('mousemove', handleMouseMove);
    el.addEventListener('wheel', handleWheel, { passive: false });
    el.addEventListener('click', handleClickCapture, true);

    return () => {
      el.removeEventListener('mousedown', handleMouseDown);
      el.removeEventListener('mouseleave', handleMouseLeave);
      el.removeEventListener('mouseup', handleMouseUp);
      el.removeEventListener('mousemove', handleMouseMove);
      el.removeEventListener('wheel', handleWheel);
      el.removeEventListener('click', handleClickCapture, true);
    };
  }, []);

  return elRef;
}
