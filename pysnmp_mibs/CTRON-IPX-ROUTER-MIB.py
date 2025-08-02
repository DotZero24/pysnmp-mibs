_A8='nwIpxEventNumber'
_A7='nwIpxEventFltrIfNum'
_A6='nwIpxEventFltrProtocol'
_A5='nwIpxEchoIfCtrIfIndex'
_A4='nwIpxEchoIfIndex'
_A3='nwIpxBcastIfCtrIfIndex'
_A2='nwIpxBcastIfIndex'
_A1='nwIpxNetBIOSIfCtrIfIndex'
_A0='nwIpxNetBIOSIfIndex'
_z='nwIpxAclSequence'
_y='nwIpxAclIdentifier'
_x='nwIpxHostMapIpxAddr'
_w='nwIpxHostMapIfIndex'
_v='nwIpxFibNetId'
_u='nwIpxSapServerIfSrcNode'
_t='nwIpxSapServerIfIfNum'
_s='nwIpxSapServerIfServiceType'
_r='nwIpxSapServerIfSocket'
_q='nwIpxSapServerIfNode'
_p='nwIpxSapServerIfNetId'
_o='nwIpxSapIfCtrIfIndex'
_n='nwIpxSapIfIndex'
_m='nwIpxRipRtSrcNode'
_l='nwIpxRipRtIfIndex'
_k='nwIpxRipRtNetId'
_j='nwIpxRipIfCtrIfIndex'
_i='nwIpxRipIfIndex'
_h='nwIpxFwdIfCtrIfIndex'
_g='nwIpxAddrIfAddress'
_f='nwIpxAddrIfIndex'
_e='canonical'
_d='encapfddisnap'
_c='encapfddi8022'
_b='encaptrsnap'
_a='encaptr8022'
_Z='encapenetnovell'
_Y='encapenetsnap'
_X='encapenet8022'
_W='encapenet'
_V='nativewan'
_U='novell'
_T='ethernet'
_S='nwIpxFwdIfIndex'
_R='TimeTicks'
_Q='remote'
_P='direct'
_O='delete'
_N='add'
_M='invalid'
_L='invalid-config'
_K='pending-enable'
_J='pending-disable'
_I='reset'
_H='CTRON-IPX-ROUTER-MIB'
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
MacAddress,=mibBuilder.importSymbols('BRIDGE-MIB','MacAddress')
nwRtrProtoSuites,=mibBuilder.importSymbols('ROUTER-OIDS','nwRtrProtoSuites')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_R,'Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class IpxAddress(OctetString):0
_NwIpxRouter_ObjectIdentity=ObjectIdentity
nwIpxRouter=_NwIpxRouter_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2))
_NwIpxMibs_ObjectIdentity=ObjectIdentity
nwIpxMibs=_NwIpxMibs_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,1))
_NwIpxMibRevText_Type=DisplayString
_NwIpxMibRevText_Object=MibScalar
nwIpxMibRevText=_NwIpxMibRevText_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,1,1),_NwIpxMibRevText_Type())
nwIpxMibRevText.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxMibRevText.setStatus(_A)
_NwIpxComponents_ObjectIdentity=ObjectIdentity
nwIpxComponents=_NwIpxComponents_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2))
_NwIpxSystem_ObjectIdentity=ObjectIdentity
nwIpxSystem=_NwIpxSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,1))
_NwIpxSysConfig_ObjectIdentity=ObjectIdentity
nwIpxSysConfig=_NwIpxSysConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,1,1))
_NwIpxSysRouterId_Type=IpxAddress
_NwIpxSysRouterId_Object=MibScalar
nwIpxSysRouterId=_NwIpxSysRouterId_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,1,1,1),_NwIpxSysRouterId_Type())
nwIpxSysRouterId.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSysRouterId.setStatus(_A)
_NwIpxSysAdministration_ObjectIdentity=ObjectIdentity
nwIpxSysAdministration=_NwIpxSysAdministration_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,1,2))
class _NwIpxSysAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxSysAdminStatus_Type.__name__=_C
_NwIpxSysAdminStatus_Object=MibScalar
nwIpxSysAdminStatus=_NwIpxSysAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,1,2,1),_NwIpxSysAdminStatus_Type())
nwIpxSysAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSysAdminStatus.setStatus(_A)
class _NwIpxSysOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_J,4),(_K,5),(_L,6)))
_NwIpxSysOperStatus_Type.__name__=_C
_NwIpxSysOperStatus_Object=MibScalar
nwIpxSysOperStatus=_NwIpxSysOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,1,2,2),_NwIpxSysOperStatus_Type())
nwIpxSysOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSysOperStatus.setStatus(_A)
class _NwIpxSysAdminReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpxSysAdminReset_Type.__name__=_C
_NwIpxSysAdminReset_Object=MibScalar
nwIpxSysAdminReset=_NwIpxSysAdminReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,1,2,3),_NwIpxSysAdminReset_Type())
nwIpxSysAdminReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSysAdminReset.setStatus(_A)
_NwIpxSysOperationalTimel_Type=TimeTicks
_NwIpxSysOperationalTimel_Object=MibScalar
nwIpxSysOperationalTimel=_NwIpxSysOperationalTimel_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,1,2,4),_NwIpxSysOperationalTimel_Type())
nwIpxSysOperationalTimel.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSysOperationalTimel.setStatus(_A)
_NwIpxSysVersion_Type=DisplayString
_NwIpxSysVersion_Object=MibScalar
nwIpxSysVersion=_NwIpxSysVersion_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,1,2,5),_NwIpxSysVersion_Type())
nwIpxSysVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSysVersion.setStatus(_A)
_NwIpxForwarding_ObjectIdentity=ObjectIdentity
nwIpxForwarding=_NwIpxForwarding_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2))
_NwIpxFwdSystem_ObjectIdentity=ObjectIdentity
nwIpxFwdSystem=_NwIpxFwdSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1))
_NwIpxFwdCounters_ObjectIdentity=ObjectIdentity
nwIpxFwdCounters=_NwIpxFwdCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1,1))
class _NwIpxFwdCtrAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxFwdCtrAdminStatus_Type.__name__=_C
_NwIpxFwdCtrAdminStatus_Object=MibScalar
nwIpxFwdCtrAdminStatus=_NwIpxFwdCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1,1,1),_NwIpxFwdCtrAdminStatus_Type())
nwIpxFwdCtrAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxFwdCtrAdminStatus.setStatus(_A)
class _NwIpxFwdCtrReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpxFwdCtrReset_Type.__name__=_C
_NwIpxFwdCtrReset_Object=MibScalar
nwIpxFwdCtrReset=_NwIpxFwdCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1,1,2),_NwIpxFwdCtrReset_Type())
nwIpxFwdCtrReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxFwdCtrReset.setStatus(_A)
_NwIpxFwdCtrOperationalTime_Type=TimeTicks
_NwIpxFwdCtrOperationalTime_Object=MibScalar
nwIpxFwdCtrOperationalTime=_NwIpxFwdCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1,1,3),_NwIpxFwdCtrOperationalTime_Type())
nwIpxFwdCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdCtrOperationalTime.setStatus(_A)
_NwIpxFwdCtrInPkts_Type=Counter32
_NwIpxFwdCtrInPkts_Object=MibScalar
nwIpxFwdCtrInPkts=_NwIpxFwdCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1,1,4),_NwIpxFwdCtrInPkts_Type())
nwIpxFwdCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdCtrInPkts.setStatus(_A)
_NwIpxFwdCtrOutPkts_Type=Counter32
_NwIpxFwdCtrOutPkts_Object=MibScalar
nwIpxFwdCtrOutPkts=_NwIpxFwdCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1,1,5),_NwIpxFwdCtrOutPkts_Type())
nwIpxFwdCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdCtrOutPkts.setStatus(_A)
_NwIpxFwdCtrFwdPkts_Type=Counter32
_NwIpxFwdCtrFwdPkts_Object=MibScalar
nwIpxFwdCtrFwdPkts=_NwIpxFwdCtrFwdPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1,1,6),_NwIpxFwdCtrFwdPkts_Type())
nwIpxFwdCtrFwdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdCtrFwdPkts.setStatus(_A)
_NwIpxFwdCtrFilteredPkts_Type=Counter32
_NwIpxFwdCtrFilteredPkts_Object=MibScalar
nwIpxFwdCtrFilteredPkts=_NwIpxFwdCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1,1,7),_NwIpxFwdCtrFilteredPkts_Type())
nwIpxFwdCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdCtrFilteredPkts.setStatus(_A)
_NwIpxFwdCtrDiscardPkts_Type=Counter32
_NwIpxFwdCtrDiscardPkts_Object=MibScalar
nwIpxFwdCtrDiscardPkts=_NwIpxFwdCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1,1,8),_NwIpxFwdCtrDiscardPkts_Type())
nwIpxFwdCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdCtrDiscardPkts.setStatus(_A)
_NwIpxFwdCtrAddrErrPkts_Type=Counter32
_NwIpxFwdCtrAddrErrPkts_Object=MibScalar
nwIpxFwdCtrAddrErrPkts=_NwIpxFwdCtrAddrErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1,1,9),_NwIpxFwdCtrAddrErrPkts_Type())
nwIpxFwdCtrAddrErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdCtrAddrErrPkts.setStatus(_A)
_NwIpxFwdCtrLenErrPkts_Type=Counter32
_NwIpxFwdCtrLenErrPkts_Object=MibScalar
nwIpxFwdCtrLenErrPkts=_NwIpxFwdCtrLenErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1,1,10),_NwIpxFwdCtrLenErrPkts_Type())
nwIpxFwdCtrLenErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdCtrLenErrPkts.setStatus(_A)
_NwIpxFwdCtrHdrErrPkts_Type=Counter32
_NwIpxFwdCtrHdrErrPkts_Object=MibScalar
nwIpxFwdCtrHdrErrPkts=_NwIpxFwdCtrHdrErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1,1,11),_NwIpxFwdCtrHdrErrPkts_Type())
nwIpxFwdCtrHdrErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdCtrHdrErrPkts.setStatus(_A)
_NwIpxFwdCtrInBytes_Type=Counter32
_NwIpxFwdCtrInBytes_Object=MibScalar
nwIpxFwdCtrInBytes=_NwIpxFwdCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1,1,12),_NwIpxFwdCtrInBytes_Type())
nwIpxFwdCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdCtrInBytes.setStatus(_A)
_NwIpxFwdCtrOutBytes_Type=Counter32
_NwIpxFwdCtrOutBytes_Object=MibScalar
nwIpxFwdCtrOutBytes=_NwIpxFwdCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1,1,13),_NwIpxFwdCtrOutBytes_Type())
nwIpxFwdCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdCtrOutBytes.setStatus(_A)
_NwIpxFwdCtrFwdBytes_Type=Counter32
_NwIpxFwdCtrFwdBytes_Object=MibScalar
nwIpxFwdCtrFwdBytes=_NwIpxFwdCtrFwdBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1,1,14),_NwIpxFwdCtrFwdBytes_Type())
nwIpxFwdCtrFwdBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdCtrFwdBytes.setStatus(_A)
_NwIpxFwdCtrFilteredBytes_Type=Counter32
_NwIpxFwdCtrFilteredBytes_Object=MibScalar
nwIpxFwdCtrFilteredBytes=_NwIpxFwdCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1,1,15),_NwIpxFwdCtrFilteredBytes_Type())
nwIpxFwdCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdCtrFilteredBytes.setStatus(_A)
_NwIpxFwdCtrDiscardBytes_Type=Counter32
_NwIpxFwdCtrDiscardBytes_Object=MibScalar
nwIpxFwdCtrDiscardBytes=_NwIpxFwdCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1,1,16),_NwIpxFwdCtrDiscardBytes_Type())
nwIpxFwdCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdCtrDiscardBytes.setStatus(_A)
_NwIpxFwdCtrHostInPkts_Type=Counter32
_NwIpxFwdCtrHostInPkts_Object=MibScalar
nwIpxFwdCtrHostInPkts=_NwIpxFwdCtrHostInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1,1,17),_NwIpxFwdCtrHostInPkts_Type())
nwIpxFwdCtrHostInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdCtrHostInPkts.setStatus(_A)
_NwIpxFwdCtrHostOutPkts_Type=Counter32
_NwIpxFwdCtrHostOutPkts_Object=MibScalar
nwIpxFwdCtrHostOutPkts=_NwIpxFwdCtrHostOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1,1,18),_NwIpxFwdCtrHostOutPkts_Type())
nwIpxFwdCtrHostOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdCtrHostOutPkts.setStatus(_A)
_NwIpxFwdCtrHostDiscardPkts_Type=Counter32
_NwIpxFwdCtrHostDiscardPkts_Object=MibScalar
nwIpxFwdCtrHostDiscardPkts=_NwIpxFwdCtrHostDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1,1,19),_NwIpxFwdCtrHostDiscardPkts_Type())
nwIpxFwdCtrHostDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdCtrHostDiscardPkts.setStatus(_A)
_NwIpxFwdCtrHostInBytes_Type=Counter32
_NwIpxFwdCtrHostInBytes_Object=MibScalar
nwIpxFwdCtrHostInBytes=_NwIpxFwdCtrHostInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1,1,20),_NwIpxFwdCtrHostInBytes_Type())
nwIpxFwdCtrHostInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdCtrHostInBytes.setStatus(_A)
_NwIpxFwdCtrHostOutBytes_Type=Counter32
_NwIpxFwdCtrHostOutBytes_Object=MibScalar
nwIpxFwdCtrHostOutBytes=_NwIpxFwdCtrHostOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1,1,21),_NwIpxFwdCtrHostOutBytes_Type())
nwIpxFwdCtrHostOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdCtrHostOutBytes.setStatus(_A)
_NwIpxFwdCtrHostDiscardBytes_Type=Counter32
_NwIpxFwdCtrHostDiscardBytes_Object=MibScalar
nwIpxFwdCtrHostDiscardBytes=_NwIpxFwdCtrHostDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,1,1,22),_NwIpxFwdCtrHostDiscardBytes_Type())
nwIpxFwdCtrHostDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdCtrHostDiscardBytes.setStatus(_A)
_NwIpxFwdInterfaces_ObjectIdentity=ObjectIdentity
nwIpxFwdInterfaces=_NwIpxFwdInterfaces_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2))
_NwIpxFwdIfConfig_ObjectIdentity=ObjectIdentity
nwIpxFwdIfConfig=_NwIpxFwdIfConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,1))
_NwIpxFwdIfTable_Object=MibTable
nwIpxFwdIfTable=_NwIpxFwdIfTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,1,1))
if mibBuilder.loadTexts:nwIpxFwdIfTable.setStatus(_A)
_NwIpxFwdIfEntry_Object=MibTableRow
nwIpxFwdIfEntry=_NwIpxFwdIfEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,1,1,1))
nwIpxFwdIfEntry.setIndexNames((0,_H,_S))
if mibBuilder.loadTexts:nwIpxFwdIfEntry.setStatus(_A)
_NwIpxFwdIfIndex_Type=Integer32
_NwIpxFwdIfIndex_Object=MibTableColumn
nwIpxFwdIfIndex=_NwIpxFwdIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,1,1,1,1),_NwIpxFwdIfIndex_Type())
nwIpxFwdIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfIndex.setStatus(_A)
class _NwIpxFwdIfAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxFwdIfAdminStatus_Type.__name__=_C
_NwIpxFwdIfAdminStatus_Object=MibTableColumn
nwIpxFwdIfAdminStatus=_NwIpxFwdIfAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,1,1,1,2),_NwIpxFwdIfAdminStatus_Type())
nwIpxFwdIfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxFwdIfAdminStatus.setStatus(_A)
class _NwIpxFwdIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_J,4),(_K,5),(_L,6)))
_NwIpxFwdIfOperStatus_Type.__name__=_C
_NwIpxFwdIfOperStatus_Object=MibTableColumn
nwIpxFwdIfOperStatus=_NwIpxFwdIfOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,1,1,1,3),_NwIpxFwdIfOperStatus_Type())
nwIpxFwdIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfOperStatus.setStatus(_A)
_NwIpxFwdIfOperationalTime_Type=TimeTicks
_NwIpxFwdIfOperationalTime_Object=MibTableColumn
nwIpxFwdIfOperationalTime=_NwIpxFwdIfOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,1,1,1,4),_NwIpxFwdIfOperationalTime_Type())
nwIpxFwdIfOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfOperationalTime.setStatus(_A)
class _NwIpxFwdIfControl_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_N,2),(_O,3)))
_NwIpxFwdIfControl_Type.__name__=_C
_NwIpxFwdIfControl_Object=MibTableColumn
nwIpxFwdIfControl=_NwIpxFwdIfControl_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,1,1,1,5),_NwIpxFwdIfControl_Type())
nwIpxFwdIfControl.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxFwdIfControl.setStatus(_A)
class _NwIpxFwdIfMtu_Type(Integer32):defaultValue=1500
_NwIpxFwdIfMtu_Type.__name__=_C
_NwIpxFwdIfMtu_Object=MibTableColumn
nwIpxFwdIfMtu=_NwIpxFwdIfMtu_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,1,1,1,6),_NwIpxFwdIfMtu_Type())
nwIpxFwdIfMtu.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxFwdIfMtu.setStatus(_A)
class _NwIpxFwdIfForwarding_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxFwdIfForwarding_Type.__name__=_C
_NwIpxFwdIfForwarding_Object=MibTableColumn
nwIpxFwdIfForwarding=_NwIpxFwdIfForwarding_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,1,1,1,7),_NwIpxFwdIfForwarding_Type())
nwIpxFwdIfForwarding.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxFwdIfForwarding.setStatus(_A)
class _NwIpxFwdIfFrameType_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,6,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_E,1),(_T,2),('snap',3),('i8022',4),(_U,6),(_V,8),(_W,9),(_X,10),(_Y,11),(_Z,12),(_a,13),(_b,14),(_c,15),(_d,16),(_e,17)))
_NwIpxFwdIfFrameType_Type.__name__=_C
_NwIpxFwdIfFrameType_Object=MibTableColumn
nwIpxFwdIfFrameType=_NwIpxFwdIfFrameType_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,1,1,1,8),_NwIpxFwdIfFrameType_Type())
nwIpxFwdIfFrameType.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxFwdIfFrameType.setStatus(_A)
class _NwIpxFwdIfAclIdentifier_Type(Integer32):defaultValue=0
_NwIpxFwdIfAclIdentifier_Type.__name__=_C
_NwIpxFwdIfAclIdentifier_Object=MibTableColumn
nwIpxFwdIfAclIdentifier=_NwIpxFwdIfAclIdentifier_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,1,1,1,9),_NwIpxFwdIfAclIdentifier_Type())
nwIpxFwdIfAclIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxFwdIfAclIdentifier.setStatus(_A)
class _NwIpxFwdIfAclStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxFwdIfAclStatus_Type.__name__=_C
_NwIpxFwdIfAclStatus_Object=MibTableColumn
nwIpxFwdIfAclStatus=_NwIpxFwdIfAclStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,1,1,1,10),_NwIpxFwdIfAclStatus_Type())
nwIpxFwdIfAclStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxFwdIfAclStatus.setStatus(_A)
class _NwIpxFwdIfCacheControl_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('disable',2),('enable',3)))
_NwIpxFwdIfCacheControl_Type.__name__=_C
_NwIpxFwdIfCacheControl_Object=MibTableColumn
nwIpxFwdIfCacheControl=_NwIpxFwdIfCacheControl_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,1,1,1,11),_NwIpxFwdIfCacheControl_Type())
nwIpxFwdIfCacheControl.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxFwdIfCacheControl.setStatus(_A)
_NwIpxFwdIfCacheEntries_Type=Counter32
_NwIpxFwdIfCacheEntries_Object=MibTableColumn
nwIpxFwdIfCacheEntries=_NwIpxFwdIfCacheEntries_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,1,1,1,12),_NwIpxFwdIfCacheEntries_Type())
nwIpxFwdIfCacheEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCacheEntries.setStatus(_A)
_NwIpxFwdIfCacheHits_Type=Counter32
_NwIpxFwdIfCacheHits_Object=MibTableColumn
nwIpxFwdIfCacheHits=_NwIpxFwdIfCacheHits_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,1,1,1,13),_NwIpxFwdIfCacheHits_Type())
nwIpxFwdIfCacheHits.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCacheHits.setStatus(_A)
_NwIpxFwdIfCacheMisses_Type=Counter32
_NwIpxFwdIfCacheMisses_Object=MibTableColumn
nwIpxFwdIfCacheMisses=_NwIpxFwdIfCacheMisses_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,1,1,1,14),_NwIpxFwdIfCacheMisses_Type())
nwIpxFwdIfCacheMisses.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCacheMisses.setStatus(_A)
_NwIpxAddressTable_Object=MibTable
nwIpxAddressTable=_NwIpxAddressTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,1,2))
if mibBuilder.loadTexts:nwIpxAddressTable.setStatus(_A)
_NwIpxAddrEntry_Object=MibTableRow
nwIpxAddrEntry=_NwIpxAddrEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,1,2,1))
nwIpxAddrEntry.setIndexNames((0,_H,_f),(0,_H,_g))
if mibBuilder.loadTexts:nwIpxAddrEntry.setStatus(_A)
_NwIpxAddrIfIndex_Type=Integer32
_NwIpxAddrIfIndex_Object=MibTableColumn
nwIpxAddrIfIndex=_NwIpxAddrIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,1,2,1,1),_NwIpxAddrIfIndex_Type())
nwIpxAddrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxAddrIfIndex.setStatus(_A)
_NwIpxAddrIfAddress_Type=IpxAddress
_NwIpxAddrIfAddress_Object=MibTableColumn
nwIpxAddrIfAddress=_NwIpxAddrIfAddress_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,1,2,1,2),_NwIpxAddrIfAddress_Type())
nwIpxAddrIfAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxAddrIfAddress.setStatus(_A)
class _NwIpxAddrIfControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_N,2),(_O,3)))
_NwIpxAddrIfControl_Type.__name__=_C
_NwIpxAddrIfControl_Object=MibTableColumn
nwIpxAddrIfControl=_NwIpxAddrIfControl_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,1,2,1,3),_NwIpxAddrIfControl_Type())
nwIpxAddrIfControl.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxAddrIfControl.setStatus(_A)
class _NwIpxAddrIfAddrType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('primary',2),('secondary',3)))
_NwIpxAddrIfAddrType_Type.__name__=_C
_NwIpxAddrIfAddrType_Object=MibTableColumn
nwIpxAddrIfAddrType=_NwIpxAddrIfAddrType_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,1,2,1,4),_NwIpxAddrIfAddrType_Type())
nwIpxAddrIfAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxAddrIfAddrType.setStatus(_A)
_NwIpxFwdIfCounters_ObjectIdentity=ObjectIdentity
nwIpxFwdIfCounters=_NwIpxFwdIfCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2))
_NwIpxFwdIfCtrTable_Object=MibTable
nwIpxFwdIfCtrTable=_NwIpxFwdIfCtrTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1))
if mibBuilder.loadTexts:nwIpxFwdIfCtrTable.setStatus(_A)
_NwIpxFwdIfCtrEntry_Object=MibTableRow
nwIpxFwdIfCtrEntry=_NwIpxFwdIfCtrEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1))
nwIpxFwdIfCtrEntry.setIndexNames((0,_H,_h))
if mibBuilder.loadTexts:nwIpxFwdIfCtrEntry.setStatus(_A)
_NwIpxFwdIfCtrIfIndex_Type=Integer32
_NwIpxFwdIfCtrIfIndex_Object=MibTableColumn
nwIpxFwdIfCtrIfIndex=_NwIpxFwdIfCtrIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1,1),_NwIpxFwdIfCtrIfIndex_Type())
nwIpxFwdIfCtrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCtrIfIndex.setStatus(_A)
class _NwIpxFwdIfCtrAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxFwdIfCtrAdminStatus_Type.__name__=_C
_NwIpxFwdIfCtrAdminStatus_Object=MibTableColumn
nwIpxFwdIfCtrAdminStatus=_NwIpxFwdIfCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1,2),_NwIpxFwdIfCtrAdminStatus_Type())
nwIpxFwdIfCtrAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxFwdIfCtrAdminStatus.setStatus(_A)
class _NwIpxFwdIfCtrReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpxFwdIfCtrReset_Type.__name__=_C
_NwIpxFwdIfCtrReset_Object=MibTableColumn
nwIpxFwdIfCtrReset=_NwIpxFwdIfCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1,3),_NwIpxFwdIfCtrReset_Type())
nwIpxFwdIfCtrReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxFwdIfCtrReset.setStatus(_A)
_NwIpxFwdIfCtrOperationalTime_Type=TimeTicks
_NwIpxFwdIfCtrOperationalTime_Object=MibTableColumn
nwIpxFwdIfCtrOperationalTime=_NwIpxFwdIfCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1,4),_NwIpxFwdIfCtrOperationalTime_Type())
nwIpxFwdIfCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCtrOperationalTime.setStatus(_A)
_NwIpxFwdIfCtrInPkts_Type=Counter32
_NwIpxFwdIfCtrInPkts_Object=MibTableColumn
nwIpxFwdIfCtrInPkts=_NwIpxFwdIfCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1,5),_NwIpxFwdIfCtrInPkts_Type())
nwIpxFwdIfCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCtrInPkts.setStatus(_A)
_NwIpxFwdIfCtrOutPkts_Type=Counter32
_NwIpxFwdIfCtrOutPkts_Object=MibTableColumn
nwIpxFwdIfCtrOutPkts=_NwIpxFwdIfCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1,6),_NwIpxFwdIfCtrOutPkts_Type())
nwIpxFwdIfCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCtrOutPkts.setStatus(_A)
_NwIpxFwdIfCtrFwdPkts_Type=Counter32
_NwIpxFwdIfCtrFwdPkts_Object=MibTableColumn
nwIpxFwdIfCtrFwdPkts=_NwIpxFwdIfCtrFwdPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1,7),_NwIpxFwdIfCtrFwdPkts_Type())
nwIpxFwdIfCtrFwdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCtrFwdPkts.setStatus(_A)
_NwIpxFwdIfCtrFilteredPkts_Type=Counter32
_NwIpxFwdIfCtrFilteredPkts_Object=MibTableColumn
nwIpxFwdIfCtrFilteredPkts=_NwIpxFwdIfCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1,8),_NwIpxFwdIfCtrFilteredPkts_Type())
nwIpxFwdIfCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCtrFilteredPkts.setStatus(_A)
_NwIpxFwdIfCtrDiscardPkts_Type=Counter32
_NwIpxFwdIfCtrDiscardPkts_Object=MibTableColumn
nwIpxFwdIfCtrDiscardPkts=_NwIpxFwdIfCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1,9),_NwIpxFwdIfCtrDiscardPkts_Type())
nwIpxFwdIfCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCtrDiscardPkts.setStatus(_A)
_NwIpxFwdIfCtrAddrErrPkts_Type=Counter32
_NwIpxFwdIfCtrAddrErrPkts_Object=MibTableColumn
nwIpxFwdIfCtrAddrErrPkts=_NwIpxFwdIfCtrAddrErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1,10),_NwIpxFwdIfCtrAddrErrPkts_Type())
nwIpxFwdIfCtrAddrErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCtrAddrErrPkts.setStatus(_A)
_NwIpxFwdIfCtrLenErrPkts_Type=Counter32
_NwIpxFwdIfCtrLenErrPkts_Object=MibTableColumn
nwIpxFwdIfCtrLenErrPkts=_NwIpxFwdIfCtrLenErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1,11),_NwIpxFwdIfCtrLenErrPkts_Type())
nwIpxFwdIfCtrLenErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCtrLenErrPkts.setStatus(_A)
_NwIpxFwdIfCtrHdrErrPkts_Type=Counter32
_NwIpxFwdIfCtrHdrErrPkts_Object=MibTableColumn
nwIpxFwdIfCtrHdrErrPkts=_NwIpxFwdIfCtrHdrErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1,12),_NwIpxFwdIfCtrHdrErrPkts_Type())
nwIpxFwdIfCtrHdrErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCtrHdrErrPkts.setStatus(_A)
_NwIpxFwdIfCtrInBytes_Type=Counter32
_NwIpxFwdIfCtrInBytes_Object=MibTableColumn
nwIpxFwdIfCtrInBytes=_NwIpxFwdIfCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1,13),_NwIpxFwdIfCtrInBytes_Type())
nwIpxFwdIfCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCtrInBytes.setStatus(_A)
_NwIpxFwdIfCtrOutBytes_Type=Counter32
_NwIpxFwdIfCtrOutBytes_Object=MibTableColumn
nwIpxFwdIfCtrOutBytes=_NwIpxFwdIfCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1,14),_NwIpxFwdIfCtrOutBytes_Type())
nwIpxFwdIfCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCtrOutBytes.setStatus(_A)
_NwIpxFwdIfCtrFwdBytes_Type=Counter32
_NwIpxFwdIfCtrFwdBytes_Object=MibTableColumn
nwIpxFwdIfCtrFwdBytes=_NwIpxFwdIfCtrFwdBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1,15),_NwIpxFwdIfCtrFwdBytes_Type())
nwIpxFwdIfCtrFwdBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCtrFwdBytes.setStatus(_A)
_NwIpxFwdIfCtrFilteredBytes_Type=Counter32
_NwIpxFwdIfCtrFilteredBytes_Object=MibTableColumn
nwIpxFwdIfCtrFilteredBytes=_NwIpxFwdIfCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1,16),_NwIpxFwdIfCtrFilteredBytes_Type())
nwIpxFwdIfCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCtrFilteredBytes.setStatus(_A)
_NwIpxFwdIfCtrDiscardBytes_Type=Counter32
_NwIpxFwdIfCtrDiscardBytes_Object=MibTableColumn
nwIpxFwdIfCtrDiscardBytes=_NwIpxFwdIfCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1,17),_NwIpxFwdIfCtrDiscardBytes_Type())
nwIpxFwdIfCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCtrDiscardBytes.setStatus(_A)
_NwIpxFwdIfCtrHostInPkts_Type=Counter32
_NwIpxFwdIfCtrHostInPkts_Object=MibTableColumn
nwIpxFwdIfCtrHostInPkts=_NwIpxFwdIfCtrHostInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1,18),_NwIpxFwdIfCtrHostInPkts_Type())
nwIpxFwdIfCtrHostInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCtrHostInPkts.setStatus(_A)
_NwIpxFwdIfCtrHostOutPkts_Type=Counter32
_NwIpxFwdIfCtrHostOutPkts_Object=MibTableColumn
nwIpxFwdIfCtrHostOutPkts=_NwIpxFwdIfCtrHostOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1,19),_NwIpxFwdIfCtrHostOutPkts_Type())
nwIpxFwdIfCtrHostOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCtrHostOutPkts.setStatus(_A)
_NwIpxFwdIfCtrHostDiscardPkts_Type=Counter32
_NwIpxFwdIfCtrHostDiscardPkts_Object=MibTableColumn
nwIpxFwdIfCtrHostDiscardPkts=_NwIpxFwdIfCtrHostDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1,20),_NwIpxFwdIfCtrHostDiscardPkts_Type())
nwIpxFwdIfCtrHostDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCtrHostDiscardPkts.setStatus(_A)
_NwIpxFwdIfCtrHostInBytes_Type=Counter32
_NwIpxFwdIfCtrHostInBytes_Object=MibTableColumn
nwIpxFwdIfCtrHostInBytes=_NwIpxFwdIfCtrHostInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1,21),_NwIpxFwdIfCtrHostInBytes_Type())
nwIpxFwdIfCtrHostInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCtrHostInBytes.setStatus(_A)
_NwIpxFwdIfCtrHostOutBytes_Type=Counter32
_NwIpxFwdIfCtrHostOutBytes_Object=MibTableColumn
nwIpxFwdIfCtrHostOutBytes=_NwIpxFwdIfCtrHostOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1,22),_NwIpxFwdIfCtrHostOutBytes_Type())
nwIpxFwdIfCtrHostOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCtrHostOutBytes.setStatus(_A)
_NwIpxFwdIfCtrHostDiscardBytes_Type=Counter32
_NwIpxFwdIfCtrHostDiscardBytes_Object=MibTableColumn
nwIpxFwdIfCtrHostDiscardBytes=_NwIpxFwdIfCtrHostDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,2,2,2,1,1,23),_NwIpxFwdIfCtrHostDiscardBytes_Type())
nwIpxFwdIfCtrHostDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFwdIfCtrHostDiscardBytes.setStatus(_A)
_NwIpxTopology_ObjectIdentity=ObjectIdentity
nwIpxTopology=_NwIpxTopology_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4))
_NwIpxDistanceVector_ObjectIdentity=ObjectIdentity
nwIpxDistanceVector=_NwIpxDistanceVector_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1))
_NwIpxRip_ObjectIdentity=ObjectIdentity
nwIpxRip=_NwIpxRip_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1))
_NwIpxRipSystem_ObjectIdentity=ObjectIdentity
nwIpxRipSystem=_NwIpxRipSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1))
_NwIpxRipConfig_ObjectIdentity=ObjectIdentity
nwIpxRipConfig=_NwIpxRipConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1,1))
class _NwIpxRipAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxRipAdminStatus_Type.__name__=_C
_NwIpxRipAdminStatus_Object=MibScalar
nwIpxRipAdminStatus=_NwIpxRipAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1,1,1),_NwIpxRipAdminStatus_Type())
nwIpxRipAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipAdminStatus.setStatus(_A)
class _NwIpxRipOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_J,4),(_K,5)))
_NwIpxRipOperStatus_Type.__name__=_C
_NwIpxRipOperStatus_Object=MibScalar
nwIpxRipOperStatus=_NwIpxRipOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1,1,2),_NwIpxRipOperStatus_Type())
nwIpxRipOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipOperStatus.setStatus(_A)
class _NwIpxRipAdminReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpxRipAdminReset_Type.__name__=_C
_NwIpxRipAdminReset_Object=MibScalar
nwIpxRipAdminReset=_NwIpxRipAdminReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1,1,3),_NwIpxRipAdminReset_Type())
nwIpxRipAdminReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipAdminReset.setStatus(_A)
_NwIpxRipOperationalTime_Type=TimeTicks
_NwIpxRipOperationalTime_Object=MibScalar
nwIpxRipOperationalTime=_NwIpxRipOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1,1,4),_NwIpxRipOperationalTime_Type())
nwIpxRipOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipOperationalTime.setStatus(_A)
_NwIpxRipVersion_Type=DisplayString
_NwIpxRipVersion_Object=MibScalar
nwIpxRipVersion=_NwIpxRipVersion_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1,1,5),_NwIpxRipVersion_Type())
nwIpxRipVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipVersion.setStatus(_A)
class _NwIpxRipStackSize_Type(Integer32):defaultValue=4096
_NwIpxRipStackSize_Type.__name__=_C
_NwIpxRipStackSize_Object=MibScalar
nwIpxRipStackSize=_NwIpxRipStackSize_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1,1,6),_NwIpxRipStackSize_Type())
nwIpxRipStackSize.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipStackSize.setStatus(_A)
class _NwIpxRipThreadPriority_Type(Integer32):defaultValue=127
_NwIpxRipThreadPriority_Type.__name__=_C
_NwIpxRipThreadPriority_Object=MibScalar
nwIpxRipThreadPriority=_NwIpxRipThreadPriority_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1,1,7),_NwIpxRipThreadPriority_Type())
nwIpxRipThreadPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipThreadPriority.setStatus(_A)
class _NwIpxRipDatabaseThreshold_Type(Integer32):defaultValue=2000
_NwIpxRipDatabaseThreshold_Type.__name__=_C
_NwIpxRipDatabaseThreshold_Object=MibScalar
nwIpxRipDatabaseThreshold=_NwIpxRipDatabaseThreshold_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1,1,8),_NwIpxRipDatabaseThreshold_Type())
nwIpxRipDatabaseThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipDatabaseThreshold.setStatus(_A)
class _NwIpxRipAgeOut_Type(Integer32):defaultValue=180
_NwIpxRipAgeOut_Type.__name__=_C
_NwIpxRipAgeOut_Object=MibScalar
nwIpxRipAgeOut=_NwIpxRipAgeOut_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1,1,9),_NwIpxRipAgeOut_Type())
nwIpxRipAgeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipAgeOut.setStatus(_A)
class _NwIpxRipHoldDown_Type(Integer32):defaultValue=120
_NwIpxRipHoldDown_Type.__name__=_C
_NwIpxRipHoldDown_Object=MibScalar
nwIpxRipHoldDown=_NwIpxRipHoldDown_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1,1,10),_NwIpxRipHoldDown_Type())
nwIpxRipHoldDown.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipHoldDown.setStatus(_A)
_NwIpxRipCounters_ObjectIdentity=ObjectIdentity
nwIpxRipCounters=_NwIpxRipCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1,2))
class _NwIpxRipCtrAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxRipCtrAdminStatus_Type.__name__=_C
_NwIpxRipCtrAdminStatus_Object=MibScalar
nwIpxRipCtrAdminStatus=_NwIpxRipCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1,2,1),_NwIpxRipCtrAdminStatus_Type())
nwIpxRipCtrAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipCtrAdminStatus.setStatus(_A)
class _NwIpxRipCtrReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpxRipCtrReset_Type.__name__=_C
_NwIpxRipCtrReset_Object=MibScalar
nwIpxRipCtrReset=_NwIpxRipCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1,2,2),_NwIpxRipCtrReset_Type())
nwIpxRipCtrReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipCtrReset.setStatus(_A)
_NwIpxRipCtrOperationalTime_Type=TimeTicks
_NwIpxRipCtrOperationalTime_Object=MibScalar
nwIpxRipCtrOperationalTime=_NwIpxRipCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1,2,3),_NwIpxRipCtrOperationalTime_Type())
nwIpxRipCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipCtrOperationalTime.setStatus(_A)
_NwIpxRipCtrInPkts_Type=Counter32
_NwIpxRipCtrInPkts_Object=MibScalar
nwIpxRipCtrInPkts=_NwIpxRipCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1,2,4),_NwIpxRipCtrInPkts_Type())
nwIpxRipCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipCtrInPkts.setStatus(_A)
_NwIpxRipCtrOutPkts_Type=Counter32
_NwIpxRipCtrOutPkts_Object=MibScalar
nwIpxRipCtrOutPkts=_NwIpxRipCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1,2,5),_NwIpxRipCtrOutPkts_Type())
nwIpxRipCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipCtrOutPkts.setStatus(_A)
_NwIpxRipCtrFilteredPkts_Type=Counter32
_NwIpxRipCtrFilteredPkts_Object=MibScalar
nwIpxRipCtrFilteredPkts=_NwIpxRipCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1,2,6),_NwIpxRipCtrFilteredPkts_Type())
nwIpxRipCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipCtrFilteredPkts.setStatus(_A)
_NwIpxRipCtrDiscardPkts_Type=Counter32
_NwIpxRipCtrDiscardPkts_Object=MibScalar
nwIpxRipCtrDiscardPkts=_NwIpxRipCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1,2,7),_NwIpxRipCtrDiscardPkts_Type())
nwIpxRipCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipCtrDiscardPkts.setStatus(_A)
_NwIpxRipCtrInBytes_Type=Counter32
_NwIpxRipCtrInBytes_Object=MibScalar
nwIpxRipCtrInBytes=_NwIpxRipCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1,2,8),_NwIpxRipCtrInBytes_Type())
nwIpxRipCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipCtrInBytes.setStatus(_A)
_NwIpxRipCtrOutBytes_Type=Counter32
_NwIpxRipCtrOutBytes_Object=MibScalar
nwIpxRipCtrOutBytes=_NwIpxRipCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1,2,9),_NwIpxRipCtrOutBytes_Type())
nwIpxRipCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipCtrOutBytes.setStatus(_A)
_NwIpxRipCtrFilteredBytes_Type=Counter32
_NwIpxRipCtrFilteredBytes_Object=MibScalar
nwIpxRipCtrFilteredBytes=_NwIpxRipCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1,2,10),_NwIpxRipCtrFilteredBytes_Type())
nwIpxRipCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipCtrFilteredBytes.setStatus(_A)
_NwIpxRipCtrDiscardBytes_Type=Counter32
_NwIpxRipCtrDiscardBytes_Object=MibScalar
nwIpxRipCtrDiscardBytes=_NwIpxRipCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,1,2,11),_NwIpxRipCtrDiscardBytes_Type())
nwIpxRipCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipCtrDiscardBytes.setStatus(_A)
_NwIpxRipInterfaces_ObjectIdentity=ObjectIdentity
nwIpxRipInterfaces=_NwIpxRipInterfaces_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2))
_NwIpxRipIfConfig_ObjectIdentity=ObjectIdentity
nwIpxRipIfConfig=_NwIpxRipIfConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,1))
_NwIpxRipIfTable_Object=MibTable
nwIpxRipIfTable=_NwIpxRipIfTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,1,1))
if mibBuilder.loadTexts:nwIpxRipIfTable.setStatus(_A)
_NwIpxRipIfEntry_Object=MibTableRow
nwIpxRipIfEntry=_NwIpxRipIfEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,1,1,1))
nwIpxRipIfEntry.setIndexNames((0,_H,_i))
if mibBuilder.loadTexts:nwIpxRipIfEntry.setStatus(_A)
_NwIpxRipIfIndex_Type=Integer32
_NwIpxRipIfIndex_Object=MibTableColumn
nwIpxRipIfIndex=_NwIpxRipIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,1,1,1,1),_NwIpxRipIfIndex_Type())
nwIpxRipIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipIfIndex.setStatus(_A)
class _NwIpxRipIfAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxRipIfAdminStatus_Type.__name__=_C
_NwIpxRipIfAdminStatus_Object=MibTableColumn
nwIpxRipIfAdminStatus=_NwIpxRipIfAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,1,1,1,2),_NwIpxRipIfAdminStatus_Type())
nwIpxRipIfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipIfAdminStatus.setStatus(_A)
class _NwIpxRipIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_J,4),(_K,5)))
_NwIpxRipIfOperStatus_Type.__name__=_C
_NwIpxRipIfOperStatus_Object=MibTableColumn
nwIpxRipIfOperStatus=_NwIpxRipIfOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,1,1,1,3),_NwIpxRipIfOperStatus_Type())
nwIpxRipIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipIfOperStatus.setStatus(_A)
_NwIpxRipIfOperationalTime_Type=TimeTicks
_NwIpxRipIfOperationalTime_Object=MibTableColumn
nwIpxRipIfOperationalTime=_NwIpxRipIfOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,1,1,1,4),_NwIpxRipIfOperationalTime_Type())
nwIpxRipIfOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipIfOperationalTime.setStatus(_A)
class _NwIpxRipIfVersion_Type(Integer32):defaultValue=1
_NwIpxRipIfVersion_Type.__name__=_C
_NwIpxRipIfVersion_Object=MibTableColumn
nwIpxRipIfVersion=_NwIpxRipIfVersion_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,1,1,1,5),_NwIpxRipIfVersion_Type())
nwIpxRipIfVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipIfVersion.setStatus(_A)
class _NwIpxRipIfAdvertisement_Type(Integer32):defaultValue=60
_NwIpxRipIfAdvertisement_Type.__name__=_C
_NwIpxRipIfAdvertisement_Object=MibTableColumn
nwIpxRipIfAdvertisement=_NwIpxRipIfAdvertisement_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,1,1,1,6),_NwIpxRipIfAdvertisement_Type())
nwIpxRipIfAdvertisement.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipIfAdvertisement.setStatus(_A)
class _NwIpxRipIfFloodDelay_Type(Integer32):defaultValue=2
_NwIpxRipIfFloodDelay_Type.__name__=_C
_NwIpxRipIfFloodDelay_Object=MibTableColumn
nwIpxRipIfFloodDelay=_NwIpxRipIfFloodDelay_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,1,1,1,7),_NwIpxRipIfFloodDelay_Type())
nwIpxRipIfFloodDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipIfFloodDelay.setStatus(_A)
class _NwIpxRipIfRequestDelay_Type(Integer32):defaultValue=6
_NwIpxRipIfRequestDelay_Type.__name__=_C
_NwIpxRipIfRequestDelay_Object=MibTableColumn
nwIpxRipIfRequestDelay=_NwIpxRipIfRequestDelay_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,1,1,1,8),_NwIpxRipIfRequestDelay_Type())
nwIpxRipIfRequestDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipIfRequestDelay.setStatus(_A)
class _NwIpxRipIfPriority_Type(Integer32):defaultValue=1
_NwIpxRipIfPriority_Type.__name__=_C
_NwIpxRipIfPriority_Object=MibTableColumn
nwIpxRipIfPriority=_NwIpxRipIfPriority_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,1,1,1,9),_NwIpxRipIfPriority_Type())
nwIpxRipIfPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipIfPriority.setStatus(_A)
class _NwIpxRipIfHelloTimer_Type(Integer32):defaultValue=10
_NwIpxRipIfHelloTimer_Type.__name__=_C
_NwIpxRipIfHelloTimer_Object=MibTableColumn
nwIpxRipIfHelloTimer=_NwIpxRipIfHelloTimer_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,1,1,1,10),_NwIpxRipIfHelloTimer_Type())
nwIpxRipIfHelloTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipIfHelloTimer.setStatus(_A)
class _NwIpxRipIfSplitHorizon_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxRipIfSplitHorizon_Type.__name__=_C
_NwIpxRipIfSplitHorizon_Object=MibTableColumn
nwIpxRipIfSplitHorizon=_NwIpxRipIfSplitHorizon_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,1,1,1,11),_NwIpxRipIfSplitHorizon_Type())
nwIpxRipIfSplitHorizon.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipIfSplitHorizon.setStatus(_A)
class _NwIpxRipIfPoisonReverse_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxRipIfPoisonReverse_Type.__name__=_C
_NwIpxRipIfPoisonReverse_Object=MibTableColumn
nwIpxRipIfPoisonReverse=_NwIpxRipIfPoisonReverse_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,1,1,1,12),_NwIpxRipIfPoisonReverse_Type())
nwIpxRipIfPoisonReverse.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipIfPoisonReverse.setStatus(_A)
class _NwIpxRipIfSnooping_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxRipIfSnooping_Type.__name__=_C
_NwIpxRipIfSnooping_Object=MibTableColumn
nwIpxRipIfSnooping=_NwIpxRipIfSnooping_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,1,1,1,13),_NwIpxRipIfSnooping_Type())
nwIpxRipIfSnooping.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipIfSnooping.setStatus(_A)
class _NwIpxRipIfType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('bma',2),('nbma',3)))
_NwIpxRipIfType_Type.__name__=_C
_NwIpxRipIfType_Object=MibTableColumn
nwIpxRipIfType=_NwIpxRipIfType_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,1,1,1,14),_NwIpxRipIfType_Type())
nwIpxRipIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipIfType.setStatus(_A)
class _NwIpxRipIfXmitCost_Type(Integer32):defaultValue=0
_NwIpxRipIfXmitCost_Type.__name__=_C
_NwIpxRipIfXmitCost_Object=MibTableColumn
nwIpxRipIfXmitCost=_NwIpxRipIfXmitCost_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,1,1,1,15),_NwIpxRipIfXmitCost_Type())
nwIpxRipIfXmitCost.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipIfXmitCost.setStatus(_A)
class _NwIpxRipIfAclIdentifier_Type(Integer32):defaultValue=0
_NwIpxRipIfAclIdentifier_Type.__name__=_C
_NwIpxRipIfAclIdentifier_Object=MibTableColumn
nwIpxRipIfAclIdentifier=_NwIpxRipIfAclIdentifier_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,1,1,1,16),_NwIpxRipIfAclIdentifier_Type())
nwIpxRipIfAclIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipIfAclIdentifier.setStatus(_A)
class _NwIpxRipIfAclStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxRipIfAclStatus_Type.__name__=_C
_NwIpxRipIfAclStatus_Object=MibTableColumn
nwIpxRipIfAclStatus=_NwIpxRipIfAclStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,1,1,1,17),_NwIpxRipIfAclStatus_Type())
nwIpxRipIfAclStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipIfAclStatus.setStatus(_A)
_NwIpxRipIfCounters_ObjectIdentity=ObjectIdentity
nwIpxRipIfCounters=_NwIpxRipIfCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,2))
_NwIpxRipIfCtrTable_Object=MibTable
nwIpxRipIfCtrTable=_NwIpxRipIfCtrTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,2,1))
if mibBuilder.loadTexts:nwIpxRipIfCtrTable.setStatus(_A)
_NwIpxRipIfCtrEntry_Object=MibTableRow
nwIpxRipIfCtrEntry=_NwIpxRipIfCtrEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,2,1,1))
nwIpxRipIfCtrEntry.setIndexNames((0,_H,_j))
if mibBuilder.loadTexts:nwIpxRipIfCtrEntry.setStatus(_A)
_NwIpxRipIfCtrIfIndex_Type=Integer32
_NwIpxRipIfCtrIfIndex_Object=MibTableColumn
nwIpxRipIfCtrIfIndex=_NwIpxRipIfCtrIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,2,1,1,1),_NwIpxRipIfCtrIfIndex_Type())
nwIpxRipIfCtrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipIfCtrIfIndex.setStatus(_A)
class _NwIpxRipIfCtrAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxRipIfCtrAdminStatus_Type.__name__=_C
_NwIpxRipIfCtrAdminStatus_Object=MibTableColumn
nwIpxRipIfCtrAdminStatus=_NwIpxRipIfCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,2,1,1,2),_NwIpxRipIfCtrAdminStatus_Type())
nwIpxRipIfCtrAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipIfCtrAdminStatus.setStatus(_A)
class _NwIpxRipIfCtrReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpxRipIfCtrReset_Type.__name__=_C
_NwIpxRipIfCtrReset_Object=MibTableColumn
nwIpxRipIfCtrReset=_NwIpxRipIfCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,2,1,1,3),_NwIpxRipIfCtrReset_Type())
nwIpxRipIfCtrReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxRipIfCtrReset.setStatus(_A)
_NwIpxRipIfCtrOperationalTime_Type=TimeTicks
_NwIpxRipIfCtrOperationalTime_Object=MibTableColumn
nwIpxRipIfCtrOperationalTime=_NwIpxRipIfCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,2,1,1,4),_NwIpxRipIfCtrOperationalTime_Type())
nwIpxRipIfCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipIfCtrOperationalTime.setStatus(_A)
_NwIpxRipIfCtrInPkts_Type=Counter32
_NwIpxRipIfCtrInPkts_Object=MibTableColumn
nwIpxRipIfCtrInPkts=_NwIpxRipIfCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,2,1,1,5),_NwIpxRipIfCtrInPkts_Type())
nwIpxRipIfCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipIfCtrInPkts.setStatus(_A)
_NwIpxRipIfCtrOutPkts_Type=Counter32
_NwIpxRipIfCtrOutPkts_Object=MibTableColumn
nwIpxRipIfCtrOutPkts=_NwIpxRipIfCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,2,1,1,6),_NwIpxRipIfCtrOutPkts_Type())
nwIpxRipIfCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipIfCtrOutPkts.setStatus(_A)
_NwIpxRipIfCtrFilteredPkts_Type=Counter32
_NwIpxRipIfCtrFilteredPkts_Object=MibTableColumn
nwIpxRipIfCtrFilteredPkts=_NwIpxRipIfCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,2,1,1,7),_NwIpxRipIfCtrFilteredPkts_Type())
nwIpxRipIfCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipIfCtrFilteredPkts.setStatus(_A)
_NwIpxRipIfCtrDiscardPkts_Type=Counter32
_NwIpxRipIfCtrDiscardPkts_Object=MibTableColumn
nwIpxRipIfCtrDiscardPkts=_NwIpxRipIfCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,2,1,1,8),_NwIpxRipIfCtrDiscardPkts_Type())
nwIpxRipIfCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipIfCtrDiscardPkts.setStatus(_A)
_NwIpxRipIfCtrInBytes_Type=Counter32
_NwIpxRipIfCtrInBytes_Object=MibTableColumn
nwIpxRipIfCtrInBytes=_NwIpxRipIfCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,2,1,1,9),_NwIpxRipIfCtrInBytes_Type())
nwIpxRipIfCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipIfCtrInBytes.setStatus(_A)
_NwIpxRipIfCtrOutBytes_Type=Counter32
_NwIpxRipIfCtrOutBytes_Object=MibTableColumn
nwIpxRipIfCtrOutBytes=_NwIpxRipIfCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,2,1,1,10),_NwIpxRipIfCtrOutBytes_Type())
nwIpxRipIfCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipIfCtrOutBytes.setStatus(_A)
_NwIpxRipIfCtrFilteredBytes_Type=Counter32
_NwIpxRipIfCtrFilteredBytes_Object=MibTableColumn
nwIpxRipIfCtrFilteredBytes=_NwIpxRipIfCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,2,1,1,11),_NwIpxRipIfCtrFilteredBytes_Type())
nwIpxRipIfCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipIfCtrFilteredBytes.setStatus(_A)
_NwIpxRipIfCtrDiscardBytes_Type=Counter32
_NwIpxRipIfCtrDiscardBytes_Object=MibTableColumn
nwIpxRipIfCtrDiscardBytes=_NwIpxRipIfCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,2,2,1,1,12),_NwIpxRipIfCtrDiscardBytes_Type())
nwIpxRipIfCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipIfCtrDiscardBytes.setStatus(_A)
_NwIpxRipDatabase_ObjectIdentity=ObjectIdentity
nwIpxRipDatabase=_NwIpxRipDatabase_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,3))
_NwIpxRipRouteTable_Object=MibTable
nwIpxRipRouteTable=_NwIpxRipRouteTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,3,1))
if mibBuilder.loadTexts:nwIpxRipRouteTable.setStatus(_A)
_NwIpxRipRouteEntry_Object=MibTableRow
nwIpxRipRouteEntry=_NwIpxRipRouteEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,3,1,1))
nwIpxRipRouteEntry.setIndexNames((0,_H,_k),(0,_H,_l),(0,_H,_m))
if mibBuilder.loadTexts:nwIpxRipRouteEntry.setStatus(_A)
_NwIpxRipRtNetId_Type=IpxAddress
_NwIpxRipRtNetId_Object=MibTableColumn
nwIpxRipRtNetId=_NwIpxRipRtNetId_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,3,1,1,1),_NwIpxRipRtNetId_Type())
nwIpxRipRtNetId.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipRtNetId.setStatus(_A)
_NwIpxRipRtIfIndex_Type=Integer32
_NwIpxRipRtIfIndex_Object=MibTableColumn
nwIpxRipRtIfIndex=_NwIpxRipRtIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,3,1,1,2),_NwIpxRipRtIfIndex_Type())
nwIpxRipRtIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipRtIfIndex.setStatus(_A)
_NwIpxRipRtSrcNode_Type=IpxAddress
_NwIpxRipRtSrcNode_Object=MibTableColumn
nwIpxRipRtSrcNode=_NwIpxRipRtSrcNode_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,3,1,1,3),_NwIpxRipRtSrcNode_Type())
nwIpxRipRtSrcNode.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipRtSrcNode.setStatus(_A)
_NwIpxRipRtHops_Type=Integer32
_NwIpxRipRtHops_Object=MibTableColumn
nwIpxRipRtHops=_NwIpxRipRtHops_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,3,1,1,4),_NwIpxRipRtHops_Type())
nwIpxRipRtHops.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipRtHops.setStatus(_A)
_NwIpxRipRtTicks_Type=Integer32
_NwIpxRipRtTicks_Object=MibTableColumn
nwIpxRipRtTicks=_NwIpxRipRtTicks_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,3,1,1,5),_NwIpxRipRtTicks_Type())
nwIpxRipRtTicks.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipRtTicks.setStatus(_A)
_NwIpxRipRtAge_Type=Integer32
_NwIpxRipRtAge_Object=MibTableColumn
nwIpxRipRtAge=_NwIpxRipRtAge_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,3,1,1,6),_NwIpxRipRtAge_Type())
nwIpxRipRtAge.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipRtAge.setStatus(_A)
class _NwIpxRipRtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_M,2),(_P,3),(_Q,4)))
_NwIpxRipRtType_Type.__name__=_C
_NwIpxRipRtType_Object=MibTableColumn
nwIpxRipRtType=_NwIpxRipRtType_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,3,1,1,7),_NwIpxRipRtType_Type())
nwIpxRipRtType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipRtType.setStatus(_A)
_NwIpxRipRtFlags_Type=Integer32
_NwIpxRipRtFlags_Object=MibTableColumn
nwIpxRipRtFlags=_NwIpxRipRtFlags_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,3,1,1,8),_NwIpxRipRtFlags_Type())
nwIpxRipRtFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxRipRtFlags.setStatus(_A)
_NwIpxRipFilters_ObjectIdentity=ObjectIdentity
nwIpxRipFilters=_NwIpxRipFilters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,1,4))
_NwIpxSap_ObjectIdentity=ObjectIdentity
nwIpxSap=_NwIpxSap_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2))
_NwIpxSapSystem_ObjectIdentity=ObjectIdentity
nwIpxSapSystem=_NwIpxSapSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1))
_NwIpxSapConfig_ObjectIdentity=ObjectIdentity
nwIpxSapConfig=_NwIpxSapConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1,1))
class _NwIpxSapAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxSapAdminStatus_Type.__name__=_C
_NwIpxSapAdminStatus_Object=MibScalar
nwIpxSapAdminStatus=_NwIpxSapAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1,1,1),_NwIpxSapAdminStatus_Type())
nwIpxSapAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapAdminStatus.setStatus(_A)
class _NwIpxSapOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_J,4),(_K,5)))
_NwIpxSapOperStatus_Type.__name__=_C
_NwIpxSapOperStatus_Object=MibScalar
nwIpxSapOperStatus=_NwIpxSapOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1,1,2),_NwIpxSapOperStatus_Type())
nwIpxSapOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapOperStatus.setStatus(_A)
class _NwIpxSapAdminReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpxSapAdminReset_Type.__name__=_C
_NwIpxSapAdminReset_Object=MibScalar
nwIpxSapAdminReset=_NwIpxSapAdminReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1,1,3),_NwIpxSapAdminReset_Type())
nwIpxSapAdminReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapAdminReset.setStatus(_A)
_NwIpxSapOperationalTime_Type=TimeTicks
_NwIpxSapOperationalTime_Object=MibScalar
nwIpxSapOperationalTime=_NwIpxSapOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1,1,4),_NwIpxSapOperationalTime_Type())
nwIpxSapOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapOperationalTime.setStatus(_A)
_NwIpxSapVersion_Type=DisplayString
_NwIpxSapVersion_Object=MibScalar
nwIpxSapVersion=_NwIpxSapVersion_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1,1,5),_NwIpxSapVersion_Type())
nwIpxSapVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapVersion.setStatus(_A)
class _NwIpxSapStackSize_Type(Integer32):defaultValue=4096
_NwIpxSapStackSize_Type.__name__=_C
_NwIpxSapStackSize_Object=MibScalar
nwIpxSapStackSize=_NwIpxSapStackSize_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1,1,6),_NwIpxSapStackSize_Type())
nwIpxSapStackSize.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapStackSize.setStatus(_A)
class _NwIpxSapThreadPriority_Type(Integer32):defaultValue=127
_NwIpxSapThreadPriority_Type.__name__=_C
_NwIpxSapThreadPriority_Object=MibScalar
nwIpxSapThreadPriority=_NwIpxSapThreadPriority_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1,1,7),_NwIpxSapThreadPriority_Type())
nwIpxSapThreadPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapThreadPriority.setStatus(_A)
class _NwIpxSapDatabaseThreshold_Type(Integer32):defaultValue=2000
_NwIpxSapDatabaseThreshold_Type.__name__=_C
_NwIpxSapDatabaseThreshold_Object=MibScalar
nwIpxSapDatabaseThreshold=_NwIpxSapDatabaseThreshold_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1,1,8),_NwIpxSapDatabaseThreshold_Type())
nwIpxSapDatabaseThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapDatabaseThreshold.setStatus(_A)
class _NwIpxSapAgeOut_Type(Integer32):defaultValue=180
_NwIpxSapAgeOut_Type.__name__=_C
_NwIpxSapAgeOut_Object=MibScalar
nwIpxSapAgeOut=_NwIpxSapAgeOut_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1,1,9),_NwIpxSapAgeOut_Type())
nwIpxSapAgeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapAgeOut.setStatus(_A)
class _NwIpxSapHoldDown_Type(Integer32):defaultValue=120
_NwIpxSapHoldDown_Type.__name__=_C
_NwIpxSapHoldDown_Object=MibScalar
nwIpxSapHoldDown=_NwIpxSapHoldDown_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1,1,10),_NwIpxSapHoldDown_Type())
nwIpxSapHoldDown.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapHoldDown.setStatus(_A)
_NwIpxSapCounters_ObjectIdentity=ObjectIdentity
nwIpxSapCounters=_NwIpxSapCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1,2))
class _NwIpxSapCtrAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxSapCtrAdminStatus_Type.__name__=_C
_NwIpxSapCtrAdminStatus_Object=MibScalar
nwIpxSapCtrAdminStatus=_NwIpxSapCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1,2,1),_NwIpxSapCtrAdminStatus_Type())
nwIpxSapCtrAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapCtrAdminStatus.setStatus(_A)
class _NwIpxSapCtrReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpxSapCtrReset_Type.__name__=_C
_NwIpxSapCtrReset_Object=MibScalar
nwIpxSapCtrReset=_NwIpxSapCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1,2,2),_NwIpxSapCtrReset_Type())
nwIpxSapCtrReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapCtrReset.setStatus(_A)
_NwIpxSapCtrOperationalTime_Type=TimeTicks
_NwIpxSapCtrOperationalTime_Object=MibScalar
nwIpxSapCtrOperationalTime=_NwIpxSapCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1,2,3),_NwIpxSapCtrOperationalTime_Type())
nwIpxSapCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapCtrOperationalTime.setStatus(_A)
_NwIpxSapCtrInPkts_Type=Counter32
_NwIpxSapCtrInPkts_Object=MibScalar
nwIpxSapCtrInPkts=_NwIpxSapCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1,2,4),_NwIpxSapCtrInPkts_Type())
nwIpxSapCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapCtrInPkts.setStatus(_A)
_NwIpxSapCtrOutPkts_Type=Counter32
_NwIpxSapCtrOutPkts_Object=MibScalar
nwIpxSapCtrOutPkts=_NwIpxSapCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1,2,5),_NwIpxSapCtrOutPkts_Type())
nwIpxSapCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapCtrOutPkts.setStatus(_A)
_NwIpxSapCtrFilteredPkts_Type=Counter32
_NwIpxSapCtrFilteredPkts_Object=MibScalar
nwIpxSapCtrFilteredPkts=_NwIpxSapCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1,2,6),_NwIpxSapCtrFilteredPkts_Type())
nwIpxSapCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapCtrFilteredPkts.setStatus(_A)
_NwIpxSapCtrDiscardPkts_Type=Counter32
_NwIpxSapCtrDiscardPkts_Object=MibScalar
nwIpxSapCtrDiscardPkts=_NwIpxSapCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1,2,7),_NwIpxSapCtrDiscardPkts_Type())
nwIpxSapCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapCtrDiscardPkts.setStatus(_A)
_NwIpxSapCtrInBytes_Type=Counter32
_NwIpxSapCtrInBytes_Object=MibScalar
nwIpxSapCtrInBytes=_NwIpxSapCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1,2,8),_NwIpxSapCtrInBytes_Type())
nwIpxSapCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapCtrInBytes.setStatus(_A)
_NwIpxSapCtrOutBytes_Type=Counter32
_NwIpxSapCtrOutBytes_Object=MibScalar
nwIpxSapCtrOutBytes=_NwIpxSapCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1,2,9),_NwIpxSapCtrOutBytes_Type())
nwIpxSapCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapCtrOutBytes.setStatus(_A)
_NwIpxSapCtrFilteredBytes_Type=Counter32
_NwIpxSapCtrFilteredBytes_Object=MibScalar
nwIpxSapCtrFilteredBytes=_NwIpxSapCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1,2,10),_NwIpxSapCtrFilteredBytes_Type())
nwIpxSapCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapCtrFilteredBytes.setStatus(_A)
_NwIpxSapCtrDiscardBytes_Type=Counter32
_NwIpxSapCtrDiscardBytes_Object=MibScalar
nwIpxSapCtrDiscardBytes=_NwIpxSapCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,1,2,11),_NwIpxSapCtrDiscardBytes_Type())
nwIpxSapCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapCtrDiscardBytes.setStatus(_A)
_NwIpxSapInterfaces_ObjectIdentity=ObjectIdentity
nwIpxSapInterfaces=_NwIpxSapInterfaces_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2))
_NwIpxSapIfConfig_ObjectIdentity=ObjectIdentity
nwIpxSapIfConfig=_NwIpxSapIfConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,1))
_NwIpxSapIfTable_Object=MibTable
nwIpxSapIfTable=_NwIpxSapIfTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,1,1))
if mibBuilder.loadTexts:nwIpxSapIfTable.setStatus(_A)
_NwIpxSapIfEntry_Object=MibTableRow
nwIpxSapIfEntry=_NwIpxSapIfEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,1,1,1))
nwIpxSapIfEntry.setIndexNames((0,_H,_n))
if mibBuilder.loadTexts:nwIpxSapIfEntry.setStatus(_A)
_NwIpxSapIfIndex_Type=Integer32
_NwIpxSapIfIndex_Object=MibTableColumn
nwIpxSapIfIndex=_NwIpxSapIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,1,1,1,1),_NwIpxSapIfIndex_Type())
nwIpxSapIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapIfIndex.setStatus(_A)
class _NwIpxSapIfAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxSapIfAdminStatus_Type.__name__=_C
_NwIpxSapIfAdminStatus_Object=MibTableColumn
nwIpxSapIfAdminStatus=_NwIpxSapIfAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,1,1,1,2),_NwIpxSapIfAdminStatus_Type())
nwIpxSapIfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapIfAdminStatus.setStatus(_A)
class _NwIpxSapIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_J,4),(_K,5)))
_NwIpxSapIfOperStatus_Type.__name__=_C
_NwIpxSapIfOperStatus_Object=MibTableColumn
nwIpxSapIfOperStatus=_NwIpxSapIfOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,1,1,1,3),_NwIpxSapIfOperStatus_Type())
nwIpxSapIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapIfOperStatus.setStatus(_A)
_NwIpxSapIfOperationalTime_Type=TimeTicks
_NwIpxSapIfOperationalTime_Object=MibTableColumn
nwIpxSapIfOperationalTime=_NwIpxSapIfOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,1,1,1,4),_NwIpxSapIfOperationalTime_Type())
nwIpxSapIfOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapIfOperationalTime.setStatus(_A)
class _NwIpxSapIfVersion_Type(Integer32):defaultValue=1
_NwIpxSapIfVersion_Type.__name__=_C
_NwIpxSapIfVersion_Object=MibTableColumn
nwIpxSapIfVersion=_NwIpxSapIfVersion_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,1,1,1,5),_NwIpxSapIfVersion_Type())
nwIpxSapIfVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapIfVersion.setStatus(_A)
class _NwIpxSapIfAdvertisement_Type(Integer32):defaultValue=60
_NwIpxSapIfAdvertisement_Type.__name__=_C
_NwIpxSapIfAdvertisement_Object=MibTableColumn
nwIpxSapIfAdvertisement=_NwIpxSapIfAdvertisement_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,1,1,1,6),_NwIpxSapIfAdvertisement_Type())
nwIpxSapIfAdvertisement.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapIfAdvertisement.setStatus(_A)
class _NwIpxSapIfFloodDelay_Type(Integer32):defaultValue=2
_NwIpxSapIfFloodDelay_Type.__name__=_C
_NwIpxSapIfFloodDelay_Object=MibTableColumn
nwIpxSapIfFloodDelay=_NwIpxSapIfFloodDelay_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,1,1,1,7),_NwIpxSapIfFloodDelay_Type())
nwIpxSapIfFloodDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapIfFloodDelay.setStatus(_A)
class _NwIpxSapIfRequestDelay_Type(Integer32):defaultValue=0
_NwIpxSapIfRequestDelay_Type.__name__=_C
_NwIpxSapIfRequestDelay_Object=MibTableColumn
nwIpxSapIfRequestDelay=_NwIpxSapIfRequestDelay_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,1,1,1,8),_NwIpxSapIfRequestDelay_Type())
nwIpxSapIfRequestDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapIfRequestDelay.setStatus(_A)
class _NwIpxSapIfPriority_Type(Integer32):defaultValue=1
_NwIpxSapIfPriority_Type.__name__=_C
_NwIpxSapIfPriority_Object=MibTableColumn
nwIpxSapIfPriority=_NwIpxSapIfPriority_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,1,1,1,9),_NwIpxSapIfPriority_Type())
nwIpxSapIfPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapIfPriority.setStatus(_A)
class _NwIpxSapIfHelloTimer_Type(Integer32):defaultValue=10
_NwIpxSapIfHelloTimer_Type.__name__=_C
_NwIpxSapIfHelloTimer_Object=MibTableColumn
nwIpxSapIfHelloTimer=_NwIpxSapIfHelloTimer_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,1,1,1,10),_NwIpxSapIfHelloTimer_Type())
nwIpxSapIfHelloTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapIfHelloTimer.setStatus(_A)
class _NwIpxSapIfSplitHorizon_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxSapIfSplitHorizon_Type.__name__=_C
_NwIpxSapIfSplitHorizon_Object=MibTableColumn
nwIpxSapIfSplitHorizon=_NwIpxSapIfSplitHorizon_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,1,1,1,11),_NwIpxSapIfSplitHorizon_Type())
nwIpxSapIfSplitHorizon.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapIfSplitHorizon.setStatus(_A)
class _NwIpxSapIfPoisonReverse_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxSapIfPoisonReverse_Type.__name__=_C
_NwIpxSapIfPoisonReverse_Object=MibTableColumn
nwIpxSapIfPoisonReverse=_NwIpxSapIfPoisonReverse_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,1,1,1,12),_NwIpxSapIfPoisonReverse_Type())
nwIpxSapIfPoisonReverse.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapIfPoisonReverse.setStatus(_A)
class _NwIpxSapIfSnooping_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxSapIfSnooping_Type.__name__=_C
_NwIpxSapIfSnooping_Object=MibTableColumn
nwIpxSapIfSnooping=_NwIpxSapIfSnooping_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,1,1,1,13),_NwIpxSapIfSnooping_Type())
nwIpxSapIfSnooping.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapIfSnooping.setStatus(_A)
class _NwIpxSapIfType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('bma',2),('nbma',3)))
_NwIpxSapIfType_Type.__name__=_C
_NwIpxSapIfType_Object=MibTableColumn
nwIpxSapIfType=_NwIpxSapIfType_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,1,1,1,14),_NwIpxSapIfType_Type())
nwIpxSapIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapIfType.setStatus(_A)
class _NwIpxSapIfXmitCost_Type(Integer32):defaultValue=0
_NwIpxSapIfXmitCost_Type.__name__=_C
_NwIpxSapIfXmitCost_Object=MibTableColumn
nwIpxSapIfXmitCost=_NwIpxSapIfXmitCost_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,1,1,1,15),_NwIpxSapIfXmitCost_Type())
nwIpxSapIfXmitCost.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapIfXmitCost.setStatus(_A)
class _NwIpxSapIfAclIdentifier_Type(Integer32):defaultValue=0
_NwIpxSapIfAclIdentifier_Type.__name__=_C
_NwIpxSapIfAclIdentifier_Object=MibTableColumn
nwIpxSapIfAclIdentifier=_NwIpxSapIfAclIdentifier_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,1,1,1,16),_NwIpxSapIfAclIdentifier_Type())
nwIpxSapIfAclIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapIfAclIdentifier.setStatus(_A)
class _NwIpxSapIfAclStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxSapIfAclStatus_Type.__name__=_C
_NwIpxSapIfAclStatus_Object=MibTableColumn
nwIpxSapIfAclStatus=_NwIpxSapIfAclStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,1,1,1,17),_NwIpxSapIfAclStatus_Type())
nwIpxSapIfAclStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapIfAclStatus.setStatus(_A)
_NwIpxSapIfCounters_ObjectIdentity=ObjectIdentity
nwIpxSapIfCounters=_NwIpxSapIfCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,2))
_NwIpxSapIfCtrTable_Object=MibTable
nwIpxSapIfCtrTable=_NwIpxSapIfCtrTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,2,1))
if mibBuilder.loadTexts:nwIpxSapIfCtrTable.setStatus(_A)
_NwIpxSapIfCtrEntry_Object=MibTableRow
nwIpxSapIfCtrEntry=_NwIpxSapIfCtrEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,2,1,1))
nwIpxSapIfCtrEntry.setIndexNames((0,_H,_o))
if mibBuilder.loadTexts:nwIpxSapIfCtrEntry.setStatus(_A)
_NwIpxSapIfCtrIfIndex_Type=Integer32
_NwIpxSapIfCtrIfIndex_Object=MibTableColumn
nwIpxSapIfCtrIfIndex=_NwIpxSapIfCtrIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,2,1,1,1),_NwIpxSapIfCtrIfIndex_Type())
nwIpxSapIfCtrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapIfCtrIfIndex.setStatus(_A)
class _NwIpxSapIfCtrAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxSapIfCtrAdminStatus_Type.__name__=_C
_NwIpxSapIfCtrAdminStatus_Object=MibTableColumn
nwIpxSapIfCtrAdminStatus=_NwIpxSapIfCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,2,1,1,2),_NwIpxSapIfCtrAdminStatus_Type())
nwIpxSapIfCtrAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapIfCtrAdminStatus.setStatus(_A)
class _NwIpxSapIfCtrReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpxSapIfCtrReset_Type.__name__=_C
_NwIpxSapIfCtrReset_Object=MibTableColumn
nwIpxSapIfCtrReset=_NwIpxSapIfCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,2,1,1,3),_NwIpxSapIfCtrReset_Type())
nwIpxSapIfCtrReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxSapIfCtrReset.setStatus(_A)
_NwIpxSapIfCtrOperationalTime_Type=TimeTicks
_NwIpxSapIfCtrOperationalTime_Object=MibTableColumn
nwIpxSapIfCtrOperationalTime=_NwIpxSapIfCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,2,1,1,4),_NwIpxSapIfCtrOperationalTime_Type())
nwIpxSapIfCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapIfCtrOperationalTime.setStatus(_A)
_NwIpxSapIfCtrInPkts_Type=Counter32
_NwIpxSapIfCtrInPkts_Object=MibTableColumn
nwIpxSapIfCtrInPkts=_NwIpxSapIfCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,2,1,1,5),_NwIpxSapIfCtrInPkts_Type())
nwIpxSapIfCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapIfCtrInPkts.setStatus(_A)
_NwIpxSapIfCtrOutPkts_Type=Counter32
_NwIpxSapIfCtrOutPkts_Object=MibTableColumn
nwIpxSapIfCtrOutPkts=_NwIpxSapIfCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,2,1,1,6),_NwIpxSapIfCtrOutPkts_Type())
nwIpxSapIfCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapIfCtrOutPkts.setStatus(_A)
_NwIpxSapIfCtrFilteredPkts_Type=Counter32
_NwIpxSapIfCtrFilteredPkts_Object=MibTableColumn
nwIpxSapIfCtrFilteredPkts=_NwIpxSapIfCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,2,1,1,7),_NwIpxSapIfCtrFilteredPkts_Type())
nwIpxSapIfCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapIfCtrFilteredPkts.setStatus(_A)
_NwIpxSapIfCtrDiscardPkts_Type=Counter32
_NwIpxSapIfCtrDiscardPkts_Object=MibTableColumn
nwIpxSapIfCtrDiscardPkts=_NwIpxSapIfCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,2,1,1,8),_NwIpxSapIfCtrDiscardPkts_Type())
nwIpxSapIfCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapIfCtrDiscardPkts.setStatus(_A)
_NwIpxSapIfCtrInBytes_Type=Counter32
_NwIpxSapIfCtrInBytes_Object=MibTableColumn
nwIpxSapIfCtrInBytes=_NwIpxSapIfCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,2,1,1,9),_NwIpxSapIfCtrInBytes_Type())
nwIpxSapIfCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapIfCtrInBytes.setStatus(_A)
_NwIpxSapIfCtrOutBytes_Type=Counter32
_NwIpxSapIfCtrOutBytes_Object=MibTableColumn
nwIpxSapIfCtrOutBytes=_NwIpxSapIfCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,2,1,1,10),_NwIpxSapIfCtrOutBytes_Type())
nwIpxSapIfCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapIfCtrOutBytes.setStatus(_A)
_NwIpxSapIfCtrFilteredBytes_Type=Counter32
_NwIpxSapIfCtrFilteredBytes_Object=MibTableColumn
nwIpxSapIfCtrFilteredBytes=_NwIpxSapIfCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,2,1,1,11),_NwIpxSapIfCtrFilteredBytes_Type())
nwIpxSapIfCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapIfCtrFilteredBytes.setStatus(_A)
_NwIpxSapIfCtrDiscardBytes_Type=Counter32
_NwIpxSapIfCtrDiscardBytes_Object=MibTableColumn
nwIpxSapIfCtrDiscardBytes=_NwIpxSapIfCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,2,2,1,1,12),_NwIpxSapIfCtrDiscardBytes_Type())
nwIpxSapIfCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapIfCtrDiscardBytes.setStatus(_A)
_NwIpxSapServerTable_ObjectIdentity=ObjectIdentity
nwIpxSapServerTable=_NwIpxSapServerTable_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,3))
_NwIpxSapServerIfTable_Object=MibTable
nwIpxSapServerIfTable=_NwIpxSapServerIfTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,3,1))
if mibBuilder.loadTexts:nwIpxSapServerIfTable.setStatus(_A)
_NwIpxSapServerIfEntry_Object=MibTableRow
nwIpxSapServerIfEntry=_NwIpxSapServerIfEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,3,1,1))
nwIpxSapServerIfEntry.setIndexNames((0,_H,_p),(0,_H,_q),(0,_H,_r),(0,_H,_s),(0,_H,_t),(0,_H,_u))
if mibBuilder.loadTexts:nwIpxSapServerIfEntry.setStatus(_A)
_NwIpxSapServerIfNetId_Type=IpxAddress
_NwIpxSapServerIfNetId_Object=MibTableColumn
nwIpxSapServerIfNetId=_NwIpxSapServerIfNetId_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,3,1,1,1),_NwIpxSapServerIfNetId_Type())
nwIpxSapServerIfNetId.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapServerIfNetId.setStatus(_A)
_NwIpxSapServerIfNode_Type=OctetString
_NwIpxSapServerIfNode_Object=MibTableColumn
nwIpxSapServerIfNode=_NwIpxSapServerIfNode_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,3,1,1,2),_NwIpxSapServerIfNode_Type())
nwIpxSapServerIfNode.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapServerIfNode.setStatus(_A)
_NwIpxSapServerIfSocket_Type=OctetString
_NwIpxSapServerIfSocket_Object=MibTableColumn
nwIpxSapServerIfSocket=_NwIpxSapServerIfSocket_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,3,1,1,3),_NwIpxSapServerIfSocket_Type())
nwIpxSapServerIfSocket.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapServerIfSocket.setStatus(_A)
_NwIpxSapServerIfServiceType_Type=Integer32
_NwIpxSapServerIfServiceType_Object=MibTableColumn
nwIpxSapServerIfServiceType=_NwIpxSapServerIfServiceType_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,3,1,1,4),_NwIpxSapServerIfServiceType_Type())
nwIpxSapServerIfServiceType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapServerIfServiceType.setStatus(_A)
_NwIpxSapServerIfIfNum_Type=Integer32
_NwIpxSapServerIfIfNum_Object=MibTableColumn
nwIpxSapServerIfIfNum=_NwIpxSapServerIfIfNum_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,3,1,1,5),_NwIpxSapServerIfIfNum_Type())
nwIpxSapServerIfIfNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapServerIfIfNum.setStatus(_A)
_NwIpxSapServerIfSrcNode_Type=OctetString
_NwIpxSapServerIfSrcNode_Object=MibTableColumn
nwIpxSapServerIfSrcNode=_NwIpxSapServerIfSrcNode_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,3,1,1,6),_NwIpxSapServerIfSrcNode_Type())
nwIpxSapServerIfSrcNode.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapServerIfSrcNode.setStatus(_A)
_NwIpxSapServerIfName_Type=OctetString
_NwIpxSapServerIfName_Object=MibTableColumn
nwIpxSapServerIfName=_NwIpxSapServerIfName_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,3,1,1,7),_NwIpxSapServerIfName_Type())
nwIpxSapServerIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapServerIfName.setStatus(_A)
_NwIpxSapServerIfHops_Type=Integer32
_NwIpxSapServerIfHops_Object=MibTableColumn
nwIpxSapServerIfHops=_NwIpxSapServerIfHops_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,3,1,1,8),_NwIpxSapServerIfHops_Type())
nwIpxSapServerIfHops.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapServerIfHops.setStatus(_A)
_NwIpxSapServerIfAge_Type=Integer32
_NwIpxSapServerIfAge_Object=MibTableColumn
nwIpxSapServerIfAge=_NwIpxSapServerIfAge_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,3,1,1,9),_NwIpxSapServerIfAge_Type())
nwIpxSapServerIfAge.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapServerIfAge.setStatus(_A)
class _NwIpxSapServerIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_M,2),(_P,3),(_Q,4)))
_NwIpxSapServerIfType_Type.__name__=_C
_NwIpxSapServerIfType_Object=MibTableColumn
nwIpxSapServerIfType=_NwIpxSapServerIfType_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,3,1,1,10),_NwIpxSapServerIfType_Type())
nwIpxSapServerIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapServerIfType.setStatus(_A)
_NwIpxSapServerIfFlags_Type=Integer32
_NwIpxSapServerIfFlags_Object=MibTableColumn
nwIpxSapServerIfFlags=_NwIpxSapServerIfFlags_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,3,1,1,11),_NwIpxSapServerIfFlags_Type())
nwIpxSapServerIfFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxSapServerIfFlags.setStatus(_A)
_NwIpxSapFilters_ObjectIdentity=ObjectIdentity
nwIpxSapFilters=_NwIpxSapFilters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,1,2,4))
_NwIpxLinkState_ObjectIdentity=ObjectIdentity
nwIpxLinkState=_NwIpxLinkState_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,2))
_NwIpxNlsp_ObjectIdentity=ObjectIdentity
nwIpxNlsp=_NwIpxNlsp_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,4,2,1))
_NwIpxFib_ObjectIdentity=ObjectIdentity
nwIpxFib=_NwIpxFib_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,5))
_NwIpxFibTable_Object=MibTable
nwIpxFibTable=_NwIpxFibTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,5,1))
if mibBuilder.loadTexts:nwIpxFibTable.setStatus(_A)
_NwIpxFibEntry_Object=MibTableRow
nwIpxFibEntry=_NwIpxFibEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,5,1,1))
nwIpxFibEntry.setIndexNames((0,_H,_v))
if mibBuilder.loadTexts:nwIpxFibEntry.setStatus(_A)
_NwIpxFibNetId_Type=IpxAddress
_NwIpxFibNetId_Object=MibTableColumn
nwIpxFibNetId=_NwIpxFibNetId_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,5,1,1,1),_NwIpxFibNetId_Type())
nwIpxFibNetId.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxFibNetId.setStatus(_A)
class _NwIpxFibHops_Type(Integer32):defaultValue=0
_NwIpxFibHops_Type.__name__=_C
_NwIpxFibHops_Object=MibTableColumn
nwIpxFibHops=_NwIpxFibHops_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,5,1,1,2),_NwIpxFibHops_Type())
nwIpxFibHops.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxFibHops.setStatus(_A)
class _NwIpxFibTimeTicks_Type(TimeTicks):defaultValue=0
_NwIpxFibTimeTicks_Type.__name__=_R
_NwIpxFibTimeTicks_Object=MibTableColumn
nwIpxFibTimeTicks=_NwIpxFibTimeTicks_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,5,1,1,3),_NwIpxFibTimeTicks_Type())
nwIpxFibTimeTicks.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxFibTimeTicks.setStatus(_A)
_NwIpxFibNextHopIf_Type=Integer32
_NwIpxFibNextHopIf_Object=MibTableColumn
nwIpxFibNextHopIf=_NwIpxFibNextHopIf_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,5,1,1,4),_NwIpxFibNextHopIf_Type())
nwIpxFibNextHopIf.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxFibNextHopIf.setStatus(_A)
_NwIpxFibNextHopNet_Type=OctetString
_NwIpxFibNextHopNet_Object=MibTableColumn
nwIpxFibNextHopNet=_NwIpxFibNextHopNet_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,5,1,1,5),_NwIpxFibNextHopNet_Type())
nwIpxFibNextHopNet.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxFibNextHopNet.setStatus(_A)
_NwIpxFibNextHopNode_Type=MacAddress
_NwIpxFibNextHopNode_Object=MibTableColumn
nwIpxFibNextHopNode=_NwIpxFibNextHopNode_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,5,1,1,6),_NwIpxFibNextHopNode_Type())
nwIpxFibNextHopNode.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxFibNextHopNode.setStatus(_A)
class _NwIpxFibRouteType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_M,2),(_P,3),(_Q,4)))
_NwIpxFibRouteType_Type.__name__=_C
_NwIpxFibRouteType_Object=MibTableColumn
nwIpxFibRouteType=_NwIpxFibRouteType_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,5,1,1,7),_NwIpxFibRouteType_Type())
nwIpxFibRouteType.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxFibRouteType.setStatus(_A)
_NwIpxEndSystems_ObjectIdentity=ObjectIdentity
nwIpxEndSystems=_NwIpxEndSystems_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,6))
_NwIpxHostsSystem_ObjectIdentity=ObjectIdentity
nwIpxHostsSystem=_NwIpxHostsSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,6,1))
_NwIpxHostsInterfaces_ObjectIdentity=ObjectIdentity
nwIpxHostsInterfaces=_NwIpxHostsInterfaces_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,6,2))
_NwIpxHostsToMedia_ObjectIdentity=ObjectIdentity
nwIpxHostsToMedia=_NwIpxHostsToMedia_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,6,3))
_NwIpxHostMapTable_Object=MibTable
nwIpxHostMapTable=_NwIpxHostMapTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,6,3,1))
if mibBuilder.loadTexts:nwIpxHostMapTable.setStatus(_A)
_NwIpxHostMapEntry_Object=MibTableRow
nwIpxHostMapEntry=_NwIpxHostMapEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,6,3,1,1))
nwIpxHostMapEntry.setIndexNames((0,_H,_w),(0,_H,_x))
if mibBuilder.loadTexts:nwIpxHostMapEntry.setStatus(_A)
_NwIpxHostMapIfIndex_Type=Integer32
_NwIpxHostMapIfIndex_Object=MibTableColumn
nwIpxHostMapIfIndex=_NwIpxHostMapIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,6,3,1,1,1),_NwIpxHostMapIfIndex_Type())
nwIpxHostMapIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxHostMapIfIndex.setStatus(_A)
_NwIpxHostMapIpxAddr_Type=IpxAddress
_NwIpxHostMapIpxAddr_Object=MibTableColumn
nwIpxHostMapIpxAddr=_NwIpxHostMapIpxAddr_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,6,3,1,1,2),_NwIpxHostMapIpxAddr_Type())
nwIpxHostMapIpxAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxHostMapIpxAddr.setStatus(_A)
_NwIpxHostMapPhysAddr_Type=PhysAddress
_NwIpxHostMapPhysAddr_Object=MibTableColumn
nwIpxHostMapPhysAddr=_NwIpxHostMapPhysAddr_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,6,3,1,1,3),_NwIpxHostMapPhysAddr_Type())
nwIpxHostMapPhysAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxHostMapPhysAddr.setStatus(_A)
class _NwIpxHostMapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_M,2),('dynamic',3),('static',4),('inactive',5)))
_NwIpxHostMapType_Type.__name__=_C
_NwIpxHostMapType_Object=MibTableColumn
nwIpxHostMapType=_NwIpxHostMapType_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,6,3,1,1,4),_NwIpxHostMapType_Type())
nwIpxHostMapType.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxHostMapType.setStatus(_A)
_NwIpxHostMapCircuitID_Type=Integer32
_NwIpxHostMapCircuitID_Object=MibTableColumn
nwIpxHostMapCircuitID=_NwIpxHostMapCircuitID_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,6,3,1,1,5),_NwIpxHostMapCircuitID_Type())
nwIpxHostMapCircuitID.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxHostMapCircuitID.setStatus(_A)
class _NwIpxHostMapFraming_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,6,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*((_E,1),(_T,2),('snap',3),('i8022',4),(_U,6),(_V,8),(_W,9),(_X,10),(_Y,11),(_Z,12),(_a,13),(_b,14),(_c,15),(_d,16),(_e,17)))
_NwIpxHostMapFraming_Type.__name__=_C
_NwIpxHostMapFraming_Object=MibTableColumn
nwIpxHostMapFraming=_NwIpxHostMapFraming_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,6,3,1,1,6),_NwIpxHostMapFraming_Type())
nwIpxHostMapFraming.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxHostMapFraming.setStatus(_A)
_NwIpxHostMapPortNumber_Type=Integer32
_NwIpxHostMapPortNumber_Object=MibTableColumn
nwIpxHostMapPortNumber=_NwIpxHostMapPortNumber_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,6,3,1,1,7),_NwIpxHostMapPortNumber_Type())
nwIpxHostMapPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxHostMapPortNumber.setStatus(_A)
_NwIpxAccessControl_ObjectIdentity=ObjectIdentity
nwIpxAccessControl=_NwIpxAccessControl_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,7))
_NwIpxAclValidEntries_Type=Gauge32
_NwIpxAclValidEntries_Object=MibScalar
nwIpxAclValidEntries=_NwIpxAclValidEntries_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,7,1),_NwIpxAclValidEntries_Type())
nwIpxAclValidEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxAclValidEntries.setStatus(_A)
_NwIpxAclTable_Object=MibTable
nwIpxAclTable=_NwIpxAclTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,7,2))
if mibBuilder.loadTexts:nwIpxAclTable.setStatus(_A)
_NwIpxAclEntry_Object=MibTableRow
nwIpxAclEntry=_NwIpxAclEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,7,2,1))
nwIpxAclEntry.setIndexNames((0,_H,_y),(0,_H,_z))
if mibBuilder.loadTexts:nwIpxAclEntry.setStatus(_A)
_NwIpxAclIdentifier_Type=Integer32
_NwIpxAclIdentifier_Object=MibTableColumn
nwIpxAclIdentifier=_NwIpxAclIdentifier_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,7,2,1,1),_NwIpxAclIdentifier_Type())
nwIpxAclIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxAclIdentifier.setStatus(_A)
_NwIpxAclSequence_Type=Integer32
_NwIpxAclSequence_Object=MibTableColumn
nwIpxAclSequence=_NwIpxAclSequence_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,7,2,1,2),_NwIpxAclSequence_Type())
nwIpxAclSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxAclSequence.setStatus(_A)
class _NwIpxAclPermission_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_M,2),('permit',3),('deny',4),('permit-bidirectional',5),('deny-bidirectional',6)))
_NwIpxAclPermission_Type.__name__=_C
_NwIpxAclPermission_Object=MibTableColumn
nwIpxAclPermission=_NwIpxAclPermission_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,7,2,1,3),_NwIpxAclPermission_Type())
nwIpxAclPermission.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxAclPermission.setStatus(_A)
_NwIpxAclMatches_Type=Counter32
_NwIpxAclMatches_Object=MibTableColumn
nwIpxAclMatches=_NwIpxAclMatches_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,7,2,1,4),_NwIpxAclMatches_Type())
nwIpxAclMatches.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxAclMatches.setStatus(_A)
_NwIpxAclDestNetNum_Type=OctetString
_NwIpxAclDestNetNum_Object=MibTableColumn
nwIpxAclDestNetNum=_NwIpxAclDestNetNum_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,7,2,1,5),_NwIpxAclDestNetNum_Type())
nwIpxAclDestNetNum.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxAclDestNetNum.setStatus(_A)
_NwIpxAclDestNode_Type=OctetString
_NwIpxAclDestNode_Object=MibTableColumn
nwIpxAclDestNode=_NwIpxAclDestNode_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,7,2,1,6),_NwIpxAclDestNode_Type())
nwIpxAclDestNode.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxAclDestNode.setStatus(_A)
_NwIpxAclDestSocket_Type=OctetString
_NwIpxAclDestSocket_Object=MibTableColumn
nwIpxAclDestSocket=_NwIpxAclDestSocket_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,7,2,1,7),_NwIpxAclDestSocket_Type())
nwIpxAclDestSocket.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxAclDestSocket.setStatus(_A)
_NwIpxAclSrcNetNum_Type=OctetString
_NwIpxAclSrcNetNum_Object=MibTableColumn
nwIpxAclSrcNetNum=_NwIpxAclSrcNetNum_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,7,2,1,8),_NwIpxAclSrcNetNum_Type())
nwIpxAclSrcNetNum.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxAclSrcNetNum.setStatus(_A)
_NwIpxAclSrcNode_Type=OctetString
_NwIpxAclSrcNode_Object=MibTableColumn
nwIpxAclSrcNode=_NwIpxAclSrcNode_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,7,2,1,9),_NwIpxAclSrcNode_Type())
nwIpxAclSrcNode.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxAclSrcNode.setStatus(_A)
_NwIpxAclSrcSocket_Type=OctetString
_NwIpxAclSrcSocket_Object=MibTableColumn
nwIpxAclSrcSocket=_NwIpxAclSrcSocket_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,7,2,1,10),_NwIpxAclSrcSocket_Type())
nwIpxAclSrcSocket.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxAclSrcSocket.setStatus(_A)
_NwIpxFilters_ObjectIdentity=ObjectIdentity
nwIpxFilters=_NwIpxFilters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,8))
_NwIpxRedirector_ObjectIdentity=ObjectIdentity
nwIpxRedirector=_NwIpxRedirector_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9))
_NwIpxNetBIOS_ObjectIdentity=ObjectIdentity
nwIpxNetBIOS=_NwIpxNetBIOS_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1))
_NwIpxNetBIOSSystem_ObjectIdentity=ObjectIdentity
nwIpxNetBIOSSystem=_NwIpxNetBIOSSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,1))
_NwIpxNetBIOSConfig_ObjectIdentity=ObjectIdentity
nwIpxNetBIOSConfig=_NwIpxNetBIOSConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,1,1))
class _NwIpxNetBIOSAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxNetBIOSAdminStatus_Type.__name__=_C
_NwIpxNetBIOSAdminStatus_Object=MibScalar
nwIpxNetBIOSAdminStatus=_NwIpxNetBIOSAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,1,1,1),_NwIpxNetBIOSAdminStatus_Type())
nwIpxNetBIOSAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxNetBIOSAdminStatus.setStatus(_A)
class _NwIpxNetBIOSOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_J,4),(_K,5),(_L,6)))
_NwIpxNetBIOSOperStatus_Type.__name__=_C
_NwIpxNetBIOSOperStatus_Object=MibScalar
nwIpxNetBIOSOperStatus=_NwIpxNetBIOSOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,1,1,2),_NwIpxNetBIOSOperStatus_Type())
nwIpxNetBIOSOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSOperStatus.setStatus(_A)
class _NwIpxNetBIOSAdminReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpxNetBIOSAdminReset_Type.__name__=_C
_NwIpxNetBIOSAdminReset_Object=MibScalar
nwIpxNetBIOSAdminReset=_NwIpxNetBIOSAdminReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,1,1,3),_NwIpxNetBIOSAdminReset_Type())
nwIpxNetBIOSAdminReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxNetBIOSAdminReset.setStatus(_A)
_NwIpxNetBIOSOperationalTime_Type=TimeTicks
_NwIpxNetBIOSOperationalTime_Object=MibScalar
nwIpxNetBIOSOperationalTime=_NwIpxNetBIOSOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,1,1,4),_NwIpxNetBIOSOperationalTime_Type())
nwIpxNetBIOSOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSOperationalTime.setStatus(_A)
_NwIpxNetBIOSVersion_Type=DisplayString
_NwIpxNetBIOSVersion_Object=MibScalar
nwIpxNetBIOSVersion=_NwIpxNetBIOSVersion_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,1,1,5),_NwIpxNetBIOSVersion_Type())
nwIpxNetBIOSVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSVersion.setStatus(_A)
_NwIpxNetBIOSCounters_ObjectIdentity=ObjectIdentity
nwIpxNetBIOSCounters=_NwIpxNetBIOSCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,1,2))
class _NwIpxNetBIOSCtrAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxNetBIOSCtrAdminStatus_Type.__name__=_C
_NwIpxNetBIOSCtrAdminStatus_Object=MibScalar
nwIpxNetBIOSCtrAdminStatus=_NwIpxNetBIOSCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,1,2,1),_NwIpxNetBIOSCtrAdminStatus_Type())
nwIpxNetBIOSCtrAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxNetBIOSCtrAdminStatus.setStatus(_A)
class _NwIpxNetBIOSCtrReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpxNetBIOSCtrReset_Type.__name__=_C
_NwIpxNetBIOSCtrReset_Object=MibScalar
nwIpxNetBIOSCtrReset=_NwIpxNetBIOSCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,1,2,2),_NwIpxNetBIOSCtrReset_Type())
nwIpxNetBIOSCtrReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxNetBIOSCtrReset.setStatus(_A)
_NwIpxNetBIOSCtrOperationalTime_Type=TimeTicks
_NwIpxNetBIOSCtrOperationalTime_Object=MibScalar
nwIpxNetBIOSCtrOperationalTime=_NwIpxNetBIOSCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,1,2,3),_NwIpxNetBIOSCtrOperationalTime_Type())
nwIpxNetBIOSCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSCtrOperationalTime.setStatus(_A)
_NwIpxNetBIOSCtrInPkts_Type=Counter32
_NwIpxNetBIOSCtrInPkts_Object=MibScalar
nwIpxNetBIOSCtrInPkts=_NwIpxNetBIOSCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,1,2,4),_NwIpxNetBIOSCtrInPkts_Type())
nwIpxNetBIOSCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSCtrInPkts.setStatus(_A)
_NwIpxNetBIOSCtrOutPkts_Type=Counter32
_NwIpxNetBIOSCtrOutPkts_Object=MibScalar
nwIpxNetBIOSCtrOutPkts=_NwIpxNetBIOSCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,1,2,5),_NwIpxNetBIOSCtrOutPkts_Type())
nwIpxNetBIOSCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSCtrOutPkts.setStatus(_A)
_NwIpxNetBIOSCtrFilteredPkts_Type=Counter32
_NwIpxNetBIOSCtrFilteredPkts_Object=MibScalar
nwIpxNetBIOSCtrFilteredPkts=_NwIpxNetBIOSCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,1,2,6),_NwIpxNetBIOSCtrFilteredPkts_Type())
nwIpxNetBIOSCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSCtrFilteredPkts.setStatus(_A)
_NwIpxNetBIOSCtrDiscardPkts_Type=Counter32
_NwIpxNetBIOSCtrDiscardPkts_Object=MibScalar
nwIpxNetBIOSCtrDiscardPkts=_NwIpxNetBIOSCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,1,2,7),_NwIpxNetBIOSCtrDiscardPkts_Type())
nwIpxNetBIOSCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSCtrDiscardPkts.setStatus(_A)
_NwIpxNetBIOSCtrInBytes_Type=Counter32
_NwIpxNetBIOSCtrInBytes_Object=MibScalar
nwIpxNetBIOSCtrInBytes=_NwIpxNetBIOSCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,1,2,8),_NwIpxNetBIOSCtrInBytes_Type())
nwIpxNetBIOSCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSCtrInBytes.setStatus(_A)
_NwIpxNetBIOSCtrOutBytes_Type=Counter32
_NwIpxNetBIOSCtrOutBytes_Object=MibScalar
nwIpxNetBIOSCtrOutBytes=_NwIpxNetBIOSCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,1,2,9),_NwIpxNetBIOSCtrOutBytes_Type())
nwIpxNetBIOSCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSCtrOutBytes.setStatus(_A)
_NwIpxNetBIOSCtrFilteredBytes_Type=Counter32
_NwIpxNetBIOSCtrFilteredBytes_Object=MibScalar
nwIpxNetBIOSCtrFilteredBytes=_NwIpxNetBIOSCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,1,2,10),_NwIpxNetBIOSCtrFilteredBytes_Type())
nwIpxNetBIOSCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSCtrFilteredBytes.setStatus(_A)
_NwIpxNetBIOSCtrDiscardBytes_Type=Counter32
_NwIpxNetBIOSCtrDiscardBytes_Object=MibScalar
nwIpxNetBIOSCtrDiscardBytes=_NwIpxNetBIOSCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,1,2,11),_NwIpxNetBIOSCtrDiscardBytes_Type())
nwIpxNetBIOSCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSCtrDiscardBytes.setStatus(_A)
_NwIpxNetBIOSInterface_ObjectIdentity=ObjectIdentity
nwIpxNetBIOSInterface=_NwIpxNetBIOSInterface_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,2))
_NwIpxNetBIOSIfConfig_ObjectIdentity=ObjectIdentity
nwIpxNetBIOSIfConfig=_NwIpxNetBIOSIfConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,2,1))
_NwIpxNetBIOSIfTable_Object=MibTable
nwIpxNetBIOSIfTable=_NwIpxNetBIOSIfTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,2,1,1))
if mibBuilder.loadTexts:nwIpxNetBIOSIfTable.setStatus(_A)
_NwIpxNetBIOSIfEntry_Object=MibTableRow
nwIpxNetBIOSIfEntry=_NwIpxNetBIOSIfEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,2,1,1,1))
nwIpxNetBIOSIfEntry.setIndexNames((0,_H,_A0))
if mibBuilder.loadTexts:nwIpxNetBIOSIfEntry.setStatus(_A)
_NwIpxNetBIOSIfIndex_Type=Integer32
_NwIpxNetBIOSIfIndex_Object=MibTableColumn
nwIpxNetBIOSIfIndex=_NwIpxNetBIOSIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,2,1,1,1,1),_NwIpxNetBIOSIfIndex_Type())
nwIpxNetBIOSIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxNetBIOSIfIndex.setStatus(_A)
class _NwIpxNetBIOSIfAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxNetBIOSIfAdminStatus_Type.__name__=_C
_NwIpxNetBIOSIfAdminStatus_Object=MibTableColumn
nwIpxNetBIOSIfAdminStatus=_NwIpxNetBIOSIfAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,2,1,1,1,2),_NwIpxNetBIOSIfAdminStatus_Type())
nwIpxNetBIOSIfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxNetBIOSIfAdminStatus.setStatus(_A)
class _NwIpxNetBIOSIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_J,4),(_K,5),(_L,6)))
_NwIpxNetBIOSIfOperStatus_Type.__name__=_C
_NwIpxNetBIOSIfOperStatus_Object=MibTableColumn
nwIpxNetBIOSIfOperStatus=_NwIpxNetBIOSIfOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,2,1,1,1,3),_NwIpxNetBIOSIfOperStatus_Type())
nwIpxNetBIOSIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSIfOperStatus.setStatus(_A)
_NwIpxNetBIOSIfOperationalTime_Type=TimeTicks
_NwIpxNetBIOSIfOperationalTime_Object=MibTableColumn
nwIpxNetBIOSIfOperationalTime=_NwIpxNetBIOSIfOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,2,1,1,1,4),_NwIpxNetBIOSIfOperationalTime_Type())
nwIpxNetBIOSIfOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSIfOperationalTime.setStatus(_A)
_NwIpxNetBIOSIfCounters_ObjectIdentity=ObjectIdentity
nwIpxNetBIOSIfCounters=_NwIpxNetBIOSIfCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,2,2))
_NwIpxNetBIOSIfCtrTable_Object=MibTable
nwIpxNetBIOSIfCtrTable=_NwIpxNetBIOSIfCtrTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,2,2,1))
if mibBuilder.loadTexts:nwIpxNetBIOSIfCtrTable.setStatus(_A)
_NwIpxNetBIOSIfCtrEntry_Object=MibTableRow
nwIpxNetBIOSIfCtrEntry=_NwIpxNetBIOSIfCtrEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,2,2,1,1))
nwIpxNetBIOSIfCtrEntry.setIndexNames((0,_H,_A1))
if mibBuilder.loadTexts:nwIpxNetBIOSIfCtrEntry.setStatus(_A)
_NwIpxNetBIOSIfCtrIfIndex_Type=Integer32
_NwIpxNetBIOSIfCtrIfIndex_Object=MibTableColumn
nwIpxNetBIOSIfCtrIfIndex=_NwIpxNetBIOSIfCtrIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,2,2,1,1,1),_NwIpxNetBIOSIfCtrIfIndex_Type())
nwIpxNetBIOSIfCtrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSIfCtrIfIndex.setStatus(_A)
class _NwIpxNetBIOSIfCtrAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxNetBIOSIfCtrAdminStatus_Type.__name__=_C
_NwIpxNetBIOSIfCtrAdminStatus_Object=MibTableColumn
nwIpxNetBIOSIfCtrAdminStatus=_NwIpxNetBIOSIfCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,2,2,1,1,2),_NwIpxNetBIOSIfCtrAdminStatus_Type())
nwIpxNetBIOSIfCtrAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxNetBIOSIfCtrAdminStatus.setStatus(_A)
class _NwIpxNetBIOSIfCtrReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpxNetBIOSIfCtrReset_Type.__name__=_C
_NwIpxNetBIOSIfCtrReset_Object=MibTableColumn
nwIpxNetBIOSIfCtrReset=_NwIpxNetBIOSIfCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,2,2,1,1,3),_NwIpxNetBIOSIfCtrReset_Type())
nwIpxNetBIOSIfCtrReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxNetBIOSIfCtrReset.setStatus(_A)
_NwIpxNetBIOSIfCtrOperationalTime_Type=TimeTicks
_NwIpxNetBIOSIfCtrOperationalTime_Object=MibTableColumn
nwIpxNetBIOSIfCtrOperationalTime=_NwIpxNetBIOSIfCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,2,2,1,1,4),_NwIpxNetBIOSIfCtrOperationalTime_Type())
nwIpxNetBIOSIfCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSIfCtrOperationalTime.setStatus(_A)
_NwIpxNetBIOSIfCtrInPkts_Type=Counter32
_NwIpxNetBIOSIfCtrInPkts_Object=MibTableColumn
nwIpxNetBIOSIfCtrInPkts=_NwIpxNetBIOSIfCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,2,2,1,1,5),_NwIpxNetBIOSIfCtrInPkts_Type())
nwIpxNetBIOSIfCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSIfCtrInPkts.setStatus(_A)
_NwIpxNetBIOSIfCtrOutPkts_Type=Counter32
_NwIpxNetBIOSIfCtrOutPkts_Object=MibTableColumn
nwIpxNetBIOSIfCtrOutPkts=_NwIpxNetBIOSIfCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,2,2,1,1,6),_NwIpxNetBIOSIfCtrOutPkts_Type())
nwIpxNetBIOSIfCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSIfCtrOutPkts.setStatus(_A)
_NwIpxNetBIOSIfCtrFilteredPkts_Type=Counter32
_NwIpxNetBIOSIfCtrFilteredPkts_Object=MibTableColumn
nwIpxNetBIOSIfCtrFilteredPkts=_NwIpxNetBIOSIfCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,2,2,1,1,7),_NwIpxNetBIOSIfCtrFilteredPkts_Type())
nwIpxNetBIOSIfCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSIfCtrFilteredPkts.setStatus(_A)
_NwIpxNetBIOSIfCtrDiscardPkts_Type=Counter32
_NwIpxNetBIOSIfCtrDiscardPkts_Object=MibTableColumn
nwIpxNetBIOSIfCtrDiscardPkts=_NwIpxNetBIOSIfCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,2,2,1,1,8),_NwIpxNetBIOSIfCtrDiscardPkts_Type())
nwIpxNetBIOSIfCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSIfCtrDiscardPkts.setStatus(_A)
_NwIpxNetBIOSIfCtrInBytes_Type=Counter32
_NwIpxNetBIOSIfCtrInBytes_Object=MibTableColumn
nwIpxNetBIOSIfCtrInBytes=_NwIpxNetBIOSIfCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,2,2,1,1,9),_NwIpxNetBIOSIfCtrInBytes_Type())
nwIpxNetBIOSIfCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSIfCtrInBytes.setStatus(_A)
_NwIpxNetBIOSIfCtrOutBytes_Type=Counter32
_NwIpxNetBIOSIfCtrOutBytes_Object=MibTableColumn
nwIpxNetBIOSIfCtrOutBytes=_NwIpxNetBIOSIfCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,2,2,1,1,10),_NwIpxNetBIOSIfCtrOutBytes_Type())
nwIpxNetBIOSIfCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSIfCtrOutBytes.setStatus(_A)
_NwIpxNetBIOSIfCtrFilteredBytes_Type=Counter32
_NwIpxNetBIOSIfCtrFilteredBytes_Object=MibTableColumn
nwIpxNetBIOSIfCtrFilteredBytes=_NwIpxNetBIOSIfCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,2,2,1,1,11),_NwIpxNetBIOSIfCtrFilteredBytes_Type())
nwIpxNetBIOSIfCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSIfCtrFilteredBytes.setStatus(_A)
_NwIpxNetBIOSIfCtrDiscardBytes_Type=Counter32
_NwIpxNetBIOSIfCtrDiscardBytes_Object=MibTableColumn
nwIpxNetBIOSIfCtrDiscardBytes=_NwIpxNetBIOSIfCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,1,2,2,1,1,12),_NwIpxNetBIOSIfCtrDiscardBytes_Type())
nwIpxNetBIOSIfCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxNetBIOSIfCtrDiscardBytes.setStatus(_A)
_NwIpxBroadcast_ObjectIdentity=ObjectIdentity
nwIpxBroadcast=_NwIpxBroadcast_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2))
_NwIpxBroadcastSystem_ObjectIdentity=ObjectIdentity
nwIpxBroadcastSystem=_NwIpxBroadcastSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,1))
_NwIpxBroadcastConfig_ObjectIdentity=ObjectIdentity
nwIpxBroadcastConfig=_NwIpxBroadcastConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,1,1))
class _NwIpxBcastAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxBcastAdminStatus_Type.__name__=_C
_NwIpxBcastAdminStatus_Object=MibScalar
nwIpxBcastAdminStatus=_NwIpxBcastAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,1,1,1),_NwIpxBcastAdminStatus_Type())
nwIpxBcastAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxBcastAdminStatus.setStatus(_A)
class _NwIpxBcastOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_J,4),(_K,5),(_L,6)))
_NwIpxBcastOperStatus_Type.__name__=_C
_NwIpxBcastOperStatus_Object=MibScalar
nwIpxBcastOperStatus=_NwIpxBcastOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,1,1,2),_NwIpxBcastOperStatus_Type())
nwIpxBcastOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastOperStatus.setStatus(_A)
class _NwIpxBcastAdminReset_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpxBcastAdminReset_Type.__name__=_C
_NwIpxBcastAdminReset_Object=MibScalar
nwIpxBcastAdminReset=_NwIpxBcastAdminReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,1,1,3),_NwIpxBcastAdminReset_Type())
nwIpxBcastAdminReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxBcastAdminReset.setStatus(_A)
_NwIpxBcastOperationalTime_Type=TimeTicks
_NwIpxBcastOperationalTime_Object=MibScalar
nwIpxBcastOperationalTime=_NwIpxBcastOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,1,1,4),_NwIpxBcastOperationalTime_Type())
nwIpxBcastOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastOperationalTime.setStatus(_A)
_NwIpxBcastVersion_Type=DisplayString
_NwIpxBcastVersion_Object=MibScalar
nwIpxBcastVersion=_NwIpxBcastVersion_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,1,1,5),_NwIpxBcastVersion_Type())
nwIpxBcastVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastVersion.setStatus(_A)
_NwIpxBroadcastCounters_ObjectIdentity=ObjectIdentity
nwIpxBroadcastCounters=_NwIpxBroadcastCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,1,2))
class _NwIpxBcastCtrAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxBcastCtrAdminStatus_Type.__name__=_C
_NwIpxBcastCtrAdminStatus_Object=MibScalar
nwIpxBcastCtrAdminStatus=_NwIpxBcastCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,1,2,1),_NwIpxBcastCtrAdminStatus_Type())
nwIpxBcastCtrAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxBcastCtrAdminStatus.setStatus(_A)
class _NwIpxBcastCtrReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpxBcastCtrReset_Type.__name__=_C
_NwIpxBcastCtrReset_Object=MibScalar
nwIpxBcastCtrReset=_NwIpxBcastCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,1,2,2),_NwIpxBcastCtrReset_Type())
nwIpxBcastCtrReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxBcastCtrReset.setStatus(_A)
_NwIpxBcastCtrOperationalTime_Type=TimeTicks
_NwIpxBcastCtrOperationalTime_Object=MibScalar
nwIpxBcastCtrOperationalTime=_NwIpxBcastCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,1,2,3),_NwIpxBcastCtrOperationalTime_Type())
nwIpxBcastCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastCtrOperationalTime.setStatus(_A)
_NwIpxBcastCtrInPkts_Type=Counter32
_NwIpxBcastCtrInPkts_Object=MibScalar
nwIpxBcastCtrInPkts=_NwIpxBcastCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,1,2,4),_NwIpxBcastCtrInPkts_Type())
nwIpxBcastCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastCtrInPkts.setStatus(_A)
_NwIpxBcastCtrOutPkts_Type=Counter32
_NwIpxBcastCtrOutPkts_Object=MibScalar
nwIpxBcastCtrOutPkts=_NwIpxBcastCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,1,2,5),_NwIpxBcastCtrOutPkts_Type())
nwIpxBcastCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastCtrOutPkts.setStatus(_A)
_NwIpxBcastCtrFilteredPkts_Type=Counter32
_NwIpxBcastCtrFilteredPkts_Object=MibScalar
nwIpxBcastCtrFilteredPkts=_NwIpxBcastCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,1,2,6),_NwIpxBcastCtrFilteredPkts_Type())
nwIpxBcastCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastCtrFilteredPkts.setStatus(_A)
_NwIpxBcastCtrDiscardPkts_Type=Counter32
_NwIpxBcastCtrDiscardPkts_Object=MibScalar
nwIpxBcastCtrDiscardPkts=_NwIpxBcastCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,1,2,7),_NwIpxBcastCtrDiscardPkts_Type())
nwIpxBcastCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastCtrDiscardPkts.setStatus(_A)
_NwIpxBcastCtrInBytes_Type=Counter32
_NwIpxBcastCtrInBytes_Object=MibScalar
nwIpxBcastCtrInBytes=_NwIpxBcastCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,1,2,8),_NwIpxBcastCtrInBytes_Type())
nwIpxBcastCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastCtrInBytes.setStatus(_A)
_NwIpxBcastCtrOutBytes_Type=Counter32
_NwIpxBcastCtrOutBytes_Object=MibScalar
nwIpxBcastCtrOutBytes=_NwIpxBcastCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,1,2,9),_NwIpxBcastCtrOutBytes_Type())
nwIpxBcastCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastCtrOutBytes.setStatus(_A)
_NwIpxBcastCtrFilteredBytes_Type=Counter32
_NwIpxBcastCtrFilteredBytes_Object=MibScalar
nwIpxBcastCtrFilteredBytes=_NwIpxBcastCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,1,2,10),_NwIpxBcastCtrFilteredBytes_Type())
nwIpxBcastCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastCtrFilteredBytes.setStatus(_A)
_NwIpxBcastCtrDiscardBytes_Type=Counter32
_NwIpxBcastCtrDiscardBytes_Object=MibScalar
nwIpxBcastCtrDiscardBytes=_NwIpxBcastCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,1,2,11),_NwIpxBcastCtrDiscardBytes_Type())
nwIpxBcastCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastCtrDiscardBytes.setStatus(_A)
_NwIpxBroadcastInterface_ObjectIdentity=ObjectIdentity
nwIpxBroadcastInterface=_NwIpxBroadcastInterface_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,2))
_NwIpxBroadcastIfConfig_ObjectIdentity=ObjectIdentity
nwIpxBroadcastIfConfig=_NwIpxBroadcastIfConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,2,1))
_NwIpxBcastIfTable_Object=MibTable
nwIpxBcastIfTable=_NwIpxBcastIfTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,2,1,1))
if mibBuilder.loadTexts:nwIpxBcastIfTable.setStatus(_A)
_NwIpxBcastIfEntry_Object=MibTableRow
nwIpxBcastIfEntry=_NwIpxBcastIfEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,2,1,1,1))
nwIpxBcastIfEntry.setIndexNames((0,_H,_A2))
if mibBuilder.loadTexts:nwIpxBcastIfEntry.setStatus(_A)
_NwIpxBcastIfIndex_Type=Integer32
_NwIpxBcastIfIndex_Object=MibTableColumn
nwIpxBcastIfIndex=_NwIpxBcastIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,2,1,1,1,1),_NwIpxBcastIfIndex_Type())
nwIpxBcastIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxBcastIfIndex.setStatus(_A)
class _NwIpxBcastIfAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxBcastIfAdminStatus_Type.__name__=_C
_NwIpxBcastIfAdminStatus_Object=MibTableColumn
nwIpxBcastIfAdminStatus=_NwIpxBcastIfAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,2,1,1,1,2),_NwIpxBcastIfAdminStatus_Type())
nwIpxBcastIfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxBcastIfAdminStatus.setStatus(_A)
class _NwIpxBcastIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_J,4),(_K,5),(_L,6)))
_NwIpxBcastIfOperStatus_Type.__name__=_C
_NwIpxBcastIfOperStatus_Object=MibTableColumn
nwIpxBcastIfOperStatus=_NwIpxBcastIfOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,2,1,1,1,3),_NwIpxBcastIfOperStatus_Type())
nwIpxBcastIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastIfOperStatus.setStatus(_A)
_NwIpxBcastIfOperationalTime_Type=TimeTicks
_NwIpxBcastIfOperationalTime_Object=MibTableColumn
nwIpxBcastIfOperationalTime=_NwIpxBcastIfOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,2,1,1,1,4),_NwIpxBcastIfOperationalTime_Type())
nwIpxBcastIfOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastIfOperationalTime.setStatus(_A)
_NwIpxBroadcastIfCounters_ObjectIdentity=ObjectIdentity
nwIpxBroadcastIfCounters=_NwIpxBroadcastIfCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,2,2))
_NwIpxBcastIfCtrTable_Object=MibTable
nwIpxBcastIfCtrTable=_NwIpxBcastIfCtrTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,2,2,1))
if mibBuilder.loadTexts:nwIpxBcastIfCtrTable.setStatus(_A)
_NwIpxBcastIfCtrEntry_Object=MibTableRow
nwIpxBcastIfCtrEntry=_NwIpxBcastIfCtrEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,2,2,1,1))
nwIpxBcastIfCtrEntry.setIndexNames((0,_H,_A3))
if mibBuilder.loadTexts:nwIpxBcastIfCtrEntry.setStatus(_A)
_NwIpxBcastIfCtrIfIndex_Type=Integer32
_NwIpxBcastIfCtrIfIndex_Object=MibTableColumn
nwIpxBcastIfCtrIfIndex=_NwIpxBcastIfCtrIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,2,2,1,1,1),_NwIpxBcastIfCtrIfIndex_Type())
nwIpxBcastIfCtrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastIfCtrIfIndex.setStatus(_A)
class _NwIpxBcastIfCtrAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxBcastIfCtrAdminStatus_Type.__name__=_C
_NwIpxBcastIfCtrAdminStatus_Object=MibTableColumn
nwIpxBcastIfCtrAdminStatus=_NwIpxBcastIfCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,2,2,1,1,2),_NwIpxBcastIfCtrAdminStatus_Type())
nwIpxBcastIfCtrAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxBcastIfCtrAdminStatus.setStatus(_A)
class _NwIpxBcastIfCtrReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpxBcastIfCtrReset_Type.__name__=_C
_NwIpxBcastIfCtrReset_Object=MibTableColumn
nwIpxBcastIfCtrReset=_NwIpxBcastIfCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,2,2,1,1,3),_NwIpxBcastIfCtrReset_Type())
nwIpxBcastIfCtrReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxBcastIfCtrReset.setStatus(_A)
_NwIpxBcastIfCtrOperationalTime_Type=TimeTicks
_NwIpxBcastIfCtrOperationalTime_Object=MibTableColumn
nwIpxBcastIfCtrOperationalTime=_NwIpxBcastIfCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,2,2,1,1,4),_NwIpxBcastIfCtrOperationalTime_Type())
nwIpxBcastIfCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastIfCtrOperationalTime.setStatus(_A)
_NwIpxBcastIfCtrInPkts_Type=Counter32
_NwIpxBcastIfCtrInPkts_Object=MibTableColumn
nwIpxBcastIfCtrInPkts=_NwIpxBcastIfCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,2,2,1,1,5),_NwIpxBcastIfCtrInPkts_Type())
nwIpxBcastIfCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastIfCtrInPkts.setStatus(_A)
_NwIpxBcastIfCtrOutPkts_Type=Counter32
_NwIpxBcastIfCtrOutPkts_Object=MibTableColumn
nwIpxBcastIfCtrOutPkts=_NwIpxBcastIfCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,2,2,1,1,6),_NwIpxBcastIfCtrOutPkts_Type())
nwIpxBcastIfCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastIfCtrOutPkts.setStatus(_A)
_NwIpxBcastIfCtrFilteredPkts_Type=Counter32
_NwIpxBcastIfCtrFilteredPkts_Object=MibTableColumn
nwIpxBcastIfCtrFilteredPkts=_NwIpxBcastIfCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,2,2,1,1,7),_NwIpxBcastIfCtrFilteredPkts_Type())
nwIpxBcastIfCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastIfCtrFilteredPkts.setStatus(_A)
_NwIpxBcastIfCtrDiscardPkts_Type=Counter32
_NwIpxBcastIfCtrDiscardPkts_Object=MibTableColumn
nwIpxBcastIfCtrDiscardPkts=_NwIpxBcastIfCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,2,2,1,1,8),_NwIpxBcastIfCtrDiscardPkts_Type())
nwIpxBcastIfCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastIfCtrDiscardPkts.setStatus(_A)
_NwIpxBcastIfCtrInBytes_Type=Counter32
_NwIpxBcastIfCtrInBytes_Object=MibTableColumn
nwIpxBcastIfCtrInBytes=_NwIpxBcastIfCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,2,2,1,1,9),_NwIpxBcastIfCtrInBytes_Type())
nwIpxBcastIfCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastIfCtrInBytes.setStatus(_A)
_NwIpxBcastIfCtrOutBytes_Type=Counter32
_NwIpxBcastIfCtrOutBytes_Object=MibTableColumn
nwIpxBcastIfCtrOutBytes=_NwIpxBcastIfCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,2,2,1,1,10),_NwIpxBcastIfCtrOutBytes_Type())
nwIpxBcastIfCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastIfCtrOutBytes.setStatus(_A)
_NwIpxBcastIfCtrFilteredBytes_Type=Counter32
_NwIpxBcastIfCtrFilteredBytes_Object=MibTableColumn
nwIpxBcastIfCtrFilteredBytes=_NwIpxBcastIfCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,2,2,1,1,11),_NwIpxBcastIfCtrFilteredBytes_Type())
nwIpxBcastIfCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastIfCtrFilteredBytes.setStatus(_A)
_NwIpxBcastIfCtrDiscardBytes_Type=Counter32
_NwIpxBcastIfCtrDiscardBytes_Object=MibTableColumn
nwIpxBcastIfCtrDiscardBytes=_NwIpxBcastIfCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,2,2,2,1,1,12),_NwIpxBcastIfCtrDiscardBytes_Type())
nwIpxBcastIfCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxBcastIfCtrDiscardBytes.setStatus(_A)
_NwIpxEcho_ObjectIdentity=ObjectIdentity
nwIpxEcho=_NwIpxEcho_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3))
_NwIpxEchoSystem_ObjectIdentity=ObjectIdentity
nwIpxEchoSystem=_NwIpxEchoSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,1))
_NwIpxEchoConfig_ObjectIdentity=ObjectIdentity
nwIpxEchoConfig=_NwIpxEchoConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,1,1))
class _NwIpxEchoAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxEchoAdminStatus_Type.__name__=_C
_NwIpxEchoAdminStatus_Object=MibScalar
nwIpxEchoAdminStatus=_NwIpxEchoAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,1,1,1),_NwIpxEchoAdminStatus_Type())
nwIpxEchoAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxEchoAdminStatus.setStatus(_A)
class _NwIpxEchoOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_J,4),(_K,5),(_L,6)))
_NwIpxEchoOperStatus_Type.__name__=_C
_NwIpxEchoOperStatus_Object=MibScalar
nwIpxEchoOperStatus=_NwIpxEchoOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,1,1,2),_NwIpxEchoOperStatus_Type())
nwIpxEchoOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoOperStatus.setStatus(_A)
class _NwIpxEchoAdminReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpxEchoAdminReset_Type.__name__=_C
_NwIpxEchoAdminReset_Object=MibScalar
nwIpxEchoAdminReset=_NwIpxEchoAdminReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,1,1,3),_NwIpxEchoAdminReset_Type())
nwIpxEchoAdminReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxEchoAdminReset.setStatus(_A)
_NwIpxEchoOperationalTime_Type=TimeTicks
_NwIpxEchoOperationalTime_Object=MibScalar
nwIpxEchoOperationalTime=_NwIpxEchoOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,1,1,4),_NwIpxEchoOperationalTime_Type())
nwIpxEchoOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoOperationalTime.setStatus(_A)
_NwIpxEchoVersion_Type=DisplayString
_NwIpxEchoVersion_Object=MibScalar
nwIpxEchoVersion=_NwIpxEchoVersion_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,1,1,5),_NwIpxEchoVersion_Type())
nwIpxEchoVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoVersion.setStatus(_A)
_NwIpxEchoCounters_ObjectIdentity=ObjectIdentity
nwIpxEchoCounters=_NwIpxEchoCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,1,2))
class _NwIpxEchoCtrAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxEchoCtrAdminStatus_Type.__name__=_C
_NwIpxEchoCtrAdminStatus_Object=MibScalar
nwIpxEchoCtrAdminStatus=_NwIpxEchoCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,1,2,1),_NwIpxEchoCtrAdminStatus_Type())
nwIpxEchoCtrAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxEchoCtrAdminStatus.setStatus(_A)
class _NwIpxEchoCtrReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpxEchoCtrReset_Type.__name__=_C
_NwIpxEchoCtrReset_Object=MibScalar
nwIpxEchoCtrReset=_NwIpxEchoCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,1,2,2),_NwIpxEchoCtrReset_Type())
nwIpxEchoCtrReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxEchoCtrReset.setStatus(_A)
_NwIpxEchoCtrOperationalTime_Type=TimeTicks
_NwIpxEchoCtrOperationalTime_Object=MibScalar
nwIpxEchoCtrOperationalTime=_NwIpxEchoCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,1,2,3),_NwIpxEchoCtrOperationalTime_Type())
nwIpxEchoCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoCtrOperationalTime.setStatus(_A)
_NwIpxEchoCtrInPkts_Type=Counter32
_NwIpxEchoCtrInPkts_Object=MibScalar
nwIpxEchoCtrInPkts=_NwIpxEchoCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,1,2,4),_NwIpxEchoCtrInPkts_Type())
nwIpxEchoCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoCtrInPkts.setStatus(_A)
_NwIpxEchoCtrOutPkts_Type=Counter32
_NwIpxEchoCtrOutPkts_Object=MibScalar
nwIpxEchoCtrOutPkts=_NwIpxEchoCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,1,2,5),_NwIpxEchoCtrOutPkts_Type())
nwIpxEchoCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoCtrOutPkts.setStatus(_A)
_NwIpxEchoCtrFilteredPkts_Type=Counter32
_NwIpxEchoCtrFilteredPkts_Object=MibScalar
nwIpxEchoCtrFilteredPkts=_NwIpxEchoCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,1,2,6),_NwIpxEchoCtrFilteredPkts_Type())
nwIpxEchoCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoCtrFilteredPkts.setStatus(_A)
_NwIpxEchoCtrDiscardPkts_Type=Counter32
_NwIpxEchoCtrDiscardPkts_Object=MibScalar
nwIpxEchoCtrDiscardPkts=_NwIpxEchoCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,1,2,7),_NwIpxEchoCtrDiscardPkts_Type())
nwIpxEchoCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoCtrDiscardPkts.setStatus(_A)
_NwIpxEchoCtrInBytes_Type=Counter32
_NwIpxEchoCtrInBytes_Object=MibScalar
nwIpxEchoCtrInBytes=_NwIpxEchoCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,1,2,8),_NwIpxEchoCtrInBytes_Type())
nwIpxEchoCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoCtrInBytes.setStatus(_A)
_NwIpxEchoCtrOutBytes_Type=Counter32
_NwIpxEchoCtrOutBytes_Object=MibScalar
nwIpxEchoCtrOutBytes=_NwIpxEchoCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,1,2,9),_NwIpxEchoCtrOutBytes_Type())
nwIpxEchoCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoCtrOutBytes.setStatus(_A)
_NwIpxEchoCtrFilteredBytes_Type=Counter32
_NwIpxEchoCtrFilteredBytes_Object=MibScalar
nwIpxEchoCtrFilteredBytes=_NwIpxEchoCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,1,2,10),_NwIpxEchoCtrFilteredBytes_Type())
nwIpxEchoCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoCtrFilteredBytes.setStatus(_A)
_NwIpxEchoSCtrDiscardBytes_Type=Counter32
_NwIpxEchoSCtrDiscardBytes_Object=MibScalar
nwIpxEchoSCtrDiscardBytes=_NwIpxEchoSCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,1,2,11),_NwIpxEchoSCtrDiscardBytes_Type())
nwIpxEchoSCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoSCtrDiscardBytes.setStatus(_A)
_NwIpxEchoInterface_ObjectIdentity=ObjectIdentity
nwIpxEchoInterface=_NwIpxEchoInterface_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,2))
_NwIpxEchoIfConfig_ObjectIdentity=ObjectIdentity
nwIpxEchoIfConfig=_NwIpxEchoIfConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,2,1))
_NwIpxEchoIfTable_Object=MibTable
nwIpxEchoIfTable=_NwIpxEchoIfTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,2,1,1))
if mibBuilder.loadTexts:nwIpxEchoIfTable.setStatus(_A)
_NwIpxEchoIfEntry_Object=MibTableRow
nwIpxEchoIfEntry=_NwIpxEchoIfEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,2,1,1,1))
nwIpxEchoIfEntry.setIndexNames((0,_H,_A4))
if mibBuilder.loadTexts:nwIpxEchoIfEntry.setStatus(_A)
_NwIpxEchoIfIndex_Type=Integer32
_NwIpxEchoIfIndex_Object=MibTableColumn
nwIpxEchoIfIndex=_NwIpxEchoIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,2,1,1,1,1),_NwIpxEchoIfIndex_Type())
nwIpxEchoIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxEchoIfIndex.setStatus(_A)
class _NwIpxEchoIfAdminStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxEchoIfAdminStatus_Type.__name__=_C
_NwIpxEchoIfAdminStatus_Object=MibTableColumn
nwIpxEchoIfAdminStatus=_NwIpxEchoIfAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,2,1,1,1,2),_NwIpxEchoIfAdminStatus_Type())
nwIpxEchoIfAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxEchoIfAdminStatus.setStatus(_A)
class _NwIpxEchoIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_J,4),(_K,5),(_L,6)))
_NwIpxEchoIfOperStatus_Type.__name__=_C
_NwIpxEchoIfOperStatus_Object=MibTableColumn
nwIpxEchoIfOperStatus=_NwIpxEchoIfOperStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,2,1,1,1,3),_NwIpxEchoIfOperStatus_Type())
nwIpxEchoIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoIfOperStatus.setStatus(_A)
_NwIpxEchoIfOperationalTime_Type=TimeTicks
_NwIpxEchoIfOperationalTime_Object=MibTableColumn
nwIpxEchoIfOperationalTime=_NwIpxEchoIfOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,2,1,1,1,4),_NwIpxEchoIfOperationalTime_Type())
nwIpxEchoIfOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoIfOperationalTime.setStatus(_A)
_NwIpxEchoIfCounters_ObjectIdentity=ObjectIdentity
nwIpxEchoIfCounters=_NwIpxEchoIfCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,2,2))
_NwIpxEchoIfCtrTable_Object=MibTable
nwIpxEchoIfCtrTable=_NwIpxEchoIfCtrTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,2,2,1))
if mibBuilder.loadTexts:nwIpxEchoIfCtrTable.setStatus(_A)
_NwIpxEchoIfCtrEntry_Object=MibTableRow
nwIpxEchoIfCtrEntry=_NwIpxEchoIfCtrEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,2,2,1,1))
nwIpxEchoIfCtrEntry.setIndexNames((0,_H,_A5))
if mibBuilder.loadTexts:nwIpxEchoIfCtrEntry.setStatus(_A)
_NwIpxEchoIfCtrIfIndex_Type=Integer32
_NwIpxEchoIfCtrIfIndex_Object=MibTableColumn
nwIpxEchoIfCtrIfIndex=_NwIpxEchoIfCtrIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,2,2,1,1,1),_NwIpxEchoIfCtrIfIndex_Type())
nwIpxEchoIfCtrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoIfCtrIfIndex.setStatus(_A)
class _NwIpxEchoIfCtrAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxEchoIfCtrAdminStatus_Type.__name__=_C
_NwIpxEchoIfCtrAdminStatus_Object=MibTableColumn
nwIpxEchoIfCtrAdminStatus=_NwIpxEchoIfCtrAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,2,2,1,1,2),_NwIpxEchoIfCtrAdminStatus_Type())
nwIpxEchoIfCtrAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxEchoIfCtrAdminStatus.setStatus(_A)
class _NwIpxEchoIfCtrReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwIpxEchoIfCtrReset_Type.__name__=_C
_NwIpxEchoIfCtrReset_Object=MibTableColumn
nwIpxEchoIfCtrReset=_NwIpxEchoIfCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,2,2,1,1,3),_NwIpxEchoIfCtrReset_Type())
nwIpxEchoIfCtrReset.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxEchoIfCtrReset.setStatus(_A)
_NwIpxEchoIfCtrOperationalTime_Type=TimeTicks
_NwIpxEchoIfCtrOperationalTime_Object=MibTableColumn
nwIpxEchoIfCtrOperationalTime=_NwIpxEchoIfCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,2,2,1,1,4),_NwIpxEchoIfCtrOperationalTime_Type())
nwIpxEchoIfCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoIfCtrOperationalTime.setStatus(_A)
_NwIpxEchoIfCtrInPkts_Type=Counter32
_NwIpxEchoIfCtrInPkts_Object=MibTableColumn
nwIpxEchoIfCtrInPkts=_NwIpxEchoIfCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,2,2,1,1,5),_NwIpxEchoIfCtrInPkts_Type())
nwIpxEchoIfCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoIfCtrInPkts.setStatus(_A)
_NwIpxEchoIfCtrOutPkts_Type=Counter32
_NwIpxEchoIfCtrOutPkts_Object=MibTableColumn
nwIpxEchoIfCtrOutPkts=_NwIpxEchoIfCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,2,2,1,1,6),_NwIpxEchoIfCtrOutPkts_Type())
nwIpxEchoIfCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoIfCtrOutPkts.setStatus(_A)
_NwIpxEchoIfCtrFilteredPkts_Type=Counter32
_NwIpxEchoIfCtrFilteredPkts_Object=MibTableColumn
nwIpxEchoIfCtrFilteredPkts=_NwIpxEchoIfCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,2,2,1,1,7),_NwIpxEchoIfCtrFilteredPkts_Type())
nwIpxEchoIfCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoIfCtrFilteredPkts.setStatus(_A)
_NwIpxEchoIfCtrDiscardPkts_Type=Counter32
_NwIpxEchoIfCtrDiscardPkts_Object=MibTableColumn
nwIpxEchoIfCtrDiscardPkts=_NwIpxEchoIfCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,2,2,1,1,8),_NwIpxEchoIfCtrDiscardPkts_Type())
nwIpxEchoIfCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoIfCtrDiscardPkts.setStatus(_A)
_NwIpxEchoIfCtrInBytes_Type=Counter32
_NwIpxEchoIfCtrInBytes_Object=MibTableColumn
nwIpxEchoIfCtrInBytes=_NwIpxEchoIfCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,2,2,1,1,9),_NwIpxEchoIfCtrInBytes_Type())
nwIpxEchoIfCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoIfCtrInBytes.setStatus(_A)
_NwIpxEchoIfCtrOutBytes_Type=Counter32
_NwIpxEchoIfCtrOutBytes_Object=MibTableColumn
nwIpxEchoIfCtrOutBytes=_NwIpxEchoIfCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,2,2,1,1,10),_NwIpxEchoIfCtrOutBytes_Type())
nwIpxEchoIfCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoIfCtrOutBytes.setStatus(_A)
_NwIpxEchoIfCtrFilteredBytes_Type=Counter32
_NwIpxEchoIfCtrFilteredBytes_Object=MibTableColumn
nwIpxEchoIfCtrFilteredBytes=_NwIpxEchoIfCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,2,2,1,1,11),_NwIpxEchoIfCtrFilteredBytes_Type())
nwIpxEchoIfCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoIfCtrFilteredBytes.setStatus(_A)
_NwIpxEchoIfCtrDiscardBytes_Type=Counter32
_NwIpxEchoIfCtrDiscardBytes_Object=MibTableColumn
nwIpxEchoIfCtrDiscardBytes=_NwIpxEchoIfCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,9,3,2,2,1,1,12),_NwIpxEchoIfCtrDiscardBytes_Type())
nwIpxEchoIfCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEchoIfCtrDiscardBytes.setStatus(_A)
_NwIpxEvent_ObjectIdentity=ObjectIdentity
nwIpxEvent=_NwIpxEvent_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10))
_NwIpxEventLogConfig_ObjectIdentity=ObjectIdentity
nwIpxEventLogConfig=_NwIpxEventLogConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10,1))
class _NwIpxEventAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxEventAdminStatus_Type.__name__=_C
_NwIpxEventAdminStatus_Object=MibScalar
nwIpxEventAdminStatus=_NwIpxEventAdminStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10,1,1),_NwIpxEventAdminStatus_Type())
nwIpxEventAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxEventAdminStatus.setStatus(_A)
class _NwIpxEventMaxEntries_Type(Integer32):defaultValue=100
_NwIpxEventMaxEntries_Type.__name__=_C
_NwIpxEventMaxEntries_Object=MibScalar
nwIpxEventMaxEntries=_NwIpxEventMaxEntries_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10,1,2),_NwIpxEventMaxEntries_Type())
nwIpxEventMaxEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxEventMaxEntries.setStatus(_A)
class _NwIpxEventTraceAll_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwIpxEventTraceAll_Type.__name__=_C
_NwIpxEventTraceAll_Object=MibScalar
nwIpxEventTraceAll=_NwIpxEventTraceAll_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10,1,3),_NwIpxEventTraceAll_Type())
nwIpxEventTraceAll.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxEventTraceAll.setStatus(_A)
_NwIpxEventLogFilterTable_ObjectIdentity=ObjectIdentity
nwIpxEventLogFilterTable=_NwIpxEventLogFilterTable_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10,2))
_NwIpxEventFilterTable_Object=MibTable
nwIpxEventFilterTable=_NwIpxEventFilterTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10,2,1))
if mibBuilder.loadTexts:nwIpxEventFilterTable.setStatus(_A)
_NwIpxEventFilterEntry_Object=MibTableRow
nwIpxEventFilterEntry=_NwIpxEventFilterEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10,2,1,1))
nwIpxEventFilterEntry.setIndexNames((0,_H,_A6),(0,_H,_A7))
if mibBuilder.loadTexts:nwIpxEventFilterEntry.setStatus(_A)
_NwIpxEventFltrProtocol_Type=Integer32
_NwIpxEventFltrProtocol_Object=MibTableColumn
nwIpxEventFltrProtocol=_NwIpxEventFltrProtocol_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10,2,1,1,1),_NwIpxEventFltrProtocol_Type())
nwIpxEventFltrProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEventFltrProtocol.setStatus(_A)
_NwIpxEventFltrIfNum_Type=Integer32
_NwIpxEventFltrIfNum_Object=MibTableColumn
nwIpxEventFltrIfNum=_NwIpxEventFltrIfNum_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10,2,1,1,2),_NwIpxEventFltrIfNum_Type())
nwIpxEventFltrIfNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEventFltrIfNum.setStatus(_A)
class _NwIpxEventFltrControl_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_O,2),(_N,3)))
_NwIpxEventFltrControl_Type.__name__=_C
_NwIpxEventFltrControl_Object=MibTableColumn
nwIpxEventFltrControl=_NwIpxEventFltrControl_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10,2,1,1,3),_NwIpxEventFltrControl_Type())
nwIpxEventFltrControl.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxEventFltrControl.setStatus(_A)
class _NwIpxEventFltrType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16,32)));namedValues=NamedValues(*(('misc',1),('timer',2),('rcv',4),('xmit',8),('event',16),('error',32)))
_NwIpxEventFltrType_Type.__name__=_C
_NwIpxEventFltrType_Object=MibTableColumn
nwIpxEventFltrType=_NwIpxEventFltrType_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10,2,1,1,4),_NwIpxEventFltrType_Type())
nwIpxEventFltrType.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxEventFltrType.setStatus(_A)
class _NwIpxEventFltrSeverity_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('highest',1),('highmed',2),('highlow',3)))
_NwIpxEventFltrSeverity_Type.__name__=_C
_NwIpxEventFltrSeverity_Object=MibTableColumn
nwIpxEventFltrSeverity=_NwIpxEventFltrSeverity_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10,2,1,1,5),_NwIpxEventFltrSeverity_Type())
nwIpxEventFltrSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxEventFltrSeverity.setStatus(_A)
class _NwIpxEventFltrAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('log',1),('trap',2),('log-trap',3)))
_NwIpxEventFltrAction_Type.__name__=_C
_NwIpxEventFltrAction_Object=MibTableColumn
nwIpxEventFltrAction=_NwIpxEventFltrAction_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10,2,1,1,6),_NwIpxEventFltrAction_Type())
nwIpxEventFltrAction.setMaxAccess(_D)
if mibBuilder.loadTexts:nwIpxEventFltrAction.setStatus(_A)
_NwIpxEventLogTable_ObjectIdentity=ObjectIdentity
nwIpxEventLogTable=_NwIpxEventLogTable_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10,3))
_NwIpxEventTable_Object=MibTable
nwIpxEventTable=_NwIpxEventTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10,3,1))
if mibBuilder.loadTexts:nwIpxEventTable.setStatus(_A)
_NwIpxEventEntry_Object=MibTableRow
nwIpxEventEntry=_NwIpxEventEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10,3,1,1))
nwIpxEventEntry.setIndexNames((0,_H,_A8))
if mibBuilder.loadTexts:nwIpxEventEntry.setStatus(_A)
_NwIpxEventNumber_Type=Integer32
_NwIpxEventNumber_Object=MibTableColumn
nwIpxEventNumber=_NwIpxEventNumber_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10,3,1,1,1),_NwIpxEventNumber_Type())
nwIpxEventNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEventNumber.setStatus(_A)
_NwIpxEventTime_Type=TimeTicks
_NwIpxEventTime_Object=MibTableColumn
nwIpxEventTime=_NwIpxEventTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10,3,1,1,2),_NwIpxEventTime_Type())
nwIpxEventTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEventTime.setStatus(_A)
class _NwIpxEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16,32)));namedValues=NamedValues(*(('misc',1),('timer',2),('rcv',4),('xmit',8),('event',16),('error',32)))
_NwIpxEventType_Type.__name__=_C
_NwIpxEventType_Object=MibTableColumn
nwIpxEventType=_NwIpxEventType_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10,3,1,1,3),_NwIpxEventType_Type())
nwIpxEventType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEventType.setStatus(_A)
class _NwIpxEventSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('highest',1),('highmed',2),('highlow',3)))
_NwIpxEventSeverity_Type.__name__=_C
_NwIpxEventSeverity_Object=MibTableColumn
nwIpxEventSeverity=_NwIpxEventSeverity_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10,3,1,1,4),_NwIpxEventSeverity_Type())
nwIpxEventSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEventSeverity.setStatus(_A)
_NwIpxEventProtocol_Type=Integer32
_NwIpxEventProtocol_Object=MibTableColumn
nwIpxEventProtocol=_NwIpxEventProtocol_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10,3,1,1,5),_NwIpxEventProtocol_Type())
nwIpxEventProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEventProtocol.setStatus(_A)
_NwIpxEventIfNum_Type=Integer32
_NwIpxEventIfNum_Object=MibTableColumn
nwIpxEventIfNum=_NwIpxEventIfNum_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10,3,1,1,6),_NwIpxEventIfNum_Type())
nwIpxEventIfNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEventIfNum.setStatus(_A)
_NwIpxEventTextString_Type=OctetString
_NwIpxEventTextString_Object=MibTableColumn
nwIpxEventTextString=_NwIpxEventTextString_Object((1,3,6,1,4,1,52,4,2,2,2,3,2,2,10,3,1,1,7),_NwIpxEventTextString_Type())
nwIpxEventTextString.setMaxAccess(_B)
if mibBuilder.loadTexts:nwIpxEventTextString.setStatus(_A)
_NwIpxWorkGroup_ObjectIdentity=ObjectIdentity
nwIpxWorkGroup=_NwIpxWorkGroup_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,2,2,11))
mibBuilder.exportSymbols(_H,**{'IpxAddress':IpxAddress,'nwIpxRouter':nwIpxRouter,'nwIpxMibs':nwIpxMibs,'nwIpxMibRevText':nwIpxMibRevText,'nwIpxComponents':nwIpxComponents,'nwIpxSystem':nwIpxSystem,'nwIpxSysConfig':nwIpxSysConfig,'nwIpxSysRouterId':nwIpxSysRouterId,'nwIpxSysAdministration':nwIpxSysAdministration,'nwIpxSysAdminStatus':nwIpxSysAdminStatus,'nwIpxSysOperStatus':nwIpxSysOperStatus,'nwIpxSysAdminReset':nwIpxSysAdminReset,'nwIpxSysOperationalTimel':nwIpxSysOperationalTimel,'nwIpxSysVersion':nwIpxSysVersion,'nwIpxForwarding':nwIpxForwarding,'nwIpxFwdSystem':nwIpxFwdSystem,'nwIpxFwdCounters':nwIpxFwdCounters,'nwIpxFwdCtrAdminStatus':nwIpxFwdCtrAdminStatus,'nwIpxFwdCtrReset':nwIpxFwdCtrReset,'nwIpxFwdCtrOperationalTime':nwIpxFwdCtrOperationalTime,'nwIpxFwdCtrInPkts':nwIpxFwdCtrInPkts,'nwIpxFwdCtrOutPkts':nwIpxFwdCtrOutPkts,'nwIpxFwdCtrFwdPkts':nwIpxFwdCtrFwdPkts,'nwIpxFwdCtrFilteredPkts':nwIpxFwdCtrFilteredPkts,'nwIpxFwdCtrDiscardPkts':nwIpxFwdCtrDiscardPkts,'nwIpxFwdCtrAddrErrPkts':nwIpxFwdCtrAddrErrPkts,'nwIpxFwdCtrLenErrPkts':nwIpxFwdCtrLenErrPkts,'nwIpxFwdCtrHdrErrPkts':nwIpxFwdCtrHdrErrPkts,'nwIpxFwdCtrInBytes':nwIpxFwdCtrInBytes,'nwIpxFwdCtrOutBytes':nwIpxFwdCtrOutBytes,'nwIpxFwdCtrFwdBytes':nwIpxFwdCtrFwdBytes,'nwIpxFwdCtrFilteredBytes':nwIpxFwdCtrFilteredBytes,'nwIpxFwdCtrDiscardBytes':nwIpxFwdCtrDiscardBytes,'nwIpxFwdCtrHostInPkts':nwIpxFwdCtrHostInPkts,'nwIpxFwdCtrHostOutPkts':nwIpxFwdCtrHostOutPkts,'nwIpxFwdCtrHostDiscardPkts':nwIpxFwdCtrHostDiscardPkts,'nwIpxFwdCtrHostInBytes':nwIpxFwdCtrHostInBytes,'nwIpxFwdCtrHostOutBytes':nwIpxFwdCtrHostOutBytes,'nwIpxFwdCtrHostDiscardBytes':nwIpxFwdCtrHostDiscardBytes,'nwIpxFwdInterfaces':nwIpxFwdInterfaces,'nwIpxFwdIfConfig':nwIpxFwdIfConfig,'nwIpxFwdIfTable':nwIpxFwdIfTable,'nwIpxFwdIfEntry':nwIpxFwdIfEntry,_S:nwIpxFwdIfIndex,'nwIpxFwdIfAdminStatus':nwIpxFwdIfAdminStatus,'nwIpxFwdIfOperStatus':nwIpxFwdIfOperStatus,'nwIpxFwdIfOperationalTime':nwIpxFwdIfOperationalTime,'nwIpxFwdIfControl':nwIpxFwdIfControl,'nwIpxFwdIfMtu':nwIpxFwdIfMtu,'nwIpxFwdIfForwarding':nwIpxFwdIfForwarding,'nwIpxFwdIfFrameType':nwIpxFwdIfFrameType,'nwIpxFwdIfAclIdentifier':nwIpxFwdIfAclIdentifier,'nwIpxFwdIfAclStatus':nwIpxFwdIfAclStatus,'nwIpxFwdIfCacheControl':nwIpxFwdIfCacheControl,'nwIpxFwdIfCacheEntries':nwIpxFwdIfCacheEntries,'nwIpxFwdIfCacheHits':nwIpxFwdIfCacheHits,'nwIpxFwdIfCacheMisses':nwIpxFwdIfCacheMisses,'nwIpxAddressTable':nwIpxAddressTable,'nwIpxAddrEntry':nwIpxAddrEntry,_f:nwIpxAddrIfIndex,_g:nwIpxAddrIfAddress,'nwIpxAddrIfControl':nwIpxAddrIfControl,'nwIpxAddrIfAddrType':nwIpxAddrIfAddrType,'nwIpxFwdIfCounters':nwIpxFwdIfCounters,'nwIpxFwdIfCtrTable':nwIpxFwdIfCtrTable,'nwIpxFwdIfCtrEntry':nwIpxFwdIfCtrEntry,_h:nwIpxFwdIfCtrIfIndex,'nwIpxFwdIfCtrAdminStatus':nwIpxFwdIfCtrAdminStatus,'nwIpxFwdIfCtrReset':nwIpxFwdIfCtrReset,'nwIpxFwdIfCtrOperationalTime':nwIpxFwdIfCtrOperationalTime,'nwIpxFwdIfCtrInPkts':nwIpxFwdIfCtrInPkts,'nwIpxFwdIfCtrOutPkts':nwIpxFwdIfCtrOutPkts,'nwIpxFwdIfCtrFwdPkts':nwIpxFwdIfCtrFwdPkts,'nwIpxFwdIfCtrFilteredPkts':nwIpxFwdIfCtrFilteredPkts,'nwIpxFwdIfCtrDiscardPkts':nwIpxFwdIfCtrDiscardPkts,'nwIpxFwdIfCtrAddrErrPkts':nwIpxFwdIfCtrAddrErrPkts,'nwIpxFwdIfCtrLenErrPkts':nwIpxFwdIfCtrLenErrPkts,'nwIpxFwdIfCtrHdrErrPkts':nwIpxFwdIfCtrHdrErrPkts,'nwIpxFwdIfCtrInBytes':nwIpxFwdIfCtrInBytes,'nwIpxFwdIfCtrOutBytes':nwIpxFwdIfCtrOutBytes,'nwIpxFwdIfCtrFwdBytes':nwIpxFwdIfCtrFwdBytes,'nwIpxFwdIfCtrFilteredBytes':nwIpxFwdIfCtrFilteredBytes,'nwIpxFwdIfCtrDiscardBytes':nwIpxFwdIfCtrDiscardBytes,'nwIpxFwdIfCtrHostInPkts':nwIpxFwdIfCtrHostInPkts,'nwIpxFwdIfCtrHostOutPkts':nwIpxFwdIfCtrHostOutPkts,'nwIpxFwdIfCtrHostDiscardPkts':nwIpxFwdIfCtrHostDiscardPkts,'nwIpxFwdIfCtrHostInBytes':nwIpxFwdIfCtrHostInBytes,'nwIpxFwdIfCtrHostOutBytes':nwIpxFwdIfCtrHostOutBytes,'nwIpxFwdIfCtrHostDiscardBytes':nwIpxFwdIfCtrHostDiscardBytes,'nwIpxTopology':nwIpxTopology,'nwIpxDistanceVector':nwIpxDistanceVector,'nwIpxRip':nwIpxRip,'nwIpxRipSystem':nwIpxRipSystem,'nwIpxRipConfig':nwIpxRipConfig,'nwIpxRipAdminStatus':nwIpxRipAdminStatus,'nwIpxRipOperStatus':nwIpxRipOperStatus,'nwIpxRipAdminReset':nwIpxRipAdminReset,'nwIpxRipOperationalTime':nwIpxRipOperationalTime,'nwIpxRipVersion':nwIpxRipVersion,'nwIpxRipStackSize':nwIpxRipStackSize,'nwIpxRipThreadPriority':nwIpxRipThreadPriority,'nwIpxRipDatabaseThreshold':nwIpxRipDatabaseThreshold,'nwIpxRipAgeOut':nwIpxRipAgeOut,'nwIpxRipHoldDown':nwIpxRipHoldDown,'nwIpxRipCounters':nwIpxRipCounters,'nwIpxRipCtrAdminStatus':nwIpxRipCtrAdminStatus,'nwIpxRipCtrReset':nwIpxRipCtrReset,'nwIpxRipCtrOperationalTime':nwIpxRipCtrOperationalTime,'nwIpxRipCtrInPkts':nwIpxRipCtrInPkts,'nwIpxRipCtrOutPkts':nwIpxRipCtrOutPkts,'nwIpxRipCtrFilteredPkts':nwIpxRipCtrFilteredPkts,'nwIpxRipCtrDiscardPkts':nwIpxRipCtrDiscardPkts,'nwIpxRipCtrInBytes':nwIpxRipCtrInBytes,'nwIpxRipCtrOutBytes':nwIpxRipCtrOutBytes,'nwIpxRipCtrFilteredBytes':nwIpxRipCtrFilteredBytes,'nwIpxRipCtrDiscardBytes':nwIpxRipCtrDiscardBytes,'nwIpxRipInterfaces':nwIpxRipInterfaces,'nwIpxRipIfConfig':nwIpxRipIfConfig,'nwIpxRipIfTable':nwIpxRipIfTable,'nwIpxRipIfEntry':nwIpxRipIfEntry,_i:nwIpxRipIfIndex,'nwIpxRipIfAdminStatus':nwIpxRipIfAdminStatus,'nwIpxRipIfOperStatus':nwIpxRipIfOperStatus,'nwIpxRipIfOperationalTime':nwIpxRipIfOperationalTime,'nwIpxRipIfVersion':nwIpxRipIfVersion,'nwIpxRipIfAdvertisement':nwIpxRipIfAdvertisement,'nwIpxRipIfFloodDelay':nwIpxRipIfFloodDelay,'nwIpxRipIfRequestDelay':nwIpxRipIfRequestDelay,'nwIpxRipIfPriority':nwIpxRipIfPriority,'nwIpxRipIfHelloTimer':nwIpxRipIfHelloTimer,'nwIpxRipIfSplitHorizon':nwIpxRipIfSplitHorizon,'nwIpxRipIfPoisonReverse':nwIpxRipIfPoisonReverse,'nwIpxRipIfSnooping':nwIpxRipIfSnooping,'nwIpxRipIfType':nwIpxRipIfType,'nwIpxRipIfXmitCost':nwIpxRipIfXmitCost,'nwIpxRipIfAclIdentifier':nwIpxRipIfAclIdentifier,'nwIpxRipIfAclStatus':nwIpxRipIfAclStatus,'nwIpxRipIfCounters':nwIpxRipIfCounters,'nwIpxRipIfCtrTable':nwIpxRipIfCtrTable,'nwIpxRipIfCtrEntry':nwIpxRipIfCtrEntry,_j:nwIpxRipIfCtrIfIndex,'nwIpxRipIfCtrAdminStatus':nwIpxRipIfCtrAdminStatus,'nwIpxRipIfCtrReset':nwIpxRipIfCtrReset,'nwIpxRipIfCtrOperationalTime':nwIpxRipIfCtrOperationalTime,'nwIpxRipIfCtrInPkts':nwIpxRipIfCtrInPkts,'nwIpxRipIfCtrOutPkts':nwIpxRipIfCtrOutPkts,'nwIpxRipIfCtrFilteredPkts':nwIpxRipIfCtrFilteredPkts,'nwIpxRipIfCtrDiscardPkts':nwIpxRipIfCtrDiscardPkts,'nwIpxRipIfCtrInBytes':nwIpxRipIfCtrInBytes,'nwIpxRipIfCtrOutBytes':nwIpxRipIfCtrOutBytes,'nwIpxRipIfCtrFilteredBytes':nwIpxRipIfCtrFilteredBytes,'nwIpxRipIfCtrDiscardBytes':nwIpxRipIfCtrDiscardBytes,'nwIpxRipDatabase':nwIpxRipDatabase,'nwIpxRipRouteTable':nwIpxRipRouteTable,'nwIpxRipRouteEntry':nwIpxRipRouteEntry,_k:nwIpxRipRtNetId,_l:nwIpxRipRtIfIndex,_m:nwIpxRipRtSrcNode,'nwIpxRipRtHops':nwIpxRipRtHops,'nwIpxRipRtTicks':nwIpxRipRtTicks,'nwIpxRipRtAge':nwIpxRipRtAge,'nwIpxRipRtType':nwIpxRipRtType,'nwIpxRipRtFlags':nwIpxRipRtFlags,'nwIpxRipFilters':nwIpxRipFilters,'nwIpxSap':nwIpxSap,'nwIpxSapSystem':nwIpxSapSystem,'nwIpxSapConfig':nwIpxSapConfig,'nwIpxSapAdminStatus':nwIpxSapAdminStatus,'nwIpxSapOperStatus':nwIpxSapOperStatus,'nwIpxSapAdminReset':nwIpxSapAdminReset,'nwIpxSapOperationalTime':nwIpxSapOperationalTime,'nwIpxSapVersion':nwIpxSapVersion,'nwIpxSapStackSize':nwIpxSapStackSize,'nwIpxSapThreadPriority':nwIpxSapThreadPriority,'nwIpxSapDatabaseThreshold':nwIpxSapDatabaseThreshold,'nwIpxSapAgeOut':nwIpxSapAgeOut,'nwIpxSapHoldDown':nwIpxSapHoldDown,'nwIpxSapCounters':nwIpxSapCounters,'nwIpxSapCtrAdminStatus':nwIpxSapCtrAdminStatus,'nwIpxSapCtrReset':nwIpxSapCtrReset,'nwIpxSapCtrOperationalTime':nwIpxSapCtrOperationalTime,'nwIpxSapCtrInPkts':nwIpxSapCtrInPkts,'nwIpxSapCtrOutPkts':nwIpxSapCtrOutPkts,'nwIpxSapCtrFilteredPkts':nwIpxSapCtrFilteredPkts,'nwIpxSapCtrDiscardPkts':nwIpxSapCtrDiscardPkts,'nwIpxSapCtrInBytes':nwIpxSapCtrInBytes,'nwIpxSapCtrOutBytes':nwIpxSapCtrOutBytes,'nwIpxSapCtrFilteredBytes':nwIpxSapCtrFilteredBytes,'nwIpxSapCtrDiscardBytes':nwIpxSapCtrDiscardBytes,'nwIpxSapInterfaces':nwIpxSapInterfaces,'nwIpxSapIfConfig':nwIpxSapIfConfig,'nwIpxSapIfTable':nwIpxSapIfTable,'nwIpxSapIfEntry':nwIpxSapIfEntry,_n:nwIpxSapIfIndex,'nwIpxSapIfAdminStatus':nwIpxSapIfAdminStatus,'nwIpxSapIfOperStatus':nwIpxSapIfOperStatus,'nwIpxSapIfOperationalTime':nwIpxSapIfOperationalTime,'nwIpxSapIfVersion':nwIpxSapIfVersion,'nwIpxSapIfAdvertisement':nwIpxSapIfAdvertisement,'nwIpxSapIfFloodDelay':nwIpxSapIfFloodDelay,'nwIpxSapIfRequestDelay':nwIpxSapIfRequestDelay,'nwIpxSapIfPriority':nwIpxSapIfPriority,'nwIpxSapIfHelloTimer':nwIpxSapIfHelloTimer,'nwIpxSapIfSplitHorizon':nwIpxSapIfSplitHorizon,'nwIpxSapIfPoisonReverse':nwIpxSapIfPoisonReverse,'nwIpxSapIfSnooping':nwIpxSapIfSnooping,'nwIpxSapIfType':nwIpxSapIfType,'nwIpxSapIfXmitCost':nwIpxSapIfXmitCost,'nwIpxSapIfAclIdentifier':nwIpxSapIfAclIdentifier,'nwIpxSapIfAclStatus':nwIpxSapIfAclStatus,'nwIpxSapIfCounters':nwIpxSapIfCounters,'nwIpxSapIfCtrTable':nwIpxSapIfCtrTable,'nwIpxSapIfCtrEntry':nwIpxSapIfCtrEntry,_o:nwIpxSapIfCtrIfIndex,'nwIpxSapIfCtrAdminStatus':nwIpxSapIfCtrAdminStatus,'nwIpxSapIfCtrReset':nwIpxSapIfCtrReset,'nwIpxSapIfCtrOperationalTime':nwIpxSapIfCtrOperationalTime,'nwIpxSapIfCtrInPkts':nwIpxSapIfCtrInPkts,'nwIpxSapIfCtrOutPkts':nwIpxSapIfCtrOutPkts,'nwIpxSapIfCtrFilteredPkts':nwIpxSapIfCtrFilteredPkts,'nwIpxSapIfCtrDiscardPkts':nwIpxSapIfCtrDiscardPkts,'nwIpxSapIfCtrInBytes':nwIpxSapIfCtrInBytes,'nwIpxSapIfCtrOutBytes':nwIpxSapIfCtrOutBytes,'nwIpxSapIfCtrFilteredBytes':nwIpxSapIfCtrFilteredBytes,'nwIpxSapIfCtrDiscardBytes':nwIpxSapIfCtrDiscardBytes,'nwIpxSapServerTable':nwIpxSapServerTable,'nwIpxSapServerIfTable':nwIpxSapServerIfTable,'nwIpxSapServerIfEntry':nwIpxSapServerIfEntry,_p:nwIpxSapServerIfNetId,_q:nwIpxSapServerIfNode,_r:nwIpxSapServerIfSocket,_s:nwIpxSapServerIfServiceType,_t:nwIpxSapServerIfIfNum,_u:nwIpxSapServerIfSrcNode,'nwIpxSapServerIfName':nwIpxSapServerIfName,'nwIpxSapServerIfHops':nwIpxSapServerIfHops,'nwIpxSapServerIfAge':nwIpxSapServerIfAge,'nwIpxSapServerIfType':nwIpxSapServerIfType,'nwIpxSapServerIfFlags':nwIpxSapServerIfFlags,'nwIpxSapFilters':nwIpxSapFilters,'nwIpxLinkState':nwIpxLinkState,'nwIpxNlsp':nwIpxNlsp,'nwIpxFib':nwIpxFib,'nwIpxFibTable':nwIpxFibTable,'nwIpxFibEntry':nwIpxFibEntry,_v:nwIpxFibNetId,'nwIpxFibHops':nwIpxFibHops,'nwIpxFibTimeTicks':nwIpxFibTimeTicks,'nwIpxFibNextHopIf':nwIpxFibNextHopIf,'nwIpxFibNextHopNet':nwIpxFibNextHopNet,'nwIpxFibNextHopNode':nwIpxFibNextHopNode,'nwIpxFibRouteType':nwIpxFibRouteType,'nwIpxEndSystems':nwIpxEndSystems,'nwIpxHostsSystem':nwIpxHostsSystem,'nwIpxHostsInterfaces':nwIpxHostsInterfaces,'nwIpxHostsToMedia':nwIpxHostsToMedia,'nwIpxHostMapTable':nwIpxHostMapTable,'nwIpxHostMapEntry':nwIpxHostMapEntry,_w:nwIpxHostMapIfIndex,_x:nwIpxHostMapIpxAddr,'nwIpxHostMapPhysAddr':nwIpxHostMapPhysAddr,'nwIpxHostMapType':nwIpxHostMapType,'nwIpxHostMapCircuitID':nwIpxHostMapCircuitID,'nwIpxHostMapFraming':nwIpxHostMapFraming,'nwIpxHostMapPortNumber':nwIpxHostMapPortNumber,'nwIpxAccessControl':nwIpxAccessControl,'nwIpxAclValidEntries':nwIpxAclValidEntries,'nwIpxAclTable':nwIpxAclTable,'nwIpxAclEntry':nwIpxAclEntry,_y:nwIpxAclIdentifier,_z:nwIpxAclSequence,'nwIpxAclPermission':nwIpxAclPermission,'nwIpxAclMatches':nwIpxAclMatches,'nwIpxAclDestNetNum':nwIpxAclDestNetNum,'nwIpxAclDestNode':nwIpxAclDestNode,'nwIpxAclDestSocket':nwIpxAclDestSocket,'nwIpxAclSrcNetNum':nwIpxAclSrcNetNum,'nwIpxAclSrcNode':nwIpxAclSrcNode,'nwIpxAclSrcSocket':nwIpxAclSrcSocket,'nwIpxFilters':nwIpxFilters,'nwIpxRedirector':nwIpxRedirector,'nwIpxNetBIOS':nwIpxNetBIOS,'nwIpxNetBIOSSystem':nwIpxNetBIOSSystem,'nwIpxNetBIOSConfig':nwIpxNetBIOSConfig,'nwIpxNetBIOSAdminStatus':nwIpxNetBIOSAdminStatus,'nwIpxNetBIOSOperStatus':nwIpxNetBIOSOperStatus,'nwIpxNetBIOSAdminReset':nwIpxNetBIOSAdminReset,'nwIpxNetBIOSOperationalTime':nwIpxNetBIOSOperationalTime,'nwIpxNetBIOSVersion':nwIpxNetBIOSVersion,'nwIpxNetBIOSCounters':nwIpxNetBIOSCounters,'nwIpxNetBIOSCtrAdminStatus':nwIpxNetBIOSCtrAdminStatus,'nwIpxNetBIOSCtrReset':nwIpxNetBIOSCtrReset,'nwIpxNetBIOSCtrOperationalTime':nwIpxNetBIOSCtrOperationalTime,'nwIpxNetBIOSCtrInPkts':nwIpxNetBIOSCtrInPkts,'nwIpxNetBIOSCtrOutPkts':nwIpxNetBIOSCtrOutPkts,'nwIpxNetBIOSCtrFilteredPkts':nwIpxNetBIOSCtrFilteredPkts,'nwIpxNetBIOSCtrDiscardPkts':nwIpxNetBIOSCtrDiscardPkts,'nwIpxNetBIOSCtrInBytes':nwIpxNetBIOSCtrInBytes,'nwIpxNetBIOSCtrOutBytes':nwIpxNetBIOSCtrOutBytes,'nwIpxNetBIOSCtrFilteredBytes':nwIpxNetBIOSCtrFilteredBytes,'nwIpxNetBIOSCtrDiscardBytes':nwIpxNetBIOSCtrDiscardBytes,'nwIpxNetBIOSInterface':nwIpxNetBIOSInterface,'nwIpxNetBIOSIfConfig':nwIpxNetBIOSIfConfig,'nwIpxNetBIOSIfTable':nwIpxNetBIOSIfTable,'nwIpxNetBIOSIfEntry':nwIpxNetBIOSIfEntry,_A0:nwIpxNetBIOSIfIndex,'nwIpxNetBIOSIfAdminStatus':nwIpxNetBIOSIfAdminStatus,'nwIpxNetBIOSIfOperStatus':nwIpxNetBIOSIfOperStatus,'nwIpxNetBIOSIfOperationalTime':nwIpxNetBIOSIfOperationalTime,'nwIpxNetBIOSIfCounters':nwIpxNetBIOSIfCounters,'nwIpxNetBIOSIfCtrTable':nwIpxNetBIOSIfCtrTable,'nwIpxNetBIOSIfCtrEntry':nwIpxNetBIOSIfCtrEntry,_A1:nwIpxNetBIOSIfCtrIfIndex,'nwIpxNetBIOSIfCtrAdminStatus':nwIpxNetBIOSIfCtrAdminStatus,'nwIpxNetBIOSIfCtrReset':nwIpxNetBIOSIfCtrReset,'nwIpxNetBIOSIfCtrOperationalTime':nwIpxNetBIOSIfCtrOperationalTime,'nwIpxNetBIOSIfCtrInPkts':nwIpxNetBIOSIfCtrInPkts,'nwIpxNetBIOSIfCtrOutPkts':nwIpxNetBIOSIfCtrOutPkts,'nwIpxNetBIOSIfCtrFilteredPkts':nwIpxNetBIOSIfCtrFilteredPkts,'nwIpxNetBIOSIfCtrDiscardPkts':nwIpxNetBIOSIfCtrDiscardPkts,'nwIpxNetBIOSIfCtrInBytes':nwIpxNetBIOSIfCtrInBytes,'nwIpxNetBIOSIfCtrOutBytes':nwIpxNetBIOSIfCtrOutBytes,'nwIpxNetBIOSIfCtrFilteredBytes':nwIpxNetBIOSIfCtrFilteredBytes,'nwIpxNetBIOSIfCtrDiscardBytes':nwIpxNetBIOSIfCtrDiscardBytes,'nwIpxBroadcast':nwIpxBroadcast,'nwIpxBroadcastSystem':nwIpxBroadcastSystem,'nwIpxBroadcastConfig':nwIpxBroadcastConfig,'nwIpxBcastAdminStatus':nwIpxBcastAdminStatus,'nwIpxBcastOperStatus':nwIpxBcastOperStatus,'nwIpxBcastAdminReset':nwIpxBcastAdminReset,'nwIpxBcastOperationalTime':nwIpxBcastOperationalTime,'nwIpxBcastVersion':nwIpxBcastVersion,'nwIpxBroadcastCounters':nwIpxBroadcastCounters,'nwIpxBcastCtrAdminStatus':nwIpxBcastCtrAdminStatus,'nwIpxBcastCtrReset':nwIpxBcastCtrReset,'nwIpxBcastCtrOperationalTime':nwIpxBcastCtrOperationalTime,'nwIpxBcastCtrInPkts':nwIpxBcastCtrInPkts,'nwIpxBcastCtrOutPkts':nwIpxBcastCtrOutPkts,'nwIpxBcastCtrFilteredPkts':nwIpxBcastCtrFilteredPkts,'nwIpxBcastCtrDiscardPkts':nwIpxBcastCtrDiscardPkts,'nwIpxBcastCtrInBytes':nwIpxBcastCtrInBytes,'nwIpxBcastCtrOutBytes':nwIpxBcastCtrOutBytes,'nwIpxBcastCtrFilteredBytes':nwIpxBcastCtrFilteredBytes,'nwIpxBcastCtrDiscardBytes':nwIpxBcastCtrDiscardBytes,'nwIpxBroadcastInterface':nwIpxBroadcastInterface,'nwIpxBroadcastIfConfig':nwIpxBroadcastIfConfig,'nwIpxBcastIfTable':nwIpxBcastIfTable,'nwIpxBcastIfEntry':nwIpxBcastIfEntry,_A2:nwIpxBcastIfIndex,'nwIpxBcastIfAdminStatus':nwIpxBcastIfAdminStatus,'nwIpxBcastIfOperStatus':nwIpxBcastIfOperStatus,'nwIpxBcastIfOperationalTime':nwIpxBcastIfOperationalTime,'nwIpxBroadcastIfCounters':nwIpxBroadcastIfCounters,'nwIpxBcastIfCtrTable':nwIpxBcastIfCtrTable,'nwIpxBcastIfCtrEntry':nwIpxBcastIfCtrEntry,_A3:nwIpxBcastIfCtrIfIndex,'nwIpxBcastIfCtrAdminStatus':nwIpxBcastIfCtrAdminStatus,'nwIpxBcastIfCtrReset':nwIpxBcastIfCtrReset,'nwIpxBcastIfCtrOperationalTime':nwIpxBcastIfCtrOperationalTime,'nwIpxBcastIfCtrInPkts':nwIpxBcastIfCtrInPkts,'nwIpxBcastIfCtrOutPkts':nwIpxBcastIfCtrOutPkts,'nwIpxBcastIfCtrFilteredPkts':nwIpxBcastIfCtrFilteredPkts,'nwIpxBcastIfCtrDiscardPkts':nwIpxBcastIfCtrDiscardPkts,'nwIpxBcastIfCtrInBytes':nwIpxBcastIfCtrInBytes,'nwIpxBcastIfCtrOutBytes':nwIpxBcastIfCtrOutBytes,'nwIpxBcastIfCtrFilteredBytes':nwIpxBcastIfCtrFilteredBytes,'nwIpxBcastIfCtrDiscardBytes':nwIpxBcastIfCtrDiscardBytes,'nwIpxEcho':nwIpxEcho,'nwIpxEchoSystem':nwIpxEchoSystem,'nwIpxEchoConfig':nwIpxEchoConfig,'nwIpxEchoAdminStatus':nwIpxEchoAdminStatus,'nwIpxEchoOperStatus':nwIpxEchoOperStatus,'nwIpxEchoAdminReset':nwIpxEchoAdminReset,'nwIpxEchoOperationalTime':nwIpxEchoOperationalTime,'nwIpxEchoVersion':nwIpxEchoVersion,'nwIpxEchoCounters':nwIpxEchoCounters,'nwIpxEchoCtrAdminStatus':nwIpxEchoCtrAdminStatus,'nwIpxEchoCtrReset':nwIpxEchoCtrReset,'nwIpxEchoCtrOperationalTime':nwIpxEchoCtrOperationalTime,'nwIpxEchoCtrInPkts':nwIpxEchoCtrInPkts,'nwIpxEchoCtrOutPkts':nwIpxEchoCtrOutPkts,'nwIpxEchoCtrFilteredPkts':nwIpxEchoCtrFilteredPkts,'nwIpxEchoCtrDiscardPkts':nwIpxEchoCtrDiscardPkts,'nwIpxEchoCtrInBytes':nwIpxEchoCtrInBytes,'nwIpxEchoCtrOutBytes':nwIpxEchoCtrOutBytes,'nwIpxEchoCtrFilteredBytes':nwIpxEchoCtrFilteredBytes,'nwIpxEchoSCtrDiscardBytes':nwIpxEchoSCtrDiscardBytes,'nwIpxEchoInterface':nwIpxEchoInterface,'nwIpxEchoIfConfig':nwIpxEchoIfConfig,'nwIpxEchoIfTable':nwIpxEchoIfTable,'nwIpxEchoIfEntry':nwIpxEchoIfEntry,_A4:nwIpxEchoIfIndex,'nwIpxEchoIfAdminStatus':nwIpxEchoIfAdminStatus,'nwIpxEchoIfOperStatus':nwIpxEchoIfOperStatus,'nwIpxEchoIfOperationalTime':nwIpxEchoIfOperationalTime,'nwIpxEchoIfCounters':nwIpxEchoIfCounters,'nwIpxEchoIfCtrTable':nwIpxEchoIfCtrTable,'nwIpxEchoIfCtrEntry':nwIpxEchoIfCtrEntry,_A5:nwIpxEchoIfCtrIfIndex,'nwIpxEchoIfCtrAdminStatus':nwIpxEchoIfCtrAdminStatus,'nwIpxEchoIfCtrReset':nwIpxEchoIfCtrReset,'nwIpxEchoIfCtrOperationalTime':nwIpxEchoIfCtrOperationalTime,'nwIpxEchoIfCtrInPkts':nwIpxEchoIfCtrInPkts,'nwIpxEchoIfCtrOutPkts':nwIpxEchoIfCtrOutPkts,'nwIpxEchoIfCtrFilteredPkts':nwIpxEchoIfCtrFilteredPkts,'nwIpxEchoIfCtrDiscardPkts':nwIpxEchoIfCtrDiscardPkts,'nwIpxEchoIfCtrInBytes':nwIpxEchoIfCtrInBytes,'nwIpxEchoIfCtrOutBytes':nwIpxEchoIfCtrOutBytes,'nwIpxEchoIfCtrFilteredBytes':nwIpxEchoIfCtrFilteredBytes,'nwIpxEchoIfCtrDiscardBytes':nwIpxEchoIfCtrDiscardBytes,'nwIpxEvent':nwIpxEvent,'nwIpxEventLogConfig':nwIpxEventLogConfig,'nwIpxEventAdminStatus':nwIpxEventAdminStatus,'nwIpxEventMaxEntries':nwIpxEventMaxEntries,'nwIpxEventTraceAll':nwIpxEventTraceAll,'nwIpxEventLogFilterTable':nwIpxEventLogFilterTable,'nwIpxEventFilterTable':nwIpxEventFilterTable,'nwIpxEventFilterEntry':nwIpxEventFilterEntry,_A6:nwIpxEventFltrProtocol,_A7:nwIpxEventFltrIfNum,'nwIpxEventFltrControl':nwIpxEventFltrControl,'nwIpxEventFltrType':nwIpxEventFltrType,'nwIpxEventFltrSeverity':nwIpxEventFltrSeverity,'nwIpxEventFltrAction':nwIpxEventFltrAction,'nwIpxEventLogTable':nwIpxEventLogTable,'nwIpxEventTable':nwIpxEventTable,'nwIpxEventEntry':nwIpxEventEntry,_A8:nwIpxEventNumber,'nwIpxEventTime':nwIpxEventTime,'nwIpxEventType':nwIpxEventType,'nwIpxEventSeverity':nwIpxEventSeverity,'nwIpxEventProtocol':nwIpxEventProtocol,'nwIpxEventIfNum':nwIpxEventIfNum,'nwIpxEventTextString':nwIpxEventTextString,'nwIpxWorkGroup':nwIpxWorkGroup})