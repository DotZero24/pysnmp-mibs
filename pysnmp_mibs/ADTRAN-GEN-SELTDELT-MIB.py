_Q='adGenSeltDeltTestRemoteDevice'
_P='adGenSeltDeltEnumTestStatus'
_O='adGenSeltDeltRetrieveData'
_N='adGenSeltDeltLastTestStatus'
_M='adGenSeltDeltCurrentTestStatus'
_L='adGenSeltDeltStopTest'
_K='adGenSeltDeltStartDELTTest'
_J='adGenSeltDeltStartSELTTest'
_I='adGenSeltDeltTestFilename'
_H='adGenSeltDeltTestPortNumber'
_G='adGenSlotInfoIndex'
_F='ADTRAN-GENSLOT-MIB'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='ADTRAN-GEN-SELTDELT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_F,_G)
adGenXdsl,adGenXdslID=mibBuilder.importSymbols('ADTRAN-SHARED-XDSL-MIB','adGenXdsl','adGenXdslID')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenSeltDeltMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,73,1,1))
if mibBuilder.loadTexts:adGenSeltDeltMIB.setRevisions(('2013-12-03 00:00','2008-07-17 00:00'))
_AdGenSeltDelt_ObjectIdentity=ObjectIdentity
adGenSeltDelt=_AdGenSeltDelt_ObjectIdentity((1,3,6,1,4,1,664,5,73,1,1))
_AdGenSeltDeltTable_Object=MibTable
adGenSeltDeltTable=_AdGenSeltDeltTable_Object((1,3,6,1,4,1,664,5,73,1,1,1))
if mibBuilder.loadTexts:adGenSeltDeltTable.setStatus(_A)
_AdGenSeltDeltEntry_Object=MibTableRow
adGenSeltDeltEntry=_AdGenSeltDeltEntry_Object((1,3,6,1,4,1,664,5,73,1,1,1,1))
adGenSeltDeltEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:adGenSeltDeltEntry.setStatus(_A)
class _AdGenSeltDeltTestPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdGenSeltDeltTestPortNumber_Type.__name__=_C
_AdGenSeltDeltTestPortNumber_Object=MibTableColumn
adGenSeltDeltTestPortNumber=_AdGenSeltDeltTestPortNumber_Object((1,3,6,1,4,1,664,5,73,1,1,1,1,1),_AdGenSeltDeltTestPortNumber_Type())
adGenSeltDeltTestPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSeltDeltTestPortNumber.setStatus(_A)
_AdGenSeltDeltTestFilename_Type=DisplayString
_AdGenSeltDeltTestFilename_Object=MibTableColumn
adGenSeltDeltTestFilename=_AdGenSeltDeltTestFilename_Object((1,3,6,1,4,1,664,5,73,1,1,1,1,2),_AdGenSeltDeltTestFilename_Type())
adGenSeltDeltTestFilename.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSeltDeltTestFilename.setStatus(_A)
class _AdGenSeltDeltStartSELTTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('start',1))
_AdGenSeltDeltStartSELTTest_Type.__name__=_C
_AdGenSeltDeltStartSELTTest_Object=MibTableColumn
adGenSeltDeltStartSELTTest=_AdGenSeltDeltStartSELTTest_Object((1,3,6,1,4,1,664,5,73,1,1,1,1,3),_AdGenSeltDeltStartSELTTest_Type())
adGenSeltDeltStartSELTTest.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSeltDeltStartSELTTest.setStatus(_A)
class _AdGenSeltDeltStartDELTTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('start',1))
_AdGenSeltDeltStartDELTTest_Type.__name__=_C
_AdGenSeltDeltStartDELTTest_Object=MibTableColumn
adGenSeltDeltStartDELTTest=_AdGenSeltDeltStartDELTTest_Object((1,3,6,1,4,1,664,5,73,1,1,1,1,4),_AdGenSeltDeltStartDELTTest_Type())
adGenSeltDeltStartDELTTest.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSeltDeltStartDELTTest.setStatus(_A)
class _AdGenSeltDeltStopTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('stop',1))
_AdGenSeltDeltStopTest_Type.__name__=_C
_AdGenSeltDeltStopTest_Object=MibTableColumn
adGenSeltDeltStopTest=_AdGenSeltDeltStopTest_Object((1,3,6,1,4,1,664,5,73,1,1,1,1,5),_AdGenSeltDeltStopTest_Type())
adGenSeltDeltStopTest.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSeltDeltStopTest.setStatus(_A)
_AdGenSeltDeltCurrentTestStatus_Type=DisplayString
_AdGenSeltDeltCurrentTestStatus_Object=MibTableColumn
adGenSeltDeltCurrentTestStatus=_AdGenSeltDeltCurrentTestStatus_Object((1,3,6,1,4,1,664,5,73,1,1,1,1,6),_AdGenSeltDeltCurrentTestStatus_Type())
adGenSeltDeltCurrentTestStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenSeltDeltCurrentTestStatus.setStatus(_A)
_AdGenSeltDeltLastTestStatus_Type=DisplayString
_AdGenSeltDeltLastTestStatus_Object=MibTableColumn
adGenSeltDeltLastTestStatus=_AdGenSeltDeltLastTestStatus_Object((1,3,6,1,4,1,664,5,73,1,1,1,1,7),_AdGenSeltDeltLastTestStatus_Type())
adGenSeltDeltLastTestStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenSeltDeltLastTestStatus.setStatus(_A)
class _AdGenSeltDeltRetrieveData_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('beginTransfer',1))
_AdGenSeltDeltRetrieveData_Type.__name__=_C
_AdGenSeltDeltRetrieveData_Object=MibTableColumn
adGenSeltDeltRetrieveData=_AdGenSeltDeltRetrieveData_Object((1,3,6,1,4,1,664,5,73,1,1,1,1,8),_AdGenSeltDeltRetrieveData_Type())
adGenSeltDeltRetrieveData.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSeltDeltRetrieveData.setStatus(_A)
class _AdGenSeltDeltEnumTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('idle',1),('active',2),('collectingData',3),('dataAvailable',4),('testFailed',5)))
_AdGenSeltDeltEnumTestStatus_Type.__name__=_C
_AdGenSeltDeltEnumTestStatus_Object=MibTableColumn
adGenSeltDeltEnumTestStatus=_AdGenSeltDeltEnumTestStatus_Object((1,3,6,1,4,1,664,5,73,1,1,1,1,9),_AdGenSeltDeltEnumTestStatus_Type())
adGenSeltDeltEnumTestStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:adGenSeltDeltEnumTestStatus.setStatus(_A)
_AdGenSeltDeltTestRemoteDevice_Type=InterfaceIndex
_AdGenSeltDeltTestRemoteDevice_Object=MibTableColumn
adGenSeltDeltTestRemoteDevice=_AdGenSeltDeltTestRemoteDevice_Object((1,3,6,1,4,1,664,5,73,1,1,1,1,10),_AdGenSeltDeltTestRemoteDevice_Type())
adGenSeltDeltTestRemoteDevice.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSeltDeltTestRemoteDevice.setStatus(_A)
_AdGenXdslMibConformance_ObjectIdentity=ObjectIdentity
adGenXdslMibConformance=_AdGenXdslMibConformance_ObjectIdentity((1,3,6,1,4,1,664,5,73,1,2))
_AdGenXdslMibGroups_ObjectIdentity=ObjectIdentity
adGenXdslMibGroups=_AdGenXdslMibGroups_ObjectIdentity((1,3,6,1,4,1,664,5,73,1,2,1))
adGenXdslSeltDeltGroup=ObjectGroup((1,3,6,1,4,1,664,5,73,1,2,1,1))
adGenXdslSeltDeltGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:adGenXdslSeltDeltGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adGenSeltDelt':adGenSeltDelt,'adGenSeltDeltTable':adGenSeltDeltTable,'adGenSeltDeltEntry':adGenSeltDeltEntry,_H:adGenSeltDeltTestPortNumber,_I:adGenSeltDeltTestFilename,_J:adGenSeltDeltStartSELTTest,_K:adGenSeltDeltStartDELTTest,_L:adGenSeltDeltStopTest,_M:adGenSeltDeltCurrentTestStatus,_N:adGenSeltDeltLastTestStatus,_O:adGenSeltDeltRetrieveData,_P:adGenSeltDeltEnumTestStatus,_Q:adGenSeltDeltTestRemoteDevice,'adGenXdslMibConformance':adGenXdslMibConformance,'adGenXdslMibGroups':adGenXdslMibGroups,'adGenXdslSeltDeltGroup':adGenXdslSeltDeltGroup,'adGenSeltDeltMIB':adGenSeltDeltMIB})