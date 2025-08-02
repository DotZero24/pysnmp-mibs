_v='hwUserlogMandatoryGroup'
_u='hwUserlogAccessFailedPackets'
_t='hwUserlogAccessFailedEntries'
_s='hwUserlogAccessTotalPackets'
_r='hwUserlogAccessTotalEntries'
_q='hwUserlogFlowFailedPackets'
_p='hwUserlogFlowFailedEntries'
_o='hwUserlogFlowTotalPackets'
_n='hwUserlogFlowTotalEntries'
_m='hwUserlogNatFailedPackets'
_l='hwUserlogNatFailedEntries'
_k='hwUserlogNatTotalPackets'
_j='hwUserlogNatTotalEntries'
_i='hwUserlogAccessSourceIP'
_h='hwUserlogAccessSyslog'
_g='hwUserlogAccessVersion'
_f='hwUserlogFlowAclNumber'
_e='hwUserlogFlowActiveTime'
_d='hwUserlogFlowFlowBegin'
_c='hwUserlogFlowSourceIP'
_b='hwUserlogFlowSyslog'
_a='hwUserlogFlowVersion'
_Z='hwUserlogNatAclNumber'
_Y='hwUserlogNatActiveTime'
_X='hwUserlogNatFlowBegin'
_W='hwUserlogNatSourceIP'
_V='hwUserlogNatSyslog'
_U='hwUserlogNatVersion'
_T='hwUserlogAccessRunSlotNumber'
_S='hwUserlogFlowRunSlotNumber'
_R='hwUserlogNatRunSlotNumber'
_Q='hwUserlogAccessUdpPort'
_P='hwUserlogAccessHostAddress'
_O='hwUserlogAccessEnable'
_N='hwUserlogFlowUdpPort'
_M='hwUserlogFlowHostAddress'
_L='hwUserlogFlowEnable'
_K='hwUserlogNatUdpPort'
_J='hwUserlogNatHostAddress'
_I='hwUserlogNatEnable'
_H='hwUserlogAccessCfgSlotNumber'
_G='hwUserlogFlowCfgSlotNumber'
_F='hwUserlogNatCfgSlotNumber'
_E='Integer32'
_D='read-only'
_C='read-write'
_B='A3COM-HUAWEI-USERLOG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
huawei,huaweiDatacomm,huaweiMgmt=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','huawei','huaweiDatacomm','huaweiMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hwUserLogMIB=ModuleIdentity((1,3,6,1,4,1,43,45,1,5,25,18))
_HwUserlogObjects_ObjectIdentity=ObjectIdentity
hwUserlogObjects=_HwUserlogObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,18,1))
_HwUserlogNatObjects_ObjectIdentity=ObjectIdentity
hwUserlogNatObjects=_HwUserlogNatObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,18,1,1))
_HwUserlogNatVersion_Type=Integer32
_HwUserlogNatVersion_Object=MibScalar
hwUserlogNatVersion=_HwUserlogNatVersion_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,1,1),_HwUserlogNatVersion_Type())
hwUserlogNatVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:hwUserlogNatVersion.setStatus(_A)
_HwUserlogNatSyslog_Type=Integer32
_HwUserlogNatSyslog_Object=MibScalar
hwUserlogNatSyslog=_HwUserlogNatSyslog_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,1,2),_HwUserlogNatSyslog_Type())
hwUserlogNatSyslog.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogNatSyslog.setStatus(_A)
_HwUserlogNatSourceIP_Type=IpAddress
_HwUserlogNatSourceIP_Object=MibScalar
hwUserlogNatSourceIP=_HwUserlogNatSourceIP_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,1,3),_HwUserlogNatSourceIP_Type())
hwUserlogNatSourceIP.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogNatSourceIP.setStatus(_A)
_HwUserlogNatFlowBegin_Type=Integer32
_HwUserlogNatFlowBegin_Object=MibScalar
hwUserlogNatFlowBegin=_HwUserlogNatFlowBegin_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,1,4),_HwUserlogNatFlowBegin_Type())
hwUserlogNatFlowBegin.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogNatFlowBegin.setStatus(_A)
_HwUserlogNatActiveTime_Type=Integer32
_HwUserlogNatActiveTime_Object=MibScalar
hwUserlogNatActiveTime=_HwUserlogNatActiveTime_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,1,5),_HwUserlogNatActiveTime_Type())
hwUserlogNatActiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogNatActiveTime.setStatus(_A)
_HwUserlogNatSlotCfgInfoTable_Object=MibTable
hwUserlogNatSlotCfgInfoTable=_HwUserlogNatSlotCfgInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,1,6))
if mibBuilder.loadTexts:hwUserlogNatSlotCfgInfoTable.setStatus(_A)
_HwUserlogNatSlotCfgInfoEntry_Object=MibTableRow
hwUserlogNatSlotCfgInfoEntry=_HwUserlogNatSlotCfgInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,1,6,1))
hwUserlogNatSlotCfgInfoEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:hwUserlogNatSlotCfgInfoEntry.setStatus(_A)
class _HwUserlogNatCfgSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_HwUserlogNatCfgSlotNumber_Type.__name__=_E
_HwUserlogNatCfgSlotNumber_Object=MibTableColumn
hwUserlogNatCfgSlotNumber=_HwUserlogNatCfgSlotNumber_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,1,6,1,1),_HwUserlogNatCfgSlotNumber_Type())
hwUserlogNatCfgSlotNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hwUserlogNatCfgSlotNumber.setStatus(_A)
_HwUserlogNatEnable_Type=Integer32
_HwUserlogNatEnable_Object=MibTableColumn
hwUserlogNatEnable=_HwUserlogNatEnable_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,1,6,1,2),_HwUserlogNatEnable_Type())
hwUserlogNatEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogNatEnable.setStatus(_A)
_HwUserlogNatAclNumber_Type=Integer32
_HwUserlogNatAclNumber_Object=MibTableColumn
hwUserlogNatAclNumber=_HwUserlogNatAclNumber_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,1,6,1,3),_HwUserlogNatAclNumber_Type())
hwUserlogNatAclNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogNatAclNumber.setStatus(_A)
_HwUserlogNatHostAddress_Type=IpAddress
_HwUserlogNatHostAddress_Object=MibTableColumn
hwUserlogNatHostAddress=_HwUserlogNatHostAddress_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,1,6,1,4),_HwUserlogNatHostAddress_Type())
hwUserlogNatHostAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogNatHostAddress.setStatus(_A)
class _HwUserlogNatUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwUserlogNatUdpPort_Type.__name__=_E
_HwUserlogNatUdpPort_Object=MibTableColumn
hwUserlogNatUdpPort=_HwUserlogNatUdpPort_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,1,6,1,5),_HwUserlogNatUdpPort_Type())
hwUserlogNatUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogNatUdpPort.setStatus(_A)
_HwUserlogNatSlotRunInfoTable_Object=MibTable
hwUserlogNatSlotRunInfoTable=_HwUserlogNatSlotRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,1,7))
if mibBuilder.loadTexts:hwUserlogNatSlotRunInfoTable.setStatus(_A)
_HwUserlogNatSlotRunInfoEntry_Object=MibTableRow
hwUserlogNatSlotRunInfoEntry=_HwUserlogNatSlotRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,1,7,1))
hwUserlogNatSlotRunInfoEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:hwUserlogNatSlotRunInfoEntry.setStatus(_A)
class _HwUserlogNatRunSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_HwUserlogNatRunSlotNumber_Type.__name__=_E
_HwUserlogNatRunSlotNumber_Object=MibTableColumn
hwUserlogNatRunSlotNumber=_HwUserlogNatRunSlotNumber_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,1,7,1,1),_HwUserlogNatRunSlotNumber_Type())
hwUserlogNatRunSlotNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hwUserlogNatRunSlotNumber.setStatus(_A)
_HwUserlogNatTotalEntries_Type=Counter32
_HwUserlogNatTotalEntries_Object=MibTableColumn
hwUserlogNatTotalEntries=_HwUserlogNatTotalEntries_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,1,7,1,2),_HwUserlogNatTotalEntries_Type())
hwUserlogNatTotalEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:hwUserlogNatTotalEntries.setStatus(_A)
_HwUserlogNatTotalPackets_Type=Counter32
_HwUserlogNatTotalPackets_Object=MibTableColumn
hwUserlogNatTotalPackets=_HwUserlogNatTotalPackets_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,1,7,1,3),_HwUserlogNatTotalPackets_Type())
hwUserlogNatTotalPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:hwUserlogNatTotalPackets.setStatus(_A)
_HwUserlogNatFailedEntries_Type=Counter32
_HwUserlogNatFailedEntries_Object=MibTableColumn
hwUserlogNatFailedEntries=_HwUserlogNatFailedEntries_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,1,7,1,4),_HwUserlogNatFailedEntries_Type())
hwUserlogNatFailedEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:hwUserlogNatFailedEntries.setStatus(_A)
_HwUserlogNatFailedPackets_Type=Counter32
_HwUserlogNatFailedPackets_Object=MibTableColumn
hwUserlogNatFailedPackets=_HwUserlogNatFailedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,1,7,1,5),_HwUserlogNatFailedPackets_Type())
hwUserlogNatFailedPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:hwUserlogNatFailedPackets.setStatus(_A)
_HwUserlogNatClearRunStat_Type=Integer32
_HwUserlogNatClearRunStat_Object=MibTableColumn
hwUserlogNatClearRunStat=_HwUserlogNatClearRunStat_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,1,7,1,6),_HwUserlogNatClearRunStat_Type())
hwUserlogNatClearRunStat.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogNatClearRunStat.setStatus(_A)
_HwUserlogFlowObjects_ObjectIdentity=ObjectIdentity
hwUserlogFlowObjects=_HwUserlogFlowObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,18,1,2))
_HwUserlogFlowVersion_Type=Integer32
_HwUserlogFlowVersion_Object=MibScalar
hwUserlogFlowVersion=_HwUserlogFlowVersion_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,2,1),_HwUserlogFlowVersion_Type())
hwUserlogFlowVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:hwUserlogFlowVersion.setStatus(_A)
_HwUserlogFlowSyslog_Type=Integer32
_HwUserlogFlowSyslog_Object=MibScalar
hwUserlogFlowSyslog=_HwUserlogFlowSyslog_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,2,2),_HwUserlogFlowSyslog_Type())
hwUserlogFlowSyslog.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogFlowSyslog.setStatus(_A)
_HwUserlogFlowSourceIP_Type=IpAddress
_HwUserlogFlowSourceIP_Object=MibScalar
hwUserlogFlowSourceIP=_HwUserlogFlowSourceIP_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,2,3),_HwUserlogFlowSourceIP_Type())
hwUserlogFlowSourceIP.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogFlowSourceIP.setStatus(_A)
_HwUserlogFlowFlowBegin_Type=Integer32
_HwUserlogFlowFlowBegin_Object=MibScalar
hwUserlogFlowFlowBegin=_HwUserlogFlowFlowBegin_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,2,4),_HwUserlogFlowFlowBegin_Type())
hwUserlogFlowFlowBegin.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogFlowFlowBegin.setStatus(_A)
_HwUserlogFlowActiveTime_Type=Integer32
_HwUserlogFlowActiveTime_Object=MibScalar
hwUserlogFlowActiveTime=_HwUserlogFlowActiveTime_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,2,5),_HwUserlogFlowActiveTime_Type())
hwUserlogFlowActiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogFlowActiveTime.setStatus(_A)
_HwUserlogFlowSlotCfgInfoTable_Object=MibTable
hwUserlogFlowSlotCfgInfoTable=_HwUserlogFlowSlotCfgInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,2,6))
if mibBuilder.loadTexts:hwUserlogFlowSlotCfgInfoTable.setStatus(_A)
_HwUserlogFlowSlotCfgInfoEntry_Object=MibTableRow
hwUserlogFlowSlotCfgInfoEntry=_HwUserlogFlowSlotCfgInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,2,6,1))
hwUserlogFlowSlotCfgInfoEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hwUserlogFlowSlotCfgInfoEntry.setStatus(_A)
class _HwUserlogFlowCfgSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_HwUserlogFlowCfgSlotNumber_Type.__name__=_E
_HwUserlogFlowCfgSlotNumber_Object=MibTableColumn
hwUserlogFlowCfgSlotNumber=_HwUserlogFlowCfgSlotNumber_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,2,6,1,1),_HwUserlogFlowCfgSlotNumber_Type())
hwUserlogFlowCfgSlotNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hwUserlogFlowCfgSlotNumber.setStatus(_A)
_HwUserlogFlowEnable_Type=Integer32
_HwUserlogFlowEnable_Object=MibTableColumn
hwUserlogFlowEnable=_HwUserlogFlowEnable_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,2,6,1,2),_HwUserlogFlowEnable_Type())
hwUserlogFlowEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogFlowEnable.setStatus(_A)
_HwUserlogFlowAclNumber_Type=Integer32
_HwUserlogFlowAclNumber_Object=MibTableColumn
hwUserlogFlowAclNumber=_HwUserlogFlowAclNumber_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,2,6,1,3),_HwUserlogFlowAclNumber_Type())
hwUserlogFlowAclNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogFlowAclNumber.setStatus(_A)
_HwUserlogFlowHostAddress_Type=IpAddress
_HwUserlogFlowHostAddress_Object=MibTableColumn
hwUserlogFlowHostAddress=_HwUserlogFlowHostAddress_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,2,6,1,4),_HwUserlogFlowHostAddress_Type())
hwUserlogFlowHostAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogFlowHostAddress.setStatus(_A)
class _HwUserlogFlowUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwUserlogFlowUdpPort_Type.__name__=_E
_HwUserlogFlowUdpPort_Object=MibTableColumn
hwUserlogFlowUdpPort=_HwUserlogFlowUdpPort_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,2,6,1,5),_HwUserlogFlowUdpPort_Type())
hwUserlogFlowUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogFlowUdpPort.setStatus(_A)
_HwUserlogFlowSlotRunInfoTable_Object=MibTable
hwUserlogFlowSlotRunInfoTable=_HwUserlogFlowSlotRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,2,7))
if mibBuilder.loadTexts:hwUserlogFlowSlotRunInfoTable.setStatus(_A)
_HwUserlogFlowSlotRunInfoEntry_Object=MibTableRow
hwUserlogFlowSlotRunInfoEntry=_HwUserlogFlowSlotRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,2,7,1))
hwUserlogFlowSlotRunInfoEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:hwUserlogFlowSlotRunInfoEntry.setStatus(_A)
class _HwUserlogFlowRunSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_HwUserlogFlowRunSlotNumber_Type.__name__=_E
_HwUserlogFlowRunSlotNumber_Object=MibTableColumn
hwUserlogFlowRunSlotNumber=_HwUserlogFlowRunSlotNumber_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,2,7,1,1),_HwUserlogFlowRunSlotNumber_Type())
hwUserlogFlowRunSlotNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hwUserlogFlowRunSlotNumber.setStatus(_A)
_HwUserlogFlowTotalEntries_Type=Counter32
_HwUserlogFlowTotalEntries_Object=MibTableColumn
hwUserlogFlowTotalEntries=_HwUserlogFlowTotalEntries_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,2,7,1,2),_HwUserlogFlowTotalEntries_Type())
hwUserlogFlowTotalEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:hwUserlogFlowTotalEntries.setStatus(_A)
_HwUserlogFlowTotalPackets_Type=Counter32
_HwUserlogFlowTotalPackets_Object=MibTableColumn
hwUserlogFlowTotalPackets=_HwUserlogFlowTotalPackets_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,2,7,1,3),_HwUserlogFlowTotalPackets_Type())
hwUserlogFlowTotalPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:hwUserlogFlowTotalPackets.setStatus(_A)
_HwUserlogFlowFailedEntries_Type=Counter32
_HwUserlogFlowFailedEntries_Object=MibTableColumn
hwUserlogFlowFailedEntries=_HwUserlogFlowFailedEntries_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,2,7,1,4),_HwUserlogFlowFailedEntries_Type())
hwUserlogFlowFailedEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:hwUserlogFlowFailedEntries.setStatus(_A)
_HwUserlogFlowFailedPackets_Type=Counter32
_HwUserlogFlowFailedPackets_Object=MibTableColumn
hwUserlogFlowFailedPackets=_HwUserlogFlowFailedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,2,7,1,5),_HwUserlogFlowFailedPackets_Type())
hwUserlogFlowFailedPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:hwUserlogFlowFailedPackets.setStatus(_A)
_HwUserlogFlowClearRunStat_Type=Integer32
_HwUserlogFlowClearRunStat_Object=MibTableColumn
hwUserlogFlowClearRunStat=_HwUserlogFlowClearRunStat_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,2,7,1,6),_HwUserlogFlowClearRunStat_Type())
hwUserlogFlowClearRunStat.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogFlowClearRunStat.setStatus(_A)
_HwUserlogAccessObjects_ObjectIdentity=ObjectIdentity
hwUserlogAccessObjects=_HwUserlogAccessObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,18,1,3))
_HwUserlogAccessVersion_Type=Integer32
_HwUserlogAccessVersion_Object=MibScalar
hwUserlogAccessVersion=_HwUserlogAccessVersion_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,3,1),_HwUserlogAccessVersion_Type())
hwUserlogAccessVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:hwUserlogAccessVersion.setStatus(_A)
_HwUserlogAccessSyslog_Type=Integer32
_HwUserlogAccessSyslog_Object=MibScalar
hwUserlogAccessSyslog=_HwUserlogAccessSyslog_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,3,2),_HwUserlogAccessSyslog_Type())
hwUserlogAccessSyslog.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogAccessSyslog.setStatus(_A)
_HwUserlogAccessSourceIP_Type=IpAddress
_HwUserlogAccessSourceIP_Object=MibScalar
hwUserlogAccessSourceIP=_HwUserlogAccessSourceIP_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,3,3),_HwUserlogAccessSourceIP_Type())
hwUserlogAccessSourceIP.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogAccessSourceIP.setStatus(_A)
_HwUserlogAccessSlotCfgInfoTable_Object=MibTable
hwUserlogAccessSlotCfgInfoTable=_HwUserlogAccessSlotCfgInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,3,4))
if mibBuilder.loadTexts:hwUserlogAccessSlotCfgInfoTable.setStatus(_A)
_HwUserlogAccessSlotCfgInfoEntry_Object=MibTableRow
hwUserlogAccessSlotCfgInfoEntry=_HwUserlogAccessSlotCfgInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,3,4,1))
hwUserlogAccessSlotCfgInfoEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hwUserlogAccessSlotCfgInfoEntry.setStatus(_A)
class _HwUserlogAccessCfgSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_HwUserlogAccessCfgSlotNumber_Type.__name__=_E
_HwUserlogAccessCfgSlotNumber_Object=MibTableColumn
hwUserlogAccessCfgSlotNumber=_HwUserlogAccessCfgSlotNumber_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,3,4,1,1),_HwUserlogAccessCfgSlotNumber_Type())
hwUserlogAccessCfgSlotNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hwUserlogAccessCfgSlotNumber.setStatus(_A)
_HwUserlogAccessEnable_Type=Integer32
_HwUserlogAccessEnable_Object=MibTableColumn
hwUserlogAccessEnable=_HwUserlogAccessEnable_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,3,4,1,2),_HwUserlogAccessEnable_Type())
hwUserlogAccessEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogAccessEnable.setStatus(_A)
_HwUserlogAccessHostAddress_Type=IpAddress
_HwUserlogAccessHostAddress_Object=MibTableColumn
hwUserlogAccessHostAddress=_HwUserlogAccessHostAddress_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,3,4,1,3),_HwUserlogAccessHostAddress_Type())
hwUserlogAccessHostAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogAccessHostAddress.setStatus(_A)
class _HwUserlogAccessUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwUserlogAccessUdpPort_Type.__name__=_E
_HwUserlogAccessUdpPort_Object=MibTableColumn
hwUserlogAccessUdpPort=_HwUserlogAccessUdpPort_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,3,4,1,4),_HwUserlogAccessUdpPort_Type())
hwUserlogAccessUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogAccessUdpPort.setStatus(_A)
_HwUserlogAccessSlotRunInfoTable_Object=MibTable
hwUserlogAccessSlotRunInfoTable=_HwUserlogAccessSlotRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,3,5))
if mibBuilder.loadTexts:hwUserlogAccessSlotRunInfoTable.setStatus(_A)
_HwUserlogAccessSlotRunInfoEntry_Object=MibTableRow
hwUserlogAccessSlotRunInfoEntry=_HwUserlogAccessSlotRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,3,5,1))
hwUserlogAccessSlotRunInfoEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:hwUserlogAccessSlotRunInfoEntry.setStatus(_A)
class _HwUserlogAccessRunSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_HwUserlogAccessRunSlotNumber_Type.__name__=_E
_HwUserlogAccessRunSlotNumber_Object=MibTableColumn
hwUserlogAccessRunSlotNumber=_HwUserlogAccessRunSlotNumber_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,3,5,1,1),_HwUserlogAccessRunSlotNumber_Type())
hwUserlogAccessRunSlotNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hwUserlogAccessRunSlotNumber.setStatus(_A)
_HwUserlogAccessTotalEntries_Type=Counter32
_HwUserlogAccessTotalEntries_Object=MibTableColumn
hwUserlogAccessTotalEntries=_HwUserlogAccessTotalEntries_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,3,5,1,2),_HwUserlogAccessTotalEntries_Type())
hwUserlogAccessTotalEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:hwUserlogAccessTotalEntries.setStatus(_A)
_HwUserlogAccessTotalPackets_Type=Counter32
_HwUserlogAccessTotalPackets_Object=MibTableColumn
hwUserlogAccessTotalPackets=_HwUserlogAccessTotalPackets_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,3,5,1,3),_HwUserlogAccessTotalPackets_Type())
hwUserlogAccessTotalPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:hwUserlogAccessTotalPackets.setStatus(_A)
_HwUserlogAccessFailedEntries_Type=Counter32
_HwUserlogAccessFailedEntries_Object=MibTableColumn
hwUserlogAccessFailedEntries=_HwUserlogAccessFailedEntries_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,3,5,1,4),_HwUserlogAccessFailedEntries_Type())
hwUserlogAccessFailedEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:hwUserlogAccessFailedEntries.setStatus(_A)
_HwUserlogAccessFailedPackets_Type=Counter32
_HwUserlogAccessFailedPackets_Object=MibTableColumn
hwUserlogAccessFailedPackets=_HwUserlogAccessFailedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,3,5,1,5),_HwUserlogAccessFailedPackets_Type())
hwUserlogAccessFailedPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:hwUserlogAccessFailedPackets.setStatus(_A)
_HwUserlogAccessClearRunStat_Type=Integer32
_HwUserlogAccessClearRunStat_Object=MibTableColumn
hwUserlogAccessClearRunStat=_HwUserlogAccessClearRunStat_Object((1,3,6,1,4,1,43,45,1,5,25,18,1,3,5,1,6),_HwUserlogAccessClearRunStat_Type())
hwUserlogAccessClearRunStat.setMaxAccess(_C)
if mibBuilder.loadTexts:hwUserlogAccessClearRunStat.setStatus(_A)
_HwUserlogNotifications_ObjectIdentity=ObjectIdentity
hwUserlogNotifications=_HwUserlogNotifications_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,18,2))
_HwUserlogConformance_ObjectIdentity=ObjectIdentity
hwUserlogConformance=_HwUserlogConformance_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,18,3))
_HwUserlogCompliances_ObjectIdentity=ObjectIdentity
hwUserlogCompliances=_HwUserlogCompliances_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,18,3,1))
_HwUserlogGroups_ObjectIdentity=ObjectIdentity
hwUserlogGroups=_HwUserlogGroups_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,18,3,2))
hwUserlogMandatoryGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,5,25,18,3,2,1))
hwUserlogMandatoryGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:hwUserlogMandatoryGroup.setStatus(_A)
hwUserlogConfigGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,5,25,18,3,2,2))
hwUserlogConfigGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_F),(_B,_I),(_B,_Z),(_B,_J),(_B,_K),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_G),(_B,_L),(_B,_f),(_B,_M),(_B,_N),(_B,_g),(_B,_h),(_B,_i),(_B,_H),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:hwUserlogConfigGroup.setStatus(_A)
hwUserlogInfoGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,5,25,18,3,2,3))
hwUserlogInfoGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:hwUserlogInfoGroup.setStatus(_A)
hwUserlogCompliance=ModuleCompliance((1,3,6,1,4,1,43,45,1,5,25,18,3,1,1))
hwUserlogCompliance.setObjects((_B,_v))
if mibBuilder.loadTexts:hwUserlogCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hwUserLogMIB':hwUserLogMIB,'hwUserlogObjects':hwUserlogObjects,'hwUserlogNatObjects':hwUserlogNatObjects,_U:hwUserlogNatVersion,_V:hwUserlogNatSyslog,_W:hwUserlogNatSourceIP,_X:hwUserlogNatFlowBegin,_Y:hwUserlogNatActiveTime,'hwUserlogNatSlotCfgInfoTable':hwUserlogNatSlotCfgInfoTable,'hwUserlogNatSlotCfgInfoEntry':hwUserlogNatSlotCfgInfoEntry,_F:hwUserlogNatCfgSlotNumber,_I:hwUserlogNatEnable,_Z:hwUserlogNatAclNumber,_J:hwUserlogNatHostAddress,_K:hwUserlogNatUdpPort,'hwUserlogNatSlotRunInfoTable':hwUserlogNatSlotRunInfoTable,'hwUserlogNatSlotRunInfoEntry':hwUserlogNatSlotRunInfoEntry,_R:hwUserlogNatRunSlotNumber,_j:hwUserlogNatTotalEntries,_k:hwUserlogNatTotalPackets,_l:hwUserlogNatFailedEntries,_m:hwUserlogNatFailedPackets,'hwUserlogNatClearRunStat':hwUserlogNatClearRunStat,'hwUserlogFlowObjects':hwUserlogFlowObjects,_a:hwUserlogFlowVersion,_b:hwUserlogFlowSyslog,_c:hwUserlogFlowSourceIP,_d:hwUserlogFlowFlowBegin,_e:hwUserlogFlowActiveTime,'hwUserlogFlowSlotCfgInfoTable':hwUserlogFlowSlotCfgInfoTable,'hwUserlogFlowSlotCfgInfoEntry':hwUserlogFlowSlotCfgInfoEntry,_G:hwUserlogFlowCfgSlotNumber,_L:hwUserlogFlowEnable,_f:hwUserlogFlowAclNumber,_M:hwUserlogFlowHostAddress,_N:hwUserlogFlowUdpPort,'hwUserlogFlowSlotRunInfoTable':hwUserlogFlowSlotRunInfoTable,'hwUserlogFlowSlotRunInfoEntry':hwUserlogFlowSlotRunInfoEntry,_S:hwUserlogFlowRunSlotNumber,_n:hwUserlogFlowTotalEntries,_o:hwUserlogFlowTotalPackets,_p:hwUserlogFlowFailedEntries,_q:hwUserlogFlowFailedPackets,'hwUserlogFlowClearRunStat':hwUserlogFlowClearRunStat,'hwUserlogAccessObjects':hwUserlogAccessObjects,_g:hwUserlogAccessVersion,_h:hwUserlogAccessSyslog,_i:hwUserlogAccessSourceIP,'hwUserlogAccessSlotCfgInfoTable':hwUserlogAccessSlotCfgInfoTable,'hwUserlogAccessSlotCfgInfoEntry':hwUserlogAccessSlotCfgInfoEntry,_H:hwUserlogAccessCfgSlotNumber,_O:hwUserlogAccessEnable,_P:hwUserlogAccessHostAddress,_Q:hwUserlogAccessUdpPort,'hwUserlogAccessSlotRunInfoTable':hwUserlogAccessSlotRunInfoTable,'hwUserlogAccessSlotRunInfoEntry':hwUserlogAccessSlotRunInfoEntry,_T:hwUserlogAccessRunSlotNumber,_r:hwUserlogAccessTotalEntries,_s:hwUserlogAccessTotalPackets,_t:hwUserlogAccessFailedEntries,_u:hwUserlogAccessFailedPackets,'hwUserlogAccessClearRunStat':hwUserlogAccessClearRunStat,'hwUserlogNotifications':hwUserlogNotifications,'hwUserlogConformance':hwUserlogConformance,'hwUserlogCompliances':hwUserlogCompliances,'hwUserlogCompliance':hwUserlogCompliance,'hwUserlogGroups':hwUserlogGroups,_v:hwUserlogMandatoryGroup,'hwUserlogConfigGroup':hwUserlogConfigGroup,'hwUserlogInfoGroup':hwUserlogInfoGroup})