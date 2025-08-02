_AO='tmnxLldpNotifV16v0Group'
_AN='tmnxLldpRemSysV16v0Group'
_AM='tmnxLldpConfigV13v0Group'
_AL='tmnxLldpConfigV11v0Group'
_AK='tmnxLldpRemManAddrEntryRemoved'
_AJ='tmnxLldpRemManAddrEntryAdded'
_AI='tmnxLldpRemEntryPeerRemoved'
_AH='tmnxLldpRemEntryPeerUpdated'
_AG='tmnxLldpRemEntryPeerAdded'
_AF='tmnxLldpRemSysAge'
_AE='tmnxLldpPortCfgPortIdSubtype'
_AD='tmnxLldpPortCfgTunnelNearestBrg'
_AC='tmnxLldpRemManAddrOID'
_AB='tmnxLldpRemManAddrIfSubtype'
_AA='tmnxLldpRemSysCapEnabled'
_A9='tmnxLldpRemSysCapSupported'
_A8='tmnxLldpRemSysDesc'
_A7='tmnxLldpRemPortDesc'
_A6='tmnxLldpLocPortDesc'
_A5='tmnxLldpLocPortId'
_A4='tmnxLldpLocPortIdSubtype'
_A3='tmnxLldpStatsTxLLDPDULengthErrs'
_A2='tmnxLldpStatsTxPortFrames'
_A1='tmnxLldpStatsRxPortAgeouts'
_A0='tmnxLldpStatsRxPortTLVUnknown'
_z='tmnxLldpStatsRxPortTLVDiscard'
_y='tmnxLldpStatsRxPortFrames'
_x='tmnxLldpStatsRxPortFrameErrs'
_w='tmnxLldpStatsRxPortFrameDiscard'
_v='tmnxLldpDestMacAddress'
_u='tmnxLldpPortCfgManAddress'
_t='tmnxLldpPortCfgManAddrSubtype'
_s='tmnxLldpPortCfgManAddrTxEnabled'
_r='tmnxLldpPortCfgTLVsTxEnable'
_q='tmnxLldpPortCfgNotifyEnable'
_p='tmnxLldpPortCfgAdminStatus'
_o='tmnxLldpAdminStatus'
_n='tmnxLldpMessageFastTxInit'
_m='tmnxLldpMessageFastTx'
_l='tmnxLldpTxCreditMax'
_k='tmnxLldpRemManAddr'
_j='tmnxLldpRemManAddrSubtype'
_i='tmnxLldpLocPortDestMACAddress'
_h='tmnxLldpStatsRxDestMACAddress'
_g='tmnxLldpStatsTxDestMACAddress'
_f='tmnxLldpAddressTableIndex'
_e='tmnxLldpPortCfgAddressIndex'
_d='disabled'
_c='seconds'
_b='TmnxEnabledDisabled'
_a='TruthValue'
_Z='LldpPortIdSubtype'
_Y='tmnxLldpRemManAddrGroup'
_X='tmnxLldpRemSysGroup'
_W='tmnxLldpLocSysGroup'
_V='tmnxLldpStatsTxGroup'
_U='tmnxLldpStatsRxGroup'
_T='tmnxLldpConfigGroup'
_S='tmnxLldpRemIndex'
_R='tmnxLldpRemLocalDestMACAddress'
_Q='tmnxLldpRemTimeMark'
_P='tmnxLldpPortCfgDestAddressIndex'
_O='tmnxLldpRemManAddrIfId'
_N='tmnxLldpRemSysName'
_M='tmnxLldpRemPortId'
_L='tmnxLldpRemPortIdSubtype'
_K='tmnxLldpRemChassisId'
_J='tmnxLldpRemChassisIdSubtype'
_I='SnmpAdminString'
_H='Integer32'
_G='ifIndex'
_F='IF-MIB'
_E='read-write'
_D='not-accessible'
_C='read-only'
_B='current'
_A='TIMETRA-LLDP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AddressFamilyNumbers,=mibBuilder.importSymbols('IANA-ADDRESS-FAMILY-NUMBERS-MIB','AddressFamilyNumbers')
ifIndex,=mibBuilder.importSymbols(_F,_G)
LldpChassisId,LldpChassisIdSubtype,LldpManAddrIfSubtype,LldpManAddress,LldpPortId,LldpPortIdSubtype,LldpSystemCapabilitiesMap=mibBuilder.importSymbols('LLDP-MIB','LldpChassisId','LldpChassisIdSubtype','LldpManAddrIfSubtype','LldpManAddress','LldpPortId',_Z,'LldpSystemCapabilitiesMap')
TimeFilter,ZeroBasedCounter32=mibBuilder.importSymbols('RMON2-MIB','TimeFilter','ZeroBasedCounter32')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_a)
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
TmnxEnabledDisabled,TmnxEnabledDisabledAdminState=mibBuilder.importSymbols('TIMETRA-TC-MIB',_b,'TmnxEnabledDisabledAdminState')
tmnxLldpMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,59))
if mibBuilder.loadTexts:tmnxLldpMIBModule.setRevisions(('2015-01-01 00:00','2009-02-28 00:00','2002-02-02 00:00'))
class TmnxLldpDestAddressTableIndex(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
class TmnxLldpManAddressIndex(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('oob',0),('system',1),('systemIpv6',2),('oobIpv6',3)))
_TmnxLldpConformance_ObjectIdentity=ObjectIdentity
tmnxLldpConformance=_TmnxLldpConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,59))
_TmnxLldpCompliances_ObjectIdentity=ObjectIdentity
tmnxLldpCompliances=_TmnxLldpCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,59,1))
_TmnxLldpGroups_ObjectIdentity=ObjectIdentity
tmnxLldpGroups=_TmnxLldpGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,59,2))
_TmnxLldpV11v0Groups_ObjectIdentity=ObjectIdentity
tmnxLldpV11v0Groups=_TmnxLldpV11v0Groups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,59,2,11))
_TmnxLldpV13v0Groups_ObjectIdentity=ObjectIdentity
tmnxLldpV13v0Groups=_TmnxLldpV13v0Groups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,59,2,12))
_TmnxLldpV16v0Groups_ObjectIdentity=ObjectIdentity
tmnxLldpV16v0Groups=_TmnxLldpV16v0Groups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,59,2,13))
_TmnxLldpObjects_ObjectIdentity=ObjectIdentity
tmnxLldpObjects=_TmnxLldpObjects_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,59))
_TmnxLldpConfiguration_ObjectIdentity=ObjectIdentity
tmnxLldpConfiguration=_TmnxLldpConfiguration_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,59,1))
class _TmnxLldpTxCreditMax_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_TmnxLldpTxCreditMax_Type.__name__=_H
_TmnxLldpTxCreditMax_Object=MibScalar
tmnxLldpTxCreditMax=_TmnxLldpTxCreditMax_Object((1,3,6,1,4,1,6527,3,1,2,59,1,1),_TmnxLldpTxCreditMax_Type())
tmnxLldpTxCreditMax.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxLldpTxCreditMax.setStatus(_B)
class _TmnxLldpMessageFastTx_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_TmnxLldpMessageFastTx_Type.__name__=_H
_TmnxLldpMessageFastTx_Object=MibScalar
tmnxLldpMessageFastTx=_TmnxLldpMessageFastTx_Object((1,3,6,1,4,1,6527,3,1,2,59,1,2),_TmnxLldpMessageFastTx_Type())
tmnxLldpMessageFastTx.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxLldpMessageFastTx.setStatus(_B)
if mibBuilder.loadTexts:tmnxLldpMessageFastTx.setUnits(_c)
class _TmnxLldpMessageFastTxInit_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_TmnxLldpMessageFastTxInit_Type.__name__=_H
_TmnxLldpMessageFastTxInit_Object=MibScalar
tmnxLldpMessageFastTxInit=_TmnxLldpMessageFastTxInit_Object((1,3,6,1,4,1,6527,3,1,2,59,1,3),_TmnxLldpMessageFastTxInit_Type())
tmnxLldpMessageFastTxInit.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxLldpMessageFastTxInit.setStatus(_B)
_TmnxLldpAdminStatus_Type=TmnxEnabledDisabledAdminState
_TmnxLldpAdminStatus_Object=MibScalar
tmnxLldpAdminStatus=_TmnxLldpAdminStatus_Object((1,3,6,1,4,1,6527,3,1,2,59,1,4),_TmnxLldpAdminStatus_Type())
tmnxLldpAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxLldpAdminStatus.setStatus(_B)
_TmnxLldpPortConfigTable_Object=MibTable
tmnxLldpPortConfigTable=_TmnxLldpPortConfigTable_Object((1,3,6,1,4,1,6527,3,1,2,59,1,5))
if mibBuilder.loadTexts:tmnxLldpPortConfigTable.setStatus(_B)
_TmnxLldpPortConfigEntry_Object=MibTableRow
tmnxLldpPortConfigEntry=_TmnxLldpPortConfigEntry_Object((1,3,6,1,4,1,6527,3,1,2,59,1,5,1))
tmnxLldpPortConfigEntry.setIndexNames((0,_F,_G),(0,_A,_P))
if mibBuilder.loadTexts:tmnxLldpPortConfigEntry.setStatus(_B)
_TmnxLldpPortCfgDestAddressIndex_Type=TmnxLldpDestAddressTableIndex
_TmnxLldpPortCfgDestAddressIndex_Object=MibTableColumn
tmnxLldpPortCfgDestAddressIndex=_TmnxLldpPortCfgDestAddressIndex_Object((1,3,6,1,4,1,6527,3,1,2,59,1,5,1,1),_TmnxLldpPortCfgDestAddressIndex_Type())
tmnxLldpPortCfgDestAddressIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxLldpPortCfgDestAddressIndex.setStatus(_B)
class _TmnxLldpPortCfgAdminStatus_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('txOnly',1),('rxOnly',2),('txAndRx',3),(_d,4)))
_TmnxLldpPortCfgAdminStatus_Type.__name__=_H
_TmnxLldpPortCfgAdminStatus_Object=MibTableColumn
tmnxLldpPortCfgAdminStatus=_TmnxLldpPortCfgAdminStatus_Object((1,3,6,1,4,1,6527,3,1,2,59,1,5,1,2),_TmnxLldpPortCfgAdminStatus_Type())
tmnxLldpPortCfgAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxLldpPortCfgAdminStatus.setStatus(_B)
class _TmnxLldpPortCfgNotifyEnable_Type(TruthValue):defaultValue=2
_TmnxLldpPortCfgNotifyEnable_Type.__name__=_a
_TmnxLldpPortCfgNotifyEnable_Object=MibTableColumn
tmnxLldpPortCfgNotifyEnable=_TmnxLldpPortCfgNotifyEnable_Object((1,3,6,1,4,1,6527,3,1,2,59,1,5,1,3),_TmnxLldpPortCfgNotifyEnable_Type())
tmnxLldpPortCfgNotifyEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxLldpPortCfgNotifyEnable.setStatus(_B)
class _TmnxLldpPortCfgTLVsTxEnable_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('portDesc',0),('sysName',1),('sysDesc',2),('sysCap',3)))
_TmnxLldpPortCfgTLVsTxEnable_Type.__name__='Bits'
_TmnxLldpPortCfgTLVsTxEnable_Object=MibTableColumn
tmnxLldpPortCfgTLVsTxEnable=_TmnxLldpPortCfgTLVsTxEnable_Object((1,3,6,1,4,1,6527,3,1,2,59,1,5,1,4),_TmnxLldpPortCfgTLVsTxEnable_Type())
tmnxLldpPortCfgTLVsTxEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxLldpPortCfgTLVsTxEnable.setStatus(_B)
class _TmnxLldpPortCfgTunnelNearestBrg_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('notApplicable',0),('enabled',1),(_d,2)))
_TmnxLldpPortCfgTunnelNearestBrg_Type.__name__=_H
_TmnxLldpPortCfgTunnelNearestBrg_Object=MibTableColumn
tmnxLldpPortCfgTunnelNearestBrg=_TmnxLldpPortCfgTunnelNearestBrg_Object((1,3,6,1,4,1,6527,3,1,2,59,1,5,1,5),_TmnxLldpPortCfgTunnelNearestBrg_Type())
tmnxLldpPortCfgTunnelNearestBrg.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxLldpPortCfgTunnelNearestBrg.setStatus(_B)
class _TmnxLldpPortCfgPortIdSubtype_Type(LldpPortIdSubtype):defaultValue=7
_TmnxLldpPortCfgPortIdSubtype_Type.__name__=_Z
_TmnxLldpPortCfgPortIdSubtype_Object=MibTableColumn
tmnxLldpPortCfgPortIdSubtype=_TmnxLldpPortCfgPortIdSubtype_Object((1,3,6,1,4,1,6527,3,1,2,59,1,5,1,6),_TmnxLldpPortCfgPortIdSubtype_Type())
tmnxLldpPortCfgPortIdSubtype.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxLldpPortCfgPortIdSubtype.setStatus(_B)
_TmnxLldpConfigManAddrPortsTable_Object=MibTable
tmnxLldpConfigManAddrPortsTable=_TmnxLldpConfigManAddrPortsTable_Object((1,3,6,1,4,1,6527,3,1,2,59,1,6))
if mibBuilder.loadTexts:tmnxLldpConfigManAddrPortsTable.setStatus(_B)
_TmnxLldpConfigManAddrPortsEntry_Object=MibTableRow
tmnxLldpConfigManAddrPortsEntry=_TmnxLldpConfigManAddrPortsEntry_Object((1,3,6,1,4,1,6527,3,1,2,59,1,6,1))
tmnxLldpConfigManAddrPortsEntry.setIndexNames((0,_F,_G),(0,_A,_P),(0,_A,_e))
if mibBuilder.loadTexts:tmnxLldpConfigManAddrPortsEntry.setStatus(_B)
_TmnxLldpPortCfgAddressIndex_Type=TmnxLldpManAddressIndex
_TmnxLldpPortCfgAddressIndex_Object=MibTableColumn
tmnxLldpPortCfgAddressIndex=_TmnxLldpPortCfgAddressIndex_Object((1,3,6,1,4,1,6527,3,1,2,59,1,6,1,1),_TmnxLldpPortCfgAddressIndex_Type())
tmnxLldpPortCfgAddressIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxLldpPortCfgAddressIndex.setStatus(_B)
class _TmnxLldpPortCfgManAddrTxEnabled_Type(TmnxEnabledDisabled):defaultValue=2
_TmnxLldpPortCfgManAddrTxEnabled_Type.__name__=_b
_TmnxLldpPortCfgManAddrTxEnabled_Object=MibTableColumn
tmnxLldpPortCfgManAddrTxEnabled=_TmnxLldpPortCfgManAddrTxEnabled_Object((1,3,6,1,4,1,6527,3,1,2,59,1,6,1,2),_TmnxLldpPortCfgManAddrTxEnabled_Type())
tmnxLldpPortCfgManAddrTxEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:tmnxLldpPortCfgManAddrTxEnabled.setStatus(_B)
_TmnxLldpPortCfgManAddrSubtype_Type=AddressFamilyNumbers
_TmnxLldpPortCfgManAddrSubtype_Object=MibTableColumn
tmnxLldpPortCfgManAddrSubtype=_TmnxLldpPortCfgManAddrSubtype_Object((1,3,6,1,4,1,6527,3,1,2,59,1,6,1,3),_TmnxLldpPortCfgManAddrSubtype_Type())
tmnxLldpPortCfgManAddrSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpPortCfgManAddrSubtype.setStatus(_B)
_TmnxLldpPortCfgManAddress_Type=LldpManAddress
_TmnxLldpPortCfgManAddress_Object=MibTableColumn
tmnxLldpPortCfgManAddress=_TmnxLldpPortCfgManAddress_Object((1,3,6,1,4,1,6527,3,1,2,59,1,6,1,4),_TmnxLldpPortCfgManAddress_Type())
tmnxLldpPortCfgManAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpPortCfgManAddress.setStatus(_B)
_TmnxLldpDestAddressTable_Object=MibTable
tmnxLldpDestAddressTable=_TmnxLldpDestAddressTable_Object((1,3,6,1,4,1,6527,3,1,2,59,1,7))
if mibBuilder.loadTexts:tmnxLldpDestAddressTable.setStatus(_B)
_TmnxLldpDestAddressTableEntry_Object=MibTableRow
tmnxLldpDestAddressTableEntry=_TmnxLldpDestAddressTableEntry_Object((1,3,6,1,4,1,6527,3,1,2,59,1,7,1))
tmnxLldpDestAddressTableEntry.setIndexNames((0,_A,_f))
if mibBuilder.loadTexts:tmnxLldpDestAddressTableEntry.setStatus(_B)
_TmnxLldpAddressTableIndex_Type=TmnxLldpDestAddressTableIndex
_TmnxLldpAddressTableIndex_Object=MibTableColumn
tmnxLldpAddressTableIndex=_TmnxLldpAddressTableIndex_Object((1,3,6,1,4,1,6527,3,1,2,59,1,7,1,1),_TmnxLldpAddressTableIndex_Type())
tmnxLldpAddressTableIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxLldpAddressTableIndex.setStatus(_B)
_TmnxLldpDestMacAddress_Type=MacAddress
_TmnxLldpDestMacAddress_Object=MibTableColumn
tmnxLldpDestMacAddress=_TmnxLldpDestMacAddress_Object((1,3,6,1,4,1,6527,3,1,2,59,1,7,1,2),_TmnxLldpDestMacAddress_Type())
tmnxLldpDestMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpDestMacAddress.setStatus(_B)
_TmnxLldpStatistics_ObjectIdentity=ObjectIdentity
tmnxLldpStatistics=_TmnxLldpStatistics_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,59,2))
_TmnxLldpStatsTxPortTable_Object=MibTable
tmnxLldpStatsTxPortTable=_TmnxLldpStatsTxPortTable_Object((1,3,6,1,4,1,6527,3,1,2,59,2,1))
if mibBuilder.loadTexts:tmnxLldpStatsTxPortTable.setStatus(_B)
_TmnxLldpStatsTxPortEntry_Object=MibTableRow
tmnxLldpStatsTxPortEntry=_TmnxLldpStatsTxPortEntry_Object((1,3,6,1,4,1,6527,3,1,2,59,2,1,1))
tmnxLldpStatsTxPortEntry.setIndexNames((0,_F,_G),(0,_A,_g))
if mibBuilder.loadTexts:tmnxLldpStatsTxPortEntry.setStatus(_B)
_TmnxLldpStatsTxDestMACAddress_Type=TmnxLldpDestAddressTableIndex
_TmnxLldpStatsTxDestMACAddress_Object=MibTableColumn
tmnxLldpStatsTxDestMACAddress=_TmnxLldpStatsTxDestMACAddress_Object((1,3,6,1,4,1,6527,3,1,2,59,2,1,1,1),_TmnxLldpStatsTxDestMACAddress_Type())
tmnxLldpStatsTxDestMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxLldpStatsTxDestMACAddress.setStatus(_B)
_TmnxLldpStatsTxPortFrames_Type=Counter32
_TmnxLldpStatsTxPortFrames_Object=MibTableColumn
tmnxLldpStatsTxPortFrames=_TmnxLldpStatsTxPortFrames_Object((1,3,6,1,4,1,6527,3,1,2,59,2,1,1,2),_TmnxLldpStatsTxPortFrames_Type())
tmnxLldpStatsTxPortFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpStatsTxPortFrames.setStatus(_B)
_TmnxLldpStatsTxLLDPDULengthErrs_Type=Counter32
_TmnxLldpStatsTxLLDPDULengthErrs_Object=MibTableColumn
tmnxLldpStatsTxLLDPDULengthErrs=_TmnxLldpStatsTxLLDPDULengthErrs_Object((1,3,6,1,4,1,6527,3,1,2,59,2,1,1,3),_TmnxLldpStatsTxLLDPDULengthErrs_Type())
tmnxLldpStatsTxLLDPDULengthErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpStatsTxLLDPDULengthErrs.setStatus(_B)
_TmnxLldpStatsRxPortTable_Object=MibTable
tmnxLldpStatsRxPortTable=_TmnxLldpStatsRxPortTable_Object((1,3,6,1,4,1,6527,3,1,2,59,2,2))
if mibBuilder.loadTexts:tmnxLldpStatsRxPortTable.setStatus(_B)
_TmnxLldpStatsRxPortEntry_Object=MibTableRow
tmnxLldpStatsRxPortEntry=_TmnxLldpStatsRxPortEntry_Object((1,3,6,1,4,1,6527,3,1,2,59,2,2,1))
tmnxLldpStatsRxPortEntry.setIndexNames((0,_F,_G),(0,_A,_h))
if mibBuilder.loadTexts:tmnxLldpStatsRxPortEntry.setStatus(_B)
_TmnxLldpStatsRxDestMACAddress_Type=TmnxLldpDestAddressTableIndex
_TmnxLldpStatsRxDestMACAddress_Object=MibTableColumn
tmnxLldpStatsRxDestMACAddress=_TmnxLldpStatsRxDestMACAddress_Object((1,3,6,1,4,1,6527,3,1,2,59,2,2,1,1),_TmnxLldpStatsRxDestMACAddress_Type())
tmnxLldpStatsRxDestMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxLldpStatsRxDestMACAddress.setStatus(_B)
_TmnxLldpStatsRxPortFrameDiscard_Type=Counter32
_TmnxLldpStatsRxPortFrameDiscard_Object=MibTableColumn
tmnxLldpStatsRxPortFrameDiscard=_TmnxLldpStatsRxPortFrameDiscard_Object((1,3,6,1,4,1,6527,3,1,2,59,2,2,1,2),_TmnxLldpStatsRxPortFrameDiscard_Type())
tmnxLldpStatsRxPortFrameDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpStatsRxPortFrameDiscard.setStatus(_B)
_TmnxLldpStatsRxPortFrameErrs_Type=Counter32
_TmnxLldpStatsRxPortFrameErrs_Object=MibTableColumn
tmnxLldpStatsRxPortFrameErrs=_TmnxLldpStatsRxPortFrameErrs_Object((1,3,6,1,4,1,6527,3,1,2,59,2,2,1,3),_TmnxLldpStatsRxPortFrameErrs_Type())
tmnxLldpStatsRxPortFrameErrs.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpStatsRxPortFrameErrs.setStatus(_B)
_TmnxLldpStatsRxPortFrames_Type=Counter32
_TmnxLldpStatsRxPortFrames_Object=MibTableColumn
tmnxLldpStatsRxPortFrames=_TmnxLldpStatsRxPortFrames_Object((1,3,6,1,4,1,6527,3,1,2,59,2,2,1,4),_TmnxLldpStatsRxPortFrames_Type())
tmnxLldpStatsRxPortFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpStatsRxPortFrames.setStatus(_B)
_TmnxLldpStatsRxPortTLVDiscard_Type=Counter32
_TmnxLldpStatsRxPortTLVDiscard_Object=MibTableColumn
tmnxLldpStatsRxPortTLVDiscard=_TmnxLldpStatsRxPortTLVDiscard_Object((1,3,6,1,4,1,6527,3,1,2,59,2,2,1,5),_TmnxLldpStatsRxPortTLVDiscard_Type())
tmnxLldpStatsRxPortTLVDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpStatsRxPortTLVDiscard.setStatus(_B)
_TmnxLldpStatsRxPortTLVUnknown_Type=Counter32
_TmnxLldpStatsRxPortTLVUnknown_Object=MibTableColumn
tmnxLldpStatsRxPortTLVUnknown=_TmnxLldpStatsRxPortTLVUnknown_Object((1,3,6,1,4,1,6527,3,1,2,59,2,2,1,6),_TmnxLldpStatsRxPortTLVUnknown_Type())
tmnxLldpStatsRxPortTLVUnknown.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpStatsRxPortTLVUnknown.setStatus(_B)
_TmnxLldpStatsRxPortAgeouts_Type=ZeroBasedCounter32
_TmnxLldpStatsRxPortAgeouts_Object=MibTableColumn
tmnxLldpStatsRxPortAgeouts=_TmnxLldpStatsRxPortAgeouts_Object((1,3,6,1,4,1,6527,3,1,2,59,2,2,1,7),_TmnxLldpStatsRxPortAgeouts_Type())
tmnxLldpStatsRxPortAgeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpStatsRxPortAgeouts.setStatus(_B)
_TmnxLldpLocalSystemData_ObjectIdentity=ObjectIdentity
tmnxLldpLocalSystemData=_TmnxLldpLocalSystemData_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,59,3))
_TmnxLldpLocPortTable_Object=MibTable
tmnxLldpLocPortTable=_TmnxLldpLocPortTable_Object((1,3,6,1,4,1,6527,3,1,2,59,3,1))
if mibBuilder.loadTexts:tmnxLldpLocPortTable.setStatus(_B)
_TmnxLldpLocPortEntry_Object=MibTableRow
tmnxLldpLocPortEntry=_TmnxLldpLocPortEntry_Object((1,3,6,1,4,1,6527,3,1,2,59,3,1,1))
tmnxLldpLocPortEntry.setIndexNames((0,_F,_G),(0,_A,_i))
if mibBuilder.loadTexts:tmnxLldpLocPortEntry.setStatus(_B)
_TmnxLldpLocPortDestMACAddress_Type=TmnxLldpDestAddressTableIndex
_TmnxLldpLocPortDestMACAddress_Object=MibTableColumn
tmnxLldpLocPortDestMACAddress=_TmnxLldpLocPortDestMACAddress_Object((1,3,6,1,4,1,6527,3,1,2,59,3,1,1,1),_TmnxLldpLocPortDestMACAddress_Type())
tmnxLldpLocPortDestMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxLldpLocPortDestMACAddress.setStatus(_B)
_TmnxLldpLocPortIdSubtype_Type=LldpPortIdSubtype
_TmnxLldpLocPortIdSubtype_Object=MibTableColumn
tmnxLldpLocPortIdSubtype=_TmnxLldpLocPortIdSubtype_Object((1,3,6,1,4,1,6527,3,1,2,59,3,1,1,2),_TmnxLldpLocPortIdSubtype_Type())
tmnxLldpLocPortIdSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpLocPortIdSubtype.setStatus(_B)
_TmnxLldpLocPortId_Type=LldpPortId
_TmnxLldpLocPortId_Object=MibTableColumn
tmnxLldpLocPortId=_TmnxLldpLocPortId_Object((1,3,6,1,4,1,6527,3,1,2,59,3,1,1,3),_TmnxLldpLocPortId_Type())
tmnxLldpLocPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpLocPortId.setStatus(_B)
class _TmnxLldpLocPortDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TmnxLldpLocPortDesc_Type.__name__=_I
_TmnxLldpLocPortDesc_Object=MibTableColumn
tmnxLldpLocPortDesc=_TmnxLldpLocPortDesc_Object((1,3,6,1,4,1,6527,3,1,2,59,3,1,1,4),_TmnxLldpLocPortDesc_Type())
tmnxLldpLocPortDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpLocPortDesc.setStatus(_B)
_TmnxLldpRemoteSystemsData_ObjectIdentity=ObjectIdentity
tmnxLldpRemoteSystemsData=_TmnxLldpRemoteSystemsData_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,59,4))
_TmnxLldpRemTable_Object=MibTable
tmnxLldpRemTable=_TmnxLldpRemTable_Object((1,3,6,1,4,1,6527,3,1,2,59,4,1))
if mibBuilder.loadTexts:tmnxLldpRemTable.setStatus(_B)
_TmnxLldpRemEntry_Object=MibTableRow
tmnxLldpRemEntry=_TmnxLldpRemEntry_Object((1,3,6,1,4,1,6527,3,1,2,59,4,1,1))
tmnxLldpRemEntry.setIndexNames((0,_A,_Q),(0,_F,_G),(0,_A,_R),(0,_A,_S))
if mibBuilder.loadTexts:tmnxLldpRemEntry.setStatus(_B)
_TmnxLldpRemTimeMark_Type=TimeFilter
_TmnxLldpRemTimeMark_Object=MibTableColumn
tmnxLldpRemTimeMark=_TmnxLldpRemTimeMark_Object((1,3,6,1,4,1,6527,3,1,2,59,4,1,1,1),_TmnxLldpRemTimeMark_Type())
tmnxLldpRemTimeMark.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxLldpRemTimeMark.setStatus(_B)
_TmnxLldpRemLocalDestMACAddress_Type=TmnxLldpDestAddressTableIndex
_TmnxLldpRemLocalDestMACAddress_Object=MibTableColumn
tmnxLldpRemLocalDestMACAddress=_TmnxLldpRemLocalDestMACAddress_Object((1,3,6,1,4,1,6527,3,1,2,59,4,1,1,2),_TmnxLldpRemLocalDestMACAddress_Type())
tmnxLldpRemLocalDestMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxLldpRemLocalDestMACAddress.setStatus(_B)
class _TmnxLldpRemIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TmnxLldpRemIndex_Type.__name__=_H
_TmnxLldpRemIndex_Object=MibTableColumn
tmnxLldpRemIndex=_TmnxLldpRemIndex_Object((1,3,6,1,4,1,6527,3,1,2,59,4,1,1,3),_TmnxLldpRemIndex_Type())
tmnxLldpRemIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxLldpRemIndex.setStatus(_B)
_TmnxLldpRemChassisIdSubtype_Type=LldpChassisIdSubtype
_TmnxLldpRemChassisIdSubtype_Object=MibTableColumn
tmnxLldpRemChassisIdSubtype=_TmnxLldpRemChassisIdSubtype_Object((1,3,6,1,4,1,6527,3,1,2,59,4,1,1,4),_TmnxLldpRemChassisIdSubtype_Type())
tmnxLldpRemChassisIdSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpRemChassisIdSubtype.setStatus(_B)
_TmnxLldpRemChassisId_Type=LldpChassisId
_TmnxLldpRemChassisId_Object=MibTableColumn
tmnxLldpRemChassisId=_TmnxLldpRemChassisId_Object((1,3,6,1,4,1,6527,3,1,2,59,4,1,1,5),_TmnxLldpRemChassisId_Type())
tmnxLldpRemChassisId.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpRemChassisId.setStatus(_B)
_TmnxLldpRemPortIdSubtype_Type=LldpPortIdSubtype
_TmnxLldpRemPortIdSubtype_Object=MibTableColumn
tmnxLldpRemPortIdSubtype=_TmnxLldpRemPortIdSubtype_Object((1,3,6,1,4,1,6527,3,1,2,59,4,1,1,6),_TmnxLldpRemPortIdSubtype_Type())
tmnxLldpRemPortIdSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpRemPortIdSubtype.setStatus(_B)
_TmnxLldpRemPortId_Type=LldpPortId
_TmnxLldpRemPortId_Object=MibTableColumn
tmnxLldpRemPortId=_TmnxLldpRemPortId_Object((1,3,6,1,4,1,6527,3,1,2,59,4,1,1,7),_TmnxLldpRemPortId_Type())
tmnxLldpRemPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpRemPortId.setStatus(_B)
class _TmnxLldpRemPortDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TmnxLldpRemPortDesc_Type.__name__=_I
_TmnxLldpRemPortDesc_Object=MibTableColumn
tmnxLldpRemPortDesc=_TmnxLldpRemPortDesc_Object((1,3,6,1,4,1,6527,3,1,2,59,4,1,1,8),_TmnxLldpRemPortDesc_Type())
tmnxLldpRemPortDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpRemPortDesc.setStatus(_B)
class _TmnxLldpRemSysName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TmnxLldpRemSysName_Type.__name__=_I
_TmnxLldpRemSysName_Object=MibTableColumn
tmnxLldpRemSysName=_TmnxLldpRemSysName_Object((1,3,6,1,4,1,6527,3,1,2,59,4,1,1,9),_TmnxLldpRemSysName_Type())
tmnxLldpRemSysName.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpRemSysName.setStatus(_B)
class _TmnxLldpRemSysDesc_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TmnxLldpRemSysDesc_Type.__name__=_I
_TmnxLldpRemSysDesc_Object=MibTableColumn
tmnxLldpRemSysDesc=_TmnxLldpRemSysDesc_Object((1,3,6,1,4,1,6527,3,1,2,59,4,1,1,10),_TmnxLldpRemSysDesc_Type())
tmnxLldpRemSysDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpRemSysDesc.setStatus(_B)
_TmnxLldpRemSysCapSupported_Type=LldpSystemCapabilitiesMap
_TmnxLldpRemSysCapSupported_Object=MibTableColumn
tmnxLldpRemSysCapSupported=_TmnxLldpRemSysCapSupported_Object((1,3,6,1,4,1,6527,3,1,2,59,4,1,1,11),_TmnxLldpRemSysCapSupported_Type())
tmnxLldpRemSysCapSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpRemSysCapSupported.setStatus(_B)
_TmnxLldpRemSysCapEnabled_Type=LldpSystemCapabilitiesMap
_TmnxLldpRemSysCapEnabled_Object=MibTableColumn
tmnxLldpRemSysCapEnabled=_TmnxLldpRemSysCapEnabled_Object((1,3,6,1,4,1,6527,3,1,2,59,4,1,1,12),_TmnxLldpRemSysCapEnabled_Type())
tmnxLldpRemSysCapEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpRemSysCapEnabled.setStatus(_B)
_TmnxLldpRemSysAge_Type=Counter64
_TmnxLldpRemSysAge_Object=MibTableColumn
tmnxLldpRemSysAge=_TmnxLldpRemSysAge_Object((1,3,6,1,4,1,6527,3,1,2,59,4,1,1,13),_TmnxLldpRemSysAge_Type())
tmnxLldpRemSysAge.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpRemSysAge.setStatus(_B)
if mibBuilder.loadTexts:tmnxLldpRemSysAge.setUnits(_c)
_TmnxLldpRemManAddrTable_Object=MibTable
tmnxLldpRemManAddrTable=_TmnxLldpRemManAddrTable_Object((1,3,6,1,4,1,6527,3,1,2,59,4,2))
if mibBuilder.loadTexts:tmnxLldpRemManAddrTable.setStatus(_B)
_TmnxLldpRemManAddrEntry_Object=MibTableRow
tmnxLldpRemManAddrEntry=_TmnxLldpRemManAddrEntry_Object((1,3,6,1,4,1,6527,3,1,2,59,4,2,1))
tmnxLldpRemManAddrEntry.setIndexNames((0,_A,_Q),(0,_F,_G),(0,_A,_R),(0,_A,_S),(0,_A,_j),(0,_A,_k))
if mibBuilder.loadTexts:tmnxLldpRemManAddrEntry.setStatus(_B)
_TmnxLldpRemManAddrSubtype_Type=AddressFamilyNumbers
_TmnxLldpRemManAddrSubtype_Object=MibTableColumn
tmnxLldpRemManAddrSubtype=_TmnxLldpRemManAddrSubtype_Object((1,3,6,1,4,1,6527,3,1,2,59,4,2,1,1),_TmnxLldpRemManAddrSubtype_Type())
tmnxLldpRemManAddrSubtype.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxLldpRemManAddrSubtype.setStatus(_B)
_TmnxLldpRemManAddr_Type=LldpManAddress
_TmnxLldpRemManAddr_Object=MibTableColumn
tmnxLldpRemManAddr=_TmnxLldpRemManAddr_Object((1,3,6,1,4,1,6527,3,1,2,59,4,2,1,2),_TmnxLldpRemManAddr_Type())
tmnxLldpRemManAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxLldpRemManAddr.setStatus(_B)
_TmnxLldpRemManAddrIfSubtype_Type=LldpManAddrIfSubtype
_TmnxLldpRemManAddrIfSubtype_Object=MibTableColumn
tmnxLldpRemManAddrIfSubtype=_TmnxLldpRemManAddrIfSubtype_Object((1,3,6,1,4,1,6527,3,1,2,59,4,2,1,3),_TmnxLldpRemManAddrIfSubtype_Type())
tmnxLldpRemManAddrIfSubtype.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpRemManAddrIfSubtype.setStatus(_B)
_TmnxLldpRemManAddrIfId_Type=Integer32
_TmnxLldpRemManAddrIfId_Object=MibTableColumn
tmnxLldpRemManAddrIfId=_TmnxLldpRemManAddrIfId_Object((1,3,6,1,4,1,6527,3,1,2,59,4,2,1,4),_TmnxLldpRemManAddrIfId_Type())
tmnxLldpRemManAddrIfId.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpRemManAddrIfId.setStatus(_B)
_TmnxLldpRemManAddrOID_Type=ObjectIdentifier
_TmnxLldpRemManAddrOID_Object=MibTableColumn
tmnxLldpRemManAddrOID=_TmnxLldpRemManAddrOID_Object((1,3,6,1,4,1,6527,3,1,2,59,4,2,1,5),_TmnxLldpRemManAddrOID_Type())
tmnxLldpRemManAddrOID.setMaxAccess(_C)
if mibBuilder.loadTexts:tmnxLldpRemManAddrOID.setStatus(_B)
_TmnxLldpNotifications_ObjectIdentity=ObjectIdentity
tmnxLldpNotifications=_TmnxLldpNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,59))
_TmnxLldpNotifs_ObjectIdentity=ObjectIdentity
tmnxLldpNotifs=_TmnxLldpNotifs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,59,0))
tmnxLldpConfigGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,59,2,1))
tmnxLldpConfigGroup.setObjects(*((_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v)))
if mibBuilder.loadTexts:tmnxLldpConfigGroup.setStatus(_B)
tmnxLldpStatsRxGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,59,2,2))
tmnxLldpStatsRxGroup.setObjects(*((_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:tmnxLldpStatsRxGroup.setStatus(_B)
tmnxLldpStatsTxGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,59,2,3))
tmnxLldpStatsTxGroup.setObjects(*((_A,_A2),(_A,_A3)))
if mibBuilder.loadTexts:tmnxLldpStatsTxGroup.setStatus(_B)
tmnxLldpLocSysGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,59,2,4))
tmnxLldpLocSysGroup.setObjects(*((_A,_A4),(_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:tmnxLldpLocSysGroup.setStatus(_B)
tmnxLldpRemSysGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,59,2,5))
tmnxLldpRemSysGroup.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_A7),(_A,_N),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:tmnxLldpRemSysGroup.setStatus(_B)
tmnxLldpRemManAddrGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,59,2,6))
tmnxLldpRemManAddrGroup.setObjects(*((_A,_AB),(_A,_O),(_A,_AC)))
if mibBuilder.loadTexts:tmnxLldpRemManAddrGroup.setStatus(_B)
tmnxLldpConfigV11v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,59,2,11,1))
tmnxLldpConfigV11v0Group.setObjects((_A,_AD))
if mibBuilder.loadTexts:tmnxLldpConfigV11v0Group.setStatus(_B)
tmnxLldpConfigV13v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,59,2,12,1))
tmnxLldpConfigV13v0Group.setObjects((_A,_AE))
if mibBuilder.loadTexts:tmnxLldpConfigV13v0Group.setStatus(_B)
tmnxLldpRemSysV16v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,59,2,13,1))
tmnxLldpRemSysV16v0Group.setObjects((_A,_AF))
if mibBuilder.loadTexts:tmnxLldpRemSysV16v0Group.setStatus(_B)
tmnxLldpRemEntryPeerAdded=NotificationType((1,3,6,1,4,1,6527,3,1,3,59,0,1))
tmnxLldpRemEntryPeerAdded.setObjects(*((_A,_N),(_A,_K),(_A,_J),(_A,_M),(_A,_L)))
if mibBuilder.loadTexts:tmnxLldpRemEntryPeerAdded.setStatus(_B)
tmnxLldpRemEntryPeerUpdated=NotificationType((1,3,6,1,4,1,6527,3,1,3,59,0,2))
tmnxLldpRemEntryPeerUpdated.setObjects(*((_A,_N),(_A,_K),(_A,_J),(_A,_M),(_A,_L)))
if mibBuilder.loadTexts:tmnxLldpRemEntryPeerUpdated.setStatus(_B)
tmnxLldpRemEntryPeerRemoved=NotificationType((1,3,6,1,4,1,6527,3,1,3,59,0,3))
tmnxLldpRemEntryPeerRemoved.setObjects(*((_A,_N),(_A,_K),(_A,_J),(_A,_M),(_A,_L)))
if mibBuilder.loadTexts:tmnxLldpRemEntryPeerRemoved.setStatus(_B)
tmnxLldpRemManAddrEntryAdded=NotificationType((1,3,6,1,4,1,6527,3,1,3,59,0,4))
tmnxLldpRemManAddrEntryAdded.setObjects((_A,_O))
if mibBuilder.loadTexts:tmnxLldpRemManAddrEntryAdded.setStatus(_B)
tmnxLldpRemManAddrEntryRemoved=NotificationType((1,3,6,1,4,1,6527,3,1,3,59,0,5))
tmnxLldpRemManAddrEntryRemoved.setObjects((_A,_O))
if mibBuilder.loadTexts:tmnxLldpRemManAddrEntryRemoved.setStatus(_B)
tmnxLldpNotifV16v0Group=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,59,2,13,2))
tmnxLldpNotifV16v0Group.setObjects(*((_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:tmnxLldpNotifV16v0Group.setStatus(_B)
tmnxLldpCompliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,59,1,1))
tmnxLldpCompliance.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:tmnxLldpCompliance.setStatus('obsolete')
tmnxLldpV11v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,59,1,2))
tmnxLldpV11v0Compliance.setObjects(*((_A,_T),(_A,_AL),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:tmnxLldpV11v0Compliance.setStatus(_B)
tmnxLldpV13v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,59,1,3))
tmnxLldpV13v0Compliance.setObjects((_A,_AM))
if mibBuilder.loadTexts:tmnxLldpV13v0Compliance.setStatus(_B)
tmnxLldpV16v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,59,1,4))
tmnxLldpV16v0Compliance.setObjects(*((_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:tmnxLldpV16v0Compliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'TmnxLldpDestAddressTableIndex':TmnxLldpDestAddressTableIndex,'TmnxLldpManAddressIndex':TmnxLldpManAddressIndex,'tmnxLldpMIBModule':tmnxLldpMIBModule,'tmnxLldpConformance':tmnxLldpConformance,'tmnxLldpCompliances':tmnxLldpCompliances,'tmnxLldpCompliance':tmnxLldpCompliance,'tmnxLldpV11v0Compliance':tmnxLldpV11v0Compliance,'tmnxLldpV13v0Compliance':tmnxLldpV13v0Compliance,'tmnxLldpV16v0Compliance':tmnxLldpV16v0Compliance,'tmnxLldpGroups':tmnxLldpGroups,_T:tmnxLldpConfigGroup,_U:tmnxLldpStatsRxGroup,_V:tmnxLldpStatsTxGroup,_W:tmnxLldpLocSysGroup,_X:tmnxLldpRemSysGroup,_Y:tmnxLldpRemManAddrGroup,'tmnxLldpV11v0Groups':tmnxLldpV11v0Groups,_AL:tmnxLldpConfigV11v0Group,'tmnxLldpV13v0Groups':tmnxLldpV13v0Groups,_AM:tmnxLldpConfigV13v0Group,'tmnxLldpV16v0Groups':tmnxLldpV16v0Groups,_AN:tmnxLldpRemSysV16v0Group,_AO:tmnxLldpNotifV16v0Group,'tmnxLldpObjects':tmnxLldpObjects,'tmnxLldpConfiguration':tmnxLldpConfiguration,_l:tmnxLldpTxCreditMax,_m:tmnxLldpMessageFastTx,_n:tmnxLldpMessageFastTxInit,_o:tmnxLldpAdminStatus,'tmnxLldpPortConfigTable':tmnxLldpPortConfigTable,'tmnxLldpPortConfigEntry':tmnxLldpPortConfigEntry,_P:tmnxLldpPortCfgDestAddressIndex,_p:tmnxLldpPortCfgAdminStatus,_q:tmnxLldpPortCfgNotifyEnable,_r:tmnxLldpPortCfgTLVsTxEnable,_AD:tmnxLldpPortCfgTunnelNearestBrg,_AE:tmnxLldpPortCfgPortIdSubtype,'tmnxLldpConfigManAddrPortsTable':tmnxLldpConfigManAddrPortsTable,'tmnxLldpConfigManAddrPortsEntry':tmnxLldpConfigManAddrPortsEntry,_e:tmnxLldpPortCfgAddressIndex,_s:tmnxLldpPortCfgManAddrTxEnabled,_t:tmnxLldpPortCfgManAddrSubtype,_u:tmnxLldpPortCfgManAddress,'tmnxLldpDestAddressTable':tmnxLldpDestAddressTable,'tmnxLldpDestAddressTableEntry':tmnxLldpDestAddressTableEntry,_f:tmnxLldpAddressTableIndex,_v:tmnxLldpDestMacAddress,'tmnxLldpStatistics':tmnxLldpStatistics,'tmnxLldpStatsTxPortTable':tmnxLldpStatsTxPortTable,'tmnxLldpStatsTxPortEntry':tmnxLldpStatsTxPortEntry,_g:tmnxLldpStatsTxDestMACAddress,_A2:tmnxLldpStatsTxPortFrames,_A3:tmnxLldpStatsTxLLDPDULengthErrs,'tmnxLldpStatsRxPortTable':tmnxLldpStatsRxPortTable,'tmnxLldpStatsRxPortEntry':tmnxLldpStatsRxPortEntry,_h:tmnxLldpStatsRxDestMACAddress,_w:tmnxLldpStatsRxPortFrameDiscard,_x:tmnxLldpStatsRxPortFrameErrs,_y:tmnxLldpStatsRxPortFrames,_z:tmnxLldpStatsRxPortTLVDiscard,_A0:tmnxLldpStatsRxPortTLVUnknown,_A1:tmnxLldpStatsRxPortAgeouts,'tmnxLldpLocalSystemData':tmnxLldpLocalSystemData,'tmnxLldpLocPortTable':tmnxLldpLocPortTable,'tmnxLldpLocPortEntry':tmnxLldpLocPortEntry,_i:tmnxLldpLocPortDestMACAddress,_A4:tmnxLldpLocPortIdSubtype,_A5:tmnxLldpLocPortId,_A6:tmnxLldpLocPortDesc,'tmnxLldpRemoteSystemsData':tmnxLldpRemoteSystemsData,'tmnxLldpRemTable':tmnxLldpRemTable,'tmnxLldpRemEntry':tmnxLldpRemEntry,_Q:tmnxLldpRemTimeMark,_R:tmnxLldpRemLocalDestMACAddress,_S:tmnxLldpRemIndex,_J:tmnxLldpRemChassisIdSubtype,_K:tmnxLldpRemChassisId,_L:tmnxLldpRemPortIdSubtype,_M:tmnxLldpRemPortId,_A7:tmnxLldpRemPortDesc,_N:tmnxLldpRemSysName,_A8:tmnxLldpRemSysDesc,_A9:tmnxLldpRemSysCapSupported,_AA:tmnxLldpRemSysCapEnabled,_AF:tmnxLldpRemSysAge,'tmnxLldpRemManAddrTable':tmnxLldpRemManAddrTable,'tmnxLldpRemManAddrEntry':tmnxLldpRemManAddrEntry,_j:tmnxLldpRemManAddrSubtype,_k:tmnxLldpRemManAddr,_AB:tmnxLldpRemManAddrIfSubtype,_O:tmnxLldpRemManAddrIfId,_AC:tmnxLldpRemManAddrOID,'tmnxLldpNotifications':tmnxLldpNotifications,'tmnxLldpNotifs':tmnxLldpNotifs,_AG:tmnxLldpRemEntryPeerAdded,_AH:tmnxLldpRemEntryPeerUpdated,_AI:tmnxLldpRemEntryPeerRemoved,_AJ:tmnxLldpRemManAddrEntryAdded,_AK:tmnxLldpRemManAddrEntryRemoved})