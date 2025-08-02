_b='tnLldpLocManAddr'
_a='tnLldpLocManAddrSubtype'
_Z='tnLldpLocPortDestMACAddress'
_Y='tnLldpStatsRxDestMACAddress'
_X='tnLldpStatsTxDestMACAddress'
_W='tnLldpAddressTableIndex'
_V='tnLldpPortCfgAddressIndex'
_U='TmnxEnabledDisabled'
_T='TruthValue'
_S='tnLldpRemManAddr'
_R='tnLldpRemManAddrSubtype'
_Q='table entries'
_P='tnLldpPortCfgDestAddressIndex'
_O='tnLldpRemIndex'
_N='tnLldpRemLocalDestMACAddress'
_M='tnLldpRemTimeMark'
_L='seconds'
_K='tnSysSwitchId'
_J='TROPIC-SYSTEM-MIB'
_I='tnPortPortID'
_H='TN-PORT-MIB'
_G='SnmpAdminString'
_F='Integer32'
_E='not-accessible'
_D='read-write'
_C='TN-LLDP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AddressFamilyNumbers,=mibBuilder.importSymbols('IANA-ADDRESS-FAMILY-NUMBERS-MIB','AddressFamilyNumbers')
LldpChassisId,LldpChassisIdSubtype,LldpManAddrIfSubtype,LldpManAddress,LldpPortId,LldpPortIdSubtype,LldpSystemCapabilitiesMap=mibBuilder.importSymbols('LLDP-MIB','LldpChassisId','LldpChassisIdSubtype','LldpManAddrIfSubtype','LldpManAddress','LldpPortId','LldpPortIdSubtype','LldpSystemCapabilitiesMap')
TimeFilter,ZeroBasedCounter32=mibBuilder.importSymbols('RMON2-MIB','TimeFilter','ZeroBasedCounter32')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_T)
tnPortPortID,=mibBuilder.importSymbols(_H,_I)
TmnxEnabledDisabled,=mibBuilder.importSymbols('TN-TC-MIB',_U)
tnSRMIBModules,tnSRNotifyPrefix,tnSRObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSRMIBModules','tnSRNotifyPrefix','tnSRObjs')
tnSysSwitchId,=mibBuilder.importSymbols(_J,_K)
tnLldpMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,3,59))
if mibBuilder.loadTexts:tnLldpMIBModule.setRevisions(('2020-09-25 00:00','2019-04-19 00:00','2017-01-13 00:00','2016-12-17 00:00','2016-06-21 00:00','2016-03-05 00:00','2016-02-23 00:00'))
class TmnxLldpDestAddressTableIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
class TmnxLldpManAddressIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('system',1))
_TnLldpObjects_ObjectIdentity=ObjectIdentity
tnLldpObjects=_TnLldpObjects_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,59))
_TnLldpConfiguration_ObjectIdentity=ObjectIdentity
tnLldpConfiguration=_TnLldpConfiguration_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,59,1))
_TnLldpConfigTable_Object=MibTable
tnLldpConfigTable=_TnLldpConfigTable_Object((1,3,6,1,4,1,7483,6,1,2,59,1,1))
if mibBuilder.loadTexts:tnLldpConfigTable.setStatus(_A)
_TnLldpConfigEntry_Object=MibTableRow
tnLldpConfigEntry=_TnLldpConfigEntry_Object((1,3,6,1,4,1,7483,6,1,2,59,1,1,1))
tnLldpConfigEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:tnLldpConfigEntry.setStatus(_A)
class _TnLldpMessageTxInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,32768))
_TnLldpMessageTxInterval_Type.__name__=_F
_TnLldpMessageTxInterval_Object=MibTableColumn
tnLldpMessageTxInterval=_TnLldpMessageTxInterval_Object((1,3,6,1,4,1,7483,6,1,2,59,1,1,1,1),_TnLldpMessageTxInterval_Type())
tnLldpMessageTxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tnLldpMessageTxInterval.setStatus(_A)
if mibBuilder.loadTexts:tnLldpMessageTxInterval.setUnits(_L)
class _TnLldpMessageTxHoldMultiplier_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_TnLldpMessageTxHoldMultiplier_Type.__name__=_F
_TnLldpMessageTxHoldMultiplier_Object=MibTableColumn
tnLldpMessageTxHoldMultiplier=_TnLldpMessageTxHoldMultiplier_Object((1,3,6,1,4,1,7483,6,1,2,59,1,1,1,2),_TnLldpMessageTxHoldMultiplier_Type())
tnLldpMessageTxHoldMultiplier.setMaxAccess(_D)
if mibBuilder.loadTexts:tnLldpMessageTxHoldMultiplier.setStatus(_A)
class _TnLldpReinitDelay_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_TnLldpReinitDelay_Type.__name__=_F
_TnLldpReinitDelay_Object=MibTableColumn
tnLldpReinitDelay=_TnLldpReinitDelay_Object((1,3,6,1,4,1,7483,6,1,2,59,1,1,1,3),_TnLldpReinitDelay_Type())
tnLldpReinitDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:tnLldpReinitDelay.setStatus(_A)
if mibBuilder.loadTexts:tnLldpReinitDelay.setUnits(_L)
class _TnLldpTxDelay_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8192))
_TnLldpTxDelay_Type.__name__=_F
_TnLldpTxDelay_Object=MibTableColumn
tnLldpTxDelay=_TnLldpTxDelay_Object((1,3,6,1,4,1,7483,6,1,2,59,1,1,1,4),_TnLldpTxDelay_Type())
tnLldpTxDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:tnLldpTxDelay.setStatus(_A)
if mibBuilder.loadTexts:tnLldpTxDelay.setUnits(_L)
class _TnLldpNotificationInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,3600))
_TnLldpNotificationInterval_Type.__name__=_F
_TnLldpNotificationInterval_Object=MibTableColumn
tnLldpNotificationInterval=_TnLldpNotificationInterval_Object((1,3,6,1,4,1,7483,6,1,2,59,1,1,1,5),_TnLldpNotificationInterval_Type())
tnLldpNotificationInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tnLldpNotificationInterval.setStatus(_A)
if mibBuilder.loadTexts:tnLldpNotificationInterval.setUnits(_L)
class _TnLldpTxCreditMax_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_TnLldpTxCreditMax_Type.__name__=_F
_TnLldpTxCreditMax_Object=MibTableColumn
tnLldpTxCreditMax=_TnLldpTxCreditMax_Object((1,3,6,1,4,1,7483,6,1,2,59,1,1,1,6),_TnLldpTxCreditMax_Type())
tnLldpTxCreditMax.setMaxAccess(_D)
if mibBuilder.loadTexts:tnLldpTxCreditMax.setStatus(_A)
class _TnLldpMessageFastTx_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_TnLldpMessageFastTx_Type.__name__=_F
_TnLldpMessageFastTx_Object=MibTableColumn
tnLldpMessageFastTx=_TnLldpMessageFastTx_Object((1,3,6,1,4,1,7483,6,1,2,59,1,1,1,7),_TnLldpMessageFastTx_Type())
tnLldpMessageFastTx.setMaxAccess(_D)
if mibBuilder.loadTexts:tnLldpMessageFastTx.setStatus(_A)
if mibBuilder.loadTexts:tnLldpMessageFastTx.setUnits(_L)
class _TnLldpMessageFastTxInit_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_TnLldpMessageFastTxInit_Type.__name__=_F
_TnLldpMessageFastTxInit_Object=MibTableColumn
tnLldpMessageFastTxInit=_TnLldpMessageFastTxInit_Object((1,3,6,1,4,1,7483,6,1,2,59,1,1,1,8),_TnLldpMessageFastTxInit_Type())
tnLldpMessageFastTxInit.setMaxAccess(_D)
if mibBuilder.loadTexts:tnLldpMessageFastTxInit.setStatus(_A)
_TnLldpAdminStatus_Type=TmnxEnabledDisabled
_TnLldpAdminStatus_Object=MibTableColumn
tnLldpAdminStatus=_TnLldpAdminStatus_Object((1,3,6,1,4,1,7483,6,1,2,59,1,1,1,9),_TnLldpAdminStatus_Type())
tnLldpAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tnLldpAdminStatus.setStatus(_A)
_TnLldpPortConfigTable_Object=MibTable
tnLldpPortConfigTable=_TnLldpPortConfigTable_Object((1,3,6,1,4,1,7483,6,1,2,59,1,2))
if mibBuilder.loadTexts:tnLldpPortConfigTable.setStatus(_A)
_TnLldpPortConfigEntry_Object=MibTableRow
tnLldpPortConfigEntry=_TnLldpPortConfigEntry_Object((1,3,6,1,4,1,7483,6,1,2,59,1,2,1))
tnLldpPortConfigEntry.setIndexNames((0,_H,_I),(0,_C,_P))
if mibBuilder.loadTexts:tnLldpPortConfigEntry.setStatus(_A)
_TnLldpPortCfgDestAddressIndex_Type=TmnxLldpDestAddressTableIndex
_TnLldpPortCfgDestAddressIndex_Object=MibTableColumn
tnLldpPortCfgDestAddressIndex=_TnLldpPortCfgDestAddressIndex_Object((1,3,6,1,4,1,7483,6,1,2,59,1,2,1,1),_TnLldpPortCfgDestAddressIndex_Type())
tnLldpPortCfgDestAddressIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:tnLldpPortCfgDestAddressIndex.setStatus(_A)
class _TnLldpPortCfgAdminStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('txOnly',1),('rxOnly',2),('txAndRx',3),('disabled',4)))
_TnLldpPortCfgAdminStatus_Type.__name__=_F
_TnLldpPortCfgAdminStatus_Object=MibTableColumn
tnLldpPortCfgAdminStatus=_TnLldpPortCfgAdminStatus_Object((1,3,6,1,4,1,7483,6,1,2,59,1,2,1,2),_TnLldpPortCfgAdminStatus_Type())
tnLldpPortCfgAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tnLldpPortCfgAdminStatus.setStatus(_A)
class _TnLldpPortCfgNotifyEnable_Type(TruthValue):defaultValue=2
_TnLldpPortCfgNotifyEnable_Type.__name__=_T
_TnLldpPortCfgNotifyEnable_Object=MibTableColumn
tnLldpPortCfgNotifyEnable=_TnLldpPortCfgNotifyEnable_Object((1,3,6,1,4,1,7483,6,1,2,59,1,2,1,3),_TnLldpPortCfgNotifyEnable_Type())
tnLldpPortCfgNotifyEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:tnLldpPortCfgNotifyEnable.setStatus(_A)
class _TnLldpPortCfgTLVsTxEnable_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('portDesc',0),('sysName',1),('sysDesc',2),('sysCap',3)))
_TnLldpPortCfgTLVsTxEnable_Type.__name__='Bits'
_TnLldpPortCfgTLVsTxEnable_Object=MibTableColumn
tnLldpPortCfgTLVsTxEnable=_TnLldpPortCfgTLVsTxEnable_Object((1,3,6,1,4,1,7483,6,1,2,59,1,2,1,4),_TnLldpPortCfgTLVsTxEnable_Type())
tnLldpPortCfgTLVsTxEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:tnLldpPortCfgTLVsTxEnable.setStatus(_A)
_TnLldpConfigManAddrPortsTable_Object=MibTable
tnLldpConfigManAddrPortsTable=_TnLldpConfigManAddrPortsTable_Object((1,3,6,1,4,1,7483,6,1,2,59,1,3))
if mibBuilder.loadTexts:tnLldpConfigManAddrPortsTable.setStatus(_A)
_TnLldpConfigManAddrPortsEntry_Object=MibTableRow
tnLldpConfigManAddrPortsEntry=_TnLldpConfigManAddrPortsEntry_Object((1,3,6,1,4,1,7483,6,1,2,59,1,3,1))
tnLldpConfigManAddrPortsEntry.setIndexNames((0,_H,_I),(0,_C,_P),(0,_C,_V))
if mibBuilder.loadTexts:tnLldpConfigManAddrPortsEntry.setStatus(_A)
_TnLldpPortCfgAddressIndex_Type=TmnxLldpManAddressIndex
_TnLldpPortCfgAddressIndex_Object=MibTableColumn
tnLldpPortCfgAddressIndex=_TnLldpPortCfgAddressIndex_Object((1,3,6,1,4,1,7483,6,1,2,59,1,3,1,1),_TnLldpPortCfgAddressIndex_Type())
tnLldpPortCfgAddressIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:tnLldpPortCfgAddressIndex.setStatus(_A)
class _TnLldpPortCfgManAddrTxEnabled_Type(TmnxEnabledDisabled):defaultValue=2
_TnLldpPortCfgManAddrTxEnabled_Type.__name__=_U
_TnLldpPortCfgManAddrTxEnabled_Object=MibTableColumn
tnLldpPortCfgManAddrTxEnabled=_TnLldpPortCfgManAddrTxEnabled_Object((1,3,6,1,4,1,7483,6,1,2,59,1,3,1,2),_TnLldpPortCfgManAddrTxEnabled_Type())
tnLldpPortCfgManAddrTxEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:tnLldpPortCfgManAddrTxEnabled.setStatus(_A)
_TnLldpPortCfgManAddrSubtype_Type=AddressFamilyNumbers
_TnLldpPortCfgManAddrSubtype_Object=MibTableColumn
tnLldpPortCfgManAddrSubtype=_TnLldpPortCfgManAddrSubtype_Object((1,3,6,1,4,1,7483,6,1,2,59,1,3,1,3),_TnLldpPortCfgManAddrSubtype_Type())
tnLldpPortCfgManAddrSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpPortCfgManAddrSubtype.setStatus(_A)
_TnLldpPortCfgManAddress_Type=LldpManAddress
_TnLldpPortCfgManAddress_Object=MibTableColumn
tnLldpPortCfgManAddress=_TnLldpPortCfgManAddress_Object((1,3,6,1,4,1,7483,6,1,2,59,1,3,1,4),_TnLldpPortCfgManAddress_Type())
tnLldpPortCfgManAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpPortCfgManAddress.setStatus(_A)
_TnLldpDestAddressTable_Object=MibTable
tnLldpDestAddressTable=_TnLldpDestAddressTable_Object((1,3,6,1,4,1,7483,6,1,2,59,1,4))
if mibBuilder.loadTexts:tnLldpDestAddressTable.setStatus(_A)
_TnLldpDestAddressTableEntry_Object=MibTableRow
tnLldpDestAddressTableEntry=_TnLldpDestAddressTableEntry_Object((1,3,6,1,4,1,7483,6,1,2,59,1,4,1))
tnLldpDestAddressTableEntry.setIndexNames((0,_J,_K),(0,_C,_W))
if mibBuilder.loadTexts:tnLldpDestAddressTableEntry.setStatus(_A)
_TnLldpAddressTableIndex_Type=TmnxLldpDestAddressTableIndex
_TnLldpAddressTableIndex_Object=MibTableColumn
tnLldpAddressTableIndex=_TnLldpAddressTableIndex_Object((1,3,6,1,4,1,7483,6,1,2,59,1,4,1,1),_TnLldpAddressTableIndex_Type())
tnLldpAddressTableIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:tnLldpAddressTableIndex.setStatus(_A)
_TnLldpDestMacAddress_Type=MacAddress
_TnLldpDestMacAddress_Object=MibTableColumn
tnLldpDestMacAddress=_TnLldpDestMacAddress_Object((1,3,6,1,4,1,7483,6,1,2,59,1,4,1,2),_TnLldpDestMacAddress_Type())
tnLldpDestMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpDestMacAddress.setStatus(_A)
_TnLldpStatistics_ObjectIdentity=ObjectIdentity
tnLldpStatistics=_TnLldpStatistics_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,59,2))
_TnLldpStatsTxPortTable_Object=MibTable
tnLldpStatsTxPortTable=_TnLldpStatsTxPortTable_Object((1,3,6,1,4,1,7483,6,1,2,59,2,1))
if mibBuilder.loadTexts:tnLldpStatsTxPortTable.setStatus(_A)
_TnLldpStatsTxPortEntry_Object=MibTableRow
tnLldpStatsTxPortEntry=_TnLldpStatsTxPortEntry_Object((1,3,6,1,4,1,7483,6,1,2,59,2,1,1))
tnLldpStatsTxPortEntry.setIndexNames((0,_H,_I),(0,_C,_X))
if mibBuilder.loadTexts:tnLldpStatsTxPortEntry.setStatus(_A)
_TnLldpStatsTxDestMACAddress_Type=TmnxLldpDestAddressTableIndex
_TnLldpStatsTxDestMACAddress_Object=MibTableColumn
tnLldpStatsTxDestMACAddress=_TnLldpStatsTxDestMACAddress_Object((1,3,6,1,4,1,7483,6,1,2,59,2,1,1,1),_TnLldpStatsTxDestMACAddress_Type())
tnLldpStatsTxDestMACAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:tnLldpStatsTxDestMACAddress.setStatus(_A)
_TnLldpStatsTxPortFrames_Type=Counter32
_TnLldpStatsTxPortFrames_Object=MibTableColumn
tnLldpStatsTxPortFrames=_TnLldpStatsTxPortFrames_Object((1,3,6,1,4,1,7483,6,1,2,59,2,1,1,2),_TnLldpStatsTxPortFrames_Type())
tnLldpStatsTxPortFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpStatsTxPortFrames.setStatus(_A)
_TnLldpStatsTxLLDPDULengthErrs_Type=Counter32
_TnLldpStatsTxLLDPDULengthErrs_Object=MibTableColumn
tnLldpStatsTxLLDPDULengthErrs=_TnLldpStatsTxLLDPDULengthErrs_Object((1,3,6,1,4,1,7483,6,1,2,59,2,1,1,3),_TnLldpStatsTxLLDPDULengthErrs_Type())
tnLldpStatsTxLLDPDULengthErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpStatsTxLLDPDULengthErrs.setStatus(_A)
_TnLldpStatsRemTable_Object=MibTable
tnLldpStatsRemTable=_TnLldpStatsRemTable_Object((1,3,6,1,4,1,7483,6,1,2,59,2,2))
if mibBuilder.loadTexts:tnLldpStatsRemTable.setStatus(_A)
_TnLldpStatsRemEntry_Object=MibTableRow
tnLldpStatsRemEntry=_TnLldpStatsRemEntry_Object((1,3,6,1,4,1,7483,6,1,2,59,2,2,1))
tnLldpStatsRemEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:tnLldpStatsRemEntry.setStatus(_A)
_TnLldpStatsRemTablesLastChangeTime_Type=Unsigned32
_TnLldpStatsRemTablesLastChangeTime_Object=MibTableColumn
tnLldpStatsRemTablesLastChangeTime=_TnLldpStatsRemTablesLastChangeTime_Object((1,3,6,1,4,1,7483,6,1,2,59,2,2,1,1),_TnLldpStatsRemTablesLastChangeTime_Type())
tnLldpStatsRemTablesLastChangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpStatsRemTablesLastChangeTime.setStatus(_A)
_TnLldpStatsRemTablesInserts_Type=ZeroBasedCounter32
_TnLldpStatsRemTablesInserts_Object=MibTableColumn
tnLldpStatsRemTablesInserts=_TnLldpStatsRemTablesInserts_Object((1,3,6,1,4,1,7483,6,1,2,59,2,2,1,2),_TnLldpStatsRemTablesInserts_Type())
tnLldpStatsRemTablesInserts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpStatsRemTablesInserts.setStatus(_A)
if mibBuilder.loadTexts:tnLldpStatsRemTablesInserts.setUnits(_Q)
_TnLldpStatsRemTablesDeletes_Type=ZeroBasedCounter32
_TnLldpStatsRemTablesDeletes_Object=MibTableColumn
tnLldpStatsRemTablesDeletes=_TnLldpStatsRemTablesDeletes_Object((1,3,6,1,4,1,7483,6,1,2,59,2,2,1,3),_TnLldpStatsRemTablesDeletes_Type())
tnLldpStatsRemTablesDeletes.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpStatsRemTablesDeletes.setStatus(_A)
if mibBuilder.loadTexts:tnLldpStatsRemTablesDeletes.setUnits(_Q)
_TnLldpStatsRemTablesDrops_Type=ZeroBasedCounter32
_TnLldpStatsRemTablesDrops_Object=MibTableColumn
tnLldpStatsRemTablesDrops=_TnLldpStatsRemTablesDrops_Object((1,3,6,1,4,1,7483,6,1,2,59,2,2,1,4),_TnLldpStatsRemTablesDrops_Type())
tnLldpStatsRemTablesDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpStatsRemTablesDrops.setStatus(_A)
if mibBuilder.loadTexts:tnLldpStatsRemTablesDrops.setUnits(_Q)
_TnLldpStatsRemTablesAgeouts_Type=ZeroBasedCounter32
_TnLldpStatsRemTablesAgeouts_Object=MibTableColumn
tnLldpStatsRemTablesAgeouts=_TnLldpStatsRemTablesAgeouts_Object((1,3,6,1,4,1,7483,6,1,2,59,2,2,1,5),_TnLldpStatsRemTablesAgeouts_Type())
tnLldpStatsRemTablesAgeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpStatsRemTablesAgeouts.setStatus(_A)
_TnLldpStatsRxPortTable_Object=MibTable
tnLldpStatsRxPortTable=_TnLldpStatsRxPortTable_Object((1,3,6,1,4,1,7483,6,1,2,59,2,3))
if mibBuilder.loadTexts:tnLldpStatsRxPortTable.setStatus(_A)
_TnLldpStatsRxPortEntry_Object=MibTableRow
tnLldpStatsRxPortEntry=_TnLldpStatsRxPortEntry_Object((1,3,6,1,4,1,7483,6,1,2,59,2,3,1))
tnLldpStatsRxPortEntry.setIndexNames((0,_H,_I),(0,_C,_Y))
if mibBuilder.loadTexts:tnLldpStatsRxPortEntry.setStatus(_A)
_TnLldpStatsRxDestMACAddress_Type=TmnxLldpDestAddressTableIndex
_TnLldpStatsRxDestMACAddress_Object=MibTableColumn
tnLldpStatsRxDestMACAddress=_TnLldpStatsRxDestMACAddress_Object((1,3,6,1,4,1,7483,6,1,2,59,2,3,1,1),_TnLldpStatsRxDestMACAddress_Type())
tnLldpStatsRxDestMACAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:tnLldpStatsRxDestMACAddress.setStatus(_A)
_TnLldpStatsRxPortFrameDiscard_Type=Counter32
_TnLldpStatsRxPortFrameDiscard_Object=MibTableColumn
tnLldpStatsRxPortFrameDiscard=_TnLldpStatsRxPortFrameDiscard_Object((1,3,6,1,4,1,7483,6,1,2,59,2,3,1,2),_TnLldpStatsRxPortFrameDiscard_Type())
tnLldpStatsRxPortFrameDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpStatsRxPortFrameDiscard.setStatus(_A)
_TnLldpStatsRxPortFrameErrs_Type=Counter32
_TnLldpStatsRxPortFrameErrs_Object=MibTableColumn
tnLldpStatsRxPortFrameErrs=_TnLldpStatsRxPortFrameErrs_Object((1,3,6,1,4,1,7483,6,1,2,59,2,3,1,3),_TnLldpStatsRxPortFrameErrs_Type())
tnLldpStatsRxPortFrameErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpStatsRxPortFrameErrs.setStatus(_A)
_TnLldpStatsRxPortFrames_Type=Counter32
_TnLldpStatsRxPortFrames_Object=MibTableColumn
tnLldpStatsRxPortFrames=_TnLldpStatsRxPortFrames_Object((1,3,6,1,4,1,7483,6,1,2,59,2,3,1,4),_TnLldpStatsRxPortFrames_Type())
tnLldpStatsRxPortFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpStatsRxPortFrames.setStatus(_A)
_TnLldpStatsRxPortTLVDiscard_Type=Counter32
_TnLldpStatsRxPortTLVDiscard_Object=MibTableColumn
tnLldpStatsRxPortTLVDiscard=_TnLldpStatsRxPortTLVDiscard_Object((1,3,6,1,4,1,7483,6,1,2,59,2,3,1,5),_TnLldpStatsRxPortTLVDiscard_Type())
tnLldpStatsRxPortTLVDiscard.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpStatsRxPortTLVDiscard.setStatus(_A)
_TnLldpStatsRxPortTLVUnknown_Type=Counter32
_TnLldpStatsRxPortTLVUnknown_Object=MibTableColumn
tnLldpStatsRxPortTLVUnknown=_TnLldpStatsRxPortTLVUnknown_Object((1,3,6,1,4,1,7483,6,1,2,59,2,3,1,6),_TnLldpStatsRxPortTLVUnknown_Type())
tnLldpStatsRxPortTLVUnknown.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpStatsRxPortTLVUnknown.setStatus(_A)
_TnLldpStatsRxPortAgeouts_Type=ZeroBasedCounter32
_TnLldpStatsRxPortAgeouts_Object=MibTableColumn
tnLldpStatsRxPortAgeouts=_TnLldpStatsRxPortAgeouts_Object((1,3,6,1,4,1,7483,6,1,2,59,2,3,1,7),_TnLldpStatsRxPortAgeouts_Type())
tnLldpStatsRxPortAgeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpStatsRxPortAgeouts.setStatus(_A)
_TnLldpStatsRxPortTtl_Type=Unsigned32
_TnLldpStatsRxPortTtl_Object=MibTableColumn
tnLldpStatsRxPortTtl=_TnLldpStatsRxPortTtl_Object((1,3,6,1,4,1,7483,6,1,2,59,2,3,1,8),_TnLldpStatsRxPortTtl_Type())
tnLldpStatsRxPortTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpStatsRxPortTtl.setStatus(_A)
_TnLldpLocalSystemData_ObjectIdentity=ObjectIdentity
tnLldpLocalSystemData=_TnLldpLocalSystemData_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,59,3))
_TnLldpLocSysDataTable_Object=MibTable
tnLldpLocSysDataTable=_TnLldpLocSysDataTable_Object((1,3,6,1,4,1,7483,6,1,2,59,3,1))
if mibBuilder.loadTexts:tnLldpLocSysDataTable.setStatus(_A)
_TnLldpLocSysDataEntry_Object=MibTableRow
tnLldpLocSysDataEntry=_TnLldpLocSysDataEntry_Object((1,3,6,1,4,1,7483,6,1,2,59,3,1,1))
tnLldpLocSysDataEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:tnLldpLocSysDataEntry.setStatus(_A)
_TnLldpLocChassisIdSubtype_Type=LldpChassisIdSubtype
_TnLldpLocChassisIdSubtype_Object=MibTableColumn
tnLldpLocChassisIdSubtype=_TnLldpLocChassisIdSubtype_Object((1,3,6,1,4,1,7483,6,1,2,59,3,1,1,1),_TnLldpLocChassisIdSubtype_Type())
tnLldpLocChassisIdSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpLocChassisIdSubtype.setStatus(_A)
_TnLldpLocChassisId_Type=LldpChassisId
_TnLldpLocChassisId_Object=MibTableColumn
tnLldpLocChassisId=_TnLldpLocChassisId_Object((1,3,6,1,4,1,7483,6,1,2,59,3,1,1,2),_TnLldpLocChassisId_Type())
tnLldpLocChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpLocChassisId.setStatus(_A)
class _TnLldpLocSysName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TnLldpLocSysName_Type.__name__=_G
_TnLldpLocSysName_Object=MibTableColumn
tnLldpLocSysName=_TnLldpLocSysName_Object((1,3,6,1,4,1,7483,6,1,2,59,3,1,1,3),_TnLldpLocSysName_Type())
tnLldpLocSysName.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpLocSysName.setStatus(_A)
class _TnLldpLocSysDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TnLldpLocSysDesc_Type.__name__=_G
_TnLldpLocSysDesc_Object=MibTableColumn
tnLldpLocSysDesc=_TnLldpLocSysDesc_Object((1,3,6,1,4,1,7483,6,1,2,59,3,1,1,4),_TnLldpLocSysDesc_Type())
tnLldpLocSysDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpLocSysDesc.setStatus(_A)
_TnLldpLocSysCapSupported_Type=LldpSystemCapabilitiesMap
_TnLldpLocSysCapSupported_Object=MibTableColumn
tnLldpLocSysCapSupported=_TnLldpLocSysCapSupported_Object((1,3,6,1,4,1,7483,6,1,2,59,3,1,1,5),_TnLldpLocSysCapSupported_Type())
tnLldpLocSysCapSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpLocSysCapSupported.setStatus(_A)
_TnLldpLocSysCapEnabled_Type=LldpSystemCapabilitiesMap
_TnLldpLocSysCapEnabled_Object=MibTableColumn
tnLldpLocSysCapEnabled=_TnLldpLocSysCapEnabled_Object((1,3,6,1,4,1,7483,6,1,2,59,3,1,1,6),_TnLldpLocSysCapEnabled_Type())
tnLldpLocSysCapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpLocSysCapEnabled.setStatus(_A)
_TnLldpLocPortTable_Object=MibTable
tnLldpLocPortTable=_TnLldpLocPortTable_Object((1,3,6,1,4,1,7483,6,1,2,59,3,2))
if mibBuilder.loadTexts:tnLldpLocPortTable.setStatus(_A)
_TnLldpLocPortEntry_Object=MibTableRow
tnLldpLocPortEntry=_TnLldpLocPortEntry_Object((1,3,6,1,4,1,7483,6,1,2,59,3,2,1))
tnLldpLocPortEntry.setIndexNames((0,_H,_I),(0,_C,_Z))
if mibBuilder.loadTexts:tnLldpLocPortEntry.setStatus(_A)
_TnLldpLocPortDestMACAddress_Type=TmnxLldpDestAddressTableIndex
_TnLldpLocPortDestMACAddress_Object=MibTableColumn
tnLldpLocPortDestMACAddress=_TnLldpLocPortDestMACAddress_Object((1,3,6,1,4,1,7483,6,1,2,59,3,2,1,1),_TnLldpLocPortDestMACAddress_Type())
tnLldpLocPortDestMACAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:tnLldpLocPortDestMACAddress.setStatus(_A)
_TnLldpLocPortIdSubtype_Type=LldpPortIdSubtype
_TnLldpLocPortIdSubtype_Object=MibTableColumn
tnLldpLocPortIdSubtype=_TnLldpLocPortIdSubtype_Object((1,3,6,1,4,1,7483,6,1,2,59,3,2,1,2),_TnLldpLocPortIdSubtype_Type())
tnLldpLocPortIdSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpLocPortIdSubtype.setStatus(_A)
_TnLldpLocPortId_Type=LldpPortId
_TnLldpLocPortId_Object=MibTableColumn
tnLldpLocPortId=_TnLldpLocPortId_Object((1,3,6,1,4,1,7483,6,1,2,59,3,2,1,3),_TnLldpLocPortId_Type())
tnLldpLocPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpLocPortId.setStatus(_A)
class _TnLldpLocPortDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TnLldpLocPortDesc_Type.__name__=_G
_TnLldpLocPortDesc_Object=MibTableColumn
tnLldpLocPortDesc=_TnLldpLocPortDesc_Object((1,3,6,1,4,1,7483,6,1,2,59,3,2,1,4),_TnLldpLocPortDesc_Type())
tnLldpLocPortDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpLocPortDesc.setStatus(_A)
_TnLldpLocManAddrTable_Object=MibTable
tnLldpLocManAddrTable=_TnLldpLocManAddrTable_Object((1,3,6,1,4,1,7483,6,1,2,59,3,3))
if mibBuilder.loadTexts:tnLldpLocManAddrTable.setStatus(_A)
_TnLldpLocManAddrEntry_Object=MibTableRow
tnLldpLocManAddrEntry=_TnLldpLocManAddrEntry_Object((1,3,6,1,4,1,7483,6,1,2,59,3,3,1))
tnLldpLocManAddrEntry.setIndexNames((0,_J,_K),(0,_C,_a),(0,_C,_b))
if mibBuilder.loadTexts:tnLldpLocManAddrEntry.setStatus(_A)
_TnLldpLocManAddrSubtype_Type=AddressFamilyNumbers
_TnLldpLocManAddrSubtype_Object=MibTableColumn
tnLldpLocManAddrSubtype=_TnLldpLocManAddrSubtype_Object((1,3,6,1,4,1,7483,6,1,2,59,3,3,1,1),_TnLldpLocManAddrSubtype_Type())
tnLldpLocManAddrSubtype.setMaxAccess(_E)
if mibBuilder.loadTexts:tnLldpLocManAddrSubtype.setStatus(_A)
_TnLldpLocManAddr_Type=LldpManAddress
_TnLldpLocManAddr_Object=MibTableColumn
tnLldpLocManAddr=_TnLldpLocManAddr_Object((1,3,6,1,4,1,7483,6,1,2,59,3,3,1,2),_TnLldpLocManAddr_Type())
tnLldpLocManAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:tnLldpLocManAddr.setStatus(_A)
_TnLldpLocManAddrLen_Type=Integer32
_TnLldpLocManAddrLen_Object=MibTableColumn
tnLldpLocManAddrLen=_TnLldpLocManAddrLen_Object((1,3,6,1,4,1,7483,6,1,2,59,3,3,1,3),_TnLldpLocManAddrLen_Type())
tnLldpLocManAddrLen.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpLocManAddrLen.setStatus(_A)
_TnLldpLocManAddrIfSubtype_Type=LldpManAddrIfSubtype
_TnLldpLocManAddrIfSubtype_Object=MibTableColumn
tnLldpLocManAddrIfSubtype=_TnLldpLocManAddrIfSubtype_Object((1,3,6,1,4,1,7483,6,1,2,59,3,3,1,4),_TnLldpLocManAddrIfSubtype_Type())
tnLldpLocManAddrIfSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpLocManAddrIfSubtype.setStatus(_A)
_TnLldpLocManAddrIfId_Type=Integer32
_TnLldpLocManAddrIfId_Object=MibTableColumn
tnLldpLocManAddrIfId=_TnLldpLocManAddrIfId_Object((1,3,6,1,4,1,7483,6,1,2,59,3,3,1,5),_TnLldpLocManAddrIfId_Type())
tnLldpLocManAddrIfId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpLocManAddrIfId.setStatus(_A)
_TnLldpLocManAddrOID_Type=ObjectIdentifier
_TnLldpLocManAddrOID_Object=MibTableColumn
tnLldpLocManAddrOID=_TnLldpLocManAddrOID_Object((1,3,6,1,4,1,7483,6,1,2,59,3,3,1,6),_TnLldpLocManAddrOID_Type())
tnLldpLocManAddrOID.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpLocManAddrOID.setStatus(_A)
_TnLldpRemoteSystemsData_ObjectIdentity=ObjectIdentity
tnLldpRemoteSystemsData=_TnLldpRemoteSystemsData_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,59,4))
_TnLldpRemTable_Object=MibTable
tnLldpRemTable=_TnLldpRemTable_Object((1,3,6,1,4,1,7483,6,1,2,59,4,1))
if mibBuilder.loadTexts:tnLldpRemTable.setStatus(_A)
_TnLldpRemEntry_Object=MibTableRow
tnLldpRemEntry=_TnLldpRemEntry_Object((1,3,6,1,4,1,7483,6,1,2,59,4,1,1))
tnLldpRemEntry.setIndexNames((0,_J,_K),(0,_C,_M),(0,_H,_I),(0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:tnLldpRemEntry.setStatus(_A)
_TnLldpRemTimeMark_Type=TimeFilter
_TnLldpRemTimeMark_Object=MibTableColumn
tnLldpRemTimeMark=_TnLldpRemTimeMark_Object((1,3,6,1,4,1,7483,6,1,2,59,4,1,1,1),_TnLldpRemTimeMark_Type())
tnLldpRemTimeMark.setMaxAccess(_E)
if mibBuilder.loadTexts:tnLldpRemTimeMark.setStatus(_A)
_TnLldpRemLocalDestMACAddress_Type=TmnxLldpDestAddressTableIndex
_TnLldpRemLocalDestMACAddress_Object=MibTableColumn
tnLldpRemLocalDestMACAddress=_TnLldpRemLocalDestMACAddress_Object((1,3,6,1,4,1,7483,6,1,2,59,4,1,1,2),_TnLldpRemLocalDestMACAddress_Type())
tnLldpRemLocalDestMACAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:tnLldpRemLocalDestMACAddress.setStatus(_A)
class _TnLldpRemIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TnLldpRemIndex_Type.__name__=_F
_TnLldpRemIndex_Object=MibTableColumn
tnLldpRemIndex=_TnLldpRemIndex_Object((1,3,6,1,4,1,7483,6,1,2,59,4,1,1,3),_TnLldpRemIndex_Type())
tnLldpRemIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:tnLldpRemIndex.setStatus(_A)
_TnLldpRemChassisIdSubtype_Type=LldpChassisIdSubtype
_TnLldpRemChassisIdSubtype_Object=MibTableColumn
tnLldpRemChassisIdSubtype=_TnLldpRemChassisIdSubtype_Object((1,3,6,1,4,1,7483,6,1,2,59,4,1,1,4),_TnLldpRemChassisIdSubtype_Type())
tnLldpRemChassisIdSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemChassisIdSubtype.setStatus(_A)
_TnLldpRemChassisId_Type=LldpChassisId
_TnLldpRemChassisId_Object=MibTableColumn
tnLldpRemChassisId=_TnLldpRemChassisId_Object((1,3,6,1,4,1,7483,6,1,2,59,4,1,1,5),_TnLldpRemChassisId_Type())
tnLldpRemChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemChassisId.setStatus(_A)
_TnLldpRemPortIdSubtype_Type=LldpPortIdSubtype
_TnLldpRemPortIdSubtype_Object=MibTableColumn
tnLldpRemPortIdSubtype=_TnLldpRemPortIdSubtype_Object((1,3,6,1,4,1,7483,6,1,2,59,4,1,1,6),_TnLldpRemPortIdSubtype_Type())
tnLldpRemPortIdSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemPortIdSubtype.setStatus(_A)
_TnLldpRemPortId_Type=LldpPortId
_TnLldpRemPortId_Object=MibTableColumn
tnLldpRemPortId=_TnLldpRemPortId_Object((1,3,6,1,4,1,7483,6,1,2,59,4,1,1,7),_TnLldpRemPortId_Type())
tnLldpRemPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemPortId.setStatus(_A)
class _TnLldpRemPortDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TnLldpRemPortDesc_Type.__name__=_G
_TnLldpRemPortDesc_Object=MibTableColumn
tnLldpRemPortDesc=_TnLldpRemPortDesc_Object((1,3,6,1,4,1,7483,6,1,2,59,4,1,1,8),_TnLldpRemPortDesc_Type())
tnLldpRemPortDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemPortDesc.setStatus(_A)
class _TnLldpRemSysName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TnLldpRemSysName_Type.__name__=_G
_TnLldpRemSysName_Object=MibTableColumn
tnLldpRemSysName=_TnLldpRemSysName_Object((1,3,6,1,4,1,7483,6,1,2,59,4,1,1,9),_TnLldpRemSysName_Type())
tnLldpRemSysName.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemSysName.setStatus(_A)
class _TnLldpRemSysDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TnLldpRemSysDesc_Type.__name__=_G
_TnLldpRemSysDesc_Object=MibTableColumn
tnLldpRemSysDesc=_TnLldpRemSysDesc_Object((1,3,6,1,4,1,7483,6,1,2,59,4,1,1,10),_TnLldpRemSysDesc_Type())
tnLldpRemSysDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemSysDesc.setStatus(_A)
_TnLldpRemSysCapSupported_Type=LldpSystemCapabilitiesMap
_TnLldpRemSysCapSupported_Object=MibTableColumn
tnLldpRemSysCapSupported=_TnLldpRemSysCapSupported_Object((1,3,6,1,4,1,7483,6,1,2,59,4,1,1,11),_TnLldpRemSysCapSupported_Type())
tnLldpRemSysCapSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemSysCapSupported.setStatus(_A)
_TnLldpRemSysCapEnabled_Type=LldpSystemCapabilitiesMap
_TnLldpRemSysCapEnabled_Object=MibTableColumn
tnLldpRemSysCapEnabled=_TnLldpRemSysCapEnabled_Object((1,3,6,1,4,1,7483,6,1,2,59,4,1,1,12),_TnLldpRemSysCapEnabled_Type())
tnLldpRemSysCapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemSysCapEnabled.setStatus(_A)
_TnLldpRemManAddrTable_Object=MibTable
tnLldpRemManAddrTable=_TnLldpRemManAddrTable_Object((1,3,6,1,4,1,7483,6,1,2,59,4,2))
if mibBuilder.loadTexts:tnLldpRemManAddrTable.setStatus(_A)
_TnLldpRemManAddrEntry_Object=MibTableRow
tnLldpRemManAddrEntry=_TnLldpRemManAddrEntry_Object((1,3,6,1,4,1,7483,6,1,2,59,4,2,1))
tnLldpRemManAddrEntry.setIndexNames((0,_J,_K),(0,_C,_M),(0,_H,_I),(0,_C,_N),(0,_C,_O),(0,_C,_R),(0,_C,_S))
if mibBuilder.loadTexts:tnLldpRemManAddrEntry.setStatus(_A)
_TnLldpRemManAddrSubtype_Type=AddressFamilyNumbers
_TnLldpRemManAddrSubtype_Object=MibTableColumn
tnLldpRemManAddrSubtype=_TnLldpRemManAddrSubtype_Object((1,3,6,1,4,1,7483,6,1,2,59,4,2,1,1),_TnLldpRemManAddrSubtype_Type())
tnLldpRemManAddrSubtype.setMaxAccess(_E)
if mibBuilder.loadTexts:tnLldpRemManAddrSubtype.setStatus(_A)
_TnLldpRemManAddr_Type=LldpManAddress
_TnLldpRemManAddr_Object=MibTableColumn
tnLldpRemManAddr=_TnLldpRemManAddr_Object((1,3,6,1,4,1,7483,6,1,2,59,4,2,1,2),_TnLldpRemManAddr_Type())
tnLldpRemManAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:tnLldpRemManAddr.setStatus(_A)
_TnLldpRemManAddrIfSubtype_Type=LldpManAddrIfSubtype
_TnLldpRemManAddrIfSubtype_Object=MibTableColumn
tnLldpRemManAddrIfSubtype=_TnLldpRemManAddrIfSubtype_Object((1,3,6,1,4,1,7483,6,1,2,59,4,2,1,3),_TnLldpRemManAddrIfSubtype_Type())
tnLldpRemManAddrIfSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemManAddrIfSubtype.setStatus(_A)
_TnLldpRemManAddrIfId_Type=Integer32
_TnLldpRemManAddrIfId_Object=MibTableColumn
tnLldpRemManAddrIfId=_TnLldpRemManAddrIfId_Object((1,3,6,1,4,1,7483,6,1,2,59,4,2,1,4),_TnLldpRemManAddrIfId_Type())
tnLldpRemManAddrIfId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemManAddrIfId.setStatus(_A)
_TnLldpRemManAddrOID_Type=ObjectIdentifier
_TnLldpRemManAddrOID_Object=MibTableColumn
tnLldpRemManAddrOID=_TnLldpRemManAddrOID_Object((1,3,6,1,4,1,7483,6,1,2,59,4,2,1,5),_TnLldpRemManAddrOID_Type())
tnLldpRemManAddrOID.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemManAddrOID.setStatus(_A)
_TnLldpRemPortIndexTable_Object=MibTable
tnLldpRemPortIndexTable=_TnLldpRemPortIndexTable_Object((1,3,6,1,4,1,7483,6,1,2,59,4,3))
if mibBuilder.loadTexts:tnLldpRemPortIndexTable.setStatus(_A)
_TnLldpRemPortIndexEntry_Object=MibTableRow
tnLldpRemPortIndexEntry=_TnLldpRemPortIndexEntry_Object((1,3,6,1,4,1,7483,6,1,2,59,4,3,1))
tnLldpRemPortIndexEntry.setIndexNames((0,_J,_K),(0,_H,_I),(0,_C,_M),(0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:tnLldpRemPortIndexEntry.setStatus(_A)
_TnLldpRemPortIndexChassisIdSubtype_Type=LldpChassisIdSubtype
_TnLldpRemPortIndexChassisIdSubtype_Object=MibTableColumn
tnLldpRemPortIndexChassisIdSubtype=_TnLldpRemPortIndexChassisIdSubtype_Object((1,3,6,1,4,1,7483,6,1,2,59,4,3,1,1),_TnLldpRemPortIndexChassisIdSubtype_Type())
tnLldpRemPortIndexChassisIdSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemPortIndexChassisIdSubtype.setStatus(_A)
_TnLldpRemPortIndexChassisId_Type=LldpChassisId
_TnLldpRemPortIndexChassisId_Object=MibTableColumn
tnLldpRemPortIndexChassisId=_TnLldpRemPortIndexChassisId_Object((1,3,6,1,4,1,7483,6,1,2,59,4,3,1,2),_TnLldpRemPortIndexChassisId_Type())
tnLldpRemPortIndexChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemPortIndexChassisId.setStatus(_A)
_TnLldpRemPortIndexPortIdSubtype_Type=LldpPortIdSubtype
_TnLldpRemPortIndexPortIdSubtype_Object=MibTableColumn
tnLldpRemPortIndexPortIdSubtype=_TnLldpRemPortIndexPortIdSubtype_Object((1,3,6,1,4,1,7483,6,1,2,59,4,3,1,3),_TnLldpRemPortIndexPortIdSubtype_Type())
tnLldpRemPortIndexPortIdSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemPortIndexPortIdSubtype.setStatus(_A)
_TnLldpRemPortIndexPortId_Type=LldpPortId
_TnLldpRemPortIndexPortId_Object=MibTableColumn
tnLldpRemPortIndexPortId=_TnLldpRemPortIndexPortId_Object((1,3,6,1,4,1,7483,6,1,2,59,4,3,1,4),_TnLldpRemPortIndexPortId_Type())
tnLldpRemPortIndexPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemPortIndexPortId.setStatus(_A)
class _TnLldpRemPortIndexPortDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TnLldpRemPortIndexPortDesc_Type.__name__=_G
_TnLldpRemPortIndexPortDesc_Object=MibTableColumn
tnLldpRemPortIndexPortDesc=_TnLldpRemPortIndexPortDesc_Object((1,3,6,1,4,1,7483,6,1,2,59,4,3,1,5),_TnLldpRemPortIndexPortDesc_Type())
tnLldpRemPortIndexPortDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemPortIndexPortDesc.setStatus(_A)
class _TnLldpRemPortIndexSysName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TnLldpRemPortIndexSysName_Type.__name__=_G
_TnLldpRemPortIndexSysName_Object=MibTableColumn
tnLldpRemPortIndexSysName=_TnLldpRemPortIndexSysName_Object((1,3,6,1,4,1,7483,6,1,2,59,4,3,1,6),_TnLldpRemPortIndexSysName_Type())
tnLldpRemPortIndexSysName.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemPortIndexSysName.setStatus(_A)
class _TnLldpRemPortIndexSysDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TnLldpRemPortIndexSysDesc_Type.__name__=_G
_TnLldpRemPortIndexSysDesc_Object=MibTableColumn
tnLldpRemPortIndexSysDesc=_TnLldpRemPortIndexSysDesc_Object((1,3,6,1,4,1,7483,6,1,2,59,4,3,1,7),_TnLldpRemPortIndexSysDesc_Type())
tnLldpRemPortIndexSysDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemPortIndexSysDesc.setStatus(_A)
_TnLldpRemPortIndexSysCapSupported_Type=LldpSystemCapabilitiesMap
_TnLldpRemPortIndexSysCapSupported_Object=MibTableColumn
tnLldpRemPortIndexSysCapSupported=_TnLldpRemPortIndexSysCapSupported_Object((1,3,6,1,4,1,7483,6,1,2,59,4,3,1,8),_TnLldpRemPortIndexSysCapSupported_Type())
tnLldpRemPortIndexSysCapSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemPortIndexSysCapSupported.setStatus(_A)
_TnLldpRemPortIndexSysCapEnabled_Type=LldpSystemCapabilitiesMap
_TnLldpRemPortIndexSysCapEnabled_Object=MibTableColumn
tnLldpRemPortIndexSysCapEnabled=_TnLldpRemPortIndexSysCapEnabled_Object((1,3,6,1,4,1,7483,6,1,2,59,4,3,1,9),_TnLldpRemPortIndexSysCapEnabled_Type())
tnLldpRemPortIndexSysCapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemPortIndexSysCapEnabled.setStatus(_A)
_TnLldpRemManAddrPortIndexTable_Object=MibTable
tnLldpRemManAddrPortIndexTable=_TnLldpRemManAddrPortIndexTable_Object((1,3,6,1,4,1,7483,6,1,2,59,4,4))
if mibBuilder.loadTexts:tnLldpRemManAddrPortIndexTable.setStatus(_A)
_TnLldpRemManAddrPortIndexEntry_Object=MibTableRow
tnLldpRemManAddrPortIndexEntry=_TnLldpRemManAddrPortIndexEntry_Object((1,3,6,1,4,1,7483,6,1,2,59,4,4,1))
tnLldpRemManAddrPortIndexEntry.setIndexNames((0,_J,_K),(0,_H,_I),(0,_C,_M),(0,_C,_N),(0,_C,_O),(0,_C,_R),(0,_C,_S))
if mibBuilder.loadTexts:tnLldpRemManAddrPortIndexEntry.setStatus(_A)
_TnLldpRemManAddrPortIndexIfSubtype_Type=LldpManAddrIfSubtype
_TnLldpRemManAddrPortIndexIfSubtype_Object=MibTableColumn
tnLldpRemManAddrPortIndexIfSubtype=_TnLldpRemManAddrPortIndexIfSubtype_Object((1,3,6,1,4,1,7483,6,1,2,59,4,4,1,1),_TnLldpRemManAddrPortIndexIfSubtype_Type())
tnLldpRemManAddrPortIndexIfSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemManAddrPortIndexIfSubtype.setStatus(_A)
_TnLldpRemManAddrPortIndexIfId_Type=Integer32
_TnLldpRemManAddrPortIndexIfId_Object=MibTableColumn
tnLldpRemManAddrPortIndexIfId=_TnLldpRemManAddrPortIndexIfId_Object((1,3,6,1,4,1,7483,6,1,2,59,4,4,1,2),_TnLldpRemManAddrPortIndexIfId_Type())
tnLldpRemManAddrPortIndexIfId.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemManAddrPortIndexIfId.setStatus(_A)
_TnLldpRemManAddrPortIndexOID_Type=ObjectIdentifier
_TnLldpRemManAddrPortIndexOID_Object=MibTableColumn
tnLldpRemManAddrPortIndexOID=_TnLldpRemManAddrPortIndexOID_Object((1,3,6,1,4,1,7483,6,1,2,59,4,4,1,3),_TnLldpRemManAddrPortIndexOID_Type())
tnLldpRemManAddrPortIndexOID.setMaxAccess(_B)
if mibBuilder.loadTexts:tnLldpRemManAddrPortIndexOID.setStatus(_A)
_TnLldpNotifications_ObjectIdentity=ObjectIdentity
tnLldpNotifications=_TnLldpNotifications_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,59))
mibBuilder.exportSymbols(_C,**{'TmnxLldpDestAddressTableIndex':TmnxLldpDestAddressTableIndex,'TmnxLldpManAddressIndex':TmnxLldpManAddressIndex,'tnLldpMIBModule':tnLldpMIBModule,'tnLldpObjects':tnLldpObjects,'tnLldpConfiguration':tnLldpConfiguration,'tnLldpConfigTable':tnLldpConfigTable,'tnLldpConfigEntry':tnLldpConfigEntry,'tnLldpMessageTxInterval':tnLldpMessageTxInterval,'tnLldpMessageTxHoldMultiplier':tnLldpMessageTxHoldMultiplier,'tnLldpReinitDelay':tnLldpReinitDelay,'tnLldpTxDelay':tnLldpTxDelay,'tnLldpNotificationInterval':tnLldpNotificationInterval,'tnLldpTxCreditMax':tnLldpTxCreditMax,'tnLldpMessageFastTx':tnLldpMessageFastTx,'tnLldpMessageFastTxInit':tnLldpMessageFastTxInit,'tnLldpAdminStatus':tnLldpAdminStatus,'tnLldpPortConfigTable':tnLldpPortConfigTable,'tnLldpPortConfigEntry':tnLldpPortConfigEntry,_P:tnLldpPortCfgDestAddressIndex,'tnLldpPortCfgAdminStatus':tnLldpPortCfgAdminStatus,'tnLldpPortCfgNotifyEnable':tnLldpPortCfgNotifyEnable,'tnLldpPortCfgTLVsTxEnable':tnLldpPortCfgTLVsTxEnable,'tnLldpConfigManAddrPortsTable':tnLldpConfigManAddrPortsTable,'tnLldpConfigManAddrPortsEntry':tnLldpConfigManAddrPortsEntry,_V:tnLldpPortCfgAddressIndex,'tnLldpPortCfgManAddrTxEnabled':tnLldpPortCfgManAddrTxEnabled,'tnLldpPortCfgManAddrSubtype':tnLldpPortCfgManAddrSubtype,'tnLldpPortCfgManAddress':tnLldpPortCfgManAddress,'tnLldpDestAddressTable':tnLldpDestAddressTable,'tnLldpDestAddressTableEntry':tnLldpDestAddressTableEntry,_W:tnLldpAddressTableIndex,'tnLldpDestMacAddress':tnLldpDestMacAddress,'tnLldpStatistics':tnLldpStatistics,'tnLldpStatsTxPortTable':tnLldpStatsTxPortTable,'tnLldpStatsTxPortEntry':tnLldpStatsTxPortEntry,_X:tnLldpStatsTxDestMACAddress,'tnLldpStatsTxPortFrames':tnLldpStatsTxPortFrames,'tnLldpStatsTxLLDPDULengthErrs':tnLldpStatsTxLLDPDULengthErrs,'tnLldpStatsRemTable':tnLldpStatsRemTable,'tnLldpStatsRemEntry':tnLldpStatsRemEntry,'tnLldpStatsRemTablesLastChangeTime':tnLldpStatsRemTablesLastChangeTime,'tnLldpStatsRemTablesInserts':tnLldpStatsRemTablesInserts,'tnLldpStatsRemTablesDeletes':tnLldpStatsRemTablesDeletes,'tnLldpStatsRemTablesDrops':tnLldpStatsRemTablesDrops,'tnLldpStatsRemTablesAgeouts':tnLldpStatsRemTablesAgeouts,'tnLldpStatsRxPortTable':tnLldpStatsRxPortTable,'tnLldpStatsRxPortEntry':tnLldpStatsRxPortEntry,_Y:tnLldpStatsRxDestMACAddress,'tnLldpStatsRxPortFrameDiscard':tnLldpStatsRxPortFrameDiscard,'tnLldpStatsRxPortFrameErrs':tnLldpStatsRxPortFrameErrs,'tnLldpStatsRxPortFrames':tnLldpStatsRxPortFrames,'tnLldpStatsRxPortTLVDiscard':tnLldpStatsRxPortTLVDiscard,'tnLldpStatsRxPortTLVUnknown':tnLldpStatsRxPortTLVUnknown,'tnLldpStatsRxPortAgeouts':tnLldpStatsRxPortAgeouts,'tnLldpStatsRxPortTtl':tnLldpStatsRxPortTtl,'tnLldpLocalSystemData':tnLldpLocalSystemData,'tnLldpLocSysDataTable':tnLldpLocSysDataTable,'tnLldpLocSysDataEntry':tnLldpLocSysDataEntry,'tnLldpLocChassisIdSubtype':tnLldpLocChassisIdSubtype,'tnLldpLocChassisId':tnLldpLocChassisId,'tnLldpLocSysName':tnLldpLocSysName,'tnLldpLocSysDesc':tnLldpLocSysDesc,'tnLldpLocSysCapSupported':tnLldpLocSysCapSupported,'tnLldpLocSysCapEnabled':tnLldpLocSysCapEnabled,'tnLldpLocPortTable':tnLldpLocPortTable,'tnLldpLocPortEntry':tnLldpLocPortEntry,_Z:tnLldpLocPortDestMACAddress,'tnLldpLocPortIdSubtype':tnLldpLocPortIdSubtype,'tnLldpLocPortId':tnLldpLocPortId,'tnLldpLocPortDesc':tnLldpLocPortDesc,'tnLldpLocManAddrTable':tnLldpLocManAddrTable,'tnLldpLocManAddrEntry':tnLldpLocManAddrEntry,_a:tnLldpLocManAddrSubtype,_b:tnLldpLocManAddr,'tnLldpLocManAddrLen':tnLldpLocManAddrLen,'tnLldpLocManAddrIfSubtype':tnLldpLocManAddrIfSubtype,'tnLldpLocManAddrIfId':tnLldpLocManAddrIfId,'tnLldpLocManAddrOID':tnLldpLocManAddrOID,'tnLldpRemoteSystemsData':tnLldpRemoteSystemsData,'tnLldpRemTable':tnLldpRemTable,'tnLldpRemEntry':tnLldpRemEntry,_M:tnLldpRemTimeMark,_N:tnLldpRemLocalDestMACAddress,_O:tnLldpRemIndex,'tnLldpRemChassisIdSubtype':tnLldpRemChassisIdSubtype,'tnLldpRemChassisId':tnLldpRemChassisId,'tnLldpRemPortIdSubtype':tnLldpRemPortIdSubtype,'tnLldpRemPortId':tnLldpRemPortId,'tnLldpRemPortDesc':tnLldpRemPortDesc,'tnLldpRemSysName':tnLldpRemSysName,'tnLldpRemSysDesc':tnLldpRemSysDesc,'tnLldpRemSysCapSupported':tnLldpRemSysCapSupported,'tnLldpRemSysCapEnabled':tnLldpRemSysCapEnabled,'tnLldpRemManAddrTable':tnLldpRemManAddrTable,'tnLldpRemManAddrEntry':tnLldpRemManAddrEntry,_R:tnLldpRemManAddrSubtype,_S:tnLldpRemManAddr,'tnLldpRemManAddrIfSubtype':tnLldpRemManAddrIfSubtype,'tnLldpRemManAddrIfId':tnLldpRemManAddrIfId,'tnLldpRemManAddrOID':tnLldpRemManAddrOID,'tnLldpRemPortIndexTable':tnLldpRemPortIndexTable,'tnLldpRemPortIndexEntry':tnLldpRemPortIndexEntry,'tnLldpRemPortIndexChassisIdSubtype':tnLldpRemPortIndexChassisIdSubtype,'tnLldpRemPortIndexChassisId':tnLldpRemPortIndexChassisId,'tnLldpRemPortIndexPortIdSubtype':tnLldpRemPortIndexPortIdSubtype,'tnLldpRemPortIndexPortId':tnLldpRemPortIndexPortId,'tnLldpRemPortIndexPortDesc':tnLldpRemPortIndexPortDesc,'tnLldpRemPortIndexSysName':tnLldpRemPortIndexSysName,'tnLldpRemPortIndexSysDesc':tnLldpRemPortIndexSysDesc,'tnLldpRemPortIndexSysCapSupported':tnLldpRemPortIndexSysCapSupported,'tnLldpRemPortIndexSysCapEnabled':tnLldpRemPortIndexSysCapEnabled,'tnLldpRemManAddrPortIndexTable':tnLldpRemManAddrPortIndexTable,'tnLldpRemManAddrPortIndexEntry':tnLldpRemManAddrPortIndexEntry,'tnLldpRemManAddrPortIndexIfSubtype':tnLldpRemManAddrPortIndexIfSubtype,'tnLldpRemManAddrPortIndexIfId':tnLldpRemManAddrPortIndexIfId,'tnLldpRemManAddrPortIndexOID':tnLldpRemManAddrPortIndexOID,'tnLldpNotifications':tnLldpNotifications})