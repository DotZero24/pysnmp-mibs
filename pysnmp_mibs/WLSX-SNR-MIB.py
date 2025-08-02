_G='monitoredStaPhyAddress'
_F='monitoredApBSSID'
_E='monRadioNumber'
_D='monPhyAddress'
_C='WLSX-MON-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wlsxEnterpriseMibModules,=mibBuilder.importSymbols('ARUBA-MIB','wlsxEnterpriseMibModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','snmpModules')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TAddress,TDomain,TextualConvention,TestAndIncr,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','StorageType','TAddress','TDomain','TextualConvention','TestAndIncr','TimeInterval','TruthValue')
monPhyAddress,monRadioNumber,monitoredApBSSID,monitoredStaPhyAddress=mibBuilder.importSymbols(_C,_D,_E,_F,_G)
wlsxSNRMIB=ModuleIdentity((1,3,6,1,4,1,14823,2,2,1,7))
if mibBuilder.loadTexts:wlsxSNRMIB.setRevisions(('2020-08-14 17:45',))
_WlsxSNRGroup_ObjectIdentity=ObjectIdentity
wlsxSNRGroup=_WlsxSNRGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,7,1))
_WlsxAPSnrTable_Object=MibTable
wlsxAPSnrTable=_WlsxAPSnrTable_Object((1,3,6,1,4,1,14823,2,2,1,7,1,1))
if mibBuilder.loadTexts:wlsxAPSnrTable.setStatus(_A)
_WlsxAPSnrEntry_Object=MibTableRow
wlsxAPSnrEntry=_WlsxAPSnrEntry_Object((1,3,6,1,4,1,14823,2,2,1,7,1,1,1))
wlsxAPSnrEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:wlsxAPSnrEntry.setStatus(_A)
_ApSnrAverageSignalStrength_Type=Integer32
_ApSnrAverageSignalStrength_Object=MibTableColumn
apSnrAverageSignalStrength=_ApSnrAverageSignalStrength_Object((1,3,6,1,4,1,14823,2,2,1,7,1,1,1,1),_ApSnrAverageSignalStrength_Type())
apSnrAverageSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:apSnrAverageSignalStrength.setStatus(_A)
_ApSnrSignalPkts_Type=Integer32
_ApSnrSignalPkts_Object=MibTableColumn
apSnrSignalPkts=_ApSnrSignalPkts_Object((1,3,6,1,4,1,14823,2,2,1,7,1,1,1,2),_ApSnrSignalPkts_Type())
apSnrSignalPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apSnrSignalPkts.setStatus(_A)
_ApSnrHighestRxSignalStrength_Type=Integer32
_ApSnrHighestRxSignalStrength_Object=MibTableColumn
apSnrHighestRxSignalStrength=_ApSnrHighestRxSignalStrength_Object((1,3,6,1,4,1,14823,2,2,1,7,1,1,1,3),_ApSnrHighestRxSignalStrength_Type())
apSnrHighestRxSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:apSnrHighestRxSignalStrength.setStatus(_A)
_ApSnrLowestRxSignalStrength_Type=Integer32
_ApSnrLowestRxSignalStrength_Object=MibTableColumn
apSnrLowestRxSignalStrength=_ApSnrLowestRxSignalStrength_Object((1,3,6,1,4,1,14823,2,2,1,7,1,1,1,4),_ApSnrLowestRxSignalStrength_Type())
apSnrLowestRxSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:apSnrLowestRxSignalStrength.setStatus(_A)
_ApSnrSampleTime_Type=Integer32
_ApSnrSampleTime_Object=MibTableColumn
apSnrSampleTime=_ApSnrSampleTime_Object((1,3,6,1,4,1,14823,2,2,1,7,1,1,1,5),_ApSnrSampleTime_Type())
apSnrSampleTime.setMaxAccess(_B)
if mibBuilder.loadTexts:apSnrSampleTime.setStatus(_A)
_WlsxStaSnrTable_Object=MibTable
wlsxStaSnrTable=_WlsxStaSnrTable_Object((1,3,6,1,4,1,14823,2,2,1,7,1,2))
if mibBuilder.loadTexts:wlsxStaSnrTable.setStatus(_A)
_WlsxStaSnrEntry_Object=MibTableRow
wlsxStaSnrEntry=_WlsxStaSnrEntry_Object((1,3,6,1,4,1,14823,2,2,1,7,1,2,1))
wlsxStaSnrEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_C,_G))
if mibBuilder.loadTexts:wlsxStaSnrEntry.setStatus(_A)
_StaSnrAverageSignalStrength_Type=Integer32
_StaSnrAverageSignalStrength_Object=MibTableColumn
staSnrAverageSignalStrength=_StaSnrAverageSignalStrength_Object((1,3,6,1,4,1,14823,2,2,1,7,1,2,1,1),_StaSnrAverageSignalStrength_Type())
staSnrAverageSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:staSnrAverageSignalStrength.setStatus(_A)
_StaSnrSignalPkts_Type=Integer32
_StaSnrSignalPkts_Object=MibTableColumn
staSnrSignalPkts=_StaSnrSignalPkts_Object((1,3,6,1,4,1,14823,2,2,1,7,1,2,1,2),_StaSnrSignalPkts_Type())
staSnrSignalPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:staSnrSignalPkts.setStatus(_A)
_StaSnrHighestRxSignalStrength_Type=Integer32
_StaSnrHighestRxSignalStrength_Object=MibTableColumn
staSnrHighestRxSignalStrength=_StaSnrHighestRxSignalStrength_Object((1,3,6,1,4,1,14823,2,2,1,7,1,2,1,3),_StaSnrHighestRxSignalStrength_Type())
staSnrHighestRxSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:staSnrHighestRxSignalStrength.setStatus(_A)
_StaSnrLowestRxSignalStrength_Type=Integer32
_StaSnrLowestRxSignalStrength_Object=MibTableColumn
staSnrLowestRxSignalStrength=_StaSnrLowestRxSignalStrength_Object((1,3,6,1,4,1,14823,2,2,1,7,1,2,1,4),_StaSnrLowestRxSignalStrength_Type())
staSnrLowestRxSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:staSnrLowestRxSignalStrength.setStatus(_A)
_StaSnrSampleTime_Type=Integer32
_StaSnrSampleTime_Object=MibTableColumn
staSnrSampleTime=_StaSnrSampleTime_Object((1,3,6,1,4,1,14823,2,2,1,7,1,2,1,5),_StaSnrSampleTime_Type())
staSnrSampleTime.setMaxAccess(_B)
if mibBuilder.loadTexts:staSnrSampleTime.setStatus(_A)
_WlsxAPSnrBSSIDTable_Object=MibTable
wlsxAPSnrBSSIDTable=_WlsxAPSnrBSSIDTable_Object((1,3,6,1,4,1,14823,2,2,1,7,1,3))
if mibBuilder.loadTexts:wlsxAPSnrBSSIDTable.setStatus(_A)
_WlsxAPSnrBSSIDEntry_Object=MibTableRow
wlsxAPSnrBSSIDEntry=_WlsxAPSnrBSSIDEntry_Object((1,3,6,1,4,1,14823,2,2,1,7,1,3,1))
wlsxAPSnrBSSIDEntry.setIndexNames((0,_C,_F),(0,_C,_D),(0,_C,_E))
if mibBuilder.loadTexts:wlsxAPSnrBSSIDEntry.setStatus(_A)
_ApSnrBSSIDAverageSignalStrength_Type=Integer32
_ApSnrBSSIDAverageSignalStrength_Object=MibTableColumn
apSnrBSSIDAverageSignalStrength=_ApSnrBSSIDAverageSignalStrength_Object((1,3,6,1,4,1,14823,2,2,1,7,1,3,1,1),_ApSnrBSSIDAverageSignalStrength_Type())
apSnrBSSIDAverageSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:apSnrBSSIDAverageSignalStrength.setStatus(_A)
_ApSnrBSSIDSignalPkts_Type=Integer32
_ApSnrBSSIDSignalPkts_Object=MibTableColumn
apSnrBSSIDSignalPkts=_ApSnrBSSIDSignalPkts_Object((1,3,6,1,4,1,14823,2,2,1,7,1,3,1,2),_ApSnrBSSIDSignalPkts_Type())
apSnrBSSIDSignalPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:apSnrBSSIDSignalPkts.setStatus(_A)
_ApSnrBSSIDHighestRxSignalStrength_Type=Integer32
_ApSnrBSSIDHighestRxSignalStrength_Object=MibTableColumn
apSnrBSSIDHighestRxSignalStrength=_ApSnrBSSIDHighestRxSignalStrength_Object((1,3,6,1,4,1,14823,2,2,1,7,1,3,1,3),_ApSnrBSSIDHighestRxSignalStrength_Type())
apSnrBSSIDHighestRxSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:apSnrBSSIDHighestRxSignalStrength.setStatus(_A)
_ApSnrBSSIDLowestRxSignalStrength_Type=Integer32
_ApSnrBSSIDLowestRxSignalStrength_Object=MibTableColumn
apSnrBSSIDLowestRxSignalStrength=_ApSnrBSSIDLowestRxSignalStrength_Object((1,3,6,1,4,1,14823,2,2,1,7,1,3,1,4),_ApSnrBSSIDLowestRxSignalStrength_Type())
apSnrBSSIDLowestRxSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:apSnrBSSIDLowestRxSignalStrength.setStatus(_A)
_ApSnrBSSIDSampleTime_Type=Integer32
_ApSnrBSSIDSampleTime_Object=MibTableColumn
apSnrBSSIDSampleTime=_ApSnrBSSIDSampleTime_Object((1,3,6,1,4,1,14823,2,2,1,7,1,3,1,5),_ApSnrBSSIDSampleTime_Type())
apSnrBSSIDSampleTime.setMaxAccess(_B)
if mibBuilder.loadTexts:apSnrBSSIDSampleTime.setStatus(_A)
_WlsxStaSnrPhyTable_Object=MibTable
wlsxStaSnrPhyTable=_WlsxStaSnrPhyTable_Object((1,3,6,1,4,1,14823,2,2,1,7,1,4))
if mibBuilder.loadTexts:wlsxStaSnrPhyTable.setStatus(_A)
_WlsxStaSnrPhyEntry_Object=MibTableRow
wlsxStaSnrPhyEntry=_WlsxStaSnrPhyEntry_Object((1,3,6,1,4,1,14823,2,2,1,7,1,4,1))
wlsxStaSnrPhyEntry.setIndexNames((0,_C,_G),(0,_C,_D),(0,_C,_E))
if mibBuilder.loadTexts:wlsxStaSnrPhyEntry.setStatus(_A)
_StaSnrPhyAverageSignalStrength_Type=Integer32
_StaSnrPhyAverageSignalStrength_Object=MibTableColumn
staSnrPhyAverageSignalStrength=_StaSnrPhyAverageSignalStrength_Object((1,3,6,1,4,1,14823,2,2,1,7,1,4,1,1),_StaSnrPhyAverageSignalStrength_Type())
staSnrPhyAverageSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:staSnrPhyAverageSignalStrength.setStatus(_A)
_StaSnrPhySignalPkts_Type=Integer32
_StaSnrPhySignalPkts_Object=MibTableColumn
staSnrPhySignalPkts=_StaSnrPhySignalPkts_Object((1,3,6,1,4,1,14823,2,2,1,7,1,4,1,2),_StaSnrPhySignalPkts_Type())
staSnrPhySignalPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:staSnrPhySignalPkts.setStatus(_A)
_StaSnrPhyHighestRxSignalStrength_Type=Integer32
_StaSnrPhyHighestRxSignalStrength_Object=MibTableColumn
staSnrPhyHighestRxSignalStrength=_StaSnrPhyHighestRxSignalStrength_Object((1,3,6,1,4,1,14823,2,2,1,7,1,4,1,3),_StaSnrPhyHighestRxSignalStrength_Type())
staSnrPhyHighestRxSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:staSnrPhyHighestRxSignalStrength.setStatus(_A)
_StaSnrPhyLowestRxSignalStrength_Type=Integer32
_StaSnrPhyLowestRxSignalStrength_Object=MibTableColumn
staSnrPhyLowestRxSignalStrength=_StaSnrPhyLowestRxSignalStrength_Object((1,3,6,1,4,1,14823,2,2,1,7,1,4,1,4),_StaSnrPhyLowestRxSignalStrength_Type())
staSnrPhyLowestRxSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:staSnrPhyLowestRxSignalStrength.setStatus(_A)
_StaSnrPhySampleTime_Type=Integer32
_StaSnrPhySampleTime_Object=MibTableColumn
staSnrPhySampleTime=_StaSnrPhySampleTime_Object((1,3,6,1,4,1,14823,2,2,1,7,1,4,1,5),_StaSnrPhySampleTime_Type())
staSnrPhySampleTime.setMaxAccess(_B)
if mibBuilder.loadTexts:staSnrPhySampleTime.setStatus(_A)
mibBuilder.exportSymbols('WLSX-SNR-MIB',**{'wlsxSNRMIB':wlsxSNRMIB,'wlsxSNRGroup':wlsxSNRGroup,'wlsxAPSnrTable':wlsxAPSnrTable,'wlsxAPSnrEntry':wlsxAPSnrEntry,'apSnrAverageSignalStrength':apSnrAverageSignalStrength,'apSnrSignalPkts':apSnrSignalPkts,'apSnrHighestRxSignalStrength':apSnrHighestRxSignalStrength,'apSnrLowestRxSignalStrength':apSnrLowestRxSignalStrength,'apSnrSampleTime':apSnrSampleTime,'wlsxStaSnrTable':wlsxStaSnrTable,'wlsxStaSnrEntry':wlsxStaSnrEntry,'staSnrAverageSignalStrength':staSnrAverageSignalStrength,'staSnrSignalPkts':staSnrSignalPkts,'staSnrHighestRxSignalStrength':staSnrHighestRxSignalStrength,'staSnrLowestRxSignalStrength':staSnrLowestRxSignalStrength,'staSnrSampleTime':staSnrSampleTime,'wlsxAPSnrBSSIDTable':wlsxAPSnrBSSIDTable,'wlsxAPSnrBSSIDEntry':wlsxAPSnrBSSIDEntry,'apSnrBSSIDAverageSignalStrength':apSnrBSSIDAverageSignalStrength,'apSnrBSSIDSignalPkts':apSnrBSSIDSignalPkts,'apSnrBSSIDHighestRxSignalStrength':apSnrBSSIDHighestRxSignalStrength,'apSnrBSSIDLowestRxSignalStrength':apSnrBSSIDLowestRxSignalStrength,'apSnrBSSIDSampleTime':apSnrBSSIDSampleTime,'wlsxStaSnrPhyTable':wlsxStaSnrPhyTable,'wlsxStaSnrPhyEntry':wlsxStaSnrPhyEntry,'staSnrPhyAverageSignalStrength':staSnrPhyAverageSignalStrength,'staSnrPhySignalPkts':staSnrPhySignalPkts,'staSnrPhyHighestRxSignalStrength':staSnrPhyHighestRxSignalStrength,'staSnrPhyLowestRxSignalStrength':staSnrPhyLowestRxSignalStrength,'staSnrPhySampleTime':staSnrPhySampleTime})