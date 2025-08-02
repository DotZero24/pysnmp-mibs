_v='hpnicfUserlogMandatoryGroup'
_u='hpnicfUserlogAccessFailedPackets'
_t='hpnicfUserlogAccessFailedEntries'
_s='hpnicfUserlogAccessTotalPackets'
_r='hpnicfUserlogAccessTotalEntries'
_q='hpnicfUserlogFlowFailedPackets'
_p='hpnicfUserlogFlowFailedEntries'
_o='hpnicfUserlogFlowTotalPackets'
_n='hpnicfUserlogFlowTotalEntries'
_m='hpnicfUserlogNatFailedPackets'
_l='hpnicfUserlogNatFailedEntries'
_k='hpnicfUserlogNatTotalPackets'
_j='hpnicfUserlogNatTotalEntries'
_i='hpnicfUserlogAccessSourceIP'
_h='hpnicfUserlogAccessSyslog'
_g='hpnicfUserlogAccessVersion'
_f='hpnicfUserlogFlowAclNumber'
_e='hpnicfUserlogFlowActiveTime'
_d='hpnicfUserlogFlowFlowBegin'
_c='hpnicfUserlogFlowSourceIP'
_b='hpnicfUserlogFlowSyslog'
_a='hpnicfUserlogFlowVersion'
_Z='hpnicfUserlogNatAclNumber'
_Y='hpnicfUserlogNatActiveTime'
_X='hpnicfUserlogNatFlowBegin'
_W='hpnicfUserlogNatSourceIP'
_V='hpnicfUserlogNatSyslog'
_U='hpnicfUserlogNatVersion'
_T='hpnicfUserlogAccessRunSlotNumber'
_S='hpnicfUserlogFlowRunSlotNumber'
_R='hpnicfUserlogNatRunSlotNumber'
_Q='hpnicfUserlogAccessUdpPort'
_P='hpnicfUserlogAccessHostAddress'
_O='hpnicfUserlogAccessEnable'
_N='hpnicfUserlogFlowUdpPort'
_M='hpnicfUserlogFlowHostAddress'
_L='hpnicfUserlogFlowEnable'
_K='hpnicfUserlogNatUdpPort'
_J='hpnicfUserlogNatHostAddress'
_I='hpnicfUserlogNatEnable'
_H='hpnicfUserlogAccessCfgSlotNumber'
_G='hpnicfUserlogFlowCfgSlotNumber'
_F='hpnicfUserlogNatCfgSlotNumber'
_E='Integer32'
_D='read-only'
_C='read-write'
_B='HPN-ICF-USERLOG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfRhw,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfRhw')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfUserLogMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,18))
_HpnicfUserlogObjects_ObjectIdentity=ObjectIdentity
hpnicfUserlogObjects=_HpnicfUserlogObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,18,1))
_HpnicfUserlogNatObjects_ObjectIdentity=ObjectIdentity
hpnicfUserlogNatObjects=_HpnicfUserlogNatObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,18,1,1))
_HpnicfUserlogNatVersion_Type=Integer32
_HpnicfUserlogNatVersion_Object=MibScalar
hpnicfUserlogNatVersion=_HpnicfUserlogNatVersion_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,1,1),_HpnicfUserlogNatVersion_Type())
hpnicfUserlogNatVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfUserlogNatVersion.setStatus(_A)
_HpnicfUserlogNatSyslog_Type=Integer32
_HpnicfUserlogNatSyslog_Object=MibScalar
hpnicfUserlogNatSyslog=_HpnicfUserlogNatSyslog_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,1,2),_HpnicfUserlogNatSyslog_Type())
hpnicfUserlogNatSyslog.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogNatSyslog.setStatus(_A)
_HpnicfUserlogNatSourceIP_Type=IpAddress
_HpnicfUserlogNatSourceIP_Object=MibScalar
hpnicfUserlogNatSourceIP=_HpnicfUserlogNatSourceIP_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,1,3),_HpnicfUserlogNatSourceIP_Type())
hpnicfUserlogNatSourceIP.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogNatSourceIP.setStatus(_A)
_HpnicfUserlogNatFlowBegin_Type=Integer32
_HpnicfUserlogNatFlowBegin_Object=MibScalar
hpnicfUserlogNatFlowBegin=_HpnicfUserlogNatFlowBegin_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,1,4),_HpnicfUserlogNatFlowBegin_Type())
hpnicfUserlogNatFlowBegin.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogNatFlowBegin.setStatus(_A)
_HpnicfUserlogNatActiveTime_Type=Integer32
_HpnicfUserlogNatActiveTime_Object=MibScalar
hpnicfUserlogNatActiveTime=_HpnicfUserlogNatActiveTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,1,5),_HpnicfUserlogNatActiveTime_Type())
hpnicfUserlogNatActiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogNatActiveTime.setStatus(_A)
_HpnicfUserlogNatSlotCfgInfoTable_Object=MibTable
hpnicfUserlogNatSlotCfgInfoTable=_HpnicfUserlogNatSlotCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,1,6))
if mibBuilder.loadTexts:hpnicfUserlogNatSlotCfgInfoTable.setStatus(_A)
_HpnicfUserlogNatSlotCfgInfoEntry_Object=MibTableRow
hpnicfUserlogNatSlotCfgInfoEntry=_HpnicfUserlogNatSlotCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,1,6,1))
hpnicfUserlogNatSlotCfgInfoEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:hpnicfUserlogNatSlotCfgInfoEntry.setStatus(_A)
class _HpnicfUserlogNatCfgSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_HpnicfUserlogNatCfgSlotNumber_Type.__name__=_E
_HpnicfUserlogNatCfgSlotNumber_Object=MibTableColumn
hpnicfUserlogNatCfgSlotNumber=_HpnicfUserlogNatCfgSlotNumber_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,1,6,1,1),_HpnicfUserlogNatCfgSlotNumber_Type())
hpnicfUserlogNatCfgSlotNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfUserlogNatCfgSlotNumber.setStatus(_A)
_HpnicfUserlogNatEnable_Type=Integer32
_HpnicfUserlogNatEnable_Object=MibTableColumn
hpnicfUserlogNatEnable=_HpnicfUserlogNatEnable_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,1,6,1,2),_HpnicfUserlogNatEnable_Type())
hpnicfUserlogNatEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogNatEnable.setStatus(_A)
_HpnicfUserlogNatAclNumber_Type=Integer32
_HpnicfUserlogNatAclNumber_Object=MibTableColumn
hpnicfUserlogNatAclNumber=_HpnicfUserlogNatAclNumber_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,1,6,1,3),_HpnicfUserlogNatAclNumber_Type())
hpnicfUserlogNatAclNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogNatAclNumber.setStatus(_A)
_HpnicfUserlogNatHostAddress_Type=IpAddress
_HpnicfUserlogNatHostAddress_Object=MibTableColumn
hpnicfUserlogNatHostAddress=_HpnicfUserlogNatHostAddress_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,1,6,1,4),_HpnicfUserlogNatHostAddress_Type())
hpnicfUserlogNatHostAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogNatHostAddress.setStatus(_A)
class _HpnicfUserlogNatUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfUserlogNatUdpPort_Type.__name__=_E
_HpnicfUserlogNatUdpPort_Object=MibTableColumn
hpnicfUserlogNatUdpPort=_HpnicfUserlogNatUdpPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,1,6,1,5),_HpnicfUserlogNatUdpPort_Type())
hpnicfUserlogNatUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogNatUdpPort.setStatus(_A)
_HpnicfUserlogNatSlotRunInfoTable_Object=MibTable
hpnicfUserlogNatSlotRunInfoTable=_HpnicfUserlogNatSlotRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,1,7))
if mibBuilder.loadTexts:hpnicfUserlogNatSlotRunInfoTable.setStatus(_A)
_HpnicfUserlogNatSlotRunInfoEntry_Object=MibTableRow
hpnicfUserlogNatSlotRunInfoEntry=_HpnicfUserlogNatSlotRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,1,7,1))
hpnicfUserlogNatSlotRunInfoEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:hpnicfUserlogNatSlotRunInfoEntry.setStatus(_A)
class _HpnicfUserlogNatRunSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_HpnicfUserlogNatRunSlotNumber_Type.__name__=_E
_HpnicfUserlogNatRunSlotNumber_Object=MibTableColumn
hpnicfUserlogNatRunSlotNumber=_HpnicfUserlogNatRunSlotNumber_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,1,7,1,1),_HpnicfUserlogNatRunSlotNumber_Type())
hpnicfUserlogNatRunSlotNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfUserlogNatRunSlotNumber.setStatus(_A)
_HpnicfUserlogNatTotalEntries_Type=Counter32
_HpnicfUserlogNatTotalEntries_Object=MibTableColumn
hpnicfUserlogNatTotalEntries=_HpnicfUserlogNatTotalEntries_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,1,7,1,2),_HpnicfUserlogNatTotalEntries_Type())
hpnicfUserlogNatTotalEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfUserlogNatTotalEntries.setStatus(_A)
_HpnicfUserlogNatTotalPackets_Type=Counter32
_HpnicfUserlogNatTotalPackets_Object=MibTableColumn
hpnicfUserlogNatTotalPackets=_HpnicfUserlogNatTotalPackets_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,1,7,1,3),_HpnicfUserlogNatTotalPackets_Type())
hpnicfUserlogNatTotalPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfUserlogNatTotalPackets.setStatus(_A)
_HpnicfUserlogNatFailedEntries_Type=Counter32
_HpnicfUserlogNatFailedEntries_Object=MibTableColumn
hpnicfUserlogNatFailedEntries=_HpnicfUserlogNatFailedEntries_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,1,7,1,4),_HpnicfUserlogNatFailedEntries_Type())
hpnicfUserlogNatFailedEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfUserlogNatFailedEntries.setStatus(_A)
_HpnicfUserlogNatFailedPackets_Type=Counter32
_HpnicfUserlogNatFailedPackets_Object=MibTableColumn
hpnicfUserlogNatFailedPackets=_HpnicfUserlogNatFailedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,1,7,1,5),_HpnicfUserlogNatFailedPackets_Type())
hpnicfUserlogNatFailedPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfUserlogNatFailedPackets.setStatus(_A)
_HpnicfUserlogNatClearRunStat_Type=Integer32
_HpnicfUserlogNatClearRunStat_Object=MibTableColumn
hpnicfUserlogNatClearRunStat=_HpnicfUserlogNatClearRunStat_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,1,7,1,6),_HpnicfUserlogNatClearRunStat_Type())
hpnicfUserlogNatClearRunStat.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogNatClearRunStat.setStatus(_A)
_HpnicfUserlogFlowObjects_ObjectIdentity=ObjectIdentity
hpnicfUserlogFlowObjects=_HpnicfUserlogFlowObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,18,1,2))
_HpnicfUserlogFlowVersion_Type=Integer32
_HpnicfUserlogFlowVersion_Object=MibScalar
hpnicfUserlogFlowVersion=_HpnicfUserlogFlowVersion_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,2,1),_HpnicfUserlogFlowVersion_Type())
hpnicfUserlogFlowVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfUserlogFlowVersion.setStatus(_A)
_HpnicfUserlogFlowSyslog_Type=Integer32
_HpnicfUserlogFlowSyslog_Object=MibScalar
hpnicfUserlogFlowSyslog=_HpnicfUserlogFlowSyslog_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,2,2),_HpnicfUserlogFlowSyslog_Type())
hpnicfUserlogFlowSyslog.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogFlowSyslog.setStatus(_A)
_HpnicfUserlogFlowSourceIP_Type=IpAddress
_HpnicfUserlogFlowSourceIP_Object=MibScalar
hpnicfUserlogFlowSourceIP=_HpnicfUserlogFlowSourceIP_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,2,3),_HpnicfUserlogFlowSourceIP_Type())
hpnicfUserlogFlowSourceIP.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogFlowSourceIP.setStatus(_A)
_HpnicfUserlogFlowFlowBegin_Type=Integer32
_HpnicfUserlogFlowFlowBegin_Object=MibScalar
hpnicfUserlogFlowFlowBegin=_HpnicfUserlogFlowFlowBegin_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,2,4),_HpnicfUserlogFlowFlowBegin_Type())
hpnicfUserlogFlowFlowBegin.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogFlowFlowBegin.setStatus(_A)
_HpnicfUserlogFlowActiveTime_Type=Integer32
_HpnicfUserlogFlowActiveTime_Object=MibScalar
hpnicfUserlogFlowActiveTime=_HpnicfUserlogFlowActiveTime_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,2,5),_HpnicfUserlogFlowActiveTime_Type())
hpnicfUserlogFlowActiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogFlowActiveTime.setStatus(_A)
_HpnicfUserlogFlowSlotCfgInfoTable_Object=MibTable
hpnicfUserlogFlowSlotCfgInfoTable=_HpnicfUserlogFlowSlotCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,2,6))
if mibBuilder.loadTexts:hpnicfUserlogFlowSlotCfgInfoTable.setStatus(_A)
_HpnicfUserlogFlowSlotCfgInfoEntry_Object=MibTableRow
hpnicfUserlogFlowSlotCfgInfoEntry=_HpnicfUserlogFlowSlotCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,2,6,1))
hpnicfUserlogFlowSlotCfgInfoEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hpnicfUserlogFlowSlotCfgInfoEntry.setStatus(_A)
class _HpnicfUserlogFlowCfgSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_HpnicfUserlogFlowCfgSlotNumber_Type.__name__=_E
_HpnicfUserlogFlowCfgSlotNumber_Object=MibTableColumn
hpnicfUserlogFlowCfgSlotNumber=_HpnicfUserlogFlowCfgSlotNumber_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,2,6,1,1),_HpnicfUserlogFlowCfgSlotNumber_Type())
hpnicfUserlogFlowCfgSlotNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfUserlogFlowCfgSlotNumber.setStatus(_A)
_HpnicfUserlogFlowEnable_Type=Integer32
_HpnicfUserlogFlowEnable_Object=MibTableColumn
hpnicfUserlogFlowEnable=_HpnicfUserlogFlowEnable_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,2,6,1,2),_HpnicfUserlogFlowEnable_Type())
hpnicfUserlogFlowEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogFlowEnable.setStatus(_A)
_HpnicfUserlogFlowAclNumber_Type=Integer32
_HpnicfUserlogFlowAclNumber_Object=MibTableColumn
hpnicfUserlogFlowAclNumber=_HpnicfUserlogFlowAclNumber_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,2,6,1,3),_HpnicfUserlogFlowAclNumber_Type())
hpnicfUserlogFlowAclNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogFlowAclNumber.setStatus(_A)
_HpnicfUserlogFlowHostAddress_Type=IpAddress
_HpnicfUserlogFlowHostAddress_Object=MibTableColumn
hpnicfUserlogFlowHostAddress=_HpnicfUserlogFlowHostAddress_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,2,6,1,4),_HpnicfUserlogFlowHostAddress_Type())
hpnicfUserlogFlowHostAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogFlowHostAddress.setStatus(_A)
class _HpnicfUserlogFlowUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfUserlogFlowUdpPort_Type.__name__=_E
_HpnicfUserlogFlowUdpPort_Object=MibTableColumn
hpnicfUserlogFlowUdpPort=_HpnicfUserlogFlowUdpPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,2,6,1,5),_HpnicfUserlogFlowUdpPort_Type())
hpnicfUserlogFlowUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogFlowUdpPort.setStatus(_A)
_HpnicfUserlogFlowSlotRunInfoTable_Object=MibTable
hpnicfUserlogFlowSlotRunInfoTable=_HpnicfUserlogFlowSlotRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,2,7))
if mibBuilder.loadTexts:hpnicfUserlogFlowSlotRunInfoTable.setStatus(_A)
_HpnicfUserlogFlowSlotRunInfoEntry_Object=MibTableRow
hpnicfUserlogFlowSlotRunInfoEntry=_HpnicfUserlogFlowSlotRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,2,7,1))
hpnicfUserlogFlowSlotRunInfoEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:hpnicfUserlogFlowSlotRunInfoEntry.setStatus(_A)
class _HpnicfUserlogFlowRunSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_HpnicfUserlogFlowRunSlotNumber_Type.__name__=_E
_HpnicfUserlogFlowRunSlotNumber_Object=MibTableColumn
hpnicfUserlogFlowRunSlotNumber=_HpnicfUserlogFlowRunSlotNumber_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,2,7,1,1),_HpnicfUserlogFlowRunSlotNumber_Type())
hpnicfUserlogFlowRunSlotNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfUserlogFlowRunSlotNumber.setStatus(_A)
_HpnicfUserlogFlowTotalEntries_Type=Counter32
_HpnicfUserlogFlowTotalEntries_Object=MibTableColumn
hpnicfUserlogFlowTotalEntries=_HpnicfUserlogFlowTotalEntries_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,2,7,1,2),_HpnicfUserlogFlowTotalEntries_Type())
hpnicfUserlogFlowTotalEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfUserlogFlowTotalEntries.setStatus(_A)
_HpnicfUserlogFlowTotalPackets_Type=Counter32
_HpnicfUserlogFlowTotalPackets_Object=MibTableColumn
hpnicfUserlogFlowTotalPackets=_HpnicfUserlogFlowTotalPackets_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,2,7,1,3),_HpnicfUserlogFlowTotalPackets_Type())
hpnicfUserlogFlowTotalPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfUserlogFlowTotalPackets.setStatus(_A)
_HpnicfUserlogFlowFailedEntries_Type=Counter32
_HpnicfUserlogFlowFailedEntries_Object=MibTableColumn
hpnicfUserlogFlowFailedEntries=_HpnicfUserlogFlowFailedEntries_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,2,7,1,4),_HpnicfUserlogFlowFailedEntries_Type())
hpnicfUserlogFlowFailedEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfUserlogFlowFailedEntries.setStatus(_A)
_HpnicfUserlogFlowFailedPackets_Type=Counter32
_HpnicfUserlogFlowFailedPackets_Object=MibTableColumn
hpnicfUserlogFlowFailedPackets=_HpnicfUserlogFlowFailedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,2,7,1,5),_HpnicfUserlogFlowFailedPackets_Type())
hpnicfUserlogFlowFailedPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfUserlogFlowFailedPackets.setStatus(_A)
_HpnicfUserlogFlowClearRunStat_Type=Integer32
_HpnicfUserlogFlowClearRunStat_Object=MibTableColumn
hpnicfUserlogFlowClearRunStat=_HpnicfUserlogFlowClearRunStat_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,2,7,1,6),_HpnicfUserlogFlowClearRunStat_Type())
hpnicfUserlogFlowClearRunStat.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogFlowClearRunStat.setStatus(_A)
_HpnicfUserlogAccessObjects_ObjectIdentity=ObjectIdentity
hpnicfUserlogAccessObjects=_HpnicfUserlogAccessObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,18,1,3))
_HpnicfUserlogAccessVersion_Type=Integer32
_HpnicfUserlogAccessVersion_Object=MibScalar
hpnicfUserlogAccessVersion=_HpnicfUserlogAccessVersion_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,3,1),_HpnicfUserlogAccessVersion_Type())
hpnicfUserlogAccessVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfUserlogAccessVersion.setStatus(_A)
_HpnicfUserlogAccessSyslog_Type=Integer32
_HpnicfUserlogAccessSyslog_Object=MibScalar
hpnicfUserlogAccessSyslog=_HpnicfUserlogAccessSyslog_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,3,2),_HpnicfUserlogAccessSyslog_Type())
hpnicfUserlogAccessSyslog.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogAccessSyslog.setStatus(_A)
_HpnicfUserlogAccessSourceIP_Type=IpAddress
_HpnicfUserlogAccessSourceIP_Object=MibScalar
hpnicfUserlogAccessSourceIP=_HpnicfUserlogAccessSourceIP_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,3,3),_HpnicfUserlogAccessSourceIP_Type())
hpnicfUserlogAccessSourceIP.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogAccessSourceIP.setStatus(_A)
_HpnicfUserlogAccessSlotCfgInfoTable_Object=MibTable
hpnicfUserlogAccessSlotCfgInfoTable=_HpnicfUserlogAccessSlotCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,3,4))
if mibBuilder.loadTexts:hpnicfUserlogAccessSlotCfgInfoTable.setStatus(_A)
_HpnicfUserlogAccessSlotCfgInfoEntry_Object=MibTableRow
hpnicfUserlogAccessSlotCfgInfoEntry=_HpnicfUserlogAccessSlotCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,3,4,1))
hpnicfUserlogAccessSlotCfgInfoEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpnicfUserlogAccessSlotCfgInfoEntry.setStatus(_A)
class _HpnicfUserlogAccessCfgSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_HpnicfUserlogAccessCfgSlotNumber_Type.__name__=_E
_HpnicfUserlogAccessCfgSlotNumber_Object=MibTableColumn
hpnicfUserlogAccessCfgSlotNumber=_HpnicfUserlogAccessCfgSlotNumber_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,3,4,1,1),_HpnicfUserlogAccessCfgSlotNumber_Type())
hpnicfUserlogAccessCfgSlotNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfUserlogAccessCfgSlotNumber.setStatus(_A)
_HpnicfUserlogAccessEnable_Type=Integer32
_HpnicfUserlogAccessEnable_Object=MibTableColumn
hpnicfUserlogAccessEnable=_HpnicfUserlogAccessEnable_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,3,4,1,2),_HpnicfUserlogAccessEnable_Type())
hpnicfUserlogAccessEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogAccessEnable.setStatus(_A)
_HpnicfUserlogAccessHostAddress_Type=IpAddress
_HpnicfUserlogAccessHostAddress_Object=MibTableColumn
hpnicfUserlogAccessHostAddress=_HpnicfUserlogAccessHostAddress_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,3,4,1,3),_HpnicfUserlogAccessHostAddress_Type())
hpnicfUserlogAccessHostAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogAccessHostAddress.setStatus(_A)
class _HpnicfUserlogAccessUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfUserlogAccessUdpPort_Type.__name__=_E
_HpnicfUserlogAccessUdpPort_Object=MibTableColumn
hpnicfUserlogAccessUdpPort=_HpnicfUserlogAccessUdpPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,3,4,1,4),_HpnicfUserlogAccessUdpPort_Type())
hpnicfUserlogAccessUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogAccessUdpPort.setStatus(_A)
_HpnicfUserlogAccessSlotRunInfoTable_Object=MibTable
hpnicfUserlogAccessSlotRunInfoTable=_HpnicfUserlogAccessSlotRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,3,5))
if mibBuilder.loadTexts:hpnicfUserlogAccessSlotRunInfoTable.setStatus(_A)
_HpnicfUserlogAccessSlotRunInfoEntry_Object=MibTableRow
hpnicfUserlogAccessSlotRunInfoEntry=_HpnicfUserlogAccessSlotRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,3,5,1))
hpnicfUserlogAccessSlotRunInfoEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:hpnicfUserlogAccessSlotRunInfoEntry.setStatus(_A)
class _HpnicfUserlogAccessRunSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_HpnicfUserlogAccessRunSlotNumber_Type.__name__=_E
_HpnicfUserlogAccessRunSlotNumber_Object=MibTableColumn
hpnicfUserlogAccessRunSlotNumber=_HpnicfUserlogAccessRunSlotNumber_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,3,5,1,1),_HpnicfUserlogAccessRunSlotNumber_Type())
hpnicfUserlogAccessRunSlotNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfUserlogAccessRunSlotNumber.setStatus(_A)
_HpnicfUserlogAccessTotalEntries_Type=Counter32
_HpnicfUserlogAccessTotalEntries_Object=MibTableColumn
hpnicfUserlogAccessTotalEntries=_HpnicfUserlogAccessTotalEntries_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,3,5,1,2),_HpnicfUserlogAccessTotalEntries_Type())
hpnicfUserlogAccessTotalEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfUserlogAccessTotalEntries.setStatus(_A)
_HpnicfUserlogAccessTotalPackets_Type=Counter32
_HpnicfUserlogAccessTotalPackets_Object=MibTableColumn
hpnicfUserlogAccessTotalPackets=_HpnicfUserlogAccessTotalPackets_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,3,5,1,3),_HpnicfUserlogAccessTotalPackets_Type())
hpnicfUserlogAccessTotalPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfUserlogAccessTotalPackets.setStatus(_A)
_HpnicfUserlogAccessFailedEntries_Type=Counter32
_HpnicfUserlogAccessFailedEntries_Object=MibTableColumn
hpnicfUserlogAccessFailedEntries=_HpnicfUserlogAccessFailedEntries_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,3,5,1,4),_HpnicfUserlogAccessFailedEntries_Type())
hpnicfUserlogAccessFailedEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfUserlogAccessFailedEntries.setStatus(_A)
_HpnicfUserlogAccessFailedPackets_Type=Counter32
_HpnicfUserlogAccessFailedPackets_Object=MibTableColumn
hpnicfUserlogAccessFailedPackets=_HpnicfUserlogAccessFailedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,3,5,1,5),_HpnicfUserlogAccessFailedPackets_Type())
hpnicfUserlogAccessFailedPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfUserlogAccessFailedPackets.setStatus(_A)
_HpnicfUserlogAccessClearRunStat_Type=Integer32
_HpnicfUserlogAccessClearRunStat_Object=MibTableColumn
hpnicfUserlogAccessClearRunStat=_HpnicfUserlogAccessClearRunStat_Object((1,3,6,1,4,1,11,2,14,11,15,8,18,1,3,5,1,6),_HpnicfUserlogAccessClearRunStat_Type())
hpnicfUserlogAccessClearRunStat.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfUserlogAccessClearRunStat.setStatus(_A)
_HpnicfUserlogNotifications_ObjectIdentity=ObjectIdentity
hpnicfUserlogNotifications=_HpnicfUserlogNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,18,2))
_HpnicfUserlogConformance_ObjectIdentity=ObjectIdentity
hpnicfUserlogConformance=_HpnicfUserlogConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,18,3))
_HpnicfUserlogCompliances_ObjectIdentity=ObjectIdentity
hpnicfUserlogCompliances=_HpnicfUserlogCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,18,3,1))
_HpnicfUserlogGroups_ObjectIdentity=ObjectIdentity
hpnicfUserlogGroups=_HpnicfUserlogGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,18,3,2))
hpnicfUserlogMandatoryGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,8,18,3,2,1))
hpnicfUserlogMandatoryGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:hpnicfUserlogMandatoryGroup.setStatus(_A)
hpnicfUserlogConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,8,18,3,2,2))
hpnicfUserlogConfigGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_F),(_B,_I),(_B,_Z),(_B,_J),(_B,_K),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_G),(_B,_L),(_B,_f),(_B,_M),(_B,_N),(_B,_g),(_B,_h),(_B,_i),(_B,_H),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:hpnicfUserlogConfigGroup.setStatus(_A)
hpnicfUserlogInfoGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,8,18,3,2,3))
hpnicfUserlogInfoGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:hpnicfUserlogInfoGroup.setStatus(_A)
hpnicfUserlogCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,8,18,3,1,1))
hpnicfUserlogCompliance.setObjects((_B,_v))
if mibBuilder.loadTexts:hpnicfUserlogCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfUserLogMIB':hpnicfUserLogMIB,'hpnicfUserlogObjects':hpnicfUserlogObjects,'hpnicfUserlogNatObjects':hpnicfUserlogNatObjects,_U:hpnicfUserlogNatVersion,_V:hpnicfUserlogNatSyslog,_W:hpnicfUserlogNatSourceIP,_X:hpnicfUserlogNatFlowBegin,_Y:hpnicfUserlogNatActiveTime,'hpnicfUserlogNatSlotCfgInfoTable':hpnicfUserlogNatSlotCfgInfoTable,'hpnicfUserlogNatSlotCfgInfoEntry':hpnicfUserlogNatSlotCfgInfoEntry,_F:hpnicfUserlogNatCfgSlotNumber,_I:hpnicfUserlogNatEnable,_Z:hpnicfUserlogNatAclNumber,_J:hpnicfUserlogNatHostAddress,_K:hpnicfUserlogNatUdpPort,'hpnicfUserlogNatSlotRunInfoTable':hpnicfUserlogNatSlotRunInfoTable,'hpnicfUserlogNatSlotRunInfoEntry':hpnicfUserlogNatSlotRunInfoEntry,_R:hpnicfUserlogNatRunSlotNumber,_j:hpnicfUserlogNatTotalEntries,_k:hpnicfUserlogNatTotalPackets,_l:hpnicfUserlogNatFailedEntries,_m:hpnicfUserlogNatFailedPackets,'hpnicfUserlogNatClearRunStat':hpnicfUserlogNatClearRunStat,'hpnicfUserlogFlowObjects':hpnicfUserlogFlowObjects,_a:hpnicfUserlogFlowVersion,_b:hpnicfUserlogFlowSyslog,_c:hpnicfUserlogFlowSourceIP,_d:hpnicfUserlogFlowFlowBegin,_e:hpnicfUserlogFlowActiveTime,'hpnicfUserlogFlowSlotCfgInfoTable':hpnicfUserlogFlowSlotCfgInfoTable,'hpnicfUserlogFlowSlotCfgInfoEntry':hpnicfUserlogFlowSlotCfgInfoEntry,_G:hpnicfUserlogFlowCfgSlotNumber,_L:hpnicfUserlogFlowEnable,_f:hpnicfUserlogFlowAclNumber,_M:hpnicfUserlogFlowHostAddress,_N:hpnicfUserlogFlowUdpPort,'hpnicfUserlogFlowSlotRunInfoTable':hpnicfUserlogFlowSlotRunInfoTable,'hpnicfUserlogFlowSlotRunInfoEntry':hpnicfUserlogFlowSlotRunInfoEntry,_S:hpnicfUserlogFlowRunSlotNumber,_n:hpnicfUserlogFlowTotalEntries,_o:hpnicfUserlogFlowTotalPackets,_p:hpnicfUserlogFlowFailedEntries,_q:hpnicfUserlogFlowFailedPackets,'hpnicfUserlogFlowClearRunStat':hpnicfUserlogFlowClearRunStat,'hpnicfUserlogAccessObjects':hpnicfUserlogAccessObjects,_g:hpnicfUserlogAccessVersion,_h:hpnicfUserlogAccessSyslog,_i:hpnicfUserlogAccessSourceIP,'hpnicfUserlogAccessSlotCfgInfoTable':hpnicfUserlogAccessSlotCfgInfoTable,'hpnicfUserlogAccessSlotCfgInfoEntry':hpnicfUserlogAccessSlotCfgInfoEntry,_H:hpnicfUserlogAccessCfgSlotNumber,_O:hpnicfUserlogAccessEnable,_P:hpnicfUserlogAccessHostAddress,_Q:hpnicfUserlogAccessUdpPort,'hpnicfUserlogAccessSlotRunInfoTable':hpnicfUserlogAccessSlotRunInfoTable,'hpnicfUserlogAccessSlotRunInfoEntry':hpnicfUserlogAccessSlotRunInfoEntry,_T:hpnicfUserlogAccessRunSlotNumber,_r:hpnicfUserlogAccessTotalEntries,_s:hpnicfUserlogAccessTotalPackets,_t:hpnicfUserlogAccessFailedEntries,_u:hpnicfUserlogAccessFailedPackets,'hpnicfUserlogAccessClearRunStat':hpnicfUserlogAccessClearRunStat,'hpnicfUserlogNotifications':hpnicfUserlogNotifications,'hpnicfUserlogConformance':hpnicfUserlogConformance,'hpnicfUserlogCompliances':hpnicfUserlogCompliances,'hpnicfUserlogCompliance':hpnicfUserlogCompliance,'hpnicfUserlogGroups':hpnicfUserlogGroups,_v:hpnicfUserlogMandatoryGroup,'hpnicfUserlogConfigGroup':hpnicfUserlogConfigGroup,'hpnicfUserlogInfoGroup':hpnicfUserlogInfoGroup})