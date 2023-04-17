import { Box, Card, CardBody, Stack, Divider, Text, Heading } from '@chakra-ui/react'
import Head from "next/head";
import ResultsLayout from '@/components/results/ResultsLayout';
import DataTable from '@/components/results/DataTable'
import theme from '@/styles/theme';
import { Actions } from '@/components/results/filters/Actions';
import { WeightSlider } from '@/components/results/filters/WeightSlider';
import { Descriptors } from '@/components/results/filters/Descriptors';
import { actionsData } from '@/components/data/FetchActionsData';
import { ResultsSidebar } from '@/components/results/ResultsSidebar';
import { events } from '@/components/data/FetchAdverseEventData';

const checkboxData = [
  {
    name: 'Gene',
  },
  {
    name: 'Protein'
  },
  {
    name: 'GWAS'
  },
  {
    name: 'Phenotype'
  },
  {
    name: 'Reactome'
  },
  {
    name: 'Signor'
  },
  {
    name: 'IntAct'    
  }
]

const columns = [
  {
    id: 1,
    name: 'Adverse Event'
  }, 
  {
    id: 2,
    name: 'Associated Drugs'
  }, 
  {
    id: 3,
    name: 'Weights'
  },
  {
    id: 4,
    name: 'Dataset'
  }
]


export default function TargetToAEResults() {
 return (
      <ResultsLayout>
        <Head>
          <title>Adverse Events to Target Results</title>
        </Head>
        <Box display='flex' w="100%">
      
        <Box w="25%" minW='250px'>
        <ResultsSidebar>
            <Divider />
            <Descriptors 
              title = 'Descriptors'
              checkboxArray = {checkboxData} />
            <Divider />
            <Actions 
              title = 'Actions'
              checkboxArray = {actionsData} />
            <Divider />
            <WeightSlider
              title='Adverse Event Name'
              range={{min: '0', mid: '50', max: '100'}} 
              initial={{ min: '25', max: '75'}}/>
          </ResultsSidebar>
        </Box>
        <Box p={5} w="75%" bg="#eee">

          {/* Search Page Heading */}
          <Heading size='md' mb={4}>Adverse Event to Target Results</Heading>
          {/* Search Input Display */}
          <Box display='flex' alignItems='center' justifyContent='space-between' mb='5'>
            <Box w="100%" bg="#eee">  
            <Card>
              <CardBody>
                <Stack spacing='3'>
                  <Heading size='lg' color={theme.brand.color}>Input: Parkinson's Disease</Heading>
                    <Divider />
                    <Heading size='sm'>Description</Heading>
                  <Text>
                  A progressive degenerative disorder of the central nervous system characterized by loss of dopamine producing neurons in the substantia nigra and the presence of Lewy bodies in the substantia nigra and locus coeruleus. Signs and symptoms include tremor which is most pronounced during rest, muscle rigidity, slowing of the voluntary movements, a tendency to fall back, and a mask-like facial expression.
                  </Text>
                    <Divider />
                  <Text color='gray' fontSize='sm'>
                  EFO: MONDO_0005180| MeSH: D010300 | Orphanet: 319705 | UMLS: C0030567 | NCIt: C26845
                  </Text>
                </Stack>
              </CardBody>
            </Card>
            </Box>
          </Box>
          {/* Search Results Table */}
          <Box w='100%' mb='5'>
          <DataTable
          title="Targets from Adverse Event" 
          columns={columns}
          data={events}
          />
          </Box>
        </Box>
        </Box>
      </ResultsLayout>
        
 );
}