import { useState } from 'react';

const JobSearchService = () => {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  const apiUrl = 'http://127.0.0.1:5000/api/search';

  const fetchData = async (data) => {
    try {
      const response = await fetch(apiUrl, {
        method: "POST",
        cache: "no-cache",
        headers: {
          "Content-Type": "application/json",
          // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        referrerPolicy: "no-referrer",
        body: JSON.stringify(data),
      });
      if (!response.ok) {
        throw new Error('Failed to fetch data');
      }
      const jsonData = await response.json();
      setData(jsonData);
      setError(null);
      console.log(jsonData)
      return jsonData
    } catch (error) {
      setError(error.message);
      setData(null);
      return null;
    }
  };

  return { data, error, fetchData };
};

export default JobSearchService;
