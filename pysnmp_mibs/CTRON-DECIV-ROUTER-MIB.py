_k='nwDecIVEventNumber'
_j='highlow'
_i='highmed'
_h='highest'
_g='nwDecIVEventFltrIfNum'
_f='nwDecIVEventFltrProtocol'
_e='nwDecIVAclSequence'
_d='nwDecIVAclIdentifier'
_c='nwDecIVHostMapDecIVAddr'
_b='nwDecIVHostMapIfIndex'
_a='nwDecIVFibNodeId'
_Z='nwDecIVProtoIfCtrIfIndex'
_Y='nwDecIVProtoIfIndex'
_X='nwDecIVFwdIfCtrIfIndex'
_W='canonical'
_V='encapfddisnap'
_U='encaptrsnap'
_T='encapenetsnap'
_S='encapenet'
_R='nativewan'
_Q='ethernet'
_P='delete'
_O='nwDecIVFwdIfIndex'
_N='invalid'
_M='invalid-config'
_L='TimeTicks'
_K='pending-enable'
_J='pending-disable'
_I='reset'
_H='CTRON-DECIV-ROUTER-MIB'
_G='enabled'
_F='disabled'
_E='other'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nwRtrProtoSuites,=mibBuilder.importSymbols('ROUTER-OIDS','nwRtrProtoSuites')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_L,'Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class DecIVAddress(OctetString):0
_NwDecIVRouter_ObjectIdentity=ObjectIdentity
nwDecIVRouter=_NwDecIVRouter_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3))
_NwDecIVMibs_ObjectIdentity=ObjectIdentity
nwDecIVMibs=_NwDecIVMibs_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,1))
_NwDecIVMibRevText_Type=DisplayString
_NwDecIVMibRevText_Object=MibScalar
nwDecIVMibRevText=_NwDecIVMibRevText_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,1,1),_NwDecIVMibRevText_Type())
nwDecIVMibRevText.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVMibRevText.setStatus(_A)
_NwDecIVComponents_ObjectIdentity=ObjectIdentity
nwDecIVComponents=_NwDecIVComponents_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2))
_NwDecIVSystem_ObjectIdentity=ObjectIdentity
nwDecIVSystem=_NwDecIVSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,1))
_NwDecIVSysConfig_ObjectIdentity=ObjectIdentity
nwDecIVSysConfig=_NwDecIVSysConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,1,1))
_NwDecIVSysRouterId_Type=DecIVAddress
_NwDecIVSysRouterId_Object=MibScalar
nwDecIVSysRouterId=_NwDecIVSysRouterId_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,1,1,1),_NwDecIVSysRouterId_Type())
nwDecIVSysRouterId.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVSysRouterId.setStatus(_A)
class _NwDecIVNodeType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('routing-iv',2),('area',3)))
_NwDecIVNodeType_Type.__name__=_C
_NwDecIVNodeType_Object=MibScalar
nwDecIVNodeType=_NwDecIVNodeType_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,1,1,2),_NwDecIVNodeType_Type())
nwDecIVNodeType.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVNodeType.setStatus(_A)
class _NwDecIVMaxNodes_Type(Integer32):defaultValue=1023
_NwDecIVMaxNodes_Type.__name__=_C
_NwDecIVMaxNodes_Object=MibScalar
nwDecIVMaxNodes=_NwDecIVMaxNodes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,1,1,3),_NwDecIVMaxNodes_Type())
nwDecIVMaxNodes.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVMaxNodes.setStatus(_A)
class _NwDecIVMaxBRA_Type(Integer32):defaultValue=16
_NwDecIVMaxBRA_Type.__name__=_C
_NwDecIVMaxBRA_Object=MibScalar
nwDecIVMaxBRA=_NwDecIVMaxBRA_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,1,1,4),_NwDecIVMaxBRA_Type())
nwDecIVMaxBRA.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVMaxBRA.setStatus(_A)
class _NwDecIVMaxBEA_Type(Integer32):defaultValue=64
_NwDecIVMaxBEA_Type.__name__=_C
_NwDecIVMaxBEA_Object=MibScalar
nwDecIVMaxBEA=_NwDecIVMaxBEA_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,1,1,5),_NwDecIVMaxBEA_Type())
nwDecIVMaxBEA.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVMaxBEA.setStatus(_A)
class _NwDecIVMaxHops_Type(Integer32):defaultValue=30
_NwDecIVMaxHops_Type.__name__=_C
_NwDecIVMaxHops_Object=MibScalar
nwDecIVMaxHops=_NwDecIVMaxHops_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,1,1,6),_NwDecIVMaxHops_Type())
nwDecIVMaxHops.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVMaxHops.setStatus(_A)
class _NwDecIVMaxCost_Type(Integer32):defaultValue=1022
_NwDecIVMaxCost_Type.__name__=_C
_NwDecIVMaxCost_Object=MibScalar
nwDecIVMaxCost=_NwDecIVMaxCost_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,1,1,7),_NwDecIVMaxCost_Type())
nwDecIVMaxCost.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVMaxCost.setStatus(_A)
class _NwDecIVMaxVisits_Type(Integer32):defaultValue=63
_NwDecIVMaxVisits_Type.__name__=_C
_NwDecIVMaxVisits_Object=MibScalar
nwDecIVMaxVisits=_NwDecIVMaxVisits_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,1,1,8),_NwDecIVMaxVisits_Type())
nwDecIVMaxVisits.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVMaxVisits.setStatus(_A)
class _NwDecIVNonBroadcastTimer_Type(TimeTicks):defaultValue=1000
_NwDecIVNonBroadcastTimer_Type.__name__=_L
_NwDecIVNonBroadcastTimer_Object=MibScalar
nwDecIVNonBroadcastTimer=_NwDecIVNonBroadcastTimer_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,1,1,9),_NwDecIVNonBroadcastTimer_Type())
nwDecIVNonBroadcastTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVNonBroadcastTimer.setStatus(_A)
class _NwDecIVBroadcastTimer_Type(TimeTicks):defaultValue=1000
_NwDecIVBroadcastTimer_Type.__name__=_L
_NwDecIVBroadcastTimer_Object=MibScalar
nwDecIVBroadcastTimer=_NwDecIVBroadcastTimer_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,1,1,10),_NwDecIVBroadcastTimer_Type())
nwDecIVBroadcastTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVBroadcastTimer.setStatus(_A)
class _NwDecIVAreas_Type(Integer32):defaultValue=63
_NwDecIVAreas_Type.__name__=_C
_NwDecIVAreas_Object=MibScalar
nwDecIVAreas=_NwDecIVAreas_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,1,1,11),_NwDecIVAreas_Type())
nwDecIVAreas.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVAreas.setStatus(_A)
class _NwDecIVMaxAreaHops_Type(Integer32):defaultValue=30
_NwDecIVMaxAreaHops_Type.__name__=_C
_NwDecIVMaxAreaHops_Object=MibScalar
nwDecIVMaxAreaHops=_NwDecIVMaxAreaHops_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,1,1,12),_NwDecIVMaxAreaHops_Type())
nwDecIVMaxAreaHops.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVMaxAreaHops.setStatus(_A)
class _NwDecIVMaxAreaCost_Type(Integer32):defaultValue=1022
_NwDecIVMaxAreaCost_Type.__name__=_C
_NwDecIVMaxAreaCost_Object=MibScalar
nwDecIVMaxAreaCost=_NwDecIVMaxAreaCost_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,1,1,13),_NwDecIVMaxAreaCost_Type())
nwDecIVMaxAreaCost.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVMaxAreaCost.setStatus(_A)
_NwDecIVSysAdministration_ObjectIdentity=ObjectIdentity
nwDecIVSysAdministration=_NwDecIVSysAdministration_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,1,2))
class _NwDecIVSysAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwDecIVSysAdminStatus_Type.__name__=_C
_NwDecIVSysAdminStatus_Object=MibScalar
nwDecIVSysAdminStatus=_NwDecIVSysAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,1,2,1),_NwDecIVSysAdminStatus_Type())
nwDecIVSysAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVSysAdminStatus.setStatus(_A)
class _NwDecIVSysOperStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_J,4),(_K,5),(_M,6)))
_NwDecIVSysOperStatus_Type.__name__=_C
_NwDecIVSysOperStatus_Object=MibScalar
nwDecIVSysOperStatus=_NwDecIVSysOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,1,2,2),_NwDecIVSysOperStatus_Type())
nwDecIVSysOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVSysOperStatus.setStatus(_A)
class _NwDecIVSysAdminReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwDecIVSysAdminReset_Type.__name__=_C
_NwDecIVSysAdminReset_Object=MibScalar
nwDecIVSysAdminReset=_NwDecIVSysAdminReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,1,2,3),_NwDecIVSysAdminReset_Type())
nwDecIVSysAdminReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVSysAdminReset.setStatus(_A)
_NwDecIVSysOperationalTime_Type=TimeTicks
_NwDecIVSysOperationalTime_Object=MibScalar
nwDecIVSysOperationalTime=_NwDecIVSysOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,1,2,4),_NwDecIVSysOperationalTime_Type())
nwDecIVSysOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVSysOperationalTime.setStatus(_A)
_NwDecIVSysVersion_Type=DisplayString
_NwDecIVSysVersion_Object=MibScalar
nwDecIVSysVersion=_NwDecIVSysVersion_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,1,2,5),_NwDecIVSysVersion_Type())
nwDecIVSysVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVSysVersion.setStatus(_A)
_NwDecIVForwarding_ObjectIdentity=ObjectIdentity
nwDecIVForwarding=_NwDecIVForwarding_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2))
_NwDecIVFwdSystem_ObjectIdentity=ObjectIdentity
nwDecIVFwdSystem=_NwDecIVFwdSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1))
_NwDecIVFwdCounters_ObjectIdentity=ObjectIdentity
nwDecIVFwdCounters=_NwDecIVFwdCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1,1))
class _NwDecIVFwdCtrAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwDecIVFwdCtrAdminStatus_Type.__name__=_C
_NwDecIVFwdCtrAdminStatus_Object=MibScalar
nwDecIVFwdCtrAdminStatus=_NwDecIVFwdCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1,1,1),_NwDecIVFwdCtrAdminStatus_Type())
nwDecIVFwdCtrAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVFwdCtrAdminStatus.setStatus(_A)
class _NwDecIVFwdCtrReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwDecIVFwdCtrReset_Type.__name__=_C
_NwDecIVFwdCtrReset_Object=MibScalar
nwDecIVFwdCtrReset=_NwDecIVFwdCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1,1,2),_NwDecIVFwdCtrReset_Type())
nwDecIVFwdCtrReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVFwdCtrReset.setStatus(_A)
_NwDecIVFwdCtrOperationalTime_Type=TimeTicks
_NwDecIVFwdCtrOperationalTime_Object=MibScalar
nwDecIVFwdCtrOperationalTime=_NwDecIVFwdCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1,1,3),_NwDecIVFwdCtrOperationalTime_Type())
nwDecIVFwdCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdCtrOperationalTime.setStatus(_A)
_NwDecIVFwdCtrInPkts_Type=Counter32
_NwDecIVFwdCtrInPkts_Object=MibScalar
nwDecIVFwdCtrInPkts=_NwDecIVFwdCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1,1,4),_NwDecIVFwdCtrInPkts_Type())
nwDecIVFwdCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdCtrInPkts.setStatus(_A)
_NwDecIVFwdCtrOutPkts_Type=Counter32
_NwDecIVFwdCtrOutPkts_Object=MibScalar
nwDecIVFwdCtrOutPkts=_NwDecIVFwdCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1,1,5),_NwDecIVFwdCtrOutPkts_Type())
nwDecIVFwdCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdCtrOutPkts.setStatus(_A)
_NwDecIVFwdCtrFwdPkts_Type=Counter32
_NwDecIVFwdCtrFwdPkts_Object=MibScalar
nwDecIVFwdCtrFwdPkts=_NwDecIVFwdCtrFwdPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1,1,6),_NwDecIVFwdCtrFwdPkts_Type())
nwDecIVFwdCtrFwdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdCtrFwdPkts.setStatus(_A)
_NwDecIVFwdCtrFilteredPkts_Type=Counter32
_NwDecIVFwdCtrFilteredPkts_Object=MibScalar
nwDecIVFwdCtrFilteredPkts=_NwDecIVFwdCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1,1,7),_NwDecIVFwdCtrFilteredPkts_Type())
nwDecIVFwdCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdCtrFilteredPkts.setStatus(_A)
_NwDecIVFwdCtrDiscardPkts_Type=Counter32
_NwDecIVFwdCtrDiscardPkts_Object=MibScalar
nwDecIVFwdCtrDiscardPkts=_NwDecIVFwdCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1,1,8),_NwDecIVFwdCtrDiscardPkts_Type())
nwDecIVFwdCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdCtrDiscardPkts.setStatus(_A)
_NwDecIVFwdCtrAddrErrPkts_Type=Counter32
_NwDecIVFwdCtrAddrErrPkts_Object=MibScalar
nwDecIVFwdCtrAddrErrPkts=_NwDecIVFwdCtrAddrErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1,1,9),_NwDecIVFwdCtrAddrErrPkts_Type())
nwDecIVFwdCtrAddrErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdCtrAddrErrPkts.setStatus(_A)
_NwDecIVFwdCtrLenErrPkts_Type=Counter32
_NwDecIVFwdCtrLenErrPkts_Object=MibScalar
nwDecIVFwdCtrLenErrPkts=_NwDecIVFwdCtrLenErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1,1,10),_NwDecIVFwdCtrLenErrPkts_Type())
nwDecIVFwdCtrLenErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdCtrLenErrPkts.setStatus(_A)
_NwDecIVFwdCtrHdrErrPkts_Type=Counter32
_NwDecIVFwdCtrHdrErrPkts_Object=MibScalar
nwDecIVFwdCtrHdrErrPkts=_NwDecIVFwdCtrHdrErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1,1,11),_NwDecIVFwdCtrHdrErrPkts_Type())
nwDecIVFwdCtrHdrErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdCtrHdrErrPkts.setStatus(_A)
_NwDecIVFwdCtrInBytes_Type=Counter32
_NwDecIVFwdCtrInBytes_Object=MibScalar
nwDecIVFwdCtrInBytes=_NwDecIVFwdCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1,1,12),_NwDecIVFwdCtrInBytes_Type())
nwDecIVFwdCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdCtrInBytes.setStatus(_A)
_NwDecIVFwdCtrOutBytes_Type=Counter32
_NwDecIVFwdCtrOutBytes_Object=MibScalar
nwDecIVFwdCtrOutBytes=_NwDecIVFwdCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1,1,13),_NwDecIVFwdCtrOutBytes_Type())
nwDecIVFwdCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdCtrOutBytes.setStatus(_A)
_NwDecIVFwdCtrFwdBytes_Type=Counter32
_NwDecIVFwdCtrFwdBytes_Object=MibScalar
nwDecIVFwdCtrFwdBytes=_NwDecIVFwdCtrFwdBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1,1,14),_NwDecIVFwdCtrFwdBytes_Type())
nwDecIVFwdCtrFwdBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdCtrFwdBytes.setStatus(_A)
_NwDecIVFwdCtrFilteredBytes_Type=Counter32
_NwDecIVFwdCtrFilteredBytes_Object=MibScalar
nwDecIVFwdCtrFilteredBytes=_NwDecIVFwdCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1,1,15),_NwDecIVFwdCtrFilteredBytes_Type())
nwDecIVFwdCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdCtrFilteredBytes.setStatus(_A)
_NwDecIVFwdCtrDiscardBytes_Type=Counter32
_NwDecIVFwdCtrDiscardBytes_Object=MibScalar
nwDecIVFwdCtrDiscardBytes=_NwDecIVFwdCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1,1,16),_NwDecIVFwdCtrDiscardBytes_Type())
nwDecIVFwdCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdCtrDiscardBytes.setStatus(_A)
_NwDecIVFwdCtrHostInPkts_Type=Counter32
_NwDecIVFwdCtrHostInPkts_Object=MibScalar
nwDecIVFwdCtrHostInPkts=_NwDecIVFwdCtrHostInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1,1,17),_NwDecIVFwdCtrHostInPkts_Type())
nwDecIVFwdCtrHostInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdCtrHostInPkts.setStatus(_A)
_NwDecIVFwdCtrHostOutPkts_Type=Counter32
_NwDecIVFwdCtrHostOutPkts_Object=MibScalar
nwDecIVFwdCtrHostOutPkts=_NwDecIVFwdCtrHostOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1,1,18),_NwDecIVFwdCtrHostOutPkts_Type())
nwDecIVFwdCtrHostOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdCtrHostOutPkts.setStatus(_A)
_NwDecIVFwdCtrHostDiscardPkts_Type=Counter32
_NwDecIVFwdCtrHostDiscardPkts_Object=MibScalar
nwDecIVFwdCtrHostDiscardPkts=_NwDecIVFwdCtrHostDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1,1,19),_NwDecIVFwdCtrHostDiscardPkts_Type())
nwDecIVFwdCtrHostDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdCtrHostDiscardPkts.setStatus(_A)
_NwDecIVFwdCtrHostInBytes_Type=Counter32
_NwDecIVFwdCtrHostInBytes_Object=MibScalar
nwDecIVFwdCtrHostInBytes=_NwDecIVFwdCtrHostInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1,1,20),_NwDecIVFwdCtrHostInBytes_Type())
nwDecIVFwdCtrHostInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdCtrHostInBytes.setStatus(_A)
_NwDecIVFwdCtrHostOutBytes_Type=Counter32
_NwDecIVFwdCtrHostOutBytes_Object=MibScalar
nwDecIVFwdCtrHostOutBytes=_NwDecIVFwdCtrHostOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1,1,21),_NwDecIVFwdCtrHostOutBytes_Type())
nwDecIVFwdCtrHostOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdCtrHostOutBytes.setStatus(_A)
_NwDecIVFwdCtrHostDiscardBytes_Type=Counter32
_NwDecIVFwdCtrHostDiscardBytes_Object=MibScalar
nwDecIVFwdCtrHostDiscardBytes=_NwDecIVFwdCtrHostDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,1,1,22),_NwDecIVFwdCtrHostDiscardBytes_Type())
nwDecIVFwdCtrHostDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdCtrHostDiscardBytes.setStatus(_A)
_NwDecIVFwdInterfaces_ObjectIdentity=ObjectIdentity
nwDecIVFwdInterfaces=_NwDecIVFwdInterfaces_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2))
_NwDecIVFwdIfConfig_ObjectIdentity=ObjectIdentity
nwDecIVFwdIfConfig=_NwDecIVFwdIfConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,1))
_NwDecIVFwdIfTable_Object=MibTable
nwDecIVFwdIfTable=_NwDecIVFwdIfTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,1,1))
if mibBuilder.loadTexts:nwDecIVFwdIfTable.setStatus(_A)
_NwDecIVFwdIfEntry_Object=MibTableRow
nwDecIVFwdIfEntry=_NwDecIVFwdIfEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,1,1,1))
nwDecIVFwdIfEntry.setIndexNames((0,_H,_O))
if mibBuilder.loadTexts:nwDecIVFwdIfEntry.setStatus(_A)
_NwDecIVFwdIfIndex_Type=Integer32
_NwDecIVFwdIfIndex_Object=MibTableColumn
nwDecIVFwdIfIndex=_NwDecIVFwdIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,1,1,1,1),_NwDecIVFwdIfIndex_Type())
nwDecIVFwdIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfIndex.setStatus(_A)
class _NwDecIVFwdIfAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwDecIVFwdIfAdminStatus_Type.__name__=_C
_NwDecIVFwdIfAdminStatus_Object=MibTableColumn
nwDecIVFwdIfAdminStatus=_NwDecIVFwdIfAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,1,1,1,2),_NwDecIVFwdIfAdminStatus_Type())
nwDecIVFwdIfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVFwdIfAdminStatus.setStatus(_A)
class _NwDecIVFwdIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_J,4),(_K,5),(_M,6)))
_NwDecIVFwdIfOperStatus_Type.__name__=_C
_NwDecIVFwdIfOperStatus_Object=MibTableColumn
nwDecIVFwdIfOperStatus=_NwDecIVFwdIfOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,1,1,1,3),_NwDecIVFwdIfOperStatus_Type())
nwDecIVFwdIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfOperStatus.setStatus(_A)
_NwDecIVFwdIfOperationalTime_Type=TimeTicks
_NwDecIVFwdIfOperationalTime_Object=MibTableColumn
nwDecIVFwdIfOperationalTime=_NwDecIVFwdIfOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,1,1,1,4),_NwDecIVFwdIfOperationalTime_Type())
nwDecIVFwdIfOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfOperationalTime.setStatus(_A)
class _NwDecIVFwdIfControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('add',2),(_P,3)))
_NwDecIVFwdIfControl_Type.__name__=_C
_NwDecIVFwdIfControl_Object=MibTableColumn
nwDecIVFwdIfControl=_NwDecIVFwdIfControl_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,1,1,1,5),_NwDecIVFwdIfControl_Type())
nwDecIVFwdIfControl.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVFwdIfControl.setStatus(_A)
class _NwDecIVFwdIfMtu_Type(Integer32):defaultValue=1500
_NwDecIVFwdIfMtu_Type.__name__=_C
_NwDecIVFwdIfMtu_Object=MibTableColumn
nwDecIVFwdIfMtu=_NwDecIVFwdIfMtu_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,1,1,1,6),_NwDecIVFwdIfMtu_Type())
nwDecIVFwdIfMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVFwdIfMtu.setStatus(_A)
class _NwDecIVFwdIfForwarding_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwDecIVFwdIfForwarding_Type.__name__=_C
_NwDecIVFwdIfForwarding_Object=MibTableColumn
nwDecIVFwdIfForwarding=_NwDecIVFwdIfForwarding_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,1,1,1,7),_NwDecIVFwdIfForwarding_Type())
nwDecIVFwdIfForwarding.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVFwdIfForwarding.setStatus(_A)
class _NwDecIVFwdIfFrameType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,8,9,11,14,16,17)));namedValues=NamedValues(*((_E,1),(_Q,2),('snap',3),(_R,8),(_S,9),(_T,11),(_U,14),(_V,16),(_W,17)))
_NwDecIVFwdIfFrameType_Type.__name__=_C
_NwDecIVFwdIfFrameType_Object=MibTableColumn
nwDecIVFwdIfFrameType=_NwDecIVFwdIfFrameType_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,1,1,1,8),_NwDecIVFwdIfFrameType_Type())
nwDecIVFwdIfFrameType.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVFwdIfFrameType.setStatus(_A)
class _NwDecIVFwdIfAclIdentifier_Type(Integer32):defaultValue=0
_NwDecIVFwdIfAclIdentifier_Type.__name__=_C
_NwDecIVFwdIfAclIdentifier_Object=MibTableColumn
nwDecIVFwdIfAclIdentifier=_NwDecIVFwdIfAclIdentifier_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,1,1,1,9),_NwDecIVFwdIfAclIdentifier_Type())
nwDecIVFwdIfAclIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVFwdIfAclIdentifier.setStatus(_A)
class _NwDecIVFwdIfAclStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwDecIVFwdIfAclStatus_Type.__name__=_C
_NwDecIVFwdIfAclStatus_Object=MibTableColumn
nwDecIVFwdIfAclStatus=_NwDecIVFwdIfAclStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,1,1,1,10),_NwDecIVFwdIfAclStatus_Type())
nwDecIVFwdIfAclStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVFwdIfAclStatus.setStatus(_A)
class _NwDecIVFwdIfCacheControl_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('disable',2),('enable',3)))
_NwDecIVFwdIfCacheControl_Type.__name__=_C
_NwDecIVFwdIfCacheControl_Object=MibTableColumn
nwDecIVFwdIfCacheControl=_NwDecIVFwdIfCacheControl_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,1,1,1,11),_NwDecIVFwdIfCacheControl_Type())
nwDecIVFwdIfCacheControl.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVFwdIfCacheControl.setStatus(_A)
_NwDecIVFwdIfCacheEntries_Type=Counter32
_NwDecIVFwdIfCacheEntries_Object=MibTableColumn
nwDecIVFwdIfCacheEntries=_NwDecIVFwdIfCacheEntries_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,1,1,1,12),_NwDecIVFwdIfCacheEntries_Type())
nwDecIVFwdIfCacheEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCacheEntries.setStatus(_A)
_NwDecIVFwdIfCacheHits_Type=Counter32
_NwDecIVFwdIfCacheHits_Object=MibTableColumn
nwDecIVFwdIfCacheHits=_NwDecIVFwdIfCacheHits_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,1,1,1,13),_NwDecIVFwdIfCacheHits_Type())
nwDecIVFwdIfCacheHits.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCacheHits.setStatus(_A)
_NwDecIVFwdIfCacheMisses_Type=Counter32
_NwDecIVFwdIfCacheMisses_Object=MibTableColumn
nwDecIVFwdIfCacheMisses=_NwDecIVFwdIfCacheMisses_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,1,1,1,14),_NwDecIVFwdIfCacheMisses_Type())
nwDecIVFwdIfCacheMisses.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCacheMisses.setStatus(_A)
_NwDecIVFwdIfCounters_ObjectIdentity=ObjectIdentity
nwDecIVFwdIfCounters=_NwDecIVFwdIfCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2))
_NwDecIVFwdIfCtrTable_Object=MibTable
nwDecIVFwdIfCtrTable=_NwDecIVFwdIfCtrTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1))
if mibBuilder.loadTexts:nwDecIVFwdIfCtrTable.setStatus(_A)
_NwDecIVFwdIfCtrEntry_Object=MibTableRow
nwDecIVFwdIfCtrEntry=_NwDecIVFwdIfCtrEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1))
nwDecIVFwdIfCtrEntry.setIndexNames((0,_H,_X))
if mibBuilder.loadTexts:nwDecIVFwdIfCtrEntry.setStatus(_A)
_NwDecIVFwdIfCtrIfIndex_Type=Integer32
_NwDecIVFwdIfCtrIfIndex_Object=MibTableColumn
nwDecIVFwdIfCtrIfIndex=_NwDecIVFwdIfCtrIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1,1),_NwDecIVFwdIfCtrIfIndex_Type())
nwDecIVFwdIfCtrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCtrIfIndex.setStatus(_A)
class _NwDecIVFwdIfCtrAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwDecIVFwdIfCtrAdminStatus_Type.__name__=_C
_NwDecIVFwdIfCtrAdminStatus_Object=MibTableColumn
nwDecIVFwdIfCtrAdminStatus=_NwDecIVFwdIfCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1,2),_NwDecIVFwdIfCtrAdminStatus_Type())
nwDecIVFwdIfCtrAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVFwdIfCtrAdminStatus.setStatus(_A)
class _NwDecIVFwdIfCtrReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwDecIVFwdIfCtrReset_Type.__name__=_C
_NwDecIVFwdIfCtrReset_Object=MibTableColumn
nwDecIVFwdIfCtrReset=_NwDecIVFwdIfCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1,3),_NwDecIVFwdIfCtrReset_Type())
nwDecIVFwdIfCtrReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVFwdIfCtrReset.setStatus(_A)
_NwDecIVFwdIfCtrOperationalTime_Type=TimeTicks
_NwDecIVFwdIfCtrOperationalTime_Object=MibTableColumn
nwDecIVFwdIfCtrOperationalTime=_NwDecIVFwdIfCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1,4),_NwDecIVFwdIfCtrOperationalTime_Type())
nwDecIVFwdIfCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCtrOperationalTime.setStatus(_A)
_NwDecIVFwdIfCtrInPkts_Type=Counter32
_NwDecIVFwdIfCtrInPkts_Object=MibTableColumn
nwDecIVFwdIfCtrInPkts=_NwDecIVFwdIfCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1,5),_NwDecIVFwdIfCtrInPkts_Type())
nwDecIVFwdIfCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCtrInPkts.setStatus(_A)
_NwDecIVFwdIfCtrOutPkts_Type=Counter32
_NwDecIVFwdIfCtrOutPkts_Object=MibTableColumn
nwDecIVFwdIfCtrOutPkts=_NwDecIVFwdIfCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1,6),_NwDecIVFwdIfCtrOutPkts_Type())
nwDecIVFwdIfCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCtrOutPkts.setStatus(_A)
_NwDecIVFwdIfCtrFwdPkts_Type=Counter32
_NwDecIVFwdIfCtrFwdPkts_Object=MibTableColumn
nwDecIVFwdIfCtrFwdPkts=_NwDecIVFwdIfCtrFwdPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1,7),_NwDecIVFwdIfCtrFwdPkts_Type())
nwDecIVFwdIfCtrFwdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCtrFwdPkts.setStatus(_A)
_NwDecIVFwdIfCtrFilteredPkts_Type=Counter32
_NwDecIVFwdIfCtrFilteredPkts_Object=MibTableColumn
nwDecIVFwdIfCtrFilteredPkts=_NwDecIVFwdIfCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1,8),_NwDecIVFwdIfCtrFilteredPkts_Type())
nwDecIVFwdIfCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCtrFilteredPkts.setStatus(_A)
_NwDecIVFwdIfCtrDiscardPkts_Type=Counter32
_NwDecIVFwdIfCtrDiscardPkts_Object=MibTableColumn
nwDecIVFwdIfCtrDiscardPkts=_NwDecIVFwdIfCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1,9),_NwDecIVFwdIfCtrDiscardPkts_Type())
nwDecIVFwdIfCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCtrDiscardPkts.setStatus(_A)
_NwDecIVFwdIfCtrAddrErrPkts_Type=Counter32
_NwDecIVFwdIfCtrAddrErrPkts_Object=MibTableColumn
nwDecIVFwdIfCtrAddrErrPkts=_NwDecIVFwdIfCtrAddrErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1,10),_NwDecIVFwdIfCtrAddrErrPkts_Type())
nwDecIVFwdIfCtrAddrErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCtrAddrErrPkts.setStatus(_A)
_NwDecIVFwdIfCtrLenErrPkts_Type=Counter32
_NwDecIVFwdIfCtrLenErrPkts_Object=MibTableColumn
nwDecIVFwdIfCtrLenErrPkts=_NwDecIVFwdIfCtrLenErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1,11),_NwDecIVFwdIfCtrLenErrPkts_Type())
nwDecIVFwdIfCtrLenErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCtrLenErrPkts.setStatus(_A)
_NwDecIVFwdIfCtrHdrErrPkts_Type=Counter32
_NwDecIVFwdIfCtrHdrErrPkts_Object=MibTableColumn
nwDecIVFwdIfCtrHdrErrPkts=_NwDecIVFwdIfCtrHdrErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1,12),_NwDecIVFwdIfCtrHdrErrPkts_Type())
nwDecIVFwdIfCtrHdrErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCtrHdrErrPkts.setStatus(_A)
_NwDecIVFwdIfCtrInBytes_Type=Counter32
_NwDecIVFwdIfCtrInBytes_Object=MibTableColumn
nwDecIVFwdIfCtrInBytes=_NwDecIVFwdIfCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1,13),_NwDecIVFwdIfCtrInBytes_Type())
nwDecIVFwdIfCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCtrInBytes.setStatus(_A)
_NwDecIVFwdIfCtrOutBytes_Type=Counter32
_NwDecIVFwdIfCtrOutBytes_Object=MibTableColumn
nwDecIVFwdIfCtrOutBytes=_NwDecIVFwdIfCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1,14),_NwDecIVFwdIfCtrOutBytes_Type())
nwDecIVFwdIfCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCtrOutBytes.setStatus(_A)
_NwDecIVFwdIfCtrFwdBytes_Type=Counter32
_NwDecIVFwdIfCtrFwdBytes_Object=MibTableColumn
nwDecIVFwdIfCtrFwdBytes=_NwDecIVFwdIfCtrFwdBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1,15),_NwDecIVFwdIfCtrFwdBytes_Type())
nwDecIVFwdIfCtrFwdBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCtrFwdBytes.setStatus(_A)
_NwDecIVFwdIfCtrFilteredBytes_Type=Counter32
_NwDecIVFwdIfCtrFilteredBytes_Object=MibTableColumn
nwDecIVFwdIfCtrFilteredBytes=_NwDecIVFwdIfCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1,16),_NwDecIVFwdIfCtrFilteredBytes_Type())
nwDecIVFwdIfCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCtrFilteredBytes.setStatus(_A)
_NwDecIVFwdIfCtrDiscardBytes_Type=Counter32
_NwDecIVFwdIfCtrDiscardBytes_Object=MibTableColumn
nwDecIVFwdIfCtrDiscardBytes=_NwDecIVFwdIfCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1,17),_NwDecIVFwdIfCtrDiscardBytes_Type())
nwDecIVFwdIfCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCtrDiscardBytes.setStatus(_A)
_NwDecIVFwdIfCtrHostInPkts_Type=Counter32
_NwDecIVFwdIfCtrHostInPkts_Object=MibTableColumn
nwDecIVFwdIfCtrHostInPkts=_NwDecIVFwdIfCtrHostInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1,18),_NwDecIVFwdIfCtrHostInPkts_Type())
nwDecIVFwdIfCtrHostInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCtrHostInPkts.setStatus(_A)
_NwDecIVFwdIfCtrHostOutPkts_Type=Counter32
_NwDecIVFwdIfCtrHostOutPkts_Object=MibTableColumn
nwDecIVFwdIfCtrHostOutPkts=_NwDecIVFwdIfCtrHostOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1,19),_NwDecIVFwdIfCtrHostOutPkts_Type())
nwDecIVFwdIfCtrHostOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCtrHostOutPkts.setStatus(_A)
_NwDecIVFwdIfCtrHostDiscardPkts_Type=Counter32
_NwDecIVFwdIfCtrHostDiscardPkts_Object=MibTableColumn
nwDecIVFwdIfCtrHostDiscardPkts=_NwDecIVFwdIfCtrHostDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1,20),_NwDecIVFwdIfCtrHostDiscardPkts_Type())
nwDecIVFwdIfCtrHostDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCtrHostDiscardPkts.setStatus(_A)
_NwDecIVFwdIfCtrHostInBytes_Type=Counter32
_NwDecIVFwdIfCtrHostInBytes_Object=MibTableColumn
nwDecIVFwdIfCtrHostInBytes=_NwDecIVFwdIfCtrHostInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1,21),_NwDecIVFwdIfCtrHostInBytes_Type())
nwDecIVFwdIfCtrHostInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCtrHostInBytes.setStatus(_A)
_NwDecIVFwdIfCtrHostOutBytes_Type=Counter32
_NwDecIVFwdIfCtrHostOutBytes_Object=MibTableColumn
nwDecIVFwdIfCtrHostOutBytes=_NwDecIVFwdIfCtrHostOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1,22),_NwDecIVFwdIfCtrHostOutBytes_Type())
nwDecIVFwdIfCtrHostOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCtrHostOutBytes.setStatus(_A)
_NwDecIVFwdIfCtrHostDiscardBytes_Type=Counter32
_NwDecIVFwdIfCtrHostDiscardBytes_Object=MibTableColumn
nwDecIVFwdIfCtrHostDiscardBytes=_NwDecIVFwdIfCtrHostDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,2,2,2,1,1,23),_NwDecIVFwdIfCtrHostDiscardBytes_Type())
nwDecIVFwdIfCtrHostDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFwdIfCtrHostDiscardBytes.setStatus(_A)
_NwDecIVTopology_ObjectIdentity=ObjectIdentity
nwDecIVTopology=_NwDecIVTopology_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4))
_NwDecIVDistanceVector_ObjectIdentity=ObjectIdentity
nwDecIVDistanceVector=_NwDecIVDistanceVector_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1))
_NwDecIVProto_ObjectIdentity=ObjectIdentity
nwDecIVProto=_NwDecIVProto_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1))
_NwDecIVProtoSystem_ObjectIdentity=ObjectIdentity
nwDecIVProtoSystem=_NwDecIVProtoSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1))
_NwDecIVProtoConfig_ObjectIdentity=ObjectIdentity
nwDecIVProtoConfig=_NwDecIVProtoConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1,1))
class _NwDecIVProtoAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwDecIVProtoAdminStatus_Type.__name__=_C
_NwDecIVProtoAdminStatus_Object=MibScalar
nwDecIVProtoAdminStatus=_NwDecIVProtoAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1,1,1),_NwDecIVProtoAdminStatus_Type())
nwDecIVProtoAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoAdminStatus.setStatus(_A)
class _NwDecIVProtoOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_J,4),(_K,5),(_M,6)))
_NwDecIVProtoOperStatus_Type.__name__=_C
_NwDecIVProtoOperStatus_Object=MibScalar
nwDecIVProtoOperStatus=_NwDecIVProtoOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1,1,2),_NwDecIVProtoOperStatus_Type())
nwDecIVProtoOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoOperStatus.setStatus(_A)
class _NwDecIVProtoAdminReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwDecIVProtoAdminReset_Type.__name__=_C
_NwDecIVProtoAdminReset_Object=MibScalar
nwDecIVProtoAdminReset=_NwDecIVProtoAdminReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1,1,3),_NwDecIVProtoAdminReset_Type())
nwDecIVProtoAdminReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoAdminReset.setStatus(_A)
_NwDecIVProtoOperationalTime_Type=TimeTicks
_NwDecIVProtoOperationalTime_Object=MibScalar
nwDecIVProtoOperationalTime=_NwDecIVProtoOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1,1,4),_NwDecIVProtoOperationalTime_Type())
nwDecIVProtoOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoOperationalTime.setStatus(_A)
_NwDecIVProtoVersion_Type=DisplayString
_NwDecIVProtoVersion_Object=MibScalar
nwDecIVProtoVersion=_NwDecIVProtoVersion_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1,1,5),_NwDecIVProtoVersion_Type())
nwDecIVProtoVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoVersion.setStatus(_A)
class _NwDecIVProtoStackSize_Type(Integer32):defaultValue=4096
_NwDecIVProtoStackSize_Type.__name__=_C
_NwDecIVProtoStackSize_Object=MibScalar
nwDecIVProtoStackSize=_NwDecIVProtoStackSize_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1,1,6),_NwDecIVProtoStackSize_Type())
nwDecIVProtoStackSize.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoStackSize.setStatus(_A)
class _NwDecIVProtoThreadPriority_Type(Integer32):defaultValue=127
_NwDecIVProtoThreadPriority_Type.__name__=_C
_NwDecIVProtoThreadPriority_Object=MibScalar
nwDecIVProtoThreadPriority=_NwDecIVProtoThreadPriority_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1,1,7),_NwDecIVProtoThreadPriority_Type())
nwDecIVProtoThreadPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoThreadPriority.setStatus(_A)
class _NwDecIVProtoDatabaseThreshold_Type(Integer32):defaultValue=2000
_NwDecIVProtoDatabaseThreshold_Type.__name__=_C
_NwDecIVProtoDatabaseThreshold_Object=MibScalar
nwDecIVProtoDatabaseThreshold=_NwDecIVProtoDatabaseThreshold_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1,1,8),_NwDecIVProtoDatabaseThreshold_Type())
nwDecIVProtoDatabaseThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoDatabaseThreshold.setStatus(_A)
class _NwDecIVProtoAgeOut_Type(Integer32):defaultValue=180
_NwDecIVProtoAgeOut_Type.__name__=_C
_NwDecIVProtoAgeOut_Object=MibScalar
nwDecIVProtoAgeOut=_NwDecIVProtoAgeOut_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1,1,9),_NwDecIVProtoAgeOut_Type())
nwDecIVProtoAgeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoAgeOut.setStatus(_A)
class _NwDecIVProtoHoldDown_Type(Integer32):defaultValue=120
_NwDecIVProtoHoldDown_Type.__name__=_C
_NwDecIVProtoHoldDown_Object=MibScalar
nwDecIVProtoHoldDown=_NwDecIVProtoHoldDown_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1,1,10),_NwDecIVProtoHoldDown_Type())
nwDecIVProtoHoldDown.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoHoldDown.setStatus(_A)
_NwDecIVProtoCounters_ObjectIdentity=ObjectIdentity
nwDecIVProtoCounters=_NwDecIVProtoCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1,2))
class _NwDecIVProtoCtrAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwDecIVProtoCtrAdminStatus_Type.__name__=_C
_NwDecIVProtoCtrAdminStatus_Object=MibScalar
nwDecIVProtoCtrAdminStatus=_NwDecIVProtoCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1,2,1),_NwDecIVProtoCtrAdminStatus_Type())
nwDecIVProtoCtrAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoCtrAdminStatus.setStatus(_A)
class _NwDecIVProtoCtrReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwDecIVProtoCtrReset_Type.__name__=_C
_NwDecIVProtoCtrReset_Object=MibScalar
nwDecIVProtoCtrReset=_NwDecIVProtoCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1,2,2),_NwDecIVProtoCtrReset_Type())
nwDecIVProtoCtrReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoCtrReset.setStatus(_A)
_NwDecIVProtoCtrOperationalTime_Type=TimeTicks
_NwDecIVProtoCtrOperationalTime_Object=MibScalar
nwDecIVProtoCtrOperationalTime=_NwDecIVProtoCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1,2,3),_NwDecIVProtoCtrOperationalTime_Type())
nwDecIVProtoCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoCtrOperationalTime.setStatus(_A)
_NwDecIVProtoCtrInPkts_Type=Counter32
_NwDecIVProtoCtrInPkts_Object=MibScalar
nwDecIVProtoCtrInPkts=_NwDecIVProtoCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1,2,4),_NwDecIVProtoCtrInPkts_Type())
nwDecIVProtoCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoCtrInPkts.setStatus(_A)
_NwDecIVProtoCtrOutPkts_Type=Counter32
_NwDecIVProtoCtrOutPkts_Object=MibScalar
nwDecIVProtoCtrOutPkts=_NwDecIVProtoCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1,2,5),_NwDecIVProtoCtrOutPkts_Type())
nwDecIVProtoCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoCtrOutPkts.setStatus(_A)
_NwDecIVProtoCtrFilteredPkts_Type=Counter32
_NwDecIVProtoCtrFilteredPkts_Object=MibScalar
nwDecIVProtoCtrFilteredPkts=_NwDecIVProtoCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1,2,6),_NwDecIVProtoCtrFilteredPkts_Type())
nwDecIVProtoCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoCtrFilteredPkts.setStatus(_A)
_NwDecIVProtoCtrDiscardPkts_Type=Counter32
_NwDecIVProtoCtrDiscardPkts_Object=MibScalar
nwDecIVProtoCtrDiscardPkts=_NwDecIVProtoCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1,2,7),_NwDecIVProtoCtrDiscardPkts_Type())
nwDecIVProtoCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoCtrDiscardPkts.setStatus(_A)
_NwDecIVProtoCtrInBytes_Type=Counter32
_NwDecIVProtoCtrInBytes_Object=MibScalar
nwDecIVProtoCtrInBytes=_NwDecIVProtoCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1,2,8),_NwDecIVProtoCtrInBytes_Type())
nwDecIVProtoCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoCtrInBytes.setStatus(_A)
_NwDecIVProtoCtrOutBytes_Type=Counter32
_NwDecIVProtoCtrOutBytes_Object=MibScalar
nwDecIVProtoCtrOutBytes=_NwDecIVProtoCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1,2,9),_NwDecIVProtoCtrOutBytes_Type())
nwDecIVProtoCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoCtrOutBytes.setStatus(_A)
_NwDecIVProtoCtrFilteredBytes_Type=Counter32
_NwDecIVProtoCtrFilteredBytes_Object=MibScalar
nwDecIVProtoCtrFilteredBytes=_NwDecIVProtoCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1,2,10),_NwDecIVProtoCtrFilteredBytes_Type())
nwDecIVProtoCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoCtrFilteredBytes.setStatus(_A)
_NwDecIVProtoCtrDiscardBytes_Type=Counter32
_NwDecIVProtoCtrDiscardBytes_Object=MibScalar
nwDecIVProtoCtrDiscardBytes=_NwDecIVProtoCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,1,2,11),_NwDecIVProtoCtrDiscardBytes_Type())
nwDecIVProtoCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoCtrDiscardBytes.setStatus(_A)
_NwDecIVProtoInterface_ObjectIdentity=ObjectIdentity
nwDecIVProtoInterface=_NwDecIVProtoInterface_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2))
_NwDecIVProtoIfConfig_ObjectIdentity=ObjectIdentity
nwDecIVProtoIfConfig=_NwDecIVProtoIfConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,1))
_NwDecIVProtoIfTable_Object=MibTable
nwDecIVProtoIfTable=_NwDecIVProtoIfTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,1,1))
if mibBuilder.loadTexts:nwDecIVProtoIfTable.setStatus(_A)
_NwDecIVProtoIfEntry_Object=MibTableRow
nwDecIVProtoIfEntry=_NwDecIVProtoIfEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,1,1,1))
nwDecIVProtoIfEntry.setIndexNames((0,_H,_Y))
if mibBuilder.loadTexts:nwDecIVProtoIfEntry.setStatus(_A)
_NwDecIVProtoIfIndex_Type=Integer32
_NwDecIVProtoIfIndex_Object=MibTableColumn
nwDecIVProtoIfIndex=_NwDecIVProtoIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,1,1,1,1),_NwDecIVProtoIfIndex_Type())
nwDecIVProtoIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoIfIndex.setStatus(_A)
class _NwDecIVProtoIfAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwDecIVProtoIfAdminStatus_Type.__name__=_C
_NwDecIVProtoIfAdminStatus_Object=MibTableColumn
nwDecIVProtoIfAdminStatus=_NwDecIVProtoIfAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,1,1,1,2),_NwDecIVProtoIfAdminStatus_Type())
nwDecIVProtoIfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoIfAdminStatus.setStatus(_A)
class _NwDecIVProtoIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_J,4),(_K,5)))
_NwDecIVProtoIfOperStatus_Type.__name__=_C
_NwDecIVProtoIfOperStatus_Object=MibTableColumn
nwDecIVProtoIfOperStatus=_NwDecIVProtoIfOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,1,1,1,3),_NwDecIVProtoIfOperStatus_Type())
nwDecIVProtoIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoIfOperStatus.setStatus(_A)
_NwDecIVProtoIfOperationalTime_Type=TimeTicks
_NwDecIVProtoIfOperationalTime_Object=MibTableColumn
nwDecIVProtoIfOperationalTime=_NwDecIVProtoIfOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,1,1,1,4),_NwDecIVProtoIfOperationalTime_Type())
nwDecIVProtoIfOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoIfOperationalTime.setStatus(_A)
class _NwDecIVProtoIfVersion_Type(Integer32):defaultValue=3
_NwDecIVProtoIfVersion_Type.__name__=_C
_NwDecIVProtoIfVersion_Object=MibTableColumn
nwDecIVProtoIfVersion=_NwDecIVProtoIfVersion_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,1,1,1,5),_NwDecIVProtoIfVersion_Type())
nwDecIVProtoIfVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoIfVersion.setStatus(_A)
class _NwDecIVProtoIfAdvertisement_Type(Integer32):defaultValue=40
_NwDecIVProtoIfAdvertisement_Type.__name__=_C
_NwDecIVProtoIfAdvertisement_Object=MibTableColumn
nwDecIVProtoIfAdvertisement=_NwDecIVProtoIfAdvertisement_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,1,1,1,6),_NwDecIVProtoIfAdvertisement_Type())
nwDecIVProtoIfAdvertisement.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoIfAdvertisement.setStatus(_A)
class _NwDecIVProtoIfFloodDelay_Type(Integer32):defaultValue=2
_NwDecIVProtoIfFloodDelay_Type.__name__=_C
_NwDecIVProtoIfFloodDelay_Object=MibTableColumn
nwDecIVProtoIfFloodDelay=_NwDecIVProtoIfFloodDelay_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,1,1,1,7),_NwDecIVProtoIfFloodDelay_Type())
nwDecIVProtoIfFloodDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoIfFloodDelay.setStatus(_A)
class _NwDecIVProtoIfRequestDelay_Type(Integer32):defaultValue=0
_NwDecIVProtoIfRequestDelay_Type.__name__=_C
_NwDecIVProtoIfRequestDelay_Object=MibTableColumn
nwDecIVProtoIfRequestDelay=_NwDecIVProtoIfRequestDelay_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,1,1,1,8),_NwDecIVProtoIfRequestDelay_Type())
nwDecIVProtoIfRequestDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoIfRequestDelay.setStatus(_A)
class _NwDecIVProtoIfPriority_Type(Integer32):defaultValue=64
_NwDecIVProtoIfPriority_Type.__name__=_C
_NwDecIVProtoIfPriority_Object=MibTableColumn
nwDecIVProtoIfPriority=_NwDecIVProtoIfPriority_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,1,1,1,9),_NwDecIVProtoIfPriority_Type())
nwDecIVProtoIfPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoIfPriority.setStatus(_A)
class _NwDecIVProtoIfHelloTimer_Type(Integer32):defaultValue=15
_NwDecIVProtoIfHelloTimer_Type.__name__=_C
_NwDecIVProtoIfHelloTimer_Object=MibTableColumn
nwDecIVProtoIfHelloTimer=_NwDecIVProtoIfHelloTimer_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,1,1,1,10),_NwDecIVProtoIfHelloTimer_Type())
nwDecIVProtoIfHelloTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoIfHelloTimer.setStatus(_A)
class _NwDecIVProtoIfSplitHorizon_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwDecIVProtoIfSplitHorizon_Type.__name__=_C
_NwDecIVProtoIfSplitHorizon_Object=MibTableColumn
nwDecIVProtoIfSplitHorizon=_NwDecIVProtoIfSplitHorizon_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,1,1,1,11),_NwDecIVProtoIfSplitHorizon_Type())
nwDecIVProtoIfSplitHorizon.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoIfSplitHorizon.setStatus(_A)
class _NwDecIVProtoIfPoisonReverse_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwDecIVProtoIfPoisonReverse_Type.__name__=_C
_NwDecIVProtoIfPoisonReverse_Object=MibTableColumn
nwDecIVProtoIfPoisonReverse=_NwDecIVProtoIfPoisonReverse_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,1,1,1,12),_NwDecIVProtoIfPoisonReverse_Type())
nwDecIVProtoIfPoisonReverse.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoIfPoisonReverse.setStatus(_A)
class _NwDecIVProtoIfSnooping_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwDecIVProtoIfSnooping_Type.__name__=_C
_NwDecIVProtoIfSnooping_Object=MibTableColumn
nwDecIVProtoIfSnooping=_NwDecIVProtoIfSnooping_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,1,1,1,13),_NwDecIVProtoIfSnooping_Type())
nwDecIVProtoIfSnooping.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoIfSnooping.setStatus(_A)
class _NwDecIVProtoIfType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('bma',2),('nbma',3)))
_NwDecIVProtoIfType_Type.__name__=_C
_NwDecIVProtoIfType_Object=MibTableColumn
nwDecIVProtoIfType=_NwDecIVProtoIfType_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,1,1,1,14),_NwDecIVProtoIfType_Type())
nwDecIVProtoIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoIfType.setStatus(_A)
class _NwDecIVProtoIfXmitCost_Type(Integer32):defaultValue=1
_NwDecIVProtoIfXmitCost_Type.__name__=_C
_NwDecIVProtoIfXmitCost_Object=MibTableColumn
nwDecIVProtoIfXmitCost=_NwDecIVProtoIfXmitCost_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,1,1,1,15),_NwDecIVProtoIfXmitCost_Type())
nwDecIVProtoIfXmitCost.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoIfXmitCost.setStatus(_A)
class _NwDecIVProtoIfAclIdentifier_Type(Integer32):defaultValue=0
_NwDecIVProtoIfAclIdentifier_Type.__name__=_C
_NwDecIVProtoIfAclIdentifier_Object=MibTableColumn
nwDecIVProtoIfAclIdentifier=_NwDecIVProtoIfAclIdentifier_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,1,1,1,16),_NwDecIVProtoIfAclIdentifier_Type())
nwDecIVProtoIfAclIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoIfAclIdentifier.setStatus(_A)
class _NwDecIVProtoIfAclStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwDecIVProtoIfAclStatus_Type.__name__=_C
_NwDecIVProtoIfAclStatus_Object=MibTableColumn
nwDecIVProtoIfAclStatus=_NwDecIVProtoIfAclStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,1,1,1,17),_NwDecIVProtoIfAclStatus_Type())
nwDecIVProtoIfAclStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoIfAclStatus.setStatus(_A)
_NwDecIVProtoIfCounters_ObjectIdentity=ObjectIdentity
nwDecIVProtoIfCounters=_NwDecIVProtoIfCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,2))
_NwDecIVProtoIfCtrTable_Object=MibTable
nwDecIVProtoIfCtrTable=_NwDecIVProtoIfCtrTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,2,1))
if mibBuilder.loadTexts:nwDecIVProtoIfCtrTable.setStatus(_A)
_NwDecIVProtoIfCtrEntry_Object=MibTableRow
nwDecIVProtoIfCtrEntry=_NwDecIVProtoIfCtrEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,2,1,1))
nwDecIVProtoIfCtrEntry.setIndexNames((0,_H,_Z))
if mibBuilder.loadTexts:nwDecIVProtoIfCtrEntry.setStatus(_A)
_NwDecIVProtoIfCtrIfIndex_Type=Integer32
_NwDecIVProtoIfCtrIfIndex_Object=MibTableColumn
nwDecIVProtoIfCtrIfIndex=_NwDecIVProtoIfCtrIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,2,1,1,1),_NwDecIVProtoIfCtrIfIndex_Type())
nwDecIVProtoIfCtrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoIfCtrIfIndex.setStatus(_A)
class _NwDecIVProtoIfCtrAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwDecIVProtoIfCtrAdminStatus_Type.__name__=_C
_NwDecIVProtoIfCtrAdminStatus_Object=MibTableColumn
nwDecIVProtoIfCtrAdminStatus=_NwDecIVProtoIfCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,2,1,1,2),_NwDecIVProtoIfCtrAdminStatus_Type())
nwDecIVProtoIfCtrAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoIfCtrAdminStatus.setStatus(_A)
class _NwDecIVProtoIfCtrReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwDecIVProtoIfCtrReset_Type.__name__=_C
_NwDecIVProtoIfCtrReset_Object=MibTableColumn
nwDecIVProtoIfCtrReset=_NwDecIVProtoIfCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,2,1,1,3),_NwDecIVProtoIfCtrReset_Type())
nwDecIVProtoIfCtrReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVProtoIfCtrReset.setStatus(_A)
_NwDecIVProtoIfCtrOperationalTime_Type=TimeTicks
_NwDecIVProtoIfCtrOperationalTime_Object=MibTableColumn
nwDecIVProtoIfCtrOperationalTime=_NwDecIVProtoIfCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,2,1,1,4),_NwDecIVProtoIfCtrOperationalTime_Type())
nwDecIVProtoIfCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoIfCtrOperationalTime.setStatus(_A)
_NwDecIVProtoIfCtrInPkts_Type=Counter32
_NwDecIVProtoIfCtrInPkts_Object=MibTableColumn
nwDecIVProtoIfCtrInPkts=_NwDecIVProtoIfCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,2,1,1,5),_NwDecIVProtoIfCtrInPkts_Type())
nwDecIVProtoIfCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoIfCtrInPkts.setStatus(_A)
_NwDecIVProtoIfCtrOutPkts_Type=Counter32
_NwDecIVProtoIfCtrOutPkts_Object=MibTableColumn
nwDecIVProtoIfCtrOutPkts=_NwDecIVProtoIfCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,2,1,1,6),_NwDecIVProtoIfCtrOutPkts_Type())
nwDecIVProtoIfCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoIfCtrOutPkts.setStatus(_A)
_NwDecIVProtoIfCtrFilteredPkts_Type=Counter32
_NwDecIVProtoIfCtrFilteredPkts_Object=MibTableColumn
nwDecIVProtoIfCtrFilteredPkts=_NwDecIVProtoIfCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,2,1,1,7),_NwDecIVProtoIfCtrFilteredPkts_Type())
nwDecIVProtoIfCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoIfCtrFilteredPkts.setStatus(_A)
_NwDecIVProtoIfCtrDiscardPkts_Type=Counter32
_NwDecIVProtoIfCtrDiscardPkts_Object=MibTableColumn
nwDecIVProtoIfCtrDiscardPkts=_NwDecIVProtoIfCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,2,1,1,8),_NwDecIVProtoIfCtrDiscardPkts_Type())
nwDecIVProtoIfCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoIfCtrDiscardPkts.setStatus(_A)
_NwDecIVProtoIfCtrInBytes_Type=Counter32
_NwDecIVProtoIfCtrInBytes_Object=MibTableColumn
nwDecIVProtoIfCtrInBytes=_NwDecIVProtoIfCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,2,1,1,9),_NwDecIVProtoIfCtrInBytes_Type())
nwDecIVProtoIfCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoIfCtrInBytes.setStatus(_A)
_NwDecIVProtoIfCtrOutBytes_Type=Counter32
_NwDecIVProtoIfCtrOutBytes_Object=MibTableColumn
nwDecIVProtoIfCtrOutBytes=_NwDecIVProtoIfCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,2,1,1,10),_NwDecIVProtoIfCtrOutBytes_Type())
nwDecIVProtoIfCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoIfCtrOutBytes.setStatus(_A)
_NwDecIVProtoIfCtrFilteredBytes_Type=Counter32
_NwDecIVProtoIfCtrFilteredBytes_Object=MibTableColumn
nwDecIVProtoIfCtrFilteredBytes=_NwDecIVProtoIfCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,2,1,1,11),_NwDecIVProtoIfCtrFilteredBytes_Type())
nwDecIVProtoIfCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoIfCtrFilteredBytes.setStatus(_A)
_NwDecIVProtoIfCtrDiscardBytes_Type=Counter32
_NwDecIVProtoIfCtrDiscardBytes_Object=MibTableColumn
nwDecIVProtoIfCtrDiscardBytes=_NwDecIVProtoIfCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,1,1,2,2,1,1,12),_NwDecIVProtoIfCtrDiscardBytes_Type())
nwDecIVProtoIfCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVProtoIfCtrDiscardBytes.setStatus(_A)
_NwDecIVLinkState_ObjectIdentity=ObjectIdentity
nwDecIVLinkState=_NwDecIVLinkState_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,4,2))
_NwDecIVFib_ObjectIdentity=ObjectIdentity
nwDecIVFib=_NwDecIVFib_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,5))
_NwDecIVFibTable_Object=MibTable
nwDecIVFibTable=_NwDecIVFibTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,5,1))
if mibBuilder.loadTexts:nwDecIVFibTable.setStatus(_A)
_NwDecIVFibEntry_Object=MibTableRow
nwDecIVFibEntry=_NwDecIVFibEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,5,1,1))
nwDecIVFibEntry.setIndexNames((0,_H,_a))
if mibBuilder.loadTexts:nwDecIVFibEntry.setStatus(_A)
_NwDecIVFibNodeId_Type=DecIVAddress
_NwDecIVFibNodeId_Object=MibTableColumn
nwDecIVFibNodeId=_NwDecIVFibNodeId_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,5,1,1,1),_NwDecIVFibNodeId_Type())
nwDecIVFibNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVFibNodeId.setStatus(_A)
_NwDecIVFibNextHopNodeId_Type=DecIVAddress
_NwDecIVFibNextHopNodeId_Object=MibTableColumn
nwDecIVFibNextHopNodeId=_NwDecIVFibNextHopNodeId_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,5,1,1,2),_NwDecIVFibNextHopNodeId_Type())
nwDecIVFibNextHopNodeId.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVFibNextHopNodeId.setStatus(_A)
class _NwDecIVFibNextHopIf_Type(Integer32):defaultValue=0
_NwDecIVFibNextHopIf_Type.__name__=_C
_NwDecIVFibNextHopIf_Object=MibTableColumn
nwDecIVFibNextHopIf=_NwDecIVFibNextHopIf_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,5,1,1,3),_NwDecIVFibNextHopIf_Type())
nwDecIVFibNextHopIf.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVFibNextHopIf.setStatus(_A)
class _NwDecIVFibRouteType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_N,2),('direct',3),('remote',4)))
_NwDecIVFibRouteType_Type.__name__=_C
_NwDecIVFibRouteType_Object=MibTableColumn
nwDecIVFibRouteType=_NwDecIVFibRouteType_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,5,1,1,4),_NwDecIVFibRouteType_Type())
nwDecIVFibRouteType.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVFibRouteType.setStatus(_A)
_NwDecIVEndSystems_ObjectIdentity=ObjectIdentity
nwDecIVEndSystems=_NwDecIVEndSystems_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,6))
_NwDecIVHostsSystem_ObjectIdentity=ObjectIdentity
nwDecIVHostsSystem=_NwDecIVHostsSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,6,1))
_NwDecIVHostsInterfaces_ObjectIdentity=ObjectIdentity
nwDecIVHostsInterfaces=_NwDecIVHostsInterfaces_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,6,2))
_NwDecIVHostsToMedia_ObjectIdentity=ObjectIdentity
nwDecIVHostsToMedia=_NwDecIVHostsToMedia_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,6,3))
_NwDecIVHostMapTable_Object=MibTable
nwDecIVHostMapTable=_NwDecIVHostMapTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,6,3,1))
if mibBuilder.loadTexts:nwDecIVHostMapTable.setStatus(_A)
_NwDecIVHostMapEntry_Object=MibTableRow
nwDecIVHostMapEntry=_NwDecIVHostMapEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,6,3,1,1))
nwDecIVHostMapEntry.setIndexNames((0,_H,_b),(0,_H,_c))
if mibBuilder.loadTexts:nwDecIVHostMapEntry.setStatus(_A)
_NwDecIVHostMapIfIndex_Type=Integer32
_NwDecIVHostMapIfIndex_Object=MibTableColumn
nwDecIVHostMapIfIndex=_NwDecIVHostMapIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,6,3,1,1,1),_NwDecIVHostMapIfIndex_Type())
nwDecIVHostMapIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVHostMapIfIndex.setStatus(_A)
_NwDecIVHostMapDecIVAddr_Type=DecIVAddress
_NwDecIVHostMapDecIVAddr_Object=MibTableColumn
nwDecIVHostMapDecIVAddr=_NwDecIVHostMapDecIVAddr_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,6,3,1,1,2),_NwDecIVHostMapDecIVAddr_Type())
nwDecIVHostMapDecIVAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVHostMapDecIVAddr.setStatus(_A)
class _NwDecIVHostMapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_N,2),('dynamic',3),('static',4),('inactive',5)))
_NwDecIVHostMapType_Type.__name__=_C
_NwDecIVHostMapType_Object=MibTableColumn
nwDecIVHostMapType=_NwDecIVHostMapType_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,6,3,1,1,3),_NwDecIVHostMapType_Type())
nwDecIVHostMapType.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVHostMapType.setStatus(_A)
_NwDecIVHostMapCircuitID_Type=Integer32
_NwDecIVHostMapCircuitID_Object=MibTableColumn
nwDecIVHostMapCircuitID=_NwDecIVHostMapCircuitID_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,6,3,1,1,4),_NwDecIVHostMapCircuitID_Type())
nwDecIVHostMapCircuitID.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVHostMapCircuitID.setStatus(_A)
class _NwDecIVHostMapFraming_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,8,9,11,14,16,17)));namedValues=NamedValues(*((_E,1),(_Q,2),('snap',3),(_R,8),(_S,9),(_T,11),(_U,14),(_V,16),(_W,17)))
_NwDecIVHostMapFraming_Type.__name__=_C
_NwDecIVHostMapFraming_Object=MibTableColumn
nwDecIVHostMapFraming=_NwDecIVHostMapFraming_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,6,3,1,1,5),_NwDecIVHostMapFraming_Type())
nwDecIVHostMapFraming.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVHostMapFraming.setStatus(_A)
_NwDecIVHostMapPortNumber_Type=Integer32
_NwDecIVHostMapPortNumber_Object=MibTableColumn
nwDecIVHostMapPortNumber=_NwDecIVHostMapPortNumber_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,6,3,1,1,6),_NwDecIVHostMapPortNumber_Type())
nwDecIVHostMapPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVHostMapPortNumber.setStatus(_A)
_NwDecIVAccessControl_ObjectIdentity=ObjectIdentity
nwDecIVAccessControl=_NwDecIVAccessControl_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,7))
_NwDecIVAclValidEntries_Type=Gauge32
_NwDecIVAclValidEntries_Object=MibScalar
nwDecIVAclValidEntries=_NwDecIVAclValidEntries_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,7,1),_NwDecIVAclValidEntries_Type())
nwDecIVAclValidEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVAclValidEntries.setStatus(_A)
_NwDecIVAclTable_Object=MibTable
nwDecIVAclTable=_NwDecIVAclTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,7,2))
if mibBuilder.loadTexts:nwDecIVAclTable.setStatus(_A)
_NwDecIVAclEntry_Object=MibTableRow
nwDecIVAclEntry=_NwDecIVAclEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,7,2,1))
nwDecIVAclEntry.setIndexNames((0,_H,_d),(0,_H,_e))
if mibBuilder.loadTexts:nwDecIVAclEntry.setStatus(_A)
_NwDecIVAclIdentifier_Type=Integer32
_NwDecIVAclIdentifier_Object=MibTableColumn
nwDecIVAclIdentifier=_NwDecIVAclIdentifier_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,7,2,1,1),_NwDecIVAclIdentifier_Type())
nwDecIVAclIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVAclIdentifier.setStatus(_A)
_NwDecIVAclSequence_Type=Integer32
_NwDecIVAclSequence_Object=MibTableColumn
nwDecIVAclSequence=_NwDecIVAclSequence_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,7,2,1,2),_NwDecIVAclSequence_Type())
nwDecIVAclSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVAclSequence.setStatus(_A)
class _NwDecIVAclPermission_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_N,2),('permit',3),('deny',4),('permit-bidirectional',5),('deny-bidirectional',6)))
_NwDecIVAclPermission_Type.__name__=_C
_NwDecIVAclPermission_Object=MibTableColumn
nwDecIVAclPermission=_NwDecIVAclPermission_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,7,2,1,3),_NwDecIVAclPermission_Type())
nwDecIVAclPermission.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVAclPermission.setStatus(_A)
_NwDecIVAclMatches_Type=Counter32
_NwDecIVAclMatches_Object=MibTableColumn
nwDecIVAclMatches=_NwDecIVAclMatches_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,7,2,1,4),_NwDecIVAclMatches_Type())
nwDecIVAclMatches.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVAclMatches.setStatus(_A)
_NwDecIVAclDestAddress_Type=DecIVAddress
_NwDecIVAclDestAddress_Object=MibTableColumn
nwDecIVAclDestAddress=_NwDecIVAclDestAddress_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,7,2,1,5),_NwDecIVAclDestAddress_Type())
nwDecIVAclDestAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVAclDestAddress.setStatus(_A)
_NwDecIVAclSrcAddress_Type=DecIVAddress
_NwDecIVAclSrcAddress_Object=MibTableColumn
nwDecIVAclSrcAddress=_NwDecIVAclSrcAddress_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,7,2,1,6),_NwDecIVAclSrcAddress_Type())
nwDecIVAclSrcAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVAclSrcAddress.setStatus(_A)
_NwDecIVFilters_ObjectIdentity=ObjectIdentity
nwDecIVFilters=_NwDecIVFilters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,8))
_NwDecIVRedirector_ObjectIdentity=ObjectIdentity
nwDecIVRedirector=_NwDecIVRedirector_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,9))
_NwDecIVEvent_ObjectIdentity=ObjectIdentity
nwDecIVEvent=_NwDecIVEvent_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10))
_NwDecIVEventLogConfig_ObjectIdentity=ObjectIdentity
nwDecIVEventLogConfig=_NwDecIVEventLogConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10,1))
class _NwDecIVEventAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwDecIVEventAdminStatus_Type.__name__=_C
_NwDecIVEventAdminStatus_Object=MibScalar
nwDecIVEventAdminStatus=_NwDecIVEventAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10,1,1),_NwDecIVEventAdminStatus_Type())
nwDecIVEventAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVEventAdminStatus.setStatus(_A)
class _NwDecIVEventMaxEntries_Type(Integer32):defaultValue=100
_NwDecIVEventMaxEntries_Type.__name__=_C
_NwDecIVEventMaxEntries_Object=MibScalar
nwDecIVEventMaxEntries=_NwDecIVEventMaxEntries_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10,1,2),_NwDecIVEventMaxEntries_Type())
nwDecIVEventMaxEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVEventMaxEntries.setStatus(_A)
class _NwDecIVEventTraceAll_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwDecIVEventTraceAll_Type.__name__=_C
_NwDecIVEventTraceAll_Object=MibScalar
nwDecIVEventTraceAll=_NwDecIVEventTraceAll_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10,1,3),_NwDecIVEventTraceAll_Type())
nwDecIVEventTraceAll.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVEventTraceAll.setStatus(_A)
_NwDecIVEventLogFilterTable_ObjectIdentity=ObjectIdentity
nwDecIVEventLogFilterTable=_NwDecIVEventLogFilterTable_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10,2))
_NwDecIVEventFilterTable_Object=MibTable
nwDecIVEventFilterTable=_NwDecIVEventFilterTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10,2,1))
if mibBuilder.loadTexts:nwDecIVEventFilterTable.setStatus(_A)
_NwDecIVEventFilterEntry_Object=MibTableRow
nwDecIVEventFilterEntry=_NwDecIVEventFilterEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10,2,1,1))
nwDecIVEventFilterEntry.setIndexNames((0,_H,_f),(0,_H,_g))
if mibBuilder.loadTexts:nwDecIVEventFilterEntry.setStatus(_A)
_NwDecIVEventFltrProtocol_Type=Integer32
_NwDecIVEventFltrProtocol_Object=MibTableColumn
nwDecIVEventFltrProtocol=_NwDecIVEventFltrProtocol_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10,2,1,1,1),_NwDecIVEventFltrProtocol_Type())
nwDecIVEventFltrProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVEventFltrProtocol.setStatus(_A)
_NwDecIVEventFltrIfNum_Type=Integer32
_NwDecIVEventFltrIfNum_Object=MibTableColumn
nwDecIVEventFltrIfNum=_NwDecIVEventFltrIfNum_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10,2,1,1,2),_NwDecIVEventFltrIfNum_Type())
nwDecIVEventFltrIfNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVEventFltrIfNum.setStatus(_A)
class _NwDecIVEventFltrControl_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_P,2),('add',3)))
_NwDecIVEventFltrControl_Type.__name__=_C
_NwDecIVEventFltrControl_Object=MibTableColumn
nwDecIVEventFltrControl=_NwDecIVEventFltrControl_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10,2,1,1,3),_NwDecIVEventFltrControl_Type())
nwDecIVEventFltrControl.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVEventFltrControl.setStatus(_A)
class _NwDecIVEventFltrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16,32,64)));namedValues=NamedValues(*(('misc',1),('timer',2),('rcv',4),('xmit',8),('event',16),('diags',32),('error',64)))
_NwDecIVEventFltrType_Type.__name__=_C
_NwDecIVEventFltrType_Object=MibTableColumn
nwDecIVEventFltrType=_NwDecIVEventFltrType_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10,2,1,1,4),_NwDecIVEventFltrType_Type())
nwDecIVEventFltrType.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVEventFltrType.setStatus(_A)
class _NwDecIVEventFltrSeverity_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_h,1),(_i,2),(_j,3)))
_NwDecIVEventFltrSeverity_Type.__name__=_C
_NwDecIVEventFltrSeverity_Object=MibTableColumn
nwDecIVEventFltrSeverity=_NwDecIVEventFltrSeverity_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10,2,1,1,5),_NwDecIVEventFltrSeverity_Type())
nwDecIVEventFltrSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVEventFltrSeverity.setStatus(_A)
class _NwDecIVEventFltrAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('log',1),('trap',2),('log-trap',3)))
_NwDecIVEventFltrAction_Type.__name__=_C
_NwDecIVEventFltrAction_Object=MibTableColumn
nwDecIVEventFltrAction=_NwDecIVEventFltrAction_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10,2,1,1,6),_NwDecIVEventFltrAction_Type())
nwDecIVEventFltrAction.setMaxAccess(_D)
if mibBuilder.loadTexts:nwDecIVEventFltrAction.setStatus(_A)
_NwDecIVEventLogTable_ObjectIdentity=ObjectIdentity
nwDecIVEventLogTable=_NwDecIVEventLogTable_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10,3))
_NwDecIVEventTable_Object=MibTable
nwDecIVEventTable=_NwDecIVEventTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10,3,1))
if mibBuilder.loadTexts:nwDecIVEventTable.setStatus(_A)
_NwDecIVEventEntry_Object=MibTableRow
nwDecIVEventEntry=_NwDecIVEventEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10,3,1,1))
nwDecIVEventEntry.setIndexNames((0,_H,_k))
if mibBuilder.loadTexts:nwDecIVEventEntry.setStatus(_A)
_NwDecIVEventNumber_Type=Integer32
_NwDecIVEventNumber_Object=MibTableColumn
nwDecIVEventNumber=_NwDecIVEventNumber_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10,3,1,1,1),_NwDecIVEventNumber_Type())
nwDecIVEventNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVEventNumber.setStatus(_A)
_NwDecIVEventTime_Type=TimeTicks
_NwDecIVEventTime_Object=MibTableColumn
nwDecIVEventTime=_NwDecIVEventTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10,3,1,1,2),_NwDecIVEventTime_Type())
nwDecIVEventTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVEventTime.setStatus(_A)
class _NwDecIVEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16,32)));namedValues=NamedValues(*(('misc',1),('timer',2),('rcv',4),('xmit',8),('event',16),('error',32)))
_NwDecIVEventType_Type.__name__=_C
_NwDecIVEventType_Object=MibTableColumn
nwDecIVEventType=_NwDecIVEventType_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10,3,1,1,3),_NwDecIVEventType_Type())
nwDecIVEventType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVEventType.setStatus(_A)
class _NwDecIVEventSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_h,1),(_i,2),(_j,3)))
_NwDecIVEventSeverity_Type.__name__=_C
_NwDecIVEventSeverity_Object=MibTableColumn
nwDecIVEventSeverity=_NwDecIVEventSeverity_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10,3,1,1,4),_NwDecIVEventSeverity_Type())
nwDecIVEventSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVEventSeverity.setStatus(_A)
_NwDecIVEventProtocol_Type=Integer32
_NwDecIVEventProtocol_Object=MibTableColumn
nwDecIVEventProtocol=_NwDecIVEventProtocol_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10,3,1,1,5),_NwDecIVEventProtocol_Type())
nwDecIVEventProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVEventProtocol.setStatus(_A)
_NwDecIVEventIfNum_Type=Integer32
_NwDecIVEventIfNum_Object=MibTableColumn
nwDecIVEventIfNum=_NwDecIVEventIfNum_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10,3,1,1,6),_NwDecIVEventIfNum_Type())
nwDecIVEventIfNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVEventIfNum.setStatus(_A)
_NwDecIVEventTextString_Type=OctetString
_NwDecIVEventTextString_Object=MibTableColumn
nwDecIVEventTextString=_NwDecIVEventTextString_Object((1,3,6,1,4,1,52,4,2,2,2,3,3,2,10,3,1,1,7),_NwDecIVEventTextString_Type())
nwDecIVEventTextString.setMaxAccess(_B)
if mibBuilder.loadTexts:nwDecIVEventTextString.setStatus(_A)
_NwDecIVWorkGroup_ObjectIdentity=ObjectIdentity
nwDecIVWorkGroup=_NwDecIVWorkGroup_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,3,2,11))
mibBuilder.exportSymbols(_H,**{'DecIVAddress':DecIVAddress,'nwDecIVRouter':nwDecIVRouter,'nwDecIVMibs':nwDecIVMibs,'nwDecIVMibRevText':nwDecIVMibRevText,'nwDecIVComponents':nwDecIVComponents,'nwDecIVSystem':nwDecIVSystem,'nwDecIVSysConfig':nwDecIVSysConfig,'nwDecIVSysRouterId':nwDecIVSysRouterId,'nwDecIVNodeType':nwDecIVNodeType,'nwDecIVMaxNodes':nwDecIVMaxNodes,'nwDecIVMaxBRA':nwDecIVMaxBRA,'nwDecIVMaxBEA':nwDecIVMaxBEA,'nwDecIVMaxHops':nwDecIVMaxHops,'nwDecIVMaxCost':nwDecIVMaxCost,'nwDecIVMaxVisits':nwDecIVMaxVisits,'nwDecIVNonBroadcastTimer':nwDecIVNonBroadcastTimer,'nwDecIVBroadcastTimer':nwDecIVBroadcastTimer,'nwDecIVAreas':nwDecIVAreas,'nwDecIVMaxAreaHops':nwDecIVMaxAreaHops,'nwDecIVMaxAreaCost':nwDecIVMaxAreaCost,'nwDecIVSysAdministration':nwDecIVSysAdministration,'nwDecIVSysAdminStatus':nwDecIVSysAdminStatus,'nwDecIVSysOperStatus':nwDecIVSysOperStatus,'nwDecIVSysAdminReset':nwDecIVSysAdminReset,'nwDecIVSysOperationalTime':nwDecIVSysOperationalTime,'nwDecIVSysVersion':nwDecIVSysVersion,'nwDecIVForwarding':nwDecIVForwarding,'nwDecIVFwdSystem':nwDecIVFwdSystem,'nwDecIVFwdCounters':nwDecIVFwdCounters,'nwDecIVFwdCtrAdminStatus':nwDecIVFwdCtrAdminStatus,'nwDecIVFwdCtrReset':nwDecIVFwdCtrReset,'nwDecIVFwdCtrOperationalTime':nwDecIVFwdCtrOperationalTime,'nwDecIVFwdCtrInPkts':nwDecIVFwdCtrInPkts,'nwDecIVFwdCtrOutPkts':nwDecIVFwdCtrOutPkts,'nwDecIVFwdCtrFwdPkts':nwDecIVFwdCtrFwdPkts,'nwDecIVFwdCtrFilteredPkts':nwDecIVFwdCtrFilteredPkts,'nwDecIVFwdCtrDiscardPkts':nwDecIVFwdCtrDiscardPkts,'nwDecIVFwdCtrAddrErrPkts':nwDecIVFwdCtrAddrErrPkts,'nwDecIVFwdCtrLenErrPkts':nwDecIVFwdCtrLenErrPkts,'nwDecIVFwdCtrHdrErrPkts':nwDecIVFwdCtrHdrErrPkts,'nwDecIVFwdCtrInBytes':nwDecIVFwdCtrInBytes,'nwDecIVFwdCtrOutBytes':nwDecIVFwdCtrOutBytes,'nwDecIVFwdCtrFwdBytes':nwDecIVFwdCtrFwdBytes,'nwDecIVFwdCtrFilteredBytes':nwDecIVFwdCtrFilteredBytes,'nwDecIVFwdCtrDiscardBytes':nwDecIVFwdCtrDiscardBytes,'nwDecIVFwdCtrHostInPkts':nwDecIVFwdCtrHostInPkts,'nwDecIVFwdCtrHostOutPkts':nwDecIVFwdCtrHostOutPkts,'nwDecIVFwdCtrHostDiscardPkts':nwDecIVFwdCtrHostDiscardPkts,'nwDecIVFwdCtrHostInBytes':nwDecIVFwdCtrHostInBytes,'nwDecIVFwdCtrHostOutBytes':nwDecIVFwdCtrHostOutBytes,'nwDecIVFwdCtrHostDiscardBytes':nwDecIVFwdCtrHostDiscardBytes,'nwDecIVFwdInterfaces':nwDecIVFwdInterfaces,'nwDecIVFwdIfConfig':nwDecIVFwdIfConfig,'nwDecIVFwdIfTable':nwDecIVFwdIfTable,'nwDecIVFwdIfEntry':nwDecIVFwdIfEntry,_O:nwDecIVFwdIfIndex,'nwDecIVFwdIfAdminStatus':nwDecIVFwdIfAdminStatus,'nwDecIVFwdIfOperStatus':nwDecIVFwdIfOperStatus,'nwDecIVFwdIfOperationalTime':nwDecIVFwdIfOperationalTime,'nwDecIVFwdIfControl':nwDecIVFwdIfControl,'nwDecIVFwdIfMtu':nwDecIVFwdIfMtu,'nwDecIVFwdIfForwarding':nwDecIVFwdIfForwarding,'nwDecIVFwdIfFrameType':nwDecIVFwdIfFrameType,'nwDecIVFwdIfAclIdentifier':nwDecIVFwdIfAclIdentifier,'nwDecIVFwdIfAclStatus':nwDecIVFwdIfAclStatus,'nwDecIVFwdIfCacheControl':nwDecIVFwdIfCacheControl,'nwDecIVFwdIfCacheEntries':nwDecIVFwdIfCacheEntries,'nwDecIVFwdIfCacheHits':nwDecIVFwdIfCacheHits,'nwDecIVFwdIfCacheMisses':nwDecIVFwdIfCacheMisses,'nwDecIVFwdIfCounters':nwDecIVFwdIfCounters,'nwDecIVFwdIfCtrTable':nwDecIVFwdIfCtrTable,'nwDecIVFwdIfCtrEntry':nwDecIVFwdIfCtrEntry,_X:nwDecIVFwdIfCtrIfIndex,'nwDecIVFwdIfCtrAdminStatus':nwDecIVFwdIfCtrAdminStatus,'nwDecIVFwdIfCtrReset':nwDecIVFwdIfCtrReset,'nwDecIVFwdIfCtrOperationalTime':nwDecIVFwdIfCtrOperationalTime,'nwDecIVFwdIfCtrInPkts':nwDecIVFwdIfCtrInPkts,'nwDecIVFwdIfCtrOutPkts':nwDecIVFwdIfCtrOutPkts,'nwDecIVFwdIfCtrFwdPkts':nwDecIVFwdIfCtrFwdPkts,'nwDecIVFwdIfCtrFilteredPkts':nwDecIVFwdIfCtrFilteredPkts,'nwDecIVFwdIfCtrDiscardPkts':nwDecIVFwdIfCtrDiscardPkts,'nwDecIVFwdIfCtrAddrErrPkts':nwDecIVFwdIfCtrAddrErrPkts,'nwDecIVFwdIfCtrLenErrPkts':nwDecIVFwdIfCtrLenErrPkts,'nwDecIVFwdIfCtrHdrErrPkts':nwDecIVFwdIfCtrHdrErrPkts,'nwDecIVFwdIfCtrInBytes':nwDecIVFwdIfCtrInBytes,'nwDecIVFwdIfCtrOutBytes':nwDecIVFwdIfCtrOutBytes,'nwDecIVFwdIfCtrFwdBytes':nwDecIVFwdIfCtrFwdBytes,'nwDecIVFwdIfCtrFilteredBytes':nwDecIVFwdIfCtrFilteredBytes,'nwDecIVFwdIfCtrDiscardBytes':nwDecIVFwdIfCtrDiscardBytes,'nwDecIVFwdIfCtrHostInPkts':nwDecIVFwdIfCtrHostInPkts,'nwDecIVFwdIfCtrHostOutPkts':nwDecIVFwdIfCtrHostOutPkts,'nwDecIVFwdIfCtrHostDiscardPkts':nwDecIVFwdIfCtrHostDiscardPkts,'nwDecIVFwdIfCtrHostInBytes':nwDecIVFwdIfCtrHostInBytes,'nwDecIVFwdIfCtrHostOutBytes':nwDecIVFwdIfCtrHostOutBytes,'nwDecIVFwdIfCtrHostDiscardBytes':nwDecIVFwdIfCtrHostDiscardBytes,'nwDecIVTopology':nwDecIVTopology,'nwDecIVDistanceVector':nwDecIVDistanceVector,'nwDecIVProto':nwDecIVProto,'nwDecIVProtoSystem':nwDecIVProtoSystem,'nwDecIVProtoConfig':nwDecIVProtoConfig,'nwDecIVProtoAdminStatus':nwDecIVProtoAdminStatus,'nwDecIVProtoOperStatus':nwDecIVProtoOperStatus,'nwDecIVProtoAdminReset':nwDecIVProtoAdminReset,'nwDecIVProtoOperationalTime':nwDecIVProtoOperationalTime,'nwDecIVProtoVersion':nwDecIVProtoVersion,'nwDecIVProtoStackSize':nwDecIVProtoStackSize,'nwDecIVProtoThreadPriority':nwDecIVProtoThreadPriority,'nwDecIVProtoDatabaseThreshold':nwDecIVProtoDatabaseThreshold,'nwDecIVProtoAgeOut':nwDecIVProtoAgeOut,'nwDecIVProtoHoldDown':nwDecIVProtoHoldDown,'nwDecIVProtoCounters':nwDecIVProtoCounters,'nwDecIVProtoCtrAdminStatus':nwDecIVProtoCtrAdminStatus,'nwDecIVProtoCtrReset':nwDecIVProtoCtrReset,'nwDecIVProtoCtrOperationalTime':nwDecIVProtoCtrOperationalTime,'nwDecIVProtoCtrInPkts':nwDecIVProtoCtrInPkts,'nwDecIVProtoCtrOutPkts':nwDecIVProtoCtrOutPkts,'nwDecIVProtoCtrFilteredPkts':nwDecIVProtoCtrFilteredPkts,'nwDecIVProtoCtrDiscardPkts':nwDecIVProtoCtrDiscardPkts,'nwDecIVProtoCtrInBytes':nwDecIVProtoCtrInBytes,'nwDecIVProtoCtrOutBytes':nwDecIVProtoCtrOutBytes,'nwDecIVProtoCtrFilteredBytes':nwDecIVProtoCtrFilteredBytes,'nwDecIVProtoCtrDiscardBytes':nwDecIVProtoCtrDiscardBytes,'nwDecIVProtoInterface':nwDecIVProtoInterface,'nwDecIVProtoIfConfig':nwDecIVProtoIfConfig,'nwDecIVProtoIfTable':nwDecIVProtoIfTable,'nwDecIVProtoIfEntry':nwDecIVProtoIfEntry,_Y:nwDecIVProtoIfIndex,'nwDecIVProtoIfAdminStatus':nwDecIVProtoIfAdminStatus,'nwDecIVProtoIfOperStatus':nwDecIVProtoIfOperStatus,'nwDecIVProtoIfOperationalTime':nwDecIVProtoIfOperationalTime,'nwDecIVProtoIfVersion':nwDecIVProtoIfVersion,'nwDecIVProtoIfAdvertisement':nwDecIVProtoIfAdvertisement,'nwDecIVProtoIfFloodDelay':nwDecIVProtoIfFloodDelay,'nwDecIVProtoIfRequestDelay':nwDecIVProtoIfRequestDelay,'nwDecIVProtoIfPriority':nwDecIVProtoIfPriority,'nwDecIVProtoIfHelloTimer':nwDecIVProtoIfHelloTimer,'nwDecIVProtoIfSplitHorizon':nwDecIVProtoIfSplitHorizon,'nwDecIVProtoIfPoisonReverse':nwDecIVProtoIfPoisonReverse,'nwDecIVProtoIfSnooping':nwDecIVProtoIfSnooping,'nwDecIVProtoIfType':nwDecIVProtoIfType,'nwDecIVProtoIfXmitCost':nwDecIVProtoIfXmitCost,'nwDecIVProtoIfAclIdentifier':nwDecIVProtoIfAclIdentifier,'nwDecIVProtoIfAclStatus':nwDecIVProtoIfAclStatus,'nwDecIVProtoIfCounters':nwDecIVProtoIfCounters,'nwDecIVProtoIfCtrTable':nwDecIVProtoIfCtrTable,'nwDecIVProtoIfCtrEntry':nwDecIVProtoIfCtrEntry,_Z:nwDecIVProtoIfCtrIfIndex,'nwDecIVProtoIfCtrAdminStatus':nwDecIVProtoIfCtrAdminStatus,'nwDecIVProtoIfCtrReset':nwDecIVProtoIfCtrReset,'nwDecIVProtoIfCtrOperationalTime':nwDecIVProtoIfCtrOperationalTime,'nwDecIVProtoIfCtrInPkts':nwDecIVProtoIfCtrInPkts,'nwDecIVProtoIfCtrOutPkts':nwDecIVProtoIfCtrOutPkts,'nwDecIVProtoIfCtrFilteredPkts':nwDecIVProtoIfCtrFilteredPkts,'nwDecIVProtoIfCtrDiscardPkts':nwDecIVProtoIfCtrDiscardPkts,'nwDecIVProtoIfCtrInBytes':nwDecIVProtoIfCtrInBytes,'nwDecIVProtoIfCtrOutBytes':nwDecIVProtoIfCtrOutBytes,'nwDecIVProtoIfCtrFilteredBytes':nwDecIVProtoIfCtrFilteredBytes,'nwDecIVProtoIfCtrDiscardBytes':nwDecIVProtoIfCtrDiscardBytes,'nwDecIVLinkState':nwDecIVLinkState,'nwDecIVFib':nwDecIVFib,'nwDecIVFibTable':nwDecIVFibTable,'nwDecIVFibEntry':nwDecIVFibEntry,_a:nwDecIVFibNodeId,'nwDecIVFibNextHopNodeId':nwDecIVFibNextHopNodeId,'nwDecIVFibNextHopIf':nwDecIVFibNextHopIf,'nwDecIVFibRouteType':nwDecIVFibRouteType,'nwDecIVEndSystems':nwDecIVEndSystems,'nwDecIVHostsSystem':nwDecIVHostsSystem,'nwDecIVHostsInterfaces':nwDecIVHostsInterfaces,'nwDecIVHostsToMedia':nwDecIVHostsToMedia,'nwDecIVHostMapTable':nwDecIVHostMapTable,'nwDecIVHostMapEntry':nwDecIVHostMapEntry,_b:nwDecIVHostMapIfIndex,_c:nwDecIVHostMapDecIVAddr,'nwDecIVHostMapType':nwDecIVHostMapType,'nwDecIVHostMapCircuitID':nwDecIVHostMapCircuitID,'nwDecIVHostMapFraming':nwDecIVHostMapFraming,'nwDecIVHostMapPortNumber':nwDecIVHostMapPortNumber,'nwDecIVAccessControl':nwDecIVAccessControl,'nwDecIVAclValidEntries':nwDecIVAclValidEntries,'nwDecIVAclTable':nwDecIVAclTable,'nwDecIVAclEntry':nwDecIVAclEntry,_d:nwDecIVAclIdentifier,_e:nwDecIVAclSequence,'nwDecIVAclPermission':nwDecIVAclPermission,'nwDecIVAclMatches':nwDecIVAclMatches,'nwDecIVAclDestAddress':nwDecIVAclDestAddress,'nwDecIVAclSrcAddress':nwDecIVAclSrcAddress,'nwDecIVFilters':nwDecIVFilters,'nwDecIVRedirector':nwDecIVRedirector,'nwDecIVEvent':nwDecIVEvent,'nwDecIVEventLogConfig':nwDecIVEventLogConfig,'nwDecIVEventAdminStatus':nwDecIVEventAdminStatus,'nwDecIVEventMaxEntries':nwDecIVEventMaxEntries,'nwDecIVEventTraceAll':nwDecIVEventTraceAll,'nwDecIVEventLogFilterTable':nwDecIVEventLogFilterTable,'nwDecIVEventFilterTable':nwDecIVEventFilterTable,'nwDecIVEventFilterEntry':nwDecIVEventFilterEntry,_f:nwDecIVEventFltrProtocol,_g:nwDecIVEventFltrIfNum,'nwDecIVEventFltrControl':nwDecIVEventFltrControl,'nwDecIVEventFltrType':nwDecIVEventFltrType,'nwDecIVEventFltrSeverity':nwDecIVEventFltrSeverity,'nwDecIVEventFltrAction':nwDecIVEventFltrAction,'nwDecIVEventLogTable':nwDecIVEventLogTable,'nwDecIVEventTable':nwDecIVEventTable,'nwDecIVEventEntry':nwDecIVEventEntry,_k:nwDecIVEventNumber,'nwDecIVEventTime':nwDecIVEventTime,'nwDecIVEventType':nwDecIVEventType,'nwDecIVEventSeverity':nwDecIVEventSeverity,'nwDecIVEventProtocol':nwDecIVEventProtocol,'nwDecIVEventIfNum':nwDecIVEventIfNum,'nwDecIVEventTextString':nwDecIVEventTextString,'nwDecIVWorkGroup':nwDecIVWorkGroup})