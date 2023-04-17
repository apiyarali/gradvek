// Search by Target to Adverse Event
// Data of Interest: https://platform.opentargets.org/target/ENSG00000151577
import { TabPanel, Flex, Text, Center, Button } from '@chakra-ui/react'
import React, { useState } from 'react';
import { AsyncTypeahead } from 'react-bootstrap-typeahead';
import styles from "../../styles/Search.module.css"
import Link from 'next/link';
import theme from '@/styles/theme';

// Typeahead URI - DJANGO BACKEND
const SEARCH_URI = 'http://localhost:8000/api/targets'

// Typeahead Async Search
function TargetToAESearch() {
  const [isLoading, setIsLoading] = useState(false);
  const [options, setOptions] = useState([]);
  const [selectedTypeAhead, setSelectedTypeAhead] = useState([]);

      const handleSearch = (query: string) => {
        setIsLoading(true);
        
        fetch(`${SEARCH_URI}`)
        .then((resp) => resp.json())
        .then((items) => {
          setOptions(items);
          setIsLoading(false);
        });
      };

      const handleChange = (selectedOptions) => {
        setSelectedTypeAhead(selectedOptions);
      };

      const filterByFields = ['name', 'description'];


      return (
        <TabPanel className={styles.searchInput}>
          <Text mb="4">Find adverse events that include this target</Text>
        <AsyncTypeahead
          filterBy={filterByFields}
          id="target-to-ae-search"
          isLoading={isLoading}
          labelKey="name"
          minLength={2}
          onSearch={handleSearch}
          options={options}
          maxResults={25}
          placeholder="Search for a Target..."
          onChange={handleChange}
          inputProps={{ autoComplete: "off"}}
          renderMenuItemChildren={(target) => (
            <>
              <Flex direction={"row"} className={styles.results}>
                <Text fontWeight="bold" className="target-name">
                  {target["name"]}
                </Text>
                <Text ml={"1"} className="target-description">
                  {target["description"]}
                </Text>
              </Flex>
            </>
          )}
        />
        <Center>
          <Button size="lg" bg={theme.brand.secondary} color="white" mt="5"><Link href="/adverseEvents">Search</Link></Button>
        </Center>
        </TabPanel>
      );
    };
export default TargetToAESearch;
