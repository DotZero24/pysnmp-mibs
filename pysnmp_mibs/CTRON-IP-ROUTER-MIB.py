_AE='nwIpWgHostIfIndex'
_AD='nwIpWgHostHostAddr'
_AC='nwIpWgRngIfIndex'
_AB='nwIpWgRngEndHostAddr'
_AA='nwIpWgRngBegHostAddr'
_A9='workgroupInvalid'
_A8='nwIpWgIfIfIndex'
_A7='nwIpWgIfDefIdent'
_A6='nwIpWgDefIdentifier'
_A5='nwIpEventNumber'
_A4='nwIpEventFltrIfNum'
_A3='nwIpEventFltrProtocol'
_A2='nwIpRedirectPort'
_A1='nwIpAclSequence'
_A0='nwIpAclIdentifier'
_z='nwIpHostMapIpAddr'
_y='nwIpHostMapIfIndex'
_x='nwIpHostCtlIfIndex'
_w='inactive'
_v='nwIpOspfStaticNextHop'
_u='nwIpOspfStaticForwardMask'
_t='nwIpOspfStaticDest'
_s='nwIpOspfIfCtrIfIndex'
_r='nwIpOspfIfIndex'
_q='static'
_p='nwIpRipRtSrcNode'
_o='nwIpRipRtIfIndex'
_n='nwIpRipRtNetId'
_m='nwIpRipIfCtrIfIndex'
_l='nwIpRipIfIndex'
_k='nwIpFwdIfCtrIfIndex'
_j='nwIpAddrIfAddress'
_i='nwIpAddrIfIndex'
_h='canonical'
_g='encapfddisnap'
_f='encaptrsnap'
_e='encapenetsnap'
_d='encapenet'
_c='nativewan'
_b='localtalk'
_a='ethernet'
_Z='nwIpFwdIfIndex'
_Y='OctetString'
_X='internalError'
_W='destroy'
_V='createAndWait'
_U='createAndGo'
_T='notReady'
_S='notInService'
_R='invalid'
_Q='add'
_P='invalid-config'
_O='active'
_N='enable'
_M='disable'
_L='delete'
_K='pending-enable'
_J='pending-disable'
_I='reset'
_H='enabled'
_G='CTRON-IP-ROUTER-MIB'
_F='disabled'
_E='other'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Y,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nwRtrProtoSuites,=mibBuilder.importSymbols('ROUTER-OIDS','nwRtrProtoSuites')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_NwIpRouter_ObjectIdentity=ObjectIdentity
nwIpRouter=_NwIpRouter_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1))
_NwIpMibs_ObjectIdentity=ObjectIdentity
nwIpMibs=_NwIpMibs_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,1))
_NwIpMibRevText_Type=DisplayString
_NwIpMibRevText_Object=MibScalar
nwIpMibRevText=_NwIpMibRevText_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,1,1),_NwIpMibRevText_Type())
nwIpMibRevText.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpMibRevText.setStatus(_A)
_NwIpComponents_ObjectIdentity=ObjectIdentity
nwIpComponents=_NwIpComponents_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2))
_NwIpSystem_ObjectIdentity=ObjectIdentity
nwIpSystem=_NwIpSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,1))
_NwIpSysConfig_ObjectIdentity=ObjectIdentity
nwIpSysConfig=_NwIpSysConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,1,1))
_NwIpSysRouterId_Type=IpAddress
_NwIpSysRouterId_Object=MibScalar
nwIpSysRouterId=_NwIpSysRouterId_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,1,1,1),_NwIpSysRouterId_Type())
nwIpSysRouterId.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpSysRouterId.setStatus(_A)
_NwIpSysAdministration_ObjectIdentity=ObjectIdentity
nwIpSysAdministration=_NwIpSysAdministration_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,1,2))
class _NwIpSysAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3)))
_NwIpSysAdminStatus_Type.__name__=_D
_NwIpSysAdminStatus_Object=MibScalar
nwIpSysAdminStatus=_NwIpSysAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,1,2,1),_NwIpSysAdminStatus_Type())
nwIpSysAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpSysAdminStatus.setStatus(_A)
class _NwIpSysOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3),(_J,4),(_K,5),(_P,6)))
_NwIpSysOperStatus_Type.__name__=_D
_NwIpSysOperStatus_Object=MibScalar
nwIpSysOperStatus=_NwIpSysOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,1,2,2),_NwIpSysOperStatus_Type())
nwIpSysOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpSysOperStatus.setStatus(_A)
class _NwIpSysAdminReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpSysAdminReset_Type.__name__=_D
_NwIpSysAdminReset_Object=MibScalar
nwIpSysAdminReset=_NwIpSysAdminReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,1,2,3),_NwIpSysAdminReset_Type())
nwIpSysAdminReset.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpSysAdminReset.setStatus(_A)
_NwIpSysOperationalTime_Type=TimeTicks
_NwIpSysOperationalTime_Object=MibScalar
nwIpSysOperationalTime=_NwIpSysOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,1,2,4),_NwIpSysOperationalTime_Type())
nwIpSysOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpSysOperationalTime.setStatus(_A)
_NwIpSysVersion_Type=DisplayString
_NwIpSysVersion_Object=MibScalar
nwIpSysVersion=_NwIpSysVersion_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,1,2,5),_NwIpSysVersion_Type())
nwIpSysVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpSysVersion.setStatus(_A)
_NwIpForwarding_ObjectIdentity=ObjectIdentity
nwIpForwarding=_NwIpForwarding_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2))
_NwIpFwdSystem_ObjectIdentity=ObjectIdentity
nwIpFwdSystem=_NwIpFwdSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1))
_NwIpFwdCounters_ObjectIdentity=ObjectIdentity
nwIpFwdCounters=_NwIpFwdCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1,1))
class _NwIpFwdCtrAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3)))
_NwIpFwdCtrAdminStatus_Type.__name__=_D
_NwIpFwdCtrAdminStatus_Object=MibScalar
nwIpFwdCtrAdminStatus=_NwIpFwdCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1,1,1),_NwIpFwdCtrAdminStatus_Type())
nwIpFwdCtrAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpFwdCtrAdminStatus.setStatus(_A)
class _NwIpFwdCtrReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpFwdCtrReset_Type.__name__=_D
_NwIpFwdCtrReset_Object=MibScalar
nwIpFwdCtrReset=_NwIpFwdCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1,1,2),_NwIpFwdCtrReset_Type())
nwIpFwdCtrReset.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpFwdCtrReset.setStatus(_A)
_NwIpFwdCtrOperationalTime_Type=TimeTicks
_NwIpFwdCtrOperationalTime_Object=MibScalar
nwIpFwdCtrOperationalTime=_NwIpFwdCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1,1,3),_NwIpFwdCtrOperationalTime_Type())
nwIpFwdCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdCtrOperationalTime.setStatus(_A)
_NwIpFwdCtrInPkts_Type=Counter32
_NwIpFwdCtrInPkts_Object=MibScalar
nwIpFwdCtrInPkts=_NwIpFwdCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1,1,4),_NwIpFwdCtrInPkts_Type())
nwIpFwdCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdCtrInPkts.setStatus(_A)
_NwIpFwdCtrOutPkts_Type=Counter32
_NwIpFwdCtrOutPkts_Object=MibScalar
nwIpFwdCtrOutPkts=_NwIpFwdCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1,1,5),_NwIpFwdCtrOutPkts_Type())
nwIpFwdCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdCtrOutPkts.setStatus(_A)
_NwIpFwdCtrFwdPkts_Type=Counter32
_NwIpFwdCtrFwdPkts_Object=MibScalar
nwIpFwdCtrFwdPkts=_NwIpFwdCtrFwdPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1,1,6),_NwIpFwdCtrFwdPkts_Type())
nwIpFwdCtrFwdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdCtrFwdPkts.setStatus(_A)
_NwIpFwdCtrFilteredPkts_Type=Counter32
_NwIpFwdCtrFilteredPkts_Object=MibScalar
nwIpFwdCtrFilteredPkts=_NwIpFwdCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1,1,7),_NwIpFwdCtrFilteredPkts_Type())
nwIpFwdCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdCtrFilteredPkts.setStatus(_A)
_NwIpFwdCtrDiscardPkts_Type=Counter32
_NwIpFwdCtrDiscardPkts_Object=MibScalar
nwIpFwdCtrDiscardPkts=_NwIpFwdCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1,1,8),_NwIpFwdCtrDiscardPkts_Type())
nwIpFwdCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdCtrDiscardPkts.setStatus(_A)
_NwIpFwdCtrAddrErrPkts_Type=Counter32
_NwIpFwdCtrAddrErrPkts_Object=MibScalar
nwIpFwdCtrAddrErrPkts=_NwIpFwdCtrAddrErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1,1,9),_NwIpFwdCtrAddrErrPkts_Type())
nwIpFwdCtrAddrErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdCtrAddrErrPkts.setStatus(_A)
_NwIpFwdCtrLenErrPkts_Type=Counter32
_NwIpFwdCtrLenErrPkts_Object=MibScalar
nwIpFwdCtrLenErrPkts=_NwIpFwdCtrLenErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1,1,10),_NwIpFwdCtrLenErrPkts_Type())
nwIpFwdCtrLenErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdCtrLenErrPkts.setStatus(_A)
_NwIpFwdCtrHdrErrPkts_Type=Counter32
_NwIpFwdCtrHdrErrPkts_Object=MibScalar
nwIpFwdCtrHdrErrPkts=_NwIpFwdCtrHdrErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1,1,11),_NwIpFwdCtrHdrErrPkts_Type())
nwIpFwdCtrHdrErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdCtrHdrErrPkts.setStatus(_A)
_NwIpFwdCtrInBytes_Type=Counter32
_NwIpFwdCtrInBytes_Object=MibScalar
nwIpFwdCtrInBytes=_NwIpFwdCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1,1,12),_NwIpFwdCtrInBytes_Type())
nwIpFwdCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdCtrInBytes.setStatus(_A)
_NwIpFwdCtrOutBytes_Type=Counter32
_NwIpFwdCtrOutBytes_Object=MibScalar
nwIpFwdCtrOutBytes=_NwIpFwdCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1,1,13),_NwIpFwdCtrOutBytes_Type())
nwIpFwdCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdCtrOutBytes.setStatus(_A)
_NwIpFwdCtrFwdBytes_Type=Counter32
_NwIpFwdCtrFwdBytes_Object=MibScalar
nwIpFwdCtrFwdBytes=_NwIpFwdCtrFwdBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1,1,14),_NwIpFwdCtrFwdBytes_Type())
nwIpFwdCtrFwdBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdCtrFwdBytes.setStatus(_A)
_NwIpFwdCtrFilteredBytes_Type=Counter32
_NwIpFwdCtrFilteredBytes_Object=MibScalar
nwIpFwdCtrFilteredBytes=_NwIpFwdCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1,1,15),_NwIpFwdCtrFilteredBytes_Type())
nwIpFwdCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdCtrFilteredBytes.setStatus(_A)
_NwIpFwdCtrDiscardBytes_Type=Counter32
_NwIpFwdCtrDiscardBytes_Object=MibScalar
nwIpFwdCtrDiscardBytes=_NwIpFwdCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1,1,16),_NwIpFwdCtrDiscardBytes_Type())
nwIpFwdCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdCtrDiscardBytes.setStatus(_A)
_NwIpFwdCtrHostInPkts_Type=Counter32
_NwIpFwdCtrHostInPkts_Object=MibScalar
nwIpFwdCtrHostInPkts=_NwIpFwdCtrHostInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1,1,17),_NwIpFwdCtrHostInPkts_Type())
nwIpFwdCtrHostInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdCtrHostInPkts.setStatus(_A)
_NwIpFwdCtrHostOutPkts_Type=Counter32
_NwIpFwdCtrHostOutPkts_Object=MibScalar
nwIpFwdCtrHostOutPkts=_NwIpFwdCtrHostOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1,1,18),_NwIpFwdCtrHostOutPkts_Type())
nwIpFwdCtrHostOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdCtrHostOutPkts.setStatus(_A)
_NwIpFwdCtrHostDiscardPkts_Type=Counter32
_NwIpFwdCtrHostDiscardPkts_Object=MibScalar
nwIpFwdCtrHostDiscardPkts=_NwIpFwdCtrHostDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1,1,19),_NwIpFwdCtrHostDiscardPkts_Type())
nwIpFwdCtrHostDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdCtrHostDiscardPkts.setStatus(_A)
_NwIpFwdCtrHostInBytes_Type=Counter32
_NwIpFwdCtrHostInBytes_Object=MibScalar
nwIpFwdCtrHostInBytes=_NwIpFwdCtrHostInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1,1,20),_NwIpFwdCtrHostInBytes_Type())
nwIpFwdCtrHostInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdCtrHostInBytes.setStatus(_A)
_NwIpFwdCtrHostOutBytes_Type=Counter32
_NwIpFwdCtrHostOutBytes_Object=MibScalar
nwIpFwdCtrHostOutBytes=_NwIpFwdCtrHostOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1,1,21),_NwIpFwdCtrHostOutBytes_Type())
nwIpFwdCtrHostOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdCtrHostOutBytes.setStatus(_A)
_NwIpFwdCtrHostDiscardBytes_Type=Counter32
_NwIpFwdCtrHostDiscardBytes_Object=MibScalar
nwIpFwdCtrHostDiscardBytes=_NwIpFwdCtrHostDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,1,1,22),_NwIpFwdCtrHostDiscardBytes_Type())
nwIpFwdCtrHostDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdCtrHostDiscardBytes.setStatus(_A)
_NwIpFwdInterfaces_ObjectIdentity=ObjectIdentity
nwIpFwdInterfaces=_NwIpFwdInterfaces_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2))
_NwIpFwdIfConfig_ObjectIdentity=ObjectIdentity
nwIpFwdIfConfig=_NwIpFwdIfConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1))
_NwIpFwdIfTable_Object=MibTable
nwIpFwdIfTable=_NwIpFwdIfTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,1))
if mibBuilder.loadTexts:nwIpFwdIfTable.setStatus(_A)
_NwIpFwdIfEntry_Object=MibTableRow
nwIpFwdIfEntry=_NwIpFwdIfEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,1,1))
nwIpFwdIfEntry.setIndexNames((0,_G,_Z))
if mibBuilder.loadTexts:nwIpFwdIfEntry.setStatus(_A)
_NwIpFwdIfIndex_Type=Integer32
_NwIpFwdIfIndex_Object=MibTableColumn
nwIpFwdIfIndex=_NwIpFwdIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,1,1,1),_NwIpFwdIfIndex_Type())
nwIpFwdIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfIndex.setStatus(_A)
class _NwIpFwdIfAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3)))
_NwIpFwdIfAdminStatus_Type.__name__=_D
_NwIpFwdIfAdminStatus_Object=MibTableColumn
nwIpFwdIfAdminStatus=_NwIpFwdIfAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,1,1,2),_NwIpFwdIfAdminStatus_Type())
nwIpFwdIfAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpFwdIfAdminStatus.setStatus(_A)
class _NwIpFwdIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3),(_J,4),(_K,5),(_P,6)))
_NwIpFwdIfOperStatus_Type.__name__=_D
_NwIpFwdIfOperStatus_Object=MibTableColumn
nwIpFwdIfOperStatus=_NwIpFwdIfOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,1,1,3),_NwIpFwdIfOperStatus_Type())
nwIpFwdIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfOperStatus.setStatus(_A)
_NwIpFwdIfOperationalTime_Type=TimeTicks
_NwIpFwdIfOperationalTime_Object=MibTableColumn
nwIpFwdIfOperationalTime=_NwIpFwdIfOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,1,1,4),_NwIpFwdIfOperationalTime_Type())
nwIpFwdIfOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfOperationalTime.setStatus(_A)
class _NwIpFwdIfControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_Q,2),(_L,3)))
_NwIpFwdIfControl_Type.__name__=_D
_NwIpFwdIfControl_Object=MibTableColumn
nwIpFwdIfControl=_NwIpFwdIfControl_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,1,1,5),_NwIpFwdIfControl_Type())
nwIpFwdIfControl.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpFwdIfControl.setStatus(_A)
class _NwIpFwdIfMtu_Type(Integer32):defaultValue=1500
_NwIpFwdIfMtu_Type.__name__=_D
_NwIpFwdIfMtu_Object=MibTableColumn
nwIpFwdIfMtu=_NwIpFwdIfMtu_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,1,1,6),_NwIpFwdIfMtu_Type())
nwIpFwdIfMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpFwdIfMtu.setStatus(_A)
class _NwIpFwdIfForwarding_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3)))
_NwIpFwdIfForwarding_Type.__name__=_D
_NwIpFwdIfForwarding_Object=MibTableColumn
nwIpFwdIfForwarding=_NwIpFwdIfForwarding_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,1,1,7),_NwIpFwdIfForwarding_Type())
nwIpFwdIfForwarding.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpFwdIfForwarding.setStatus(_A)
class _NwIpFwdIfFrameType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5,7,8,9,11,14,16,17)));namedValues=NamedValues(*((_E,1),(_a,2),('snap',3),('slip',5),(_b,7),(_c,8),(_d,9),(_e,11),(_f,14),(_g,16),(_h,17)))
_NwIpFwdIfFrameType_Type.__name__=_D
_NwIpFwdIfFrameType_Object=MibTableColumn
nwIpFwdIfFrameType=_NwIpFwdIfFrameType_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,1,1,8),_NwIpFwdIfFrameType_Type())
nwIpFwdIfFrameType.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpFwdIfFrameType.setStatus(_A)
class _NwIpFwdIfAclIdentifier_Type(Integer32):defaultValue=0
_NwIpFwdIfAclIdentifier_Type.__name__=_D
_NwIpFwdIfAclIdentifier_Object=MibTableColumn
nwIpFwdIfAclIdentifier=_NwIpFwdIfAclIdentifier_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,1,1,9),_NwIpFwdIfAclIdentifier_Type())
nwIpFwdIfAclIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpFwdIfAclIdentifier.setStatus(_A)
class _NwIpFwdIfAclStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3)))
_NwIpFwdIfAclStatus_Type.__name__=_D
_NwIpFwdIfAclStatus_Object=MibTableColumn
nwIpFwdIfAclStatus=_NwIpFwdIfAclStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,1,1,10),_NwIpFwdIfAclStatus_Type())
nwIpFwdIfAclStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpFwdIfAclStatus.setStatus(_A)
class _NwIpFwdIfCacheControl_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_M,2),(_N,3)))
_NwIpFwdIfCacheControl_Type.__name__=_D
_NwIpFwdIfCacheControl_Object=MibTableColumn
nwIpFwdIfCacheControl=_NwIpFwdIfCacheControl_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,1,1,11),_NwIpFwdIfCacheControl_Type())
nwIpFwdIfCacheControl.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpFwdIfCacheControl.setStatus(_A)
_NwIpFwdIfCacheEntries_Type=Counter32
_NwIpFwdIfCacheEntries_Object=MibTableColumn
nwIpFwdIfCacheEntries=_NwIpFwdIfCacheEntries_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,1,1,12),_NwIpFwdIfCacheEntries_Type())
nwIpFwdIfCacheEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCacheEntries.setStatus(_A)
_NwIpFwdIfCacheHits_Type=Counter32
_NwIpFwdIfCacheHits_Object=MibTableColumn
nwIpFwdIfCacheHits=_NwIpFwdIfCacheHits_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,1,1,13),_NwIpFwdIfCacheHits_Type())
nwIpFwdIfCacheHits.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCacheHits.setStatus(_A)
_NwIpFwdIfCacheMisses_Type=Counter32
_NwIpFwdIfCacheMisses_Object=MibTableColumn
nwIpFwdIfCacheMisses=_NwIpFwdIfCacheMisses_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,1,1,14),_NwIpFwdIfCacheMisses_Type())
nwIpFwdIfCacheMisses.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCacheMisses.setStatus(_A)
_NwIpAddressTable_Object=MibTable
nwIpAddressTable=_NwIpAddressTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,2))
if mibBuilder.loadTexts:nwIpAddressTable.setStatus(_A)
_NwIpAddrEntry_Object=MibTableRow
nwIpAddrEntry=_NwIpAddrEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,2,1))
nwIpAddrEntry.setIndexNames((0,_G,_i),(0,_G,_j))
if mibBuilder.loadTexts:nwIpAddrEntry.setStatus(_A)
_NwIpAddrIfIndex_Type=Integer32
_NwIpAddrIfIndex_Object=MibTableColumn
nwIpAddrIfIndex=_NwIpAddrIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,2,1,1),_NwIpAddrIfIndex_Type())
nwIpAddrIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpAddrIfIndex.setStatus(_A)
_NwIpAddrIfAddress_Type=IpAddress
_NwIpAddrIfAddress_Object=MibTableColumn
nwIpAddrIfAddress=_NwIpAddrIfAddress_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,2,1,2),_NwIpAddrIfAddress_Type())
nwIpAddrIfAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpAddrIfAddress.setStatus(_A)
class _NwIpAddrIfControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_Q,2),(_L,3)))
_NwIpAddrIfControl_Type.__name__=_D
_NwIpAddrIfControl_Object=MibTableColumn
nwIpAddrIfControl=_NwIpAddrIfControl_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,2,1,3),_NwIpAddrIfControl_Type())
nwIpAddrIfControl.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpAddrIfControl.setStatus(_A)
class _NwIpAddrIfAddrType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('primary',2),('secondary',3),('workgroup',4)))
_NwIpAddrIfAddrType_Type.__name__=_D
_NwIpAddrIfAddrType_Object=MibTableColumn
nwIpAddrIfAddrType=_NwIpAddrIfAddrType_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,2,1,4),_NwIpAddrIfAddrType_Type())
nwIpAddrIfAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpAddrIfAddrType.setStatus(_A)
_NwIpAddrIfMask_Type=IpAddress
_NwIpAddrIfMask_Object=MibTableColumn
nwIpAddrIfMask=_NwIpAddrIfMask_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,2,1,5),_NwIpAddrIfMask_Type())
nwIpAddrIfMask.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpAddrIfMask.setStatus(_A)
class _NwIpAddrIfBcastAddr_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('zeros',2),('ones',3)))
_NwIpAddrIfBcastAddr_Type.__name__=_D
_NwIpAddrIfBcastAddr_Object=MibTableColumn
nwIpAddrIfBcastAddr=_NwIpAddrIfBcastAddr_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,1,2,1,6),_NwIpAddrIfBcastAddr_Type())
nwIpAddrIfBcastAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpAddrIfBcastAddr.setStatus(_A)
_NwIpFwdIfCounters_ObjectIdentity=ObjectIdentity
nwIpFwdIfCounters=_NwIpFwdIfCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2))
_NwIpFwdIfCtrTable_Object=MibTable
nwIpFwdIfCtrTable=_NwIpFwdIfCtrTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1))
if mibBuilder.loadTexts:nwIpFwdIfCtrTable.setStatus(_A)
_NwIpFwdIfCtrEntry_Object=MibTableRow
nwIpFwdIfCtrEntry=_NwIpFwdIfCtrEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1))
nwIpFwdIfCtrEntry.setIndexNames((0,_G,_k))
if mibBuilder.loadTexts:nwIpFwdIfCtrEntry.setStatus(_A)
_NwIpFwdIfCtrIfIndex_Type=Integer32
_NwIpFwdIfCtrIfIndex_Object=MibTableColumn
nwIpFwdIfCtrIfIndex=_NwIpFwdIfCtrIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1,1),_NwIpFwdIfCtrIfIndex_Type())
nwIpFwdIfCtrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCtrIfIndex.setStatus(_A)
class _NwIpFwdIfCtrAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3)))
_NwIpFwdIfCtrAdminStatus_Type.__name__=_D
_NwIpFwdIfCtrAdminStatus_Object=MibTableColumn
nwIpFwdIfCtrAdminStatus=_NwIpFwdIfCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1,2),_NwIpFwdIfCtrAdminStatus_Type())
nwIpFwdIfCtrAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpFwdIfCtrAdminStatus.setStatus(_A)
class _NwIpFwdIfCtrReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpFwdIfCtrReset_Type.__name__=_D
_NwIpFwdIfCtrReset_Object=MibTableColumn
nwIpFwdIfCtrReset=_NwIpFwdIfCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1,3),_NwIpFwdIfCtrReset_Type())
nwIpFwdIfCtrReset.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpFwdIfCtrReset.setStatus(_A)
_NwIpFwdIfCtrOperationalTime_Type=TimeTicks
_NwIpFwdIfCtrOperationalTime_Object=MibTableColumn
nwIpFwdIfCtrOperationalTime=_NwIpFwdIfCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1,4),_NwIpFwdIfCtrOperationalTime_Type())
nwIpFwdIfCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCtrOperationalTime.setStatus(_A)
_NwIpFwdIfCtrInPkts_Type=Counter32
_NwIpFwdIfCtrInPkts_Object=MibTableColumn
nwIpFwdIfCtrInPkts=_NwIpFwdIfCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1,5),_NwIpFwdIfCtrInPkts_Type())
nwIpFwdIfCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCtrInPkts.setStatus(_A)
_NwIpFwdIfCtrOutPkts_Type=Counter32
_NwIpFwdIfCtrOutPkts_Object=MibTableColumn
nwIpFwdIfCtrOutPkts=_NwIpFwdIfCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1,6),_NwIpFwdIfCtrOutPkts_Type())
nwIpFwdIfCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCtrOutPkts.setStatus(_A)
_NwIpFwdIfCtrFwdPkts_Type=Counter32
_NwIpFwdIfCtrFwdPkts_Object=MibTableColumn
nwIpFwdIfCtrFwdPkts=_NwIpFwdIfCtrFwdPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1,7),_NwIpFwdIfCtrFwdPkts_Type())
nwIpFwdIfCtrFwdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCtrFwdPkts.setStatus(_A)
_NwIpFwdIfCtrFilteredPkts_Type=Counter32
_NwIpFwdIfCtrFilteredPkts_Object=MibTableColumn
nwIpFwdIfCtrFilteredPkts=_NwIpFwdIfCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1,8),_NwIpFwdIfCtrFilteredPkts_Type())
nwIpFwdIfCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCtrFilteredPkts.setStatus(_A)
_NwIpFwdIfCtrDiscardPkts_Type=Counter32
_NwIpFwdIfCtrDiscardPkts_Object=MibTableColumn
nwIpFwdIfCtrDiscardPkts=_NwIpFwdIfCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1,9),_NwIpFwdIfCtrDiscardPkts_Type())
nwIpFwdIfCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCtrDiscardPkts.setStatus(_A)
_NwIpFwdIfCtrAddrErrPkts_Type=Counter32
_NwIpFwdIfCtrAddrErrPkts_Object=MibTableColumn
nwIpFwdIfCtrAddrErrPkts=_NwIpFwdIfCtrAddrErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1,10),_NwIpFwdIfCtrAddrErrPkts_Type())
nwIpFwdIfCtrAddrErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCtrAddrErrPkts.setStatus(_A)
_NwIpFwdIfCtrLenErrPkts_Type=Counter32
_NwIpFwdIfCtrLenErrPkts_Object=MibTableColumn
nwIpFwdIfCtrLenErrPkts=_NwIpFwdIfCtrLenErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1,11),_NwIpFwdIfCtrLenErrPkts_Type())
nwIpFwdIfCtrLenErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCtrLenErrPkts.setStatus(_A)
_NwIpFwdIfCtrHdrErrPkts_Type=Counter32
_NwIpFwdIfCtrHdrErrPkts_Object=MibTableColumn
nwIpFwdIfCtrHdrErrPkts=_NwIpFwdIfCtrHdrErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1,12),_NwIpFwdIfCtrHdrErrPkts_Type())
nwIpFwdIfCtrHdrErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCtrHdrErrPkts.setStatus(_A)
_NwIpFwdIfCtrInBytes_Type=Counter32
_NwIpFwdIfCtrInBytes_Object=MibTableColumn
nwIpFwdIfCtrInBytes=_NwIpFwdIfCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1,13),_NwIpFwdIfCtrInBytes_Type())
nwIpFwdIfCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCtrInBytes.setStatus(_A)
_NwIpFwdIfCtrOutBytes_Type=Counter32
_NwIpFwdIfCtrOutBytes_Object=MibTableColumn
nwIpFwdIfCtrOutBytes=_NwIpFwdIfCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1,14),_NwIpFwdIfCtrOutBytes_Type())
nwIpFwdIfCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCtrOutBytes.setStatus(_A)
_NwIpFwdIfCtrFwdBytes_Type=Counter32
_NwIpFwdIfCtrFwdBytes_Object=MibTableColumn
nwIpFwdIfCtrFwdBytes=_NwIpFwdIfCtrFwdBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1,15),_NwIpFwdIfCtrFwdBytes_Type())
nwIpFwdIfCtrFwdBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCtrFwdBytes.setStatus(_A)
_NwIpFwdIfCtrFilteredBytes_Type=Counter32
_NwIpFwdIfCtrFilteredBytes_Object=MibTableColumn
nwIpFwdIfCtrFilteredBytes=_NwIpFwdIfCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1,16),_NwIpFwdIfCtrFilteredBytes_Type())
nwIpFwdIfCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCtrFilteredBytes.setStatus(_A)
_NwIpFwdIfCtrDiscardBytes_Type=Counter32
_NwIpFwdIfCtrDiscardBytes_Object=MibTableColumn
nwIpFwdIfCtrDiscardBytes=_NwIpFwdIfCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1,17),_NwIpFwdIfCtrDiscardBytes_Type())
nwIpFwdIfCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCtrDiscardBytes.setStatus(_A)
_NwIpFwdIfCtrHostInPkts_Type=Counter32
_NwIpFwdIfCtrHostInPkts_Object=MibTableColumn
nwIpFwdIfCtrHostInPkts=_NwIpFwdIfCtrHostInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1,18),_NwIpFwdIfCtrHostInPkts_Type())
nwIpFwdIfCtrHostInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCtrHostInPkts.setStatus(_A)
_NwIpFwdIfCtrHostOutPkts_Type=Counter32
_NwIpFwdIfCtrHostOutPkts_Object=MibTableColumn
nwIpFwdIfCtrHostOutPkts=_NwIpFwdIfCtrHostOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1,19),_NwIpFwdIfCtrHostOutPkts_Type())
nwIpFwdIfCtrHostOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCtrHostOutPkts.setStatus(_A)
_NwIpFwdIfCtrHostDiscardPkts_Type=Counter32
_NwIpFwdIfCtrHostDiscardPkts_Object=MibTableColumn
nwIpFwdIfCtrHostDiscardPkts=_NwIpFwdIfCtrHostDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1,20),_NwIpFwdIfCtrHostDiscardPkts_Type())
nwIpFwdIfCtrHostDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCtrHostDiscardPkts.setStatus(_A)
_NwIpFwdIfCtrHostInBytes_Type=Counter32
_NwIpFwdIfCtrHostInBytes_Object=MibTableColumn
nwIpFwdIfCtrHostInBytes=_NwIpFwdIfCtrHostInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1,21),_NwIpFwdIfCtrHostInBytes_Type())
nwIpFwdIfCtrHostInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCtrHostInBytes.setStatus(_A)
_NwIpFwdIfCtrHostOutBytes_Type=Counter32
_NwIpFwdIfCtrHostOutBytes_Object=MibTableColumn
nwIpFwdIfCtrHostOutBytes=_NwIpFwdIfCtrHostOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1,22),_NwIpFwdIfCtrHostOutBytes_Type())
nwIpFwdIfCtrHostOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCtrHostOutBytes.setStatus(_A)
_NwIpFwdIfCtrHostDiscardBytes_Type=Counter32
_NwIpFwdIfCtrHostDiscardBytes_Object=MibTableColumn
nwIpFwdIfCtrHostDiscardBytes=_NwIpFwdIfCtrHostDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,2,2,2,1,1,23),_NwIpFwdIfCtrHostDiscardBytes_Type())
nwIpFwdIfCtrHostDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpFwdIfCtrHostDiscardBytes.setStatus(_A)
_NwIpTopology_ObjectIdentity=ObjectIdentity
nwIpTopology=_NwIpTopology_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4))
_NwIpDistanceVector_ObjectIdentity=ObjectIdentity
nwIpDistanceVector=_NwIpDistanceVector_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1))
_NwIpRip_ObjectIdentity=ObjectIdentity
nwIpRip=_NwIpRip_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1))
_NwIpRipSystem_ObjectIdentity=ObjectIdentity
nwIpRipSystem=_NwIpRipSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1))
_NwIpRipConfig_ObjectIdentity=ObjectIdentity
nwIpRipConfig=_NwIpRipConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1,1))
class _NwIpRipAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3)))
_NwIpRipAdminStatus_Type.__name__=_D
_NwIpRipAdminStatus_Object=MibScalar
nwIpRipAdminStatus=_NwIpRipAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1,1,1),_NwIpRipAdminStatus_Type())
nwIpRipAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipAdminStatus.setStatus(_A)
class _NwIpRipOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3),(_J,4),(_K,5),(_P,6)))
_NwIpRipOperStatus_Type.__name__=_D
_NwIpRipOperStatus_Object=MibScalar
nwIpRipOperStatus=_NwIpRipOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1,1,2),_NwIpRipOperStatus_Type())
nwIpRipOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipOperStatus.setStatus(_A)
class _NwIpRipAdminReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpRipAdminReset_Type.__name__=_D
_NwIpRipAdminReset_Object=MibScalar
nwIpRipAdminReset=_NwIpRipAdminReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1,1,3),_NwIpRipAdminReset_Type())
nwIpRipAdminReset.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipAdminReset.setStatus(_A)
_NwIpRipOperationalTime_Type=TimeTicks
_NwIpRipOperationalTime_Object=MibScalar
nwIpRipOperationalTime=_NwIpRipOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1,1,4),_NwIpRipOperationalTime_Type())
nwIpRipOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipOperationalTime.setStatus(_A)
_NwIpRipVersion_Type=DisplayString
_NwIpRipVersion_Object=MibScalar
nwIpRipVersion=_NwIpRipVersion_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1,1,5),_NwIpRipVersion_Type())
nwIpRipVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipVersion.setStatus(_A)
class _NwIpRipStackSize_Type(Integer32):defaultValue=4096
_NwIpRipStackSize_Type.__name__=_D
_NwIpRipStackSize_Object=MibScalar
nwIpRipStackSize=_NwIpRipStackSize_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1,1,6),_NwIpRipStackSize_Type())
nwIpRipStackSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipStackSize.setStatus(_A)
class _NwIpRipThreadPriority_Type(Integer32):defaultValue=127
_NwIpRipThreadPriority_Type.__name__=_D
_NwIpRipThreadPriority_Object=MibScalar
nwIpRipThreadPriority=_NwIpRipThreadPriority_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1,1,7),_NwIpRipThreadPriority_Type())
nwIpRipThreadPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipThreadPriority.setStatus(_A)
class _NwIpRipDatabaseThreshold_Type(Integer32):defaultValue=2000
_NwIpRipDatabaseThreshold_Type.__name__=_D
_NwIpRipDatabaseThreshold_Object=MibScalar
nwIpRipDatabaseThreshold=_NwIpRipDatabaseThreshold_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1,1,8),_NwIpRipDatabaseThreshold_Type())
nwIpRipDatabaseThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipDatabaseThreshold.setStatus(_A)
class _NwIpRipAgeOut_Type(Integer32):defaultValue=210
_NwIpRipAgeOut_Type.__name__=_D
_NwIpRipAgeOut_Object=MibScalar
nwIpRipAgeOut=_NwIpRipAgeOut_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1,1,9),_NwIpRipAgeOut_Type())
nwIpRipAgeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipAgeOut.setStatus(_A)
class _NwIpRipHoldDown_Type(Integer32):defaultValue=120
_NwIpRipHoldDown_Type.__name__=_D
_NwIpRipHoldDown_Object=MibScalar
nwIpRipHoldDown=_NwIpRipHoldDown_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1,1,10),_NwIpRipHoldDown_Type())
nwIpRipHoldDown.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipHoldDown.setStatus(_A)
_NwIpRipCounters_ObjectIdentity=ObjectIdentity
nwIpRipCounters=_NwIpRipCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1,2))
class _NwIpRipCtrAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3)))
_NwIpRipCtrAdminStatus_Type.__name__=_D
_NwIpRipCtrAdminStatus_Object=MibScalar
nwIpRipCtrAdminStatus=_NwIpRipCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1,2,1),_NwIpRipCtrAdminStatus_Type())
nwIpRipCtrAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipCtrAdminStatus.setStatus(_A)
class _NwIpRipCtrReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpRipCtrReset_Type.__name__=_D
_NwIpRipCtrReset_Object=MibScalar
nwIpRipCtrReset=_NwIpRipCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1,2,2),_NwIpRipCtrReset_Type())
nwIpRipCtrReset.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipCtrReset.setStatus(_A)
_NwIpRipCtrOperationalTime_Type=TimeTicks
_NwIpRipCtrOperationalTime_Object=MibScalar
nwIpRipCtrOperationalTime=_NwIpRipCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1,2,3),_NwIpRipCtrOperationalTime_Type())
nwIpRipCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipCtrOperationalTime.setStatus(_A)
_NwIpRipCtrInPkts_Type=Counter32
_NwIpRipCtrInPkts_Object=MibScalar
nwIpRipCtrInPkts=_NwIpRipCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1,2,4),_NwIpRipCtrInPkts_Type())
nwIpRipCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipCtrInPkts.setStatus(_A)
_NwIpRipCtrOutPkts_Type=Counter32
_NwIpRipCtrOutPkts_Object=MibScalar
nwIpRipCtrOutPkts=_NwIpRipCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1,2,5),_NwIpRipCtrOutPkts_Type())
nwIpRipCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipCtrOutPkts.setStatus(_A)
_NwIpRipCtrFilteredPkts_Type=Counter32
_NwIpRipCtrFilteredPkts_Object=MibScalar
nwIpRipCtrFilteredPkts=_NwIpRipCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1,2,6),_NwIpRipCtrFilteredPkts_Type())
nwIpRipCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipCtrFilteredPkts.setStatus(_A)
_NwIpRipCtrDiscardPkts_Type=Counter32
_NwIpRipCtrDiscardPkts_Object=MibScalar
nwIpRipCtrDiscardPkts=_NwIpRipCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1,2,7),_NwIpRipCtrDiscardPkts_Type())
nwIpRipCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipCtrDiscardPkts.setStatus(_A)
_NwIpRipCtrInBytes_Type=Counter32
_NwIpRipCtrInBytes_Object=MibScalar
nwIpRipCtrInBytes=_NwIpRipCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1,2,8),_NwIpRipCtrInBytes_Type())
nwIpRipCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipCtrInBytes.setStatus(_A)
_NwIpRipCtrOutBytes_Type=Counter32
_NwIpRipCtrOutBytes_Object=MibScalar
nwIpRipCtrOutBytes=_NwIpRipCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1,2,9),_NwIpRipCtrOutBytes_Type())
nwIpRipCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipCtrOutBytes.setStatus(_A)
_NwIpRipCtrFilteredBytes_Type=Counter32
_NwIpRipCtrFilteredBytes_Object=MibScalar
nwIpRipCtrFilteredBytes=_NwIpRipCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1,2,10),_NwIpRipCtrFilteredBytes_Type())
nwIpRipCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipCtrFilteredBytes.setStatus(_A)
_NwIpRipCtrDiscardBytes_Type=Counter32
_NwIpRipCtrDiscardBytes_Object=MibScalar
nwIpRipCtrDiscardBytes=_NwIpRipCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,1,2,11),_NwIpRipCtrDiscardBytes_Type())
nwIpRipCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipCtrDiscardBytes.setStatus(_A)
_NwIpRipInterfaces_ObjectIdentity=ObjectIdentity
nwIpRipInterfaces=_NwIpRipInterfaces_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2))
_NwIpRipIfConfig_ObjectIdentity=ObjectIdentity
nwIpRipIfConfig=_NwIpRipIfConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,1))
_NwIpRipIfTable_Object=MibTable
nwIpRipIfTable=_NwIpRipIfTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,1,1))
if mibBuilder.loadTexts:nwIpRipIfTable.setStatus(_A)
_NwIpRipIfEntry_Object=MibTableRow
nwIpRipIfEntry=_NwIpRipIfEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,1,1,1))
nwIpRipIfEntry.setIndexNames((0,_G,_l))
if mibBuilder.loadTexts:nwIpRipIfEntry.setStatus(_A)
_NwIpRipIfIndex_Type=Integer32
_NwIpRipIfIndex_Object=MibTableColumn
nwIpRipIfIndex=_NwIpRipIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,1,1,1,1),_NwIpRipIfIndex_Type())
nwIpRipIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipIfIndex.setStatus(_A)
class _NwIpRipIfAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3)))
_NwIpRipIfAdminStatus_Type.__name__=_D
_NwIpRipIfAdminStatus_Object=MibTableColumn
nwIpRipIfAdminStatus=_NwIpRipIfAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,1,1,1,2),_NwIpRipIfAdminStatus_Type())
nwIpRipIfAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipIfAdminStatus.setStatus(_A)
class _NwIpRipIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3),(_J,4),(_K,5)))
_NwIpRipIfOperStatus_Type.__name__=_D
_NwIpRipIfOperStatus_Object=MibTableColumn
nwIpRipIfOperStatus=_NwIpRipIfOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,1,1,1,3),_NwIpRipIfOperStatus_Type())
nwIpRipIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipIfOperStatus.setStatus(_A)
_NwIpRipIfOperationalTime_Type=TimeTicks
_NwIpRipIfOperationalTime_Object=MibTableColumn
nwIpRipIfOperationalTime=_NwIpRipIfOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,1,1,1,4),_NwIpRipIfOperationalTime_Type())
nwIpRipIfOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipIfOperationalTime.setStatus(_A)
class _NwIpRipIfVersion_Type(Integer32):defaultValue=1
_NwIpRipIfVersion_Type.__name__=_D
_NwIpRipIfVersion_Object=MibTableColumn
nwIpRipIfVersion=_NwIpRipIfVersion_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,1,1,1,5),_NwIpRipIfVersion_Type())
nwIpRipIfVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipIfVersion.setStatus(_A)
class _NwIpRipIfAdvertisement_Type(Integer32):defaultValue=30
_NwIpRipIfAdvertisement_Type.__name__=_D
_NwIpRipIfAdvertisement_Object=MibTableColumn
nwIpRipIfAdvertisement=_NwIpRipIfAdvertisement_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,1,1,1,6),_NwIpRipIfAdvertisement_Type())
nwIpRipIfAdvertisement.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipIfAdvertisement.setStatus(_A)
class _NwIpRipIfFloodDelay_Type(Integer32):defaultValue=2
_NwIpRipIfFloodDelay_Type.__name__=_D
_NwIpRipIfFloodDelay_Object=MibTableColumn
nwIpRipIfFloodDelay=_NwIpRipIfFloodDelay_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,1,1,1,7),_NwIpRipIfFloodDelay_Type())
nwIpRipIfFloodDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipIfFloodDelay.setStatus(_A)
class _NwIpRipIfRequestDelay_Type(Integer32):defaultValue=0
_NwIpRipIfRequestDelay_Type.__name__=_D
_NwIpRipIfRequestDelay_Object=MibTableColumn
nwIpRipIfRequestDelay=_NwIpRipIfRequestDelay_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,1,1,1,8),_NwIpRipIfRequestDelay_Type())
nwIpRipIfRequestDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipIfRequestDelay.setStatus(_A)
class _NwIpRipIfPriority_Type(Integer32):defaultValue=1
_NwIpRipIfPriority_Type.__name__=_D
_NwIpRipIfPriority_Object=MibTableColumn
nwIpRipIfPriority=_NwIpRipIfPriority_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,1,1,1,9),_NwIpRipIfPriority_Type())
nwIpRipIfPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipIfPriority.setStatus(_A)
class _NwIpRipIfHelloTimer_Type(Integer32):defaultValue=10
_NwIpRipIfHelloTimer_Type.__name__=_D
_NwIpRipIfHelloTimer_Object=MibTableColumn
nwIpRipIfHelloTimer=_NwIpRipIfHelloTimer_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,1,1,1,10),_NwIpRipIfHelloTimer_Type())
nwIpRipIfHelloTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipIfHelloTimer.setStatus(_A)
class _NwIpRipIfSplitHorizon_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3)))
_NwIpRipIfSplitHorizon_Type.__name__=_D
_NwIpRipIfSplitHorizon_Object=MibTableColumn
nwIpRipIfSplitHorizon=_NwIpRipIfSplitHorizon_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,1,1,1,11),_NwIpRipIfSplitHorizon_Type())
nwIpRipIfSplitHorizon.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipIfSplitHorizon.setStatus(_A)
class _NwIpRipIfPoisonReverse_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3)))
_NwIpRipIfPoisonReverse_Type.__name__=_D
_NwIpRipIfPoisonReverse_Object=MibTableColumn
nwIpRipIfPoisonReverse=_NwIpRipIfPoisonReverse_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,1,1,1,12),_NwIpRipIfPoisonReverse_Type())
nwIpRipIfPoisonReverse.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipIfPoisonReverse.setStatus(_A)
class _NwIpRipIfSnooping_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3)))
_NwIpRipIfSnooping_Type.__name__=_D
_NwIpRipIfSnooping_Object=MibTableColumn
nwIpRipIfSnooping=_NwIpRipIfSnooping_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,1,1,1,13),_NwIpRipIfSnooping_Type())
nwIpRipIfSnooping.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipIfSnooping.setStatus(_A)
class _NwIpRipIfType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('bma',2),('nbma',3)))
_NwIpRipIfType_Type.__name__=_D
_NwIpRipIfType_Object=MibTableColumn
nwIpRipIfType=_NwIpRipIfType_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,1,1,1,14),_NwIpRipIfType_Type())
nwIpRipIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipIfType.setStatus(_A)
class _NwIpRipIfXmitCost_Type(Integer32):defaultValue=0
_NwIpRipIfXmitCost_Type.__name__=_D
_NwIpRipIfXmitCost_Object=MibTableColumn
nwIpRipIfXmitCost=_NwIpRipIfXmitCost_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,1,1,1,15),_NwIpRipIfXmitCost_Type())
nwIpRipIfXmitCost.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipIfXmitCost.setStatus(_A)
class _NwIpRipIfAclIdentifier_Type(Integer32):defaultValue=0
_NwIpRipIfAclIdentifier_Type.__name__=_D
_NwIpRipIfAclIdentifier_Object=MibTableColumn
nwIpRipIfAclIdentifier=_NwIpRipIfAclIdentifier_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,1,1,1,16),_NwIpRipIfAclIdentifier_Type())
nwIpRipIfAclIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipIfAclIdentifier.setStatus(_A)
class _NwIpRipIfAclStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3)))
_NwIpRipIfAclStatus_Type.__name__=_D
_NwIpRipIfAclStatus_Object=MibTableColumn
nwIpRipIfAclStatus=_NwIpRipIfAclStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,1,1,1,17),_NwIpRipIfAclStatus_Type())
nwIpRipIfAclStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipIfAclStatus.setStatus(_A)
_NwIpRipIfCounters_ObjectIdentity=ObjectIdentity
nwIpRipIfCounters=_NwIpRipIfCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,2))
_NwIpRipIfCtrTable_Object=MibTable
nwIpRipIfCtrTable=_NwIpRipIfCtrTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,2,1))
if mibBuilder.loadTexts:nwIpRipIfCtrTable.setStatus(_A)
_NwIpRipIfCtrEntry_Object=MibTableRow
nwIpRipIfCtrEntry=_NwIpRipIfCtrEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,2,1,1))
nwIpRipIfCtrEntry.setIndexNames((0,_G,_m))
if mibBuilder.loadTexts:nwIpRipIfCtrEntry.setStatus(_A)
_NwIpRipIfCtrIfIndex_Type=Integer32
_NwIpRipIfCtrIfIndex_Object=MibTableColumn
nwIpRipIfCtrIfIndex=_NwIpRipIfCtrIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,2,1,1,1),_NwIpRipIfCtrIfIndex_Type())
nwIpRipIfCtrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipIfCtrIfIndex.setStatus(_A)
class _NwIpRipIfCtrAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3)))
_NwIpRipIfCtrAdminStatus_Type.__name__=_D
_NwIpRipIfCtrAdminStatus_Object=MibTableColumn
nwIpRipIfCtrAdminStatus=_NwIpRipIfCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,2,1,1,2),_NwIpRipIfCtrAdminStatus_Type())
nwIpRipIfCtrAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipIfCtrAdminStatus.setStatus(_A)
class _NwIpRipIfCtrReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpRipIfCtrReset_Type.__name__=_D
_NwIpRipIfCtrReset_Object=MibTableColumn
nwIpRipIfCtrReset=_NwIpRipIfCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,2,1,1,3),_NwIpRipIfCtrReset_Type())
nwIpRipIfCtrReset.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipIfCtrReset.setStatus(_A)
_NwIpRipIfCtrOperationalTime_Type=TimeTicks
_NwIpRipIfCtrOperationalTime_Object=MibTableColumn
nwIpRipIfCtrOperationalTime=_NwIpRipIfCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,2,1,1,4),_NwIpRipIfCtrOperationalTime_Type())
nwIpRipIfCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipIfCtrOperationalTime.setStatus(_A)
_NwIpRipIfCtrInPkts_Type=Counter32
_NwIpRipIfCtrInPkts_Object=MibTableColumn
nwIpRipIfCtrInPkts=_NwIpRipIfCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,2,1,1,5),_NwIpRipIfCtrInPkts_Type())
nwIpRipIfCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipIfCtrInPkts.setStatus(_A)
_NwIpRipIfCtrOutPkts_Type=Counter32
_NwIpRipIfCtrOutPkts_Object=MibTableColumn
nwIpRipIfCtrOutPkts=_NwIpRipIfCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,2,1,1,6),_NwIpRipIfCtrOutPkts_Type())
nwIpRipIfCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipIfCtrOutPkts.setStatus(_A)
_NwIpRipIfCtrFilteredPkts_Type=Counter32
_NwIpRipIfCtrFilteredPkts_Object=MibTableColumn
nwIpRipIfCtrFilteredPkts=_NwIpRipIfCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,2,1,1,7),_NwIpRipIfCtrFilteredPkts_Type())
nwIpRipIfCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipIfCtrFilteredPkts.setStatus(_A)
_NwIpRipIfCtrDiscardPkts_Type=Counter32
_NwIpRipIfCtrDiscardPkts_Object=MibTableColumn
nwIpRipIfCtrDiscardPkts=_NwIpRipIfCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,2,1,1,8),_NwIpRipIfCtrDiscardPkts_Type())
nwIpRipIfCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipIfCtrDiscardPkts.setStatus(_A)
_NwIpRipIfCtrInBytes_Type=Counter32
_NwIpRipIfCtrInBytes_Object=MibTableColumn
nwIpRipIfCtrInBytes=_NwIpRipIfCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,2,1,1,9),_NwIpRipIfCtrInBytes_Type())
nwIpRipIfCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipIfCtrInBytes.setStatus(_A)
_NwIpRipIfCtrOutBytes_Type=Counter32
_NwIpRipIfCtrOutBytes_Object=MibTableColumn
nwIpRipIfCtrOutBytes=_NwIpRipIfCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,2,1,1,10),_NwIpRipIfCtrOutBytes_Type())
nwIpRipIfCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipIfCtrOutBytes.setStatus(_A)
_NwIpRipIfCtrFilteredBytes_Type=Counter32
_NwIpRipIfCtrFilteredBytes_Object=MibTableColumn
nwIpRipIfCtrFilteredBytes=_NwIpRipIfCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,2,1,1,11),_NwIpRipIfCtrFilteredBytes_Type())
nwIpRipIfCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipIfCtrFilteredBytes.setStatus(_A)
_NwIpRipIfCtrDiscardBytes_Type=Counter32
_NwIpRipIfCtrDiscardBytes_Object=MibTableColumn
nwIpRipIfCtrDiscardBytes=_NwIpRipIfCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,2,2,1,1,12),_NwIpRipIfCtrDiscardBytes_Type())
nwIpRipIfCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipIfCtrDiscardBytes.setStatus(_A)
_NwIpRipDatabase_ObjectIdentity=ObjectIdentity
nwIpRipDatabase=_NwIpRipDatabase_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,3))
_NwIpRipRouteTable_Object=MibTable
nwIpRipRouteTable=_NwIpRipRouteTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,3,1))
if mibBuilder.loadTexts:nwIpRipRouteTable.setStatus(_A)
_NwIpRipRouteEntry_Object=MibTableRow
nwIpRipRouteEntry=_NwIpRipRouteEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,3,1,1))
nwIpRipRouteEntry.setIndexNames((0,_G,_n),(0,_G,_o),(0,_G,_p))
if mibBuilder.loadTexts:nwIpRipRouteEntry.setStatus(_A)
_NwIpRipRtNetId_Type=IpAddress
_NwIpRipRtNetId_Object=MibTableColumn
nwIpRipRtNetId=_NwIpRipRtNetId_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,3,1,1,1),_NwIpRipRtNetId_Type())
nwIpRipRtNetId.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipRtNetId.setStatus(_A)
_NwIpRipRtIfIndex_Type=Integer32
_NwIpRipRtIfIndex_Object=MibTableColumn
nwIpRipRtIfIndex=_NwIpRipRtIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,3,1,1,2),_NwIpRipRtIfIndex_Type())
nwIpRipRtIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipRtIfIndex.setStatus(_A)
_NwIpRipRtSrcNode_Type=IpAddress
_NwIpRipRtSrcNode_Object=MibTableColumn
nwIpRipRtSrcNode=_NwIpRipRtSrcNode_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,3,1,1,3),_NwIpRipRtSrcNode_Type())
nwIpRipRtSrcNode.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipRtSrcNode.setStatus(_A)
_NwIpRipRtMask_Type=IpAddress
_NwIpRipRtMask_Object=MibTableColumn
nwIpRipRtMask=_NwIpRipRtMask_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,3,1,1,4),_NwIpRipRtMask_Type())
nwIpRipRtMask.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipRtMask.setStatus(_A)
_NwIpRipRtHops_Type=Integer32
_NwIpRipRtHops_Object=MibTableColumn
nwIpRipRtHops=_NwIpRipRtHops_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,3,1,1,5),_NwIpRipRtHops_Type())
nwIpRipRtHops.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipRtHops.setStatus(_A)
_NwIpRipRtAge_Type=TimeTicks
_NwIpRipRtAge_Object=MibTableColumn
nwIpRipRtAge=_NwIpRipRtAge_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,3,1,1,6),_NwIpRipRtAge_Type())
nwIpRipRtAge.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipRtAge.setStatus(_A)
class _NwIpRipRtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_R,2),('direct',3),('remote',4),(_q,5),('ospf',6)))
_NwIpRipRtType_Type.__name__=_D
_NwIpRipRtType_Object=MibTableColumn
nwIpRipRtType=_NwIpRipRtType_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,3,1,1,7),_NwIpRipRtType_Type())
nwIpRipRtType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipRtType.setStatus(_A)
_NwIpRipRtFlags_Type=Integer32
_NwIpRipRtFlags_Object=MibTableColumn
nwIpRipRtFlags=_NwIpRipRtFlags_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,3,1,1,8),_NwIpRipRtFlags_Type())
nwIpRipRtFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRipRtFlags.setStatus(_A)
_NwIpRipFilters_ObjectIdentity=ObjectIdentity
nwIpRipFilters=_NwIpRipFilters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,1,1,4))
_NwIpLinkState_ObjectIdentity=ObjectIdentity
nwIpLinkState=_NwIpLinkState_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2))
_NwIpOspf_ObjectIdentity=ObjectIdentity
nwIpOspf=_NwIpOspf_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1))
_NwIpOspfSystem_ObjectIdentity=ObjectIdentity
nwIpOspfSystem=_NwIpOspfSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,1))
_NwIpOspfConfig_ObjectIdentity=ObjectIdentity
nwIpOspfConfig=_NwIpOspfConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,1,1))
class _NwIpOspfAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3)))
_NwIpOspfAdminStatus_Type.__name__=_D
_NwIpOspfAdminStatus_Object=MibScalar
nwIpOspfAdminStatus=_NwIpOspfAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,1,1,1),_NwIpOspfAdminStatus_Type())
nwIpOspfAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpOspfAdminStatus.setStatus(_A)
class _NwIpOspfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3),(_J,4),(_K,5)))
_NwIpOspfOperStatus_Type.__name__=_D
_NwIpOspfOperStatus_Object=MibScalar
nwIpOspfOperStatus=_NwIpOspfOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,1,1,2),_NwIpOspfOperStatus_Type())
nwIpOspfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfOperStatus.setStatus(_A)
class _NwIpOspfAdminReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpOspfAdminReset_Type.__name__=_D
_NwIpOspfAdminReset_Object=MibScalar
nwIpOspfAdminReset=_NwIpOspfAdminReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,1,1,3),_NwIpOspfAdminReset_Type())
nwIpOspfAdminReset.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpOspfAdminReset.setStatus(_A)
_NwIpOspfOperationalTime_Type=TimeTicks
_NwIpOspfOperationalTime_Object=MibScalar
nwIpOspfOperationalTime=_NwIpOspfOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,1,1,4),_NwIpOspfOperationalTime_Type())
nwIpOspfOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfOperationalTime.setStatus(_A)
_NwIpOspfVersion_Type=DisplayString
_NwIpOspfVersion_Object=MibScalar
nwIpOspfVersion=_NwIpOspfVersion_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,1,1,5),_NwIpOspfVersion_Type())
nwIpOspfVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfVersion.setStatus(_A)
class _NwIpOspfStackSize_Type(Integer32):defaultValue=50000
_NwIpOspfStackSize_Type.__name__=_D
_NwIpOspfStackSize_Object=MibScalar
nwIpOspfStackSize=_NwIpOspfStackSize_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,1,1,6),_NwIpOspfStackSize_Type())
nwIpOspfStackSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpOspfStackSize.setStatus(_A)
class _NwIpOspfThreadPriority_Type(Integer32):defaultValue=127
_NwIpOspfThreadPriority_Type.__name__=_D
_NwIpOspfThreadPriority_Object=MibScalar
nwIpOspfThreadPriority=_NwIpOspfThreadPriority_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,1,1,7),_NwIpOspfThreadPriority_Type())
nwIpOspfThreadPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpOspfThreadPriority.setStatus(_A)
_NwIpOspfCounters_ObjectIdentity=ObjectIdentity
nwIpOspfCounters=_NwIpOspfCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,1,2))
class _NwIpOspfCtrAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3)))
_NwIpOspfCtrAdminStatus_Type.__name__=_D
_NwIpOspfCtrAdminStatus_Object=MibScalar
nwIpOspfCtrAdminStatus=_NwIpOspfCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,1,2,1),_NwIpOspfCtrAdminStatus_Type())
nwIpOspfCtrAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpOspfCtrAdminStatus.setStatus(_A)
class _NwIpOspfCtrReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpOspfCtrReset_Type.__name__=_D
_NwIpOspfCtrReset_Object=MibScalar
nwIpOspfCtrReset=_NwIpOspfCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,1,2,2),_NwIpOspfCtrReset_Type())
nwIpOspfCtrReset.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpOspfCtrReset.setStatus(_A)
_NwIpOspfCtrOperationalTime_Type=TimeTicks
_NwIpOspfCtrOperationalTime_Object=MibScalar
nwIpOspfCtrOperationalTime=_NwIpOspfCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,1,2,3),_NwIpOspfCtrOperationalTime_Type())
nwIpOspfCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfCtrOperationalTime.setStatus(_A)
_NwIpOspfCtrInPkts_Type=Counter32
_NwIpOspfCtrInPkts_Object=MibScalar
nwIpOspfCtrInPkts=_NwIpOspfCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,1,2,4),_NwIpOspfCtrInPkts_Type())
nwIpOspfCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfCtrInPkts.setStatus(_A)
_NwIpOspfCtrOutPkts_Type=Counter32
_NwIpOspfCtrOutPkts_Object=MibScalar
nwIpOspfCtrOutPkts=_NwIpOspfCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,1,2,5),_NwIpOspfCtrOutPkts_Type())
nwIpOspfCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfCtrOutPkts.setStatus(_A)
_NwIpOspfCtrFilteredPkts_Type=Counter32
_NwIpOspfCtrFilteredPkts_Object=MibScalar
nwIpOspfCtrFilteredPkts=_NwIpOspfCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,1,2,6),_NwIpOspfCtrFilteredPkts_Type())
nwIpOspfCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfCtrFilteredPkts.setStatus(_A)
_NwIpOspfCtrDiscardPkts_Type=Counter32
_NwIpOspfCtrDiscardPkts_Object=MibScalar
nwIpOspfCtrDiscardPkts=_NwIpOspfCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,1,2,7),_NwIpOspfCtrDiscardPkts_Type())
nwIpOspfCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfCtrDiscardPkts.setStatus(_A)
_NwIpOspfCtrInBytes_Type=Counter32
_NwIpOspfCtrInBytes_Object=MibScalar
nwIpOspfCtrInBytes=_NwIpOspfCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,1,2,8),_NwIpOspfCtrInBytes_Type())
nwIpOspfCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfCtrInBytes.setStatus(_A)
_NwIpOspfCtrOutBytes_Type=Counter32
_NwIpOspfCtrOutBytes_Object=MibScalar
nwIpOspfCtrOutBytes=_NwIpOspfCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,1,2,9),_NwIpOspfCtrOutBytes_Type())
nwIpOspfCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfCtrOutBytes.setStatus(_A)
_NwIpOspfCtrFilteredBytes_Type=Counter32
_NwIpOspfCtrFilteredBytes_Object=MibScalar
nwIpOspfCtrFilteredBytes=_NwIpOspfCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,1,2,10),_NwIpOspfCtrFilteredBytes_Type())
nwIpOspfCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfCtrFilteredBytes.setStatus(_A)
_NwIpOspfCtrDiscardBytes_Type=Counter32
_NwIpOspfCtrDiscardBytes_Object=MibScalar
nwIpOspfCtrDiscardBytes=_NwIpOspfCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,1,2,11),_NwIpOspfCtrDiscardBytes_Type())
nwIpOspfCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfCtrDiscardBytes.setStatus(_A)
_NwIpOspfInterfaces_ObjectIdentity=ObjectIdentity
nwIpOspfInterfaces=_NwIpOspfInterfaces_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2))
_NwIpOspfIfConfig_ObjectIdentity=ObjectIdentity
nwIpOspfIfConfig=_NwIpOspfIfConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,1))
_NwIpOspfIfTable_Object=MibTable
nwIpOspfIfTable=_NwIpOspfIfTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,1,1))
if mibBuilder.loadTexts:nwIpOspfIfTable.setStatus(_A)
_NwIpOspfIfEntry_Object=MibTableRow
nwIpOspfIfEntry=_NwIpOspfIfEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,1,1,1))
nwIpOspfIfEntry.setIndexNames((0,_G,_r))
if mibBuilder.loadTexts:nwIpOspfIfEntry.setStatus(_A)
_NwIpOspfIfIndex_Type=Integer32
_NwIpOspfIfIndex_Object=MibTableColumn
nwIpOspfIfIndex=_NwIpOspfIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,1,1,1,1),_NwIpOspfIfIndex_Type())
nwIpOspfIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfIfIndex.setStatus(_A)
class _NwIpOspfIfAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3)))
_NwIpOspfIfAdminStatus_Type.__name__=_D
_NwIpOspfIfAdminStatus_Object=MibTableColumn
nwIpOspfIfAdminStatus=_NwIpOspfIfAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,1,1,1,2),_NwIpOspfIfAdminStatus_Type())
nwIpOspfIfAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpOspfIfAdminStatus.setStatus(_A)
class _NwIpOspfIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3),(_J,4),(_K,5)))
_NwIpOspfIfOperStatus_Type.__name__=_D
_NwIpOspfIfOperStatus_Object=MibTableColumn
nwIpOspfIfOperStatus=_NwIpOspfIfOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,1,1,1,3),_NwIpOspfIfOperStatus_Type())
nwIpOspfIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfIfOperStatus.setStatus(_A)
_NwIpOspfIfOperationalTime_Type=TimeTicks
_NwIpOspfIfOperationalTime_Object=MibTableColumn
nwIpOspfIfOperationalTime=_NwIpOspfIfOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,1,1,1,4),_NwIpOspfIfOperationalTime_Type())
nwIpOspfIfOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfIfOperationalTime.setStatus(_A)
class _NwIpOspfIfVersion_Type(Integer32):defaultValue=1
_NwIpOspfIfVersion_Type.__name__=_D
_NwIpOspfIfVersion_Object=MibTableColumn
nwIpOspfIfVersion=_NwIpOspfIfVersion_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,1,1,1,5),_NwIpOspfIfVersion_Type())
nwIpOspfIfVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpOspfIfVersion.setStatus(_A)
class _NwIpOspfIfSnooping_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3)))
_NwIpOspfIfSnooping_Type.__name__=_D
_NwIpOspfIfSnooping_Object=MibTableColumn
nwIpOspfIfSnooping=_NwIpOspfIfSnooping_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,1,1,1,6),_NwIpOspfIfSnooping_Type())
nwIpOspfIfSnooping.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpOspfIfSnooping.setStatus(_A)
class _NwIpOspfIfType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('bma',2),('nbma',3)))
_NwIpOspfIfType_Type.__name__=_D
_NwIpOspfIfType_Object=MibTableColumn
nwIpOspfIfType=_NwIpOspfIfType_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,1,1,1,7),_NwIpOspfIfType_Type())
nwIpOspfIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfIfType.setStatus(_A)
class _NwIpOspfIfAclIdentifier_Type(Integer32):defaultValue=0
_NwIpOspfIfAclIdentifier_Type.__name__=_D
_NwIpOspfIfAclIdentifier_Object=MibTableColumn
nwIpOspfIfAclIdentifier=_NwIpOspfIfAclIdentifier_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,1,1,1,8),_NwIpOspfIfAclIdentifier_Type())
nwIpOspfIfAclIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpOspfIfAclIdentifier.setStatus(_A)
class _NwIpOspfIfAclStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3)))
_NwIpOspfIfAclStatus_Type.__name__=_D
_NwIpOspfIfAclStatus_Object=MibTableColumn
nwIpOspfIfAclStatus=_NwIpOspfIfAclStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,1,1,1,9),_NwIpOspfIfAclStatus_Type())
nwIpOspfIfAclStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpOspfIfAclStatus.setStatus(_A)
_NwIpOspfIfCounters_ObjectIdentity=ObjectIdentity
nwIpOspfIfCounters=_NwIpOspfIfCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,2))
_NwIpOspfIfCtrTable_Object=MibTable
nwIpOspfIfCtrTable=_NwIpOspfIfCtrTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,2,1))
if mibBuilder.loadTexts:nwIpOspfIfCtrTable.setStatus(_A)
_NwIpOspfIfCtrEntry_Object=MibTableRow
nwIpOspfIfCtrEntry=_NwIpOspfIfCtrEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,2,1,1))
nwIpOspfIfCtrEntry.setIndexNames((0,_G,_s))
if mibBuilder.loadTexts:nwIpOspfIfCtrEntry.setStatus(_A)
_NwIpOspfIfCtrIfIndex_Type=Integer32
_NwIpOspfIfCtrIfIndex_Object=MibTableColumn
nwIpOspfIfCtrIfIndex=_NwIpOspfIfCtrIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,2,1,1,1),_NwIpOspfIfCtrIfIndex_Type())
nwIpOspfIfCtrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfIfCtrIfIndex.setStatus(_A)
class _NwIpOspfIfCtrAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3)))
_NwIpOspfIfCtrAdminStatus_Type.__name__=_D
_NwIpOspfIfCtrAdminStatus_Object=MibTableColumn
nwIpOspfIfCtrAdminStatus=_NwIpOspfIfCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,2,1,1,2),_NwIpOspfIfCtrAdminStatus_Type())
nwIpOspfIfCtrAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpOspfIfCtrAdminStatus.setStatus(_A)
class _NwIpOspfIfCtrReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpOspfIfCtrReset_Type.__name__=_D
_NwIpOspfIfCtrReset_Object=MibTableColumn
nwIpOspfIfCtrReset=_NwIpOspfIfCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,2,1,1,3),_NwIpOspfIfCtrReset_Type())
nwIpOspfIfCtrReset.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpOspfIfCtrReset.setStatus(_A)
_NwIpOspfIfCtrOperationalTime_Type=TimeTicks
_NwIpOspfIfCtrOperationalTime_Object=MibTableColumn
nwIpOspfIfCtrOperationalTime=_NwIpOspfIfCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,2,1,1,4),_NwIpOspfIfCtrOperationalTime_Type())
nwIpOspfIfCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfIfCtrOperationalTime.setStatus(_A)
_NwIpOspfIfCtrInPkts_Type=Counter32
_NwIpOspfIfCtrInPkts_Object=MibTableColumn
nwIpOspfIfCtrInPkts=_NwIpOspfIfCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,2,1,1,5),_NwIpOspfIfCtrInPkts_Type())
nwIpOspfIfCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfIfCtrInPkts.setStatus(_A)
_NwIpOspfIfCtrOutPkts_Type=Counter32
_NwIpOspfIfCtrOutPkts_Object=MibTableColumn
nwIpOspfIfCtrOutPkts=_NwIpOspfIfCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,2,1,1,6),_NwIpOspfIfCtrOutPkts_Type())
nwIpOspfIfCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfIfCtrOutPkts.setStatus(_A)
_NwIpOspfIfCtrFilteredPkts_Type=Counter32
_NwIpOspfIfCtrFilteredPkts_Object=MibTableColumn
nwIpOspfIfCtrFilteredPkts=_NwIpOspfIfCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,2,1,1,7),_NwIpOspfIfCtrFilteredPkts_Type())
nwIpOspfIfCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfIfCtrFilteredPkts.setStatus(_A)
_NwIpOspfIfCtrDiscardPkts_Type=Counter32
_NwIpOspfIfCtrDiscardPkts_Object=MibTableColumn
nwIpOspfIfCtrDiscardPkts=_NwIpOspfIfCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,2,1,1,8),_NwIpOspfIfCtrDiscardPkts_Type())
nwIpOspfIfCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfIfCtrDiscardPkts.setStatus(_A)
_NwIpOspfIfCtrInBytes_Type=Counter32
_NwIpOspfIfCtrInBytes_Object=MibTableColumn
nwIpOspfIfCtrInBytes=_NwIpOspfIfCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,2,1,1,9),_NwIpOspfIfCtrInBytes_Type())
nwIpOspfIfCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfIfCtrInBytes.setStatus(_A)
_NwIpOspfIfCtrOutBytes_Type=Counter32
_NwIpOspfIfCtrOutBytes_Object=MibTableColumn
nwIpOspfIfCtrOutBytes=_NwIpOspfIfCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,2,1,1,10),_NwIpOspfIfCtrOutBytes_Type())
nwIpOspfIfCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfIfCtrOutBytes.setStatus(_A)
_NwIpOspfIfCtrFilteredBytes_Type=Counter32
_NwIpOspfIfCtrFilteredBytes_Object=MibTableColumn
nwIpOspfIfCtrFilteredBytes=_NwIpOspfIfCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,2,1,1,11),_NwIpOspfIfCtrFilteredBytes_Type())
nwIpOspfIfCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfIfCtrFilteredBytes.setStatus(_A)
_NwIpOspfIfCtrDiscardBytes_Type=Counter32
_NwIpOspfIfCtrDiscardBytes_Object=MibTableColumn
nwIpOspfIfCtrDiscardBytes=_NwIpOspfIfCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,2,2,1,1,12),_NwIpOspfIfCtrDiscardBytes_Type())
nwIpOspfIfCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfIfCtrDiscardBytes.setStatus(_A)
_NwIpOspfDatabase_ObjectIdentity=ObjectIdentity
nwIpOspfDatabase=_NwIpOspfDatabase_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,3))
_NwIpOspfFilters_ObjectIdentity=ObjectIdentity
nwIpOspfFilters=_NwIpOspfFilters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,4,2,1,4))
_NwIpFib_ObjectIdentity=ObjectIdentity
nwIpFib=_NwIpFib_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,5))
_NwIpFibSystem_ObjectIdentity=ObjectIdentity
nwIpFibSystem=_NwIpFibSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,5,1))
class _NwIpRipRoutePriority_Type(Integer32):defaultValue=16
_NwIpRipRoutePriority_Type.__name__=_D
_NwIpRipRoutePriority_Object=MibScalar
nwIpRipRoutePriority=_NwIpRipRoutePriority_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,5,1,1),_NwIpRipRoutePriority_Type())
nwIpRipRoutePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRipRoutePriority.setStatus(_A)
class _NwIpOSPFRoutePriority_Type(Integer32):defaultValue=32
_NwIpOSPFRoutePriority_Type.__name__=_D
_NwIpOSPFRoutePriority_Object=MibScalar
nwIpOSPFRoutePriority=_NwIpOSPFRoutePriority_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,5,1,2),_NwIpOSPFRoutePriority_Type())
nwIpOSPFRoutePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpOSPFRoutePriority.setStatus(_A)
class _NwIpStaticRoutePriority_Type(Integer32):defaultValue=48
_NwIpStaticRoutePriority_Type.__name__=_D
_NwIpStaticRoutePriority_Object=MibScalar
nwIpStaticRoutePriority=_NwIpStaticRoutePriority_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,5,1,3),_NwIpStaticRoutePriority_Type())
nwIpStaticRoutePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpStaticRoutePriority.setStatus(_A)
_NwIpOspfFib_ObjectIdentity=ObjectIdentity
nwIpOspfFib=_NwIpOspfFib_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,5,2))
_NwIpOspfFibControl_ObjectIdentity=ObjectIdentity
nwIpOspfFibControl=_NwIpOspfFibControl_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,5,2,1))
_NwIpOspfForward_Type=Integer32
_NwIpOspfForward_Object=MibScalar
nwIpOspfForward=_NwIpOspfForward_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,5,2,1,1),_NwIpOspfForward_Type())
nwIpOspfForward.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfForward.setStatus(_A)
class _NwIpOspfLeakAllStaticRoutes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_F,2)))
_NwIpOspfLeakAllStaticRoutes_Type.__name__=_D
_NwIpOspfLeakAllStaticRoutes_Object=MibScalar
nwIpOspfLeakAllStaticRoutes=_NwIpOspfLeakAllStaticRoutes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,5,2,1,2),_NwIpOspfLeakAllStaticRoutes_Type())
nwIpOspfLeakAllStaticRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpOspfLeakAllStaticRoutes.setStatus(_A)
_NwIpOspfLeakAllRipRoutes_Type=Integer32
_NwIpOspfLeakAllRipRoutes_Object=MibScalar
nwIpOspfLeakAllRipRoutes=_NwIpOspfLeakAllRipRoutes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,5,2,1,3),_NwIpOspfLeakAllRipRoutes_Type())
nwIpOspfLeakAllRipRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpOspfLeakAllRipRoutes.setStatus(_A)
_NwIpOspfLeakAllBgp4Routes_Type=Integer32
_NwIpOspfLeakAllBgp4Routes_Object=MibScalar
nwIpOspfLeakAllBgp4Routes=_NwIpOspfLeakAllBgp4Routes_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,5,2,1,4),_NwIpOspfLeakAllBgp4Routes_Type())
nwIpOspfLeakAllBgp4Routes.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpOspfLeakAllBgp4Routes.setStatus(_A)
_NwIpOspfFibEntries_ObjectIdentity=ObjectIdentity
nwIpOspfFibEntries=_NwIpOspfFibEntries_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,5,2,2))
_NwIpOspfStaticTable_Object=MibTable
nwIpOspfStaticTable=_NwIpOspfStaticTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,5,2,2,1))
if mibBuilder.loadTexts:nwIpOspfStaticTable.setStatus(_A)
_NwIpOspfStaticEntry_Object=MibTableRow
nwIpOspfStaticEntry=_NwIpOspfStaticEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,5,2,2,1,1))
nwIpOspfStaticEntry.setIndexNames((0,_G,_t),(0,_G,_u),(0,_G,_v))
if mibBuilder.loadTexts:nwIpOspfStaticEntry.setStatus(_A)
_NwIpOspfStaticDest_Type=IpAddress
_NwIpOspfStaticDest_Object=MibTableColumn
nwIpOspfStaticDest=_NwIpOspfStaticDest_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,5,2,2,1,1,1),_NwIpOspfStaticDest_Type())
nwIpOspfStaticDest.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfStaticDest.setStatus(_A)
_NwIpOspfStaticForwardMask_Type=IpAddress
_NwIpOspfStaticForwardMask_Object=MibTableColumn
nwIpOspfStaticForwardMask=_NwIpOspfStaticForwardMask_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,5,2,2,1,1,2),_NwIpOspfStaticForwardMask_Type())
nwIpOspfStaticForwardMask.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfStaticForwardMask.setStatus(_A)
_NwIpOspfStaticNextHop_Type=IpAddress
_NwIpOspfStaticNextHop_Object=MibTableColumn
nwIpOspfStaticNextHop=_NwIpOspfStaticNextHop_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,5,2,2,1,1,3),_NwIpOspfStaticNextHop_Type())
nwIpOspfStaticNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpOspfStaticNextHop.setStatus(_A)
_NwIpOspfStaticMetric_Type=Integer32
_NwIpOspfStaticMetric_Object=MibTableColumn
nwIpOspfStaticMetric=_NwIpOspfStaticMetric_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,5,2,2,1,1,4),_NwIpOspfStaticMetric_Type())
nwIpOspfStaticMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpOspfStaticMetric.setStatus(_A)
_NwIpOspfStaticMetricType_Type=Integer32
_NwIpOspfStaticMetricType_Object=MibTableColumn
nwIpOspfStaticMetricType=_NwIpOspfStaticMetricType_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,5,2,2,1,1,5),_NwIpOspfStaticMetricType_Type())
nwIpOspfStaticMetricType.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpOspfStaticMetricType.setStatus(_A)
class _NwIpOspfStaticStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_w,1),(_O,2),(_L,3)))
_NwIpOspfStaticStatus_Type.__name__=_D
_NwIpOspfStaticStatus_Object=MibTableColumn
nwIpOspfStaticStatus=_NwIpOspfStaticStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,5,2,2,1,1,6),_NwIpOspfStaticStatus_Type())
nwIpOspfStaticStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpOspfStaticStatus.setStatus(_A)
_NwIpOspfDynamicTable_ObjectIdentity=ObjectIdentity
nwIpOspfDynamicTable=_NwIpOspfDynamicTable_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,5,2,2,2))
_NwIpOspfRipTable_ObjectIdentity=ObjectIdentity
nwIpOspfRipTable=_NwIpOspfRipTable_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,5,2,2,3))
_NwIpOspfBgp4Table_ObjectIdentity=ObjectIdentity
nwIpOspfBgp4Table=_NwIpOspfBgp4Table_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,5,2,2,4))
_NwIpEndSystems_ObjectIdentity=ObjectIdentity
nwIpEndSystems=_NwIpEndSystems_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6))
_NwIpHostsSystem_ObjectIdentity=ObjectIdentity
nwIpHostsSystem=_NwIpHostsSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,1))
_NwIpHostsTimeToLive_Type=Integer32
_NwIpHostsTimeToLive_Object=MibScalar
nwIpHostsTimeToLive=_NwIpHostsTimeToLive_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,1,1),_NwIpHostsTimeToLive_Type())
nwIpHostsTimeToLive.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpHostsTimeToLive.setStatus(_A)
_NwIpHostsRetryCount_Type=Counter32
_NwIpHostsRetryCount_Object=MibScalar
nwIpHostsRetryCount=_NwIpHostsRetryCount_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,1,2),_NwIpHostsRetryCount_Type())
nwIpHostsRetryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpHostsRetryCount.setStatus(_A)
_NwIpHostsInterfaces_ObjectIdentity=ObjectIdentity
nwIpHostsInterfaces=_NwIpHostsInterfaces_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,2))
_NwIpHostCtlTable_Object=MibTable
nwIpHostCtlTable=_NwIpHostCtlTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,2,1))
if mibBuilder.loadTexts:nwIpHostCtlTable.setStatus(_A)
_NwIpHostCtlEntry_Object=MibTableRow
nwIpHostCtlEntry=_NwIpHostCtlEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,2,1,1))
nwIpHostCtlEntry.setIndexNames((0,_G,_x))
if mibBuilder.loadTexts:nwIpHostCtlEntry.setStatus(_A)
_NwIpHostCtlIfIndex_Type=Integer32
_NwIpHostCtlIfIndex_Object=MibTableColumn
nwIpHostCtlIfIndex=_NwIpHostCtlIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,2,1,1,1),_NwIpHostCtlIfIndex_Type())
nwIpHostCtlIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpHostCtlIfIndex.setStatus(_A)
class _NwIpHostCtlAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_M,2),(_N,3)))
_NwIpHostCtlAdminStatus_Type.__name__=_D
_NwIpHostCtlAdminStatus_Object=MibTableColumn
nwIpHostCtlAdminStatus=_NwIpHostCtlAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,2,1,1,2),_NwIpHostCtlAdminStatus_Type())
nwIpHostCtlAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpHostCtlAdminStatus.setStatus(_A)
class _NwIpHostCtlOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3),(_J,4),(_K,5)))
_NwIpHostCtlOperStatus_Type.__name__=_D
_NwIpHostCtlOperStatus_Object=MibTableColumn
nwIpHostCtlOperStatus=_NwIpHostCtlOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,2,1,1,3),_NwIpHostCtlOperStatus_Type())
nwIpHostCtlOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpHostCtlOperStatus.setStatus(_A)
_NwIpHostCtlOperationalTime_Type=TimeTicks
_NwIpHostCtlOperationalTime_Object=MibTableColumn
nwIpHostCtlOperationalTime=_NwIpHostCtlOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,2,1,1,4),_NwIpHostCtlOperationalTime_Type())
nwIpHostCtlOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpHostCtlOperationalTime.setStatus(_A)
class _NwIpHostCtlProtocol_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_M,2),(_N,3)))
_NwIpHostCtlProtocol_Type.__name__=_D
_NwIpHostCtlProtocol_Object=MibTableColumn
nwIpHostCtlProtocol=_NwIpHostCtlProtocol_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,2,1,1,5),_NwIpHostCtlProtocol_Type())
nwIpHostCtlProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpHostCtlProtocol.setStatus(_A)
class _NwIpHostCtlSnooping_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_M,2),(_N,3)))
_NwIpHostCtlSnooping_Type.__name__=_D
_NwIpHostCtlSnooping_Object=MibTableColumn
nwIpHostCtlSnooping=_NwIpHostCtlSnooping_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,2,1,1,6),_NwIpHostCtlSnooping_Type())
nwIpHostCtlSnooping.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpHostCtlSnooping.setStatus(_A)
class _NwIpHostCtlProxy_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_M,2),(_N,3)))
_NwIpHostCtlProxy_Type.__name__=_D
_NwIpHostCtlProxy_Object=MibTableColumn
nwIpHostCtlProxy=_NwIpHostCtlProxy_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,2,1,1,7),_NwIpHostCtlProxy_Type())
nwIpHostCtlProxy.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpHostCtlProxy.setStatus(_A)
class _NwIpHostCtlCacheMax_Type(Integer32):defaultValue=1024
_NwIpHostCtlCacheMax_Type.__name__=_D
_NwIpHostCtlCacheMax_Object=MibTableColumn
nwIpHostCtlCacheMax=_NwIpHostCtlCacheMax_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,2,1,1,8),_NwIpHostCtlCacheMax_Type())
nwIpHostCtlCacheMax.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpHostCtlCacheMax.setStatus(_A)
_NwIpHostCtlCacheSize_Type=Integer32
_NwIpHostCtlCacheSize_Object=MibTableColumn
nwIpHostCtlCacheSize=_NwIpHostCtlCacheSize_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,2,1,1,9),_NwIpHostCtlCacheSize_Type())
nwIpHostCtlCacheSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpHostCtlCacheSize.setStatus(_A)
_NwIpHostCtlNumStatics_Type=Counter32
_NwIpHostCtlNumStatics_Object=MibTableColumn
nwIpHostCtlNumStatics=_NwIpHostCtlNumStatics_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,2,1,1,10),_NwIpHostCtlNumStatics_Type())
nwIpHostCtlNumStatics.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpHostCtlNumStatics.setStatus(_A)
_NwIpHostCtlNumDynamics_Type=Counter32
_NwIpHostCtlNumDynamics_Object=MibTableColumn
nwIpHostCtlNumDynamics=_NwIpHostCtlNumDynamics_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,2,1,1,11),_NwIpHostCtlNumDynamics_Type())
nwIpHostCtlNumDynamics.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpHostCtlNumDynamics.setStatus(_A)
_NwIpHostCtlCacheHits_Type=Counter32
_NwIpHostCtlCacheHits_Object=MibTableColumn
nwIpHostCtlCacheHits=_NwIpHostCtlCacheHits_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,2,1,1,12),_NwIpHostCtlCacheHits_Type())
nwIpHostCtlCacheHits.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpHostCtlCacheHits.setStatus(_A)
_NwIpHostCtlCacheMisses_Type=Counter32
_NwIpHostCtlCacheMisses_Object=MibTableColumn
nwIpHostCtlCacheMisses=_NwIpHostCtlCacheMisses_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,2,1,1,13),_NwIpHostCtlCacheMisses_Type())
nwIpHostCtlCacheMisses.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpHostCtlCacheMisses.setStatus(_A)
_NwIpHostsToMedia_ObjectIdentity=ObjectIdentity
nwIpHostsToMedia=_NwIpHostsToMedia_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,3))
_NwIpHostMapTable_Object=MibTable
nwIpHostMapTable=_NwIpHostMapTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,3,1))
if mibBuilder.loadTexts:nwIpHostMapTable.setStatus(_A)
_NwIpHostMapEntry_Object=MibTableRow
nwIpHostMapEntry=_NwIpHostMapEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,3,1,1))
nwIpHostMapEntry.setIndexNames((0,_G,_y),(0,_G,_z))
if mibBuilder.loadTexts:nwIpHostMapEntry.setStatus(_A)
_NwIpHostMapIfIndex_Type=Integer32
_NwIpHostMapIfIndex_Object=MibTableColumn
nwIpHostMapIfIndex=_NwIpHostMapIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,3,1,1,1),_NwIpHostMapIfIndex_Type())
nwIpHostMapIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpHostMapIfIndex.setStatus(_A)
_NwIpHostMapIpAddr_Type=IpAddress
_NwIpHostMapIpAddr_Object=MibTableColumn
nwIpHostMapIpAddr=_NwIpHostMapIpAddr_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,3,1,1,2),_NwIpHostMapIpAddr_Type())
nwIpHostMapIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpHostMapIpAddr.setStatus(_A)
_NwIpHostMapPhysAddr_Type=PhysAddress
_NwIpHostMapPhysAddr_Object=MibTableColumn
nwIpHostMapPhysAddr=_NwIpHostMapPhysAddr_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,3,1,1,3),_NwIpHostMapPhysAddr_Type())
nwIpHostMapPhysAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpHostMapPhysAddr.setStatus(_A)
class _NwIpHostMapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_R,2),('dynamic',3),(_q,4),(_w,5)))
_NwIpHostMapType_Type.__name__=_D
_NwIpHostMapType_Object=MibTableColumn
nwIpHostMapType=_NwIpHostMapType_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,3,1,1,4),_NwIpHostMapType_Type())
nwIpHostMapType.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpHostMapType.setStatus(_A)
_NwIpHostMapCircuitID_Type=Integer32
_NwIpHostMapCircuitID_Object=MibTableColumn
nwIpHostMapCircuitID=_NwIpHostMapCircuitID_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,3,1,1,5),_NwIpHostMapCircuitID_Type())
nwIpHostMapCircuitID.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpHostMapCircuitID.setStatus(_A)
class _NwIpHostMapFraming_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5,7,8,9,11,14,16,17)));namedValues=NamedValues(*((_E,1),(_a,2),('snap',3),('slip',5),(_b,7),(_c,8),(_d,9),(_e,11),(_f,14),(_g,16),(_h,17)))
_NwIpHostMapFraming_Type.__name__=_D
_NwIpHostMapFraming_Object=MibTableColumn
nwIpHostMapFraming=_NwIpHostMapFraming_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,3,1,1,6),_NwIpHostMapFraming_Type())
nwIpHostMapFraming.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpHostMapFraming.setStatus(_A)
_NwIpHostMapPortNumber_Type=Integer32
_NwIpHostMapPortNumber_Object=MibTableColumn
nwIpHostMapPortNumber=_NwIpHostMapPortNumber_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,6,3,1,1,7),_NwIpHostMapPortNumber_Type())
nwIpHostMapPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpHostMapPortNumber.setStatus(_A)
_NwIpAccessControl_ObjectIdentity=ObjectIdentity
nwIpAccessControl=_NwIpAccessControl_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,7))
_NwIpAclValidEntries_Type=Gauge32
_NwIpAclValidEntries_Object=MibScalar
nwIpAclValidEntries=_NwIpAclValidEntries_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,7,1),_NwIpAclValidEntries_Type())
nwIpAclValidEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpAclValidEntries.setStatus(_A)
_NwIpAclTable_Object=MibTable
nwIpAclTable=_NwIpAclTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,7,2))
if mibBuilder.loadTexts:nwIpAclTable.setStatus(_A)
_NwIpAclEntry_Object=MibTableRow
nwIpAclEntry=_NwIpAclEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,7,2,1))
nwIpAclEntry.setIndexNames((0,_G,_A0),(0,_G,_A1))
if mibBuilder.loadTexts:nwIpAclEntry.setStatus(_A)
_NwIpAclIdentifier_Type=Integer32
_NwIpAclIdentifier_Object=MibTableColumn
nwIpAclIdentifier=_NwIpAclIdentifier_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,7,2,1,1),_NwIpAclIdentifier_Type())
nwIpAclIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpAclIdentifier.setStatus(_A)
_NwIpAclSequence_Type=Integer32
_NwIpAclSequence_Object=MibTableColumn
nwIpAclSequence=_NwIpAclSequence_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,7,2,1,2),_NwIpAclSequence_Type())
nwIpAclSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpAclSequence.setStatus(_A)
class _NwIpAclPermission_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_R,2),('permit',3),('deny',4),('permit-bidirectional',5),('deny-bidirectional',6)))
_NwIpAclPermission_Type.__name__=_D
_NwIpAclPermission_Object=MibTableColumn
nwIpAclPermission=_NwIpAclPermission_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,7,2,1,3),_NwIpAclPermission_Type())
nwIpAclPermission.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpAclPermission.setStatus(_A)
_NwIpAclMatches_Type=Counter32
_NwIpAclMatches_Object=MibTableColumn
nwIpAclMatches=_NwIpAclMatches_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,7,2,1,4),_NwIpAclMatches_Type())
nwIpAclMatches.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpAclMatches.setStatus(_A)
_NwIpAclDestAddress_Type=IpAddress
_NwIpAclDestAddress_Object=MibTableColumn
nwIpAclDestAddress=_NwIpAclDestAddress_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,7,2,1,5),_NwIpAclDestAddress_Type())
nwIpAclDestAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpAclDestAddress.setStatus(_A)
_NwIpAclDestMask_Type=IpAddress
_NwIpAclDestMask_Object=MibTableColumn
nwIpAclDestMask=_NwIpAclDestMask_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,7,2,1,6),_NwIpAclDestMask_Type())
nwIpAclDestMask.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpAclDestMask.setStatus(_A)
_NwIpAclSrcAddress_Type=IpAddress
_NwIpAclSrcAddress_Object=MibTableColumn
nwIpAclSrcAddress=_NwIpAclSrcAddress_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,7,2,1,7),_NwIpAclSrcAddress_Type())
nwIpAclSrcAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpAclSrcAddress.setStatus(_A)
_NwIpAclSrcMask_Type=IpAddress
_NwIpAclSrcMask_Object=MibTableColumn
nwIpAclSrcMask=_NwIpAclSrcMask_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,7,2,1,8),_NwIpAclSrcMask_Type())
nwIpAclSrcMask.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpAclSrcMask.setStatus(_A)
class _NwIpAclProtocol_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('all',2),('icmp',3),('udp',4),('tcp',5)))
_NwIpAclProtocol_Type.__name__=_D
_NwIpAclProtocol_Object=MibTableColumn
nwIpAclProtocol=_NwIpAclProtocol_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,7,2,1,9),_NwIpAclProtocol_Type())
nwIpAclProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpAclProtocol.setStatus(_A)
_NwIpAclPortNumber_Type=Integer32
_NwIpAclPortNumber_Object=MibTableColumn
nwIpAclPortNumber=_NwIpAclPortNumber_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,7,2,1,10),_NwIpAclPortNumber_Type())
nwIpAclPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpAclPortNumber.setStatus(_A)
_NwIpFilters_ObjectIdentity=ObjectIdentity
nwIpFilters=_NwIpFilters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,8))
_NwIpRedirector_ObjectIdentity=ObjectIdentity
nwIpRedirector=_NwIpRedirector_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,9))
_NwIpRedirectorSystem_ObjectIdentity=ObjectIdentity
nwIpRedirectorSystem=_NwIpRedirectorSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,9,1))
_NwIpRedirectTable_Object=MibTable
nwIpRedirectTable=_NwIpRedirectTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,9,1,1))
if mibBuilder.loadTexts:nwIpRedirectTable.setStatus(_A)
_NwIpRedirectEntry_Object=MibTableRow
nwIpRedirectEntry=_NwIpRedirectEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,9,1,1,1))
nwIpRedirectEntry.setIndexNames((0,_G,_A2))
if mibBuilder.loadTexts:nwIpRedirectEntry.setStatus(_A)
_NwIpRedirectPort_Type=Integer32
_NwIpRedirectPort_Object=MibTableColumn
nwIpRedirectPort=_NwIpRedirectPort_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,9,1,1,1,1),_NwIpRedirectPort_Type())
nwIpRedirectPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRedirectPort.setStatus(_A)
_NwIpRedirectAddress_Type=IpAddress
_NwIpRedirectAddress_Object=MibTableColumn
nwIpRedirectAddress=_NwIpRedirectAddress_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,9,1,1,1,2),_NwIpRedirectAddress_Type())
nwIpRedirectAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRedirectAddress.setStatus(_A)
class _NwIpRedirectType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forward',1),(_L,2)))
_NwIpRedirectType_Type.__name__=_D
_NwIpRedirectType_Object=MibTableColumn
nwIpRedirectType=_NwIpRedirectType_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,9,1,1,1,3),_NwIpRedirectType_Type())
nwIpRedirectType.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpRedirectType.setStatus(_A)
_NwIpRedirectCount_Type=Counter32
_NwIpRedirectCount_Object=MibTableColumn
nwIpRedirectCount=_NwIpRedirectCount_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,9,1,1,1,4),_NwIpRedirectCount_Type())
nwIpRedirectCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpRedirectCount.setStatus(_A)
_NwIpRedirectorInterface_ObjectIdentity=ObjectIdentity
nwIpRedirectorInterface=_NwIpRedirectorInterface_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,9,2))
_NwIpEvent_ObjectIdentity=ObjectIdentity
nwIpEvent=_NwIpEvent_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10))
_NwIpEventLogConfig_ObjectIdentity=ObjectIdentity
nwIpEventLogConfig=_NwIpEventLogConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10,1))
class _NwIpEventAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3)))
_NwIpEventAdminStatus_Type.__name__=_D
_NwIpEventAdminStatus_Object=MibScalar
nwIpEventAdminStatus=_NwIpEventAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10,1,1),_NwIpEventAdminStatus_Type())
nwIpEventAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpEventAdminStatus.setStatus(_A)
class _NwIpEventMaxEntries_Type(Integer32):defaultValue=100
_NwIpEventMaxEntries_Type.__name__=_D
_NwIpEventMaxEntries_Object=MibScalar
nwIpEventMaxEntries=_NwIpEventMaxEntries_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10,1,2),_NwIpEventMaxEntries_Type())
nwIpEventMaxEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpEventMaxEntries.setStatus(_A)
class _NwIpEventTraceAll_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3)))
_NwIpEventTraceAll_Type.__name__=_D
_NwIpEventTraceAll_Object=MibScalar
nwIpEventTraceAll=_NwIpEventTraceAll_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10,1,3),_NwIpEventTraceAll_Type())
nwIpEventTraceAll.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpEventTraceAll.setStatus(_A)
_NwIpEventLogFilterTable_ObjectIdentity=ObjectIdentity
nwIpEventLogFilterTable=_NwIpEventLogFilterTable_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10,2))
_NwIpEventFilterTable_Object=MibTable
nwIpEventFilterTable=_NwIpEventFilterTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10,2,1))
if mibBuilder.loadTexts:nwIpEventFilterTable.setStatus(_A)
_NwIpEventFilterEntry_Object=MibTableRow
nwIpEventFilterEntry=_NwIpEventFilterEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10,2,1,1))
nwIpEventFilterEntry.setIndexNames((0,_G,_A3),(0,_G,_A4))
if mibBuilder.loadTexts:nwIpEventFilterEntry.setStatus(_A)
_NwIpEventFltrProtocol_Type=Integer32
_NwIpEventFltrProtocol_Object=MibTableColumn
nwIpEventFltrProtocol=_NwIpEventFltrProtocol_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10,2,1,1,1),_NwIpEventFltrProtocol_Type())
nwIpEventFltrProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpEventFltrProtocol.setStatus(_A)
_NwIpEventFltrIfNum_Type=Integer32
_NwIpEventFltrIfNum_Object=MibTableColumn
nwIpEventFltrIfNum=_NwIpEventFltrIfNum_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10,2,1,1,2),_NwIpEventFltrIfNum_Type())
nwIpEventFltrIfNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpEventFltrIfNum.setStatus(_A)
class _NwIpEventFltrControl_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_L,2),(_Q,3)))
_NwIpEventFltrControl_Type.__name__=_D
_NwIpEventFltrControl_Object=MibTableColumn
nwIpEventFltrControl=_NwIpEventFltrControl_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10,2,1,1,3),_NwIpEventFltrControl_Type())
nwIpEventFltrControl.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpEventFltrControl.setStatus(_A)
class _NwIpEventFltrType_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16,32,64)));namedValues=NamedValues(*(('misc',1),('timer',2),('rcv',4),('xmit',8),('event',16),('diags',32),('error',64)))
_NwIpEventFltrType_Type.__name__=_D
_NwIpEventFltrType_Object=MibTableColumn
nwIpEventFltrType=_NwIpEventFltrType_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10,2,1,1,4),_NwIpEventFltrType_Type())
nwIpEventFltrType.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpEventFltrType.setStatus(_A)
class _NwIpEventFltrSeverity_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('highest',1),('highmed',2),('highlow',3)))
_NwIpEventFltrSeverity_Type.__name__=_D
_NwIpEventFltrSeverity_Object=MibTableColumn
nwIpEventFltrSeverity=_NwIpEventFltrSeverity_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10,2,1,1,5),_NwIpEventFltrSeverity_Type())
nwIpEventFltrSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpEventFltrSeverity.setStatus(_A)
class _NwIpEventFltrAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('log',1),('trap',2),('log-trap',3)))
_NwIpEventFltrAction_Type.__name__=_D
_NwIpEventFltrAction_Object=MibTableColumn
nwIpEventFltrAction=_NwIpEventFltrAction_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10,2,1,1,6),_NwIpEventFltrAction_Type())
nwIpEventFltrAction.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpEventFltrAction.setStatus(_A)
_NwIpEventLogTable_ObjectIdentity=ObjectIdentity
nwIpEventLogTable=_NwIpEventLogTable_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10,3))
_NwIpEventTable_Object=MibTable
nwIpEventTable=_NwIpEventTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10,3,1))
if mibBuilder.loadTexts:nwIpEventTable.setStatus(_A)
_NwIpEventEntry_Object=MibTableRow
nwIpEventEntry=_NwIpEventEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10,3,1,1))
nwIpEventEntry.setIndexNames((0,_G,_A5))
if mibBuilder.loadTexts:nwIpEventEntry.setStatus(_A)
_NwIpEventNumber_Type=Integer32
_NwIpEventNumber_Object=MibTableColumn
nwIpEventNumber=_NwIpEventNumber_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10,3,1,1,1),_NwIpEventNumber_Type())
nwIpEventNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpEventNumber.setStatus(_A)
_NwIpEventTime_Type=TimeTicks
_NwIpEventTime_Object=MibTableColumn
nwIpEventTime=_NwIpEventTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10,3,1,1,2),_NwIpEventTime_Type())
nwIpEventTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpEventTime.setStatus(_A)
class _NwIpEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16,32,64)));namedValues=NamedValues(*(('misc',1),('timer',2),('rcv',4),('xmit',8),('event',16),('diags',32),('error',64)))
_NwIpEventType_Type.__name__=_D
_NwIpEventType_Object=MibTableColumn
nwIpEventType=_NwIpEventType_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10,3,1,1,3),_NwIpEventType_Type())
nwIpEventType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpEventType.setStatus(_A)
class _NwIpEventSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('highest',1),('highmed',2),('highlow',3)))
_NwIpEventSeverity_Type.__name__=_D
_NwIpEventSeverity_Object=MibTableColumn
nwIpEventSeverity=_NwIpEventSeverity_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10,3,1,1,4),_NwIpEventSeverity_Type())
nwIpEventSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpEventSeverity.setStatus(_A)
_NwIpEventProtocol_Type=Integer32
_NwIpEventProtocol_Object=MibTableColumn
nwIpEventProtocol=_NwIpEventProtocol_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10,3,1,1,5),_NwIpEventProtocol_Type())
nwIpEventProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpEventProtocol.setStatus(_A)
_NwIpEventIfNum_Type=Integer32
_NwIpEventIfNum_Object=MibTableColumn
nwIpEventIfNum=_NwIpEventIfNum_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10,3,1,1,6),_NwIpEventIfNum_Type())
nwIpEventIfNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpEventIfNum.setStatus(_A)
_NwIpEventTextString_Type=OctetString
_NwIpEventTextString_Object=MibTableColumn
nwIpEventTextString=_NwIpEventTextString_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,10,3,1,1,7),_NwIpEventTextString_Type())
nwIpEventTextString.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpEventTextString.setStatus(_A)
_NwIpWorkGroup_ObjectIdentity=ObjectIdentity
nwIpWorkGroup=_NwIpWorkGroup_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11))
_NwIpWgDefTable_Object=MibTable
nwIpWgDefTable=_NwIpWgDefTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,1))
if mibBuilder.loadTexts:nwIpWgDefTable.setStatus(_A)
_NwIpWgDefEntry_Object=MibTableRow
nwIpWgDefEntry=_NwIpWgDefEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,1,1))
nwIpWgDefEntry.setIndexNames((0,_G,_A6))
if mibBuilder.loadTexts:nwIpWgDefEntry.setStatus(_A)
_NwIpWgDefIdentifier_Type=Integer32
_NwIpWgDefIdentifier_Object=MibTableColumn
nwIpWgDefIdentifier=_NwIpWgDefIdentifier_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,1,1,1),_NwIpWgDefIdentifier_Type())
nwIpWgDefIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpWgDefIdentifier.setStatus(_A)
_NwIpWgDefHostAddress_Type=IpAddress
_NwIpWgDefHostAddress_Object=MibTableColumn
nwIpWgDefHostAddress=_NwIpWgDefHostAddress_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,1,1,2),_NwIpWgDefHostAddress_Type())
nwIpWgDefHostAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpWgDefHostAddress.setStatus(_A)
_NwIpWgDefSubnetMask_Type=IpAddress
_NwIpWgDefSubnetMask_Object=MibTableColumn
nwIpWgDefSubnetMask=_NwIpWgDefSubnetMask_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,1,1,3),_NwIpWgDefSubnetMask_Type())
nwIpWgDefSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpWgDefSubnetMask.setStatus(_A)
class _NwIpWgDefSecurity_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('low',2),('medium',3),('high',4)))
_NwIpWgDefSecurity_Type.__name__=_D
_NwIpWgDefSecurity_Object=MibTableColumn
nwIpWgDefSecurity=_NwIpWgDefSecurity_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,1,1,4),_NwIpWgDefSecurity_Type())
nwIpWgDefSecurity.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpWgDefSecurity.setStatus(_A)
class _NwIpWgDefFastPath_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3)))
_NwIpWgDefFastPath_Type.__name__=_D
_NwIpWgDefFastPath_Object=MibTableColumn
nwIpWgDefFastPath=_NwIpWgDefFastPath_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,1,1,5),_NwIpWgDefFastPath_Type())
nwIpWgDefFastPath.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpWgDefFastPath.setStatus(_A)
class _NwIpWgDefRowStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_S,2),(_T,3),(_U,4),(_V,5),(_W,6)))
_NwIpWgDefRowStatus_Type.__name__=_D
_NwIpWgDefRowStatus_Object=MibTableColumn
nwIpWgDefRowStatus=_NwIpWgDefRowStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,1,1,6),_NwIpWgDefRowStatus_Type())
nwIpWgDefRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpWgDefRowStatus.setStatus(_A)
class _NwIpWgDefOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ok',1),(_F,2),('subnetConflict',3),(_X,4)))
_NwIpWgDefOperStatus_Type.__name__=_D
_NwIpWgDefOperStatus_Object=MibTableColumn
nwIpWgDefOperStatus=_NwIpWgDefOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,1,1,7),_NwIpWgDefOperStatus_Type())
nwIpWgDefOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpWgDefOperStatus.setStatus(_A)
_NwIpWgDefNumActiveIntf_Type=Integer32
_NwIpWgDefNumActiveIntf_Object=MibTableColumn
nwIpWgDefNumActiveIntf=_NwIpWgDefNumActiveIntf_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,1,1,8),_NwIpWgDefNumActiveIntf_Type())
nwIpWgDefNumActiveIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpWgDefNumActiveIntf.setStatus(_A)
_NwIpWgDefNumTotalIntf_Type=Integer32
_NwIpWgDefNumTotalIntf_Object=MibTableColumn
nwIpWgDefNumTotalIntf=_NwIpWgDefNumTotalIntf_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,1,1,9),_NwIpWgDefNumTotalIntf_Type())
nwIpWgDefNumTotalIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpWgDefNumTotalIntf.setStatus(_A)
_NwIpWgIfTable_Object=MibTable
nwIpWgIfTable=_NwIpWgIfTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,2))
if mibBuilder.loadTexts:nwIpWgIfTable.setStatus(_A)
_NwIpWgIfEntry_Object=MibTableRow
nwIpWgIfEntry=_NwIpWgIfEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,2,1))
nwIpWgIfEntry.setIndexNames((0,_G,_A7),(0,_G,_A8))
if mibBuilder.loadTexts:nwIpWgIfEntry.setStatus(_A)
_NwIpWgIfDefIdent_Type=Integer32
_NwIpWgIfDefIdent_Object=MibTableColumn
nwIpWgIfDefIdent=_NwIpWgIfDefIdent_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,2,1,1),_NwIpWgIfDefIdent_Type())
nwIpWgIfDefIdent.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpWgIfDefIdent.setStatus(_A)
_NwIpWgIfIfIndex_Type=Integer32
_NwIpWgIfIfIndex_Object=MibTableColumn
nwIpWgIfIfIndex=_NwIpWgIfIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,2,1,2),_NwIpWgIfIfIndex_Type())
nwIpWgIfIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpWgIfIfIndex.setStatus(_A)
_NwIpWgIfNumActiveHosts_Type=Integer32
_NwIpWgIfNumActiveHosts_Object=MibTableColumn
nwIpWgIfNumActiveHosts=_NwIpWgIfNumActiveHosts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,2,1,3),_NwIpWgIfNumActiveHosts_Type())
nwIpWgIfNumActiveHosts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpWgIfNumActiveHosts.setStatus(_A)
_NwIpWgIfNumKnownHosts_Type=Counter32
_NwIpWgIfNumKnownHosts_Object=MibTableColumn
nwIpWgIfNumKnownHosts=_NwIpWgIfNumKnownHosts_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,2,1,4),_NwIpWgIfNumKnownHosts_Type())
nwIpWgIfNumKnownHosts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpWgIfNumKnownHosts.setStatus(_A)
class _NwIpWgIfRowStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_S,2),(_T,3),(_U,4),(_V,5),(_W,6)))
_NwIpWgIfRowStatus_Type.__name__=_D
_NwIpWgIfRowStatus_Object=MibTableColumn
nwIpWgIfRowStatus=_NwIpWgIfRowStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,2,1,5),_NwIpWgIfRowStatus_Type())
nwIpWgIfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpWgIfRowStatus.setStatus(_A)
class _NwIpWgIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('ok',1),(_F,2),(_A9,3),('addressConflict',4),('resetRequired',5),('linkDown',6),('routingDown',7),(_X,8)))
_NwIpWgIfOperStatus_Type.__name__=_D
_NwIpWgIfOperStatus_Object=MibTableColumn
nwIpWgIfOperStatus=_NwIpWgIfOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,2,1,6),_NwIpWgIfOperStatus_Type())
nwIpWgIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpWgIfOperStatus.setStatus(_A)
_NwIpWgRngTable_Object=MibTable
nwIpWgRngTable=_NwIpWgRngTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,3))
if mibBuilder.loadTexts:nwIpWgRngTable.setStatus(_A)
_NwIpWgRngEntry_Object=MibTableRow
nwIpWgRngEntry=_NwIpWgRngEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,3,1))
nwIpWgRngEntry.setIndexNames((0,_G,_AA),(0,_G,_AB),(0,_G,_AC))
if mibBuilder.loadTexts:nwIpWgRngEntry.setStatus(_A)
_NwIpWgRngBegHostAddr_Type=IpAddress
_NwIpWgRngBegHostAddr_Object=MibTableColumn
nwIpWgRngBegHostAddr=_NwIpWgRngBegHostAddr_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,3,1,1),_NwIpWgRngBegHostAddr_Type())
nwIpWgRngBegHostAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpWgRngBegHostAddr.setStatus(_A)
_NwIpWgRngEndHostAddr_Type=IpAddress
_NwIpWgRngEndHostAddr_Object=MibTableColumn
nwIpWgRngEndHostAddr=_NwIpWgRngEndHostAddr_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,3,1,2),_NwIpWgRngEndHostAddr_Type())
nwIpWgRngEndHostAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpWgRngEndHostAddr.setStatus(_A)
_NwIpWgRngIfIndex_Type=Integer32
_NwIpWgRngIfIndex_Object=MibTableColumn
nwIpWgRngIfIndex=_NwIpWgRngIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,3,1,3),_NwIpWgRngIfIndex_Type())
nwIpWgRngIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpWgRngIfIndex.setStatus(_A)
class _NwIpWgRngPhysAddr_Type(OctetString):defaultHexValue='000000000000'
_NwIpWgRngPhysAddr_Type.__name__=_Y
_NwIpWgRngPhysAddr_Object=MibTableColumn
nwIpWgRngPhysAddr=_NwIpWgRngPhysAddr_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,3,1,4),_NwIpWgRngPhysAddr_Type())
nwIpWgRngPhysAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpWgRngPhysAddr.setStatus(_A)
class _NwIpWgRngRowStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),(_S,2),(_T,3),(_U,4),(_V,5),(_W,6)))
_NwIpWgRngRowStatus_Type.__name__=_D
_NwIpWgRngRowStatus_Object=MibTableColumn
nwIpWgRngRowStatus=_NwIpWgRngRowStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,3,1,5),_NwIpWgRngRowStatus_Type())
nwIpWgRngRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwIpWgRngRowStatus.setStatus(_A)
class _NwIpWgRngOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ok',1),(_F,2),(_A9,3),('interfaceInvalid',4),('physAddrRequired',5),(_X,6)))
_NwIpWgRngOperStatus_Type.__name__=_D
_NwIpWgRngOperStatus_Object=MibTableColumn
nwIpWgRngOperStatus=_NwIpWgRngOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,3,1,6),_NwIpWgRngOperStatus_Type())
nwIpWgRngOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpWgRngOperStatus.setStatus(_A)
_NwIpWgHostTable_Object=MibTable
nwIpWgHostTable=_NwIpWgHostTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,4))
if mibBuilder.loadTexts:nwIpWgHostTable.setStatus(_A)
_NwIpWgHostEntry_Object=MibTableRow
nwIpWgHostEntry=_NwIpWgHostEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,4,1))
nwIpWgHostEntry.setIndexNames((0,_G,_AD),(0,_G,_AE))
if mibBuilder.loadTexts:nwIpWgHostEntry.setStatus(_A)
_NwIpWgHostHostAddr_Type=IpAddress
_NwIpWgHostHostAddr_Object=MibTableColumn
nwIpWgHostHostAddr=_NwIpWgHostHostAddr_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,4,1,1),_NwIpWgHostHostAddr_Type())
nwIpWgHostHostAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpWgHostHostAddr.setStatus(_A)
_NwIpWgHostIfIndex_Type=Integer32
_NwIpWgHostIfIndex_Object=MibTableColumn
nwIpWgHostIfIndex=_NwIpWgHostIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,4,1,2),_NwIpWgHostIfIndex_Type())
nwIpWgHostIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpWgHostIfIndex.setStatus(_A)
_NwIpWgHostDefIdent_Type=Integer32
_NwIpWgHostDefIdent_Object=MibTableColumn
nwIpWgHostDefIdent=_NwIpWgHostDefIdent_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,4,1,3),_NwIpWgHostDefIdent_Type())
nwIpWgHostDefIdent.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpWgHostDefIdent.setStatus(_A)
_NwIpWgHostPhysAddr_Type=OctetString
_NwIpWgHostPhysAddr_Object=MibTableColumn
nwIpWgHostPhysAddr=_NwIpWgHostPhysAddr_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,4,1,4),_NwIpWgHostPhysAddr_Type())
nwIpWgHostPhysAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpWgHostPhysAddr.setStatus(_A)
class _NwIpWgHostStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_E,1),('unknown',2),('valid',3),('invalid-multiple',4),('invalid-physaddr',5),('invalid-range',6),('invalid-interface',7),('invalid-workgroup',8),('invalid-expired',9)))
_NwIpWgHostStatus_Type.__name__=_D
_NwIpWgHostStatus_Object=MibTableColumn
nwIpWgHostStatus=_NwIpWgHostStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,1,2,11,4,1,5),_NwIpWgHostStatus_Type())
nwIpWgHostStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpWgHostStatus.setStatus(_A)
_NwIpClientServices_ObjectIdentity=ObjectIdentity
nwIpClientServices=_NwIpClientServices_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,1,2,12))
mibBuilder.exportSymbols(_G,**{'nwIpRouter':nwIpRouter,'nwIpMibs':nwIpMibs,'nwIpMibRevText':nwIpMibRevText,'nwIpComponents':nwIpComponents,'nwIpSystem':nwIpSystem,'nwIpSysConfig':nwIpSysConfig,'nwIpSysRouterId':nwIpSysRouterId,'nwIpSysAdministration':nwIpSysAdministration,'nwIpSysAdminStatus':nwIpSysAdminStatus,'nwIpSysOperStatus':nwIpSysOperStatus,'nwIpSysAdminReset':nwIpSysAdminReset,'nwIpSysOperationalTime':nwIpSysOperationalTime,'nwIpSysVersion':nwIpSysVersion,'nwIpForwarding':nwIpForwarding,'nwIpFwdSystem':nwIpFwdSystem,'nwIpFwdCounters':nwIpFwdCounters,'nwIpFwdCtrAdminStatus':nwIpFwdCtrAdminStatus,'nwIpFwdCtrReset':nwIpFwdCtrReset,'nwIpFwdCtrOperationalTime':nwIpFwdCtrOperationalTime,'nwIpFwdCtrInPkts':nwIpFwdCtrInPkts,'nwIpFwdCtrOutPkts':nwIpFwdCtrOutPkts,'nwIpFwdCtrFwdPkts':nwIpFwdCtrFwdPkts,'nwIpFwdCtrFilteredPkts':nwIpFwdCtrFilteredPkts,'nwIpFwdCtrDiscardPkts':nwIpFwdCtrDiscardPkts,'nwIpFwdCtrAddrErrPkts':nwIpFwdCtrAddrErrPkts,'nwIpFwdCtrLenErrPkts':nwIpFwdCtrLenErrPkts,'nwIpFwdCtrHdrErrPkts':nwIpFwdCtrHdrErrPkts,'nwIpFwdCtrInBytes':nwIpFwdCtrInBytes,'nwIpFwdCtrOutBytes':nwIpFwdCtrOutBytes,'nwIpFwdCtrFwdBytes':nwIpFwdCtrFwdBytes,'nwIpFwdCtrFilteredBytes':nwIpFwdCtrFilteredBytes,'nwIpFwdCtrDiscardBytes':nwIpFwdCtrDiscardBytes,'nwIpFwdCtrHostInPkts':nwIpFwdCtrHostInPkts,'nwIpFwdCtrHostOutPkts':nwIpFwdCtrHostOutPkts,'nwIpFwdCtrHostDiscardPkts':nwIpFwdCtrHostDiscardPkts,'nwIpFwdCtrHostInBytes':nwIpFwdCtrHostInBytes,'nwIpFwdCtrHostOutBytes':nwIpFwdCtrHostOutBytes,'nwIpFwdCtrHostDiscardBytes':nwIpFwdCtrHostDiscardBytes,'nwIpFwdInterfaces':nwIpFwdInterfaces,'nwIpFwdIfConfig':nwIpFwdIfConfig,'nwIpFwdIfTable':nwIpFwdIfTable,'nwIpFwdIfEntry':nwIpFwdIfEntry,_Z:nwIpFwdIfIndex,'nwIpFwdIfAdminStatus':nwIpFwdIfAdminStatus,'nwIpFwdIfOperStatus':nwIpFwdIfOperStatus,'nwIpFwdIfOperationalTime':nwIpFwdIfOperationalTime,'nwIpFwdIfControl':nwIpFwdIfControl,'nwIpFwdIfMtu':nwIpFwdIfMtu,'nwIpFwdIfForwarding':nwIpFwdIfForwarding,'nwIpFwdIfFrameType':nwIpFwdIfFrameType,'nwIpFwdIfAclIdentifier':nwIpFwdIfAclIdentifier,'nwIpFwdIfAclStatus':nwIpFwdIfAclStatus,'nwIpFwdIfCacheControl':nwIpFwdIfCacheControl,'nwIpFwdIfCacheEntries':nwIpFwdIfCacheEntries,'nwIpFwdIfCacheHits':nwIpFwdIfCacheHits,'nwIpFwdIfCacheMisses':nwIpFwdIfCacheMisses,'nwIpAddressTable':nwIpAddressTable,'nwIpAddrEntry':nwIpAddrEntry,_i:nwIpAddrIfIndex,_j:nwIpAddrIfAddress,'nwIpAddrIfControl':nwIpAddrIfControl,'nwIpAddrIfAddrType':nwIpAddrIfAddrType,'nwIpAddrIfMask':nwIpAddrIfMask,'nwIpAddrIfBcastAddr':nwIpAddrIfBcastAddr,'nwIpFwdIfCounters':nwIpFwdIfCounters,'nwIpFwdIfCtrTable':nwIpFwdIfCtrTable,'nwIpFwdIfCtrEntry':nwIpFwdIfCtrEntry,_k:nwIpFwdIfCtrIfIndex,'nwIpFwdIfCtrAdminStatus':nwIpFwdIfCtrAdminStatus,'nwIpFwdIfCtrReset':nwIpFwdIfCtrReset,'nwIpFwdIfCtrOperationalTime':nwIpFwdIfCtrOperationalTime,'nwIpFwdIfCtrInPkts':nwIpFwdIfCtrInPkts,'nwIpFwdIfCtrOutPkts':nwIpFwdIfCtrOutPkts,'nwIpFwdIfCtrFwdPkts':nwIpFwdIfCtrFwdPkts,'nwIpFwdIfCtrFilteredPkts':nwIpFwdIfCtrFilteredPkts,'nwIpFwdIfCtrDiscardPkts':nwIpFwdIfCtrDiscardPkts,'nwIpFwdIfCtrAddrErrPkts':nwIpFwdIfCtrAddrErrPkts,'nwIpFwdIfCtrLenErrPkts':nwIpFwdIfCtrLenErrPkts,'nwIpFwdIfCtrHdrErrPkts':nwIpFwdIfCtrHdrErrPkts,'nwIpFwdIfCtrInBytes':nwIpFwdIfCtrInBytes,'nwIpFwdIfCtrOutBytes':nwIpFwdIfCtrOutBytes,'nwIpFwdIfCtrFwdBytes':nwIpFwdIfCtrFwdBytes,'nwIpFwdIfCtrFilteredBytes':nwIpFwdIfCtrFilteredBytes,'nwIpFwdIfCtrDiscardBytes':nwIpFwdIfCtrDiscardBytes,'nwIpFwdIfCtrHostInPkts':nwIpFwdIfCtrHostInPkts,'nwIpFwdIfCtrHostOutPkts':nwIpFwdIfCtrHostOutPkts,'nwIpFwdIfCtrHostDiscardPkts':nwIpFwdIfCtrHostDiscardPkts,'nwIpFwdIfCtrHostInBytes':nwIpFwdIfCtrHostInBytes,'nwIpFwdIfCtrHostOutBytes':nwIpFwdIfCtrHostOutBytes,'nwIpFwdIfCtrHostDiscardBytes':nwIpFwdIfCtrHostDiscardBytes,'nwIpTopology':nwIpTopology,'nwIpDistanceVector':nwIpDistanceVector,'nwIpRip':nwIpRip,'nwIpRipSystem':nwIpRipSystem,'nwIpRipConfig':nwIpRipConfig,'nwIpRipAdminStatus':nwIpRipAdminStatus,'nwIpRipOperStatus':nwIpRipOperStatus,'nwIpRipAdminReset':nwIpRipAdminReset,'nwIpRipOperationalTime':nwIpRipOperationalTime,'nwIpRipVersion':nwIpRipVersion,'nwIpRipStackSize':nwIpRipStackSize,'nwIpRipThreadPriority':nwIpRipThreadPriority,'nwIpRipDatabaseThreshold':nwIpRipDatabaseThreshold,'nwIpRipAgeOut':nwIpRipAgeOut,'nwIpRipHoldDown':nwIpRipHoldDown,'nwIpRipCounters':nwIpRipCounters,'nwIpRipCtrAdminStatus':nwIpRipCtrAdminStatus,'nwIpRipCtrReset':nwIpRipCtrReset,'nwIpRipCtrOperationalTime':nwIpRipCtrOperationalTime,'nwIpRipCtrInPkts':nwIpRipCtrInPkts,'nwIpRipCtrOutPkts':nwIpRipCtrOutPkts,'nwIpRipCtrFilteredPkts':nwIpRipCtrFilteredPkts,'nwIpRipCtrDiscardPkts':nwIpRipCtrDiscardPkts,'nwIpRipCtrInBytes':nwIpRipCtrInBytes,'nwIpRipCtrOutBytes':nwIpRipCtrOutBytes,'nwIpRipCtrFilteredBytes':nwIpRipCtrFilteredBytes,'nwIpRipCtrDiscardBytes':nwIpRipCtrDiscardBytes,'nwIpRipInterfaces':nwIpRipInterfaces,'nwIpRipIfConfig':nwIpRipIfConfig,'nwIpRipIfTable':nwIpRipIfTable,'nwIpRipIfEntry':nwIpRipIfEntry,_l:nwIpRipIfIndex,'nwIpRipIfAdminStatus':nwIpRipIfAdminStatus,'nwIpRipIfOperStatus':nwIpRipIfOperStatus,'nwIpRipIfOperationalTime':nwIpRipIfOperationalTime,'nwIpRipIfVersion':nwIpRipIfVersion,'nwIpRipIfAdvertisement':nwIpRipIfAdvertisement,'nwIpRipIfFloodDelay':nwIpRipIfFloodDelay,'nwIpRipIfRequestDelay':nwIpRipIfRequestDelay,'nwIpRipIfPriority':nwIpRipIfPriority,'nwIpRipIfHelloTimer':nwIpRipIfHelloTimer,'nwIpRipIfSplitHorizon':nwIpRipIfSplitHorizon,'nwIpRipIfPoisonReverse':nwIpRipIfPoisonReverse,'nwIpRipIfSnooping':nwIpRipIfSnooping,'nwIpRipIfType':nwIpRipIfType,'nwIpRipIfXmitCost':nwIpRipIfXmitCost,'nwIpRipIfAclIdentifier':nwIpRipIfAclIdentifier,'nwIpRipIfAclStatus':nwIpRipIfAclStatus,'nwIpRipIfCounters':nwIpRipIfCounters,'nwIpRipIfCtrTable':nwIpRipIfCtrTable,'nwIpRipIfCtrEntry':nwIpRipIfCtrEntry,_m:nwIpRipIfCtrIfIndex,'nwIpRipIfCtrAdminStatus':nwIpRipIfCtrAdminStatus,'nwIpRipIfCtrReset':nwIpRipIfCtrReset,'nwIpRipIfCtrOperationalTime':nwIpRipIfCtrOperationalTime,'nwIpRipIfCtrInPkts':nwIpRipIfCtrInPkts,'nwIpRipIfCtrOutPkts':nwIpRipIfCtrOutPkts,'nwIpRipIfCtrFilteredPkts':nwIpRipIfCtrFilteredPkts,'nwIpRipIfCtrDiscardPkts':nwIpRipIfCtrDiscardPkts,'nwIpRipIfCtrInBytes':nwIpRipIfCtrInBytes,'nwIpRipIfCtrOutBytes':nwIpRipIfCtrOutBytes,'nwIpRipIfCtrFilteredBytes':nwIpRipIfCtrFilteredBytes,'nwIpRipIfCtrDiscardBytes':nwIpRipIfCtrDiscardBytes,'nwIpRipDatabase':nwIpRipDatabase,'nwIpRipRouteTable':nwIpRipRouteTable,'nwIpRipRouteEntry':nwIpRipRouteEntry,_n:nwIpRipRtNetId,_o:nwIpRipRtIfIndex,_p:nwIpRipRtSrcNode,'nwIpRipRtMask':nwIpRipRtMask,'nwIpRipRtHops':nwIpRipRtHops,'nwIpRipRtAge':nwIpRipRtAge,'nwIpRipRtType':nwIpRipRtType,'nwIpRipRtFlags':nwIpRipRtFlags,'nwIpRipFilters':nwIpRipFilters,'nwIpLinkState':nwIpLinkState,'nwIpOspf':nwIpOspf,'nwIpOspfSystem':nwIpOspfSystem,'nwIpOspfConfig':nwIpOspfConfig,'nwIpOspfAdminStatus':nwIpOspfAdminStatus,'nwIpOspfOperStatus':nwIpOspfOperStatus,'nwIpOspfAdminReset':nwIpOspfAdminReset,'nwIpOspfOperationalTime':nwIpOspfOperationalTime,'nwIpOspfVersion':nwIpOspfVersion,'nwIpOspfStackSize':nwIpOspfStackSize,'nwIpOspfThreadPriority':nwIpOspfThreadPriority,'nwIpOspfCounters':nwIpOspfCounters,'nwIpOspfCtrAdminStatus':nwIpOspfCtrAdminStatus,'nwIpOspfCtrReset':nwIpOspfCtrReset,'nwIpOspfCtrOperationalTime':nwIpOspfCtrOperationalTime,'nwIpOspfCtrInPkts':nwIpOspfCtrInPkts,'nwIpOspfCtrOutPkts':nwIpOspfCtrOutPkts,'nwIpOspfCtrFilteredPkts':nwIpOspfCtrFilteredPkts,'nwIpOspfCtrDiscardPkts':nwIpOspfCtrDiscardPkts,'nwIpOspfCtrInBytes':nwIpOspfCtrInBytes,'nwIpOspfCtrOutBytes':nwIpOspfCtrOutBytes,'nwIpOspfCtrFilteredBytes':nwIpOspfCtrFilteredBytes,'nwIpOspfCtrDiscardBytes':nwIpOspfCtrDiscardBytes,'nwIpOspfInterfaces':nwIpOspfInterfaces,'nwIpOspfIfConfig':nwIpOspfIfConfig,'nwIpOspfIfTable':nwIpOspfIfTable,'nwIpOspfIfEntry':nwIpOspfIfEntry,_r:nwIpOspfIfIndex,'nwIpOspfIfAdminStatus':nwIpOspfIfAdminStatus,'nwIpOspfIfOperStatus':nwIpOspfIfOperStatus,'nwIpOspfIfOperationalTime':nwIpOspfIfOperationalTime,'nwIpOspfIfVersion':nwIpOspfIfVersion,'nwIpOspfIfSnooping':nwIpOspfIfSnooping,'nwIpOspfIfType':nwIpOspfIfType,'nwIpOspfIfAclIdentifier':nwIpOspfIfAclIdentifier,'nwIpOspfIfAclStatus':nwIpOspfIfAclStatus,'nwIpOspfIfCounters':nwIpOspfIfCounters,'nwIpOspfIfCtrTable':nwIpOspfIfCtrTable,'nwIpOspfIfCtrEntry':nwIpOspfIfCtrEntry,_s:nwIpOspfIfCtrIfIndex,'nwIpOspfIfCtrAdminStatus':nwIpOspfIfCtrAdminStatus,'nwIpOspfIfCtrReset':nwIpOspfIfCtrReset,'nwIpOspfIfCtrOperationalTime':nwIpOspfIfCtrOperationalTime,'nwIpOspfIfCtrInPkts':nwIpOspfIfCtrInPkts,'nwIpOspfIfCtrOutPkts':nwIpOspfIfCtrOutPkts,'nwIpOspfIfCtrFilteredPkts':nwIpOspfIfCtrFilteredPkts,'nwIpOspfIfCtrDiscardPkts':nwIpOspfIfCtrDiscardPkts,'nwIpOspfIfCtrInBytes':nwIpOspfIfCtrInBytes,'nwIpOspfIfCtrOutBytes':nwIpOspfIfCtrOutBytes,'nwIpOspfIfCtrFilteredBytes':nwIpOspfIfCtrFilteredBytes,'nwIpOspfIfCtrDiscardBytes':nwIpOspfIfCtrDiscardBytes,'nwIpOspfDatabase':nwIpOspfDatabase,'nwIpOspfFilters':nwIpOspfFilters,'nwIpFib':nwIpFib,'nwIpFibSystem':nwIpFibSystem,'nwIpRipRoutePriority':nwIpRipRoutePriority,'nwIpOSPFRoutePriority':nwIpOSPFRoutePriority,'nwIpStaticRoutePriority':nwIpStaticRoutePriority,'nwIpOspfFib':nwIpOspfFib,'nwIpOspfFibControl':nwIpOspfFibControl,'nwIpOspfForward':nwIpOspfForward,'nwIpOspfLeakAllStaticRoutes':nwIpOspfLeakAllStaticRoutes,'nwIpOspfLeakAllRipRoutes':nwIpOspfLeakAllRipRoutes,'nwIpOspfLeakAllBgp4Routes':nwIpOspfLeakAllBgp4Routes,'nwIpOspfFibEntries':nwIpOspfFibEntries,'nwIpOspfStaticTable':nwIpOspfStaticTable,'nwIpOspfStaticEntry':nwIpOspfStaticEntry,_t:nwIpOspfStaticDest,_u:nwIpOspfStaticForwardMask,_v:nwIpOspfStaticNextHop,'nwIpOspfStaticMetric':nwIpOspfStaticMetric,'nwIpOspfStaticMetricType':nwIpOspfStaticMetricType,'nwIpOspfStaticStatus':nwIpOspfStaticStatus,'nwIpOspfDynamicTable':nwIpOspfDynamicTable,'nwIpOspfRipTable':nwIpOspfRipTable,'nwIpOspfBgp4Table':nwIpOspfBgp4Table,'nwIpEndSystems':nwIpEndSystems,'nwIpHostsSystem':nwIpHostsSystem,'nwIpHostsTimeToLive':nwIpHostsTimeToLive,'nwIpHostsRetryCount':nwIpHostsRetryCount,'nwIpHostsInterfaces':nwIpHostsInterfaces,'nwIpHostCtlTable':nwIpHostCtlTable,'nwIpHostCtlEntry':nwIpHostCtlEntry,_x:nwIpHostCtlIfIndex,'nwIpHostCtlAdminStatus':nwIpHostCtlAdminStatus,'nwIpHostCtlOperStatus':nwIpHostCtlOperStatus,'nwIpHostCtlOperationalTime':nwIpHostCtlOperationalTime,'nwIpHostCtlProtocol':nwIpHostCtlProtocol,'nwIpHostCtlSnooping':nwIpHostCtlSnooping,'nwIpHostCtlProxy':nwIpHostCtlProxy,'nwIpHostCtlCacheMax':nwIpHostCtlCacheMax,'nwIpHostCtlCacheSize':nwIpHostCtlCacheSize,'nwIpHostCtlNumStatics':nwIpHostCtlNumStatics,'nwIpHostCtlNumDynamics':nwIpHostCtlNumDynamics,'nwIpHostCtlCacheHits':nwIpHostCtlCacheHits,'nwIpHostCtlCacheMisses':nwIpHostCtlCacheMisses,'nwIpHostsToMedia':nwIpHostsToMedia,'nwIpHostMapTable':nwIpHostMapTable,'nwIpHostMapEntry':nwIpHostMapEntry,_y:nwIpHostMapIfIndex,_z:nwIpHostMapIpAddr,'nwIpHostMapPhysAddr':nwIpHostMapPhysAddr,'nwIpHostMapType':nwIpHostMapType,'nwIpHostMapCircuitID':nwIpHostMapCircuitID,'nwIpHostMapFraming':nwIpHostMapFraming,'nwIpHostMapPortNumber':nwIpHostMapPortNumber,'nwIpAccessControl':nwIpAccessControl,'nwIpAclValidEntries':nwIpAclValidEntries,'nwIpAclTable':nwIpAclTable,'nwIpAclEntry':nwIpAclEntry,_A0:nwIpAclIdentifier,_A1:nwIpAclSequence,'nwIpAclPermission':nwIpAclPermission,'nwIpAclMatches':nwIpAclMatches,'nwIpAclDestAddress':nwIpAclDestAddress,'nwIpAclDestMask':nwIpAclDestMask,'nwIpAclSrcAddress':nwIpAclSrcAddress,'nwIpAclSrcMask':nwIpAclSrcMask,'nwIpAclProtocol':nwIpAclProtocol,'nwIpAclPortNumber':nwIpAclPortNumber,'nwIpFilters':nwIpFilters,'nwIpRedirector':nwIpRedirector,'nwIpRedirectorSystem':nwIpRedirectorSystem,'nwIpRedirectTable':nwIpRedirectTable,'nwIpRedirectEntry':nwIpRedirectEntry,_A2:nwIpRedirectPort,'nwIpRedirectAddress':nwIpRedirectAddress,'nwIpRedirectType':nwIpRedirectType,'nwIpRedirectCount':nwIpRedirectCount,'nwIpRedirectorInterface':nwIpRedirectorInterface,'nwIpEvent':nwIpEvent,'nwIpEventLogConfig':nwIpEventLogConfig,'nwIpEventAdminStatus':nwIpEventAdminStatus,'nwIpEventMaxEntries':nwIpEventMaxEntries,'nwIpEventTraceAll':nwIpEventTraceAll,'nwIpEventLogFilterTable':nwIpEventLogFilterTable,'nwIpEventFilterTable':nwIpEventFilterTable,'nwIpEventFilterEntry':nwIpEventFilterEntry,_A3:nwIpEventFltrProtocol,_A4:nwIpEventFltrIfNum,'nwIpEventFltrControl':nwIpEventFltrControl,'nwIpEventFltrType':nwIpEventFltrType,'nwIpEventFltrSeverity':nwIpEventFltrSeverity,'nwIpEventFltrAction':nwIpEventFltrAction,'nwIpEventLogTable':nwIpEventLogTable,'nwIpEventTable':nwIpEventTable,'nwIpEventEntry':nwIpEventEntry,_A5:nwIpEventNumber,'nwIpEventTime':nwIpEventTime,'nwIpEventType':nwIpEventType,'nwIpEventSeverity':nwIpEventSeverity,'nwIpEventProtocol':nwIpEventProtocol,'nwIpEventIfNum':nwIpEventIfNum,'nwIpEventTextString':nwIpEventTextString,'nwIpWorkGroup':nwIpWorkGroup,'nwIpWgDefTable':nwIpWgDefTable,'nwIpWgDefEntry':nwIpWgDefEntry,_A6:nwIpWgDefIdentifier,'nwIpWgDefHostAddress':nwIpWgDefHostAddress,'nwIpWgDefSubnetMask':nwIpWgDefSubnetMask,'nwIpWgDefSecurity':nwIpWgDefSecurity,'nwIpWgDefFastPath':nwIpWgDefFastPath,'nwIpWgDefRowStatus':nwIpWgDefRowStatus,'nwIpWgDefOperStatus':nwIpWgDefOperStatus,'nwIpWgDefNumActiveIntf':nwIpWgDefNumActiveIntf,'nwIpWgDefNumTotalIntf':nwIpWgDefNumTotalIntf,'nwIpWgIfTable':nwIpWgIfTable,'nwIpWgIfEntry':nwIpWgIfEntry,_A7:nwIpWgIfDefIdent,_A8:nwIpWgIfIfIndex,'nwIpWgIfNumActiveHosts':nwIpWgIfNumActiveHosts,'nwIpWgIfNumKnownHosts':nwIpWgIfNumKnownHosts,'nwIpWgIfRowStatus':nwIpWgIfRowStatus,'nwIpWgIfOperStatus':nwIpWgIfOperStatus,'nwIpWgRngTable':nwIpWgRngTable,'nwIpWgRngEntry':nwIpWgRngEntry,_AA:nwIpWgRngBegHostAddr,_AB:nwIpWgRngEndHostAddr,_AC:nwIpWgRngIfIndex,'nwIpWgRngPhysAddr':nwIpWgRngPhysAddr,'nwIpWgRngRowStatus':nwIpWgRngRowStatus,'nwIpWgRngOperStatus':nwIpWgRngOperStatus,'nwIpWgHostTable':nwIpWgHostTable,'nwIpWgHostEntry':nwIpWgHostEntry,_AD:nwIpWgHostHostAddr,_AE:nwIpWgHostIfIndex,'nwIpWgHostDefIdent':nwIpWgHostDefIdent,'nwIpWgHostPhysAddr':nwIpWgHostPhysAddr,'nwIpWgHostStatus':nwIpWgHostStatus,'nwIpClientServices':nwIpClientServices})