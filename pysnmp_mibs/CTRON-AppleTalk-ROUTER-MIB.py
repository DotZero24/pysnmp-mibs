_y='nwAtportZoneName'
_x='nwAtportZonePort'
_w='nwAtEventNumber'
_v='highlow'
_u='highmed'
_t='highest'
_s='nwAtEventFltrIfNum'
_r='nwAtEventFltrProtocol'
_q='nwAtAclSequence'
_p='nwAtAclIdentifier'
_o='nwAtHostMapAtAddr'
_n='nwAtHostMapIfIndex'
_m='nwAtHostCtlIfIndex'
_l='nwAtFibStartNet'
_k='nwAtProtoIfCtrIfIndex'
_j='nwAtProtoIfIndex'
_i='nwAtFwdIfCtrIfIndex'
_h='softSeed'
_g='conflictAverseSeed'
_f='guessed'
_e='garnered'
_d='conflictOrientedSeed'
_c='nwAtportIndex'
_b='canonical'
_a='encapfddisnap'
_Z='encapenetsnap'
_Y='encapenet'
_X='nativewan'
_W='ethernet'
_V='delete'
_U='nwAtFwdIfIndex'
_T='invalid-config'
_S='done'
_R='inProgress'
_Q='unconfigured'
_P='noAction'
_O='invalid'
_N='inactive'
_M='enable'
_L='disable'
_K='pending-enable'
_J='pending-disable'
_I='reset'
_H='CTRON-AppleTalk-ROUTER-MIB'
_G='enabled'
_F='disabled'
_E='other'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nwRouter,nwRtrProtoSuites=mibBuilder.importSymbols('ROUTER-OIDS','nwRouter','nwRtrProtoSuites')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class AtNetworkNumber(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
class AtDdpNodeAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
class AtName(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NwAtRouter_ObjectIdentity=ObjectIdentity
nwAtRouter=_NwAtRouter_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4))
_NwAtMibs_ObjectIdentity=ObjectIdentity
nwAtMibs=_NwAtMibs_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,1))
_NwAtMibRevText_Type=DisplayString
_NwAtMibRevText_Object=MibScalar
nwAtMibRevText=_NwAtMibRevText_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,1,1),_NwAtMibRevText_Type())
nwAtMibRevText.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtMibRevText.setStatus(_A)
_NwAtComponents_ObjectIdentity=ObjectIdentity
nwAtComponents=_NwAtComponents_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2))
_NwAtSystem_ObjectIdentity=ObjectIdentity
nwAtSystem=_NwAtSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,1))
_NwAtSysConfig_ObjectIdentity=ObjectIdentity
nwAtSysConfig=_NwAtSysConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,1,1))
_NwAtSysRouterId_Type=AtNetworkNumber
_NwAtSysRouterId_Object=MibScalar
nwAtSysRouterId=_NwAtSysRouterId_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,1,1,1),_NwAtSysRouterId_Type())
nwAtSysRouterId.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtSysRouterId.setStatus(_A)
_NwAtSysAdministration_ObjectIdentity=ObjectIdentity
nwAtSysAdministration=_NwAtSysAdministration_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,1,2))
class _NwAtSysAdminSTATUS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwAtSysAdminSTATUS_Type.__name__=_D
_NwAtSysAdminSTATUS_Object=MibScalar
nwAtSysAdminSTATUS=_NwAtSysAdminSTATUS_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,1,2,1),_NwAtSysAdminSTATUS_Type())
nwAtSysAdminSTATUS.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtSysAdminSTATUS.setStatus(_A)
class _NwAtSysOperSTATUS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_J,4),(_K,5),(_T,6)))
_NwAtSysOperSTATUS_Type.__name__=_D
_NwAtSysOperSTATUS_Object=MibScalar
nwAtSysOperSTATUS=_NwAtSysOperSTATUS_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,1,2,2),_NwAtSysOperSTATUS_Type())
nwAtSysOperSTATUS.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtSysOperSTATUS.setStatus(_A)
class _NwAtSysAdminReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwAtSysAdminReset_Type.__name__=_D
_NwAtSysAdminReset_Object=MibScalar
nwAtSysAdminReset=_NwAtSysAdminReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,1,2,3),_NwAtSysAdminReset_Type())
nwAtSysAdminReset.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtSysAdminReset.setStatus(_A)
_NwAtSysOperationalTime_Type=TimeTicks
_NwAtSysOperationalTime_Object=MibScalar
nwAtSysOperationalTime=_NwAtSysOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,1,2,4),_NwAtSysOperationalTime_Type())
nwAtSysOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtSysOperationalTime.setStatus(_A)
_NwAtSysVersion_Type=DisplayString
_NwAtSysVersion_Object=MibScalar
nwAtSysVersion=_NwAtSysVersion_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,1,2,5),_NwAtSysVersion_Type())
nwAtSysVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtSysVersion.setStatus(_A)
_NwAtForwarding_ObjectIdentity=ObjectIdentity
nwAtForwarding=_NwAtForwarding_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2))
_NwAtFwdSystem_ObjectIdentity=ObjectIdentity
nwAtFwdSystem=_NwAtFwdSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1))
_NwAtFwdCounters_ObjectIdentity=ObjectIdentity
nwAtFwdCounters=_NwAtFwdCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1,1))
class _NwAtFwdCtrAdminSTATUS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwAtFwdCtrAdminSTATUS_Type.__name__=_D
_NwAtFwdCtrAdminSTATUS_Object=MibScalar
nwAtFwdCtrAdminSTATUS=_NwAtFwdCtrAdminSTATUS_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1,1,1),_NwAtFwdCtrAdminSTATUS_Type())
nwAtFwdCtrAdminSTATUS.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtFwdCtrAdminSTATUS.setStatus(_A)
class _NwAtFwdCtrReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwAtFwdCtrReset_Type.__name__=_D
_NwAtFwdCtrReset_Object=MibScalar
nwAtFwdCtrReset=_NwAtFwdCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1,1,2),_NwAtFwdCtrReset_Type())
nwAtFwdCtrReset.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtFwdCtrReset.setStatus(_A)
_NwAtFwdCtrOperationalTime_Type=TimeTicks
_NwAtFwdCtrOperationalTime_Object=MibScalar
nwAtFwdCtrOperationalTime=_NwAtFwdCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1,1,3),_NwAtFwdCtrOperationalTime_Type())
nwAtFwdCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdCtrOperationalTime.setStatus(_A)
_NwAtFwdCtrInPkts_Type=Counter32
_NwAtFwdCtrInPkts_Object=MibScalar
nwAtFwdCtrInPkts=_NwAtFwdCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1,1,4),_NwAtFwdCtrInPkts_Type())
nwAtFwdCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdCtrInPkts.setStatus(_A)
_NwAtFwdCtrOutPkts_Type=Counter32
_NwAtFwdCtrOutPkts_Object=MibScalar
nwAtFwdCtrOutPkts=_NwAtFwdCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1,1,5),_NwAtFwdCtrOutPkts_Type())
nwAtFwdCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdCtrOutPkts.setStatus(_A)
_NwAtFwdCtrFwdPkts_Type=Counter32
_NwAtFwdCtrFwdPkts_Object=MibScalar
nwAtFwdCtrFwdPkts=_NwAtFwdCtrFwdPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1,1,6),_NwAtFwdCtrFwdPkts_Type())
nwAtFwdCtrFwdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdCtrFwdPkts.setStatus(_A)
_NwAtFwdCtrFilteredPkts_Type=Counter32
_NwAtFwdCtrFilteredPkts_Object=MibScalar
nwAtFwdCtrFilteredPkts=_NwAtFwdCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1,1,7),_NwAtFwdCtrFilteredPkts_Type())
nwAtFwdCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdCtrFilteredPkts.setStatus(_A)
_NwAtFwdCtrDiscardPkts_Type=Counter32
_NwAtFwdCtrDiscardPkts_Object=MibScalar
nwAtFwdCtrDiscardPkts=_NwAtFwdCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1,1,8),_NwAtFwdCtrDiscardPkts_Type())
nwAtFwdCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdCtrDiscardPkts.setStatus(_A)
_NwAtFwdCtrAddrErrPkts_Type=Counter32
_NwAtFwdCtrAddrErrPkts_Object=MibScalar
nwAtFwdCtrAddrErrPkts=_NwAtFwdCtrAddrErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1,1,9),_NwAtFwdCtrAddrErrPkts_Type())
nwAtFwdCtrAddrErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdCtrAddrErrPkts.setStatus(_A)
_NwAtFwdCtrLenErrPkts_Type=Counter32
_NwAtFwdCtrLenErrPkts_Object=MibScalar
nwAtFwdCtrLenErrPkts=_NwAtFwdCtrLenErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1,1,10),_NwAtFwdCtrLenErrPkts_Type())
nwAtFwdCtrLenErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdCtrLenErrPkts.setStatus(_A)
_NwAtFwdCtrHdrErrPkts_Type=Counter32
_NwAtFwdCtrHdrErrPkts_Object=MibScalar
nwAtFwdCtrHdrErrPkts=_NwAtFwdCtrHdrErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1,1,11),_NwAtFwdCtrHdrErrPkts_Type())
nwAtFwdCtrHdrErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdCtrHdrErrPkts.setStatus(_A)
_NwAtFwdCtrInBytes_Type=Counter32
_NwAtFwdCtrInBytes_Object=MibScalar
nwAtFwdCtrInBytes=_NwAtFwdCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1,1,12),_NwAtFwdCtrInBytes_Type())
nwAtFwdCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdCtrInBytes.setStatus(_A)
_NwAtFwdCtrOutBytes_Type=Counter32
_NwAtFwdCtrOutBytes_Object=MibScalar
nwAtFwdCtrOutBytes=_NwAtFwdCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1,1,13),_NwAtFwdCtrOutBytes_Type())
nwAtFwdCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdCtrOutBytes.setStatus(_A)
_NwAtFwdCtrFwdBytes_Type=Counter32
_NwAtFwdCtrFwdBytes_Object=MibScalar
nwAtFwdCtrFwdBytes=_NwAtFwdCtrFwdBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1,1,14),_NwAtFwdCtrFwdBytes_Type())
nwAtFwdCtrFwdBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdCtrFwdBytes.setStatus(_A)
_NwAtFwdCtrFilteredBytes_Type=Counter32
_NwAtFwdCtrFilteredBytes_Object=MibScalar
nwAtFwdCtrFilteredBytes=_NwAtFwdCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1,1,15),_NwAtFwdCtrFilteredBytes_Type())
nwAtFwdCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdCtrFilteredBytes.setStatus(_A)
_NwAtFwdCtrDiscardBytes_Type=Counter32
_NwAtFwdCtrDiscardBytes_Object=MibScalar
nwAtFwdCtrDiscardBytes=_NwAtFwdCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1,1,16),_NwAtFwdCtrDiscardBytes_Type())
nwAtFwdCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdCtrDiscardBytes.setStatus(_A)
_NwAtFwdCtrHostInPkts_Type=Counter32
_NwAtFwdCtrHostInPkts_Object=MibScalar
nwAtFwdCtrHostInPkts=_NwAtFwdCtrHostInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1,1,17),_NwAtFwdCtrHostInPkts_Type())
nwAtFwdCtrHostInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdCtrHostInPkts.setStatus(_A)
_NwAtFwdCtrHostOutPkts_Type=Counter32
_NwAtFwdCtrHostOutPkts_Object=MibScalar
nwAtFwdCtrHostOutPkts=_NwAtFwdCtrHostOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1,1,18),_NwAtFwdCtrHostOutPkts_Type())
nwAtFwdCtrHostOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdCtrHostOutPkts.setStatus(_A)
_NwAtFwdCtrHostDiscardPkts_Type=Counter32
_NwAtFwdCtrHostDiscardPkts_Object=MibScalar
nwAtFwdCtrHostDiscardPkts=_NwAtFwdCtrHostDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1,1,19),_NwAtFwdCtrHostDiscardPkts_Type())
nwAtFwdCtrHostDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdCtrHostDiscardPkts.setStatus(_A)
_NwAtFwdCtrHostInBytes_Type=Counter32
_NwAtFwdCtrHostInBytes_Object=MibScalar
nwAtFwdCtrHostInBytes=_NwAtFwdCtrHostInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1,1,20),_NwAtFwdCtrHostInBytes_Type())
nwAtFwdCtrHostInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdCtrHostInBytes.setStatus(_A)
_NwAtFwdCtrHostOutBytes_Type=Counter32
_NwAtFwdCtrHostOutBytes_Object=MibScalar
nwAtFwdCtrHostOutBytes=_NwAtFwdCtrHostOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1,1,21),_NwAtFwdCtrHostOutBytes_Type())
nwAtFwdCtrHostOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdCtrHostOutBytes.setStatus(_A)
_NwAtFwdCtrHostDiscardBytes_Type=Counter32
_NwAtFwdCtrHostDiscardBytes_Object=MibScalar
nwAtFwdCtrHostDiscardBytes=_NwAtFwdCtrHostDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,1,1,22),_NwAtFwdCtrHostDiscardBytes_Type())
nwAtFwdCtrHostDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdCtrHostDiscardBytes.setStatus(_A)
_NwAtFwdInterfaces_ObjectIdentity=ObjectIdentity
nwAtFwdInterfaces=_NwAtFwdInterfaces_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2))
_NwAtFwdIfConfig_ObjectIdentity=ObjectIdentity
nwAtFwdIfConfig=_NwAtFwdIfConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1))
_NwAtFwdIfTable_Object=MibTable
nwAtFwdIfTable=_NwAtFwdIfTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,1))
if mibBuilder.loadTexts:nwAtFwdIfTable.setStatus(_A)
_NwAtFwdIfEntry_Object=MibTableRow
nwAtFwdIfEntry=_NwAtFwdIfEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,1,1))
nwAtFwdIfEntry.setIndexNames((0,_H,_U))
if mibBuilder.loadTexts:nwAtFwdIfEntry.setStatus(_A)
_NwAtFwdIfIndex_Type=Integer32
_NwAtFwdIfIndex_Object=MibTableColumn
nwAtFwdIfIndex=_NwAtFwdIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,1,1,1),_NwAtFwdIfIndex_Type())
nwAtFwdIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfIndex.setStatus(_A)
class _NwAtFwdIfAdminSTATUS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwAtFwdIfAdminSTATUS_Type.__name__=_D
_NwAtFwdIfAdminSTATUS_Object=MibTableColumn
nwAtFwdIfAdminSTATUS=_NwAtFwdIfAdminSTATUS_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,1,1,2),_NwAtFwdIfAdminSTATUS_Type())
nwAtFwdIfAdminSTATUS.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtFwdIfAdminSTATUS.setStatus(_A)
class _NwAtFwdIfOperSTATUS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_J,4),(_K,5),(_T,6)))
_NwAtFwdIfOperSTATUS_Type.__name__=_D
_NwAtFwdIfOperSTATUS_Object=MibTableColumn
nwAtFwdIfOperSTATUS=_NwAtFwdIfOperSTATUS_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,1,1,3),_NwAtFwdIfOperSTATUS_Type())
nwAtFwdIfOperSTATUS.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfOperSTATUS.setStatus(_A)
_NwAtFwdIfOperationalTime_Type=TimeTicks
_NwAtFwdIfOperationalTime_Object=MibTableColumn
nwAtFwdIfOperationalTime=_NwAtFwdIfOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,1,1,4),_NwAtFwdIfOperationalTime_Type())
nwAtFwdIfOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfOperationalTime.setStatus(_A)
class _NwAtFwdIfControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('add',2),(_V,3)))
_NwAtFwdIfControl_Type.__name__=_D
_NwAtFwdIfControl_Object=MibTableColumn
nwAtFwdIfControl=_NwAtFwdIfControl_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,1,1,5),_NwAtFwdIfControl_Type())
nwAtFwdIfControl.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtFwdIfControl.setStatus(_A)
_NwAtFwdIfMtu_Type=Integer32
_NwAtFwdIfMtu_Object=MibTableColumn
nwAtFwdIfMtu=_NwAtFwdIfMtu_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,1,1,6),_NwAtFwdIfMtu_Type())
nwAtFwdIfMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtFwdIfMtu.setStatus(_A)
class _NwAtFwdIfForwarding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwAtFwdIfForwarding_Type.__name__=_D
_NwAtFwdIfForwarding_Object=MibTableColumn
nwAtFwdIfForwarding=_NwAtFwdIfForwarding_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,1,1,7),_NwAtFwdIfForwarding_Type())
nwAtFwdIfForwarding.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtFwdIfForwarding.setStatus(_A)
class _NwAtFwdIfFrameType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,8,9,11,16,17)));namedValues=NamedValues(*((_E,1),(_W,2),('snap',3),(_X,8),(_Y,9),(_Z,11),(_a,16),(_b,17)))
_NwAtFwdIfFrameType_Type.__name__=_D
_NwAtFwdIfFrameType_Object=MibTableColumn
nwAtFwdIfFrameType=_NwAtFwdIfFrameType_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,1,1,8),_NwAtFwdIfFrameType_Type())
nwAtFwdIfFrameType.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtFwdIfFrameType.setStatus(_A)
_NwAtFwdIfAclIdentifier_Type=Integer32
_NwAtFwdIfAclIdentifier_Object=MibTableColumn
nwAtFwdIfAclIdentifier=_NwAtFwdIfAclIdentifier_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,1,1,9),_NwAtFwdIfAclIdentifier_Type())
nwAtFwdIfAclIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtFwdIfAclIdentifier.setStatus(_A)
class _NwAtFwdIfAclSTATUS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwAtFwdIfAclSTATUS_Type.__name__=_D
_NwAtFwdIfAclSTATUS_Object=MibTableColumn
nwAtFwdIfAclSTATUS=_NwAtFwdIfAclSTATUS_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,1,1,10),_NwAtFwdIfAclSTATUS_Type())
nwAtFwdIfAclSTATUS.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtFwdIfAclSTATUS.setStatus(_A)
class _NwAtFwdIfCacheControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_L,2),(_M,3)))
_NwAtFwdIfCacheControl_Type.__name__=_D
_NwAtFwdIfCacheControl_Object=MibTableColumn
nwAtFwdIfCacheControl=_NwAtFwdIfCacheControl_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,1,1,11),_NwAtFwdIfCacheControl_Type())
nwAtFwdIfCacheControl.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtFwdIfCacheControl.setStatus(_A)
_NwAtFwdIfCacheEntries_Type=Counter32
_NwAtFwdIfCacheEntries_Object=MibTableColumn
nwAtFwdIfCacheEntries=_NwAtFwdIfCacheEntries_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,1,1,12),_NwAtFwdIfCacheEntries_Type())
nwAtFwdIfCacheEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCacheEntries.setStatus(_A)
_NwAtFwdIfCacheHits_Type=Counter32
_NwAtFwdIfCacheHits_Object=MibTableColumn
nwAtFwdIfCacheHits=_NwAtFwdIfCacheHits_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,1,1,13),_NwAtFwdIfCacheHits_Type())
nwAtFwdIfCacheHits.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCacheHits.setStatus(_A)
_NwAtFwdIfCacheMisses_Type=Counter32
_NwAtFwdIfCacheMisses_Object=MibTableColumn
nwAtFwdIfCacheMisses=_NwAtFwdIfCacheMisses_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,1,1,14),_NwAtFwdIfCacheMisses_Type())
nwAtFwdIfCacheMisses.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCacheMisses.setStatus(_A)
_NwAtportTable_Object=MibTable
nwAtportTable=_NwAtportTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,2))
if mibBuilder.loadTexts:nwAtportTable.setStatus(_A)
_NwAtportEntry_Object=MibTableRow
nwAtportEntry=_NwAtportEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,2,1))
nwAtportEntry.setIndexNames((0,_H,_c))
if mibBuilder.loadTexts:nwAtportEntry.setStatus(_A)
_NwAtportIndex_Type=Integer32
_NwAtportIndex_Object=MibTableColumn
nwAtportIndex=_NwAtportIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,2,1,1),_NwAtportIndex_Type())
nwAtportIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtportIndex.setStatus(_A)
_NwAtportDescr_Type=DisplayString
_NwAtportDescr_Object=MibTableColumn
nwAtportDescr=_NwAtportDescr_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,2,1,2),_NwAtportDescr_Type())
nwAtportDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtportDescr.setStatus(_A)
class _NwAtportType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*((_E,1),('localtalk',2),('ethertalk1',3),('ethertalk2',4),('tokentalk',5),('iptalk',6),('serialPPP',7),('serialNonstandard',8),('virtual',9),('fdditalk',10),('arctalk',11),('smdstalk',12),('aurp',13),('frameRelay',14),('x25',15),('ip',16),('osi',17),('decnetIV',18),('arap',19),('isdnInThePacketMode',20),('nonAppleTalk3Com',21),('ipx',22),('arns',23),('hdlc',24)))
_NwAtportType_Type.__name__=_D
_NwAtportType_Object=MibTableColumn
nwAtportType=_NwAtportType_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,2,1,3),_NwAtportType_Type())
nwAtportType.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtportType.setStatus(_A)
_NwAtportNetStart_Type=AtNetworkNumber
_NwAtportNetStart_Object=MibTableColumn
nwAtportNetStart=_NwAtportNetStart_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,2,1,4),_NwAtportNetStart_Type())
nwAtportNetStart.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtportNetStart.setStatus(_A)
_NwAtportNetEnd_Type=AtNetworkNumber
_NwAtportNetEnd_Object=MibTableColumn
nwAtportNetEnd=_NwAtportNetEnd_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,2,1,5),_NwAtportNetEnd_Type())
nwAtportNetEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtportNetEnd.setStatus(_A)
_NwAtportNetAddress_Type=AtDdpNodeAddress
_NwAtportNetAddress_Object=MibTableColumn
nwAtportNetAddress=_NwAtportNetAddress_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,2,1,6),_NwAtportNetAddress_Type())
nwAtportNetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtportNetAddress.setStatus(_A)
class _NwAtportSTATUS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('routing',1),(_Q,2),('off',3),(_O,4),('endNode',5),('offDueToConflict',6),(_E,7)))
_NwAtportSTATUS_Type.__name__=_D
_NwAtportSTATUS_Object=MibTableColumn
nwAtportSTATUS=_NwAtportSTATUS_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,2,1,7),_NwAtportSTATUS_Type())
nwAtportSTATUS.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtportSTATUS.setStatus(_A)
class _NwAtportNetConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_d,1),(_e,2),(_f,3),(_Q,4),(_g,5),(_h,6)))
_NwAtportNetConfig_Type.__name__=_D
_NwAtportNetConfig_Object=MibTableColumn
nwAtportNetConfig=_NwAtportNetConfig_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,2,1,8),_NwAtportNetConfig_Type())
nwAtportNetConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtportNetConfig.setStatus(_A)
class _NwAtportZoneConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_d,1),(_e,2),(_f,3),(_Q,4),(_g,5),(_h,6)))
_NwAtportZoneConfig_Type.__name__=_D
_NwAtportZoneConfig_Object=MibTableColumn
nwAtportZoneConfig=_NwAtportZoneConfig_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,2,1,9),_NwAtportZoneConfig_Type())
nwAtportZoneConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtportZoneConfig.setStatus(_A)
_NwAtportZoneDefault_Type=AtName
_NwAtportZoneDefault_Object=MibTableColumn
nwAtportZoneDefault=_NwAtportZoneDefault_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,2,1,10),_NwAtportZoneDefault_Type())
nwAtportZoneDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtportZoneDefault.setStatus(_A)
_NwAtportIfIndex_Type=Integer32
_NwAtportIfIndex_Object=MibTableColumn
nwAtportIfIndex=_NwAtportIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,2,1,11),_NwAtportIfIndex_Type())
nwAtportIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtportIfIndex.setStatus(_A)
_NwAtportNetFrom_Type=AtDdpNodeAddress
_NwAtportNetFrom_Object=MibTableColumn
nwAtportNetFrom=_NwAtportNetFrom_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,2,1,12),_NwAtportNetFrom_Type())
nwAtportNetFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtportNetFrom.setStatus(_A)
_NwAtportZoneFrom_Type=AtDdpNodeAddress
_NwAtportZoneFrom_Object=MibTableColumn
nwAtportZoneFrom=_NwAtportZoneFrom_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,2,1,13),_NwAtportZoneFrom_Type())
nwAtportZoneFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtportZoneFrom.setStatus(_A)
_NwAtportInPkts_Type=Counter32
_NwAtportInPkts_Object=MibTableColumn
nwAtportInPkts=_NwAtportInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,2,1,14),_NwAtportInPkts_Type())
nwAtportInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtportInPkts.setStatus(_A)
_NwAtportOutPkts_Type=Counter32
_NwAtportOutPkts_Object=MibTableColumn
nwAtportOutPkts=_NwAtportOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,2,1,15),_NwAtportOutPkts_Type())
nwAtportOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtportOutPkts.setStatus(_A)
class _NwAtportHome_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('home',1),('notHome',2)))
_NwAtportHome_Type.__name__=_D
_NwAtportHome_Object=MibTableColumn
nwAtportHome=_NwAtportHome_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,2,1,16),_NwAtportHome_Type())
nwAtportHome.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtportHome.setStatus(_A)
_NwAtportCurrentZone_Type=AtName
_NwAtportCurrentZone_Object=MibTableColumn
nwAtportCurrentZone=_NwAtportCurrentZone_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,2,1,17),_NwAtportCurrentZone_Type())
nwAtportCurrentZone.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtportCurrentZone.setStatus(_A)
_NwAtportConflictPhysAddr_Type=OctetString
_NwAtportConflictPhysAddr_Object=MibTableColumn
nwAtportConflictPhysAddr=_NwAtportConflictPhysAddr_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,1,2,1,18),_NwAtportConflictPhysAddr_Type())
nwAtportConflictPhysAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtportConflictPhysAddr.setStatus(_A)
_NwAtFwdIfCounters_ObjectIdentity=ObjectIdentity
nwAtFwdIfCounters=_NwAtFwdIfCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2))
_NwAtFwdIfCtrTable_Object=MibTable
nwAtFwdIfCtrTable=_NwAtFwdIfCtrTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1))
if mibBuilder.loadTexts:nwAtFwdIfCtrTable.setStatus(_A)
_NwAtFwdIfCtrEntry_Object=MibTableRow
nwAtFwdIfCtrEntry=_NwAtFwdIfCtrEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1))
nwAtFwdIfCtrEntry.setIndexNames((0,_H,_i))
if mibBuilder.loadTexts:nwAtFwdIfCtrEntry.setStatus(_A)
_NwAtFwdIfCtrIfIndex_Type=Integer32
_NwAtFwdIfCtrIfIndex_Object=MibTableColumn
nwAtFwdIfCtrIfIndex=_NwAtFwdIfCtrIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1,1),_NwAtFwdIfCtrIfIndex_Type())
nwAtFwdIfCtrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCtrIfIndex.setStatus(_A)
class _NwAtFwdIfCtrAdminSTATUS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwAtFwdIfCtrAdminSTATUS_Type.__name__=_D
_NwAtFwdIfCtrAdminSTATUS_Object=MibTableColumn
nwAtFwdIfCtrAdminSTATUS=_NwAtFwdIfCtrAdminSTATUS_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1,2),_NwAtFwdIfCtrAdminSTATUS_Type())
nwAtFwdIfCtrAdminSTATUS.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtFwdIfCtrAdminSTATUS.setStatus(_A)
class _NwAtFwdIfCtrReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwAtFwdIfCtrReset_Type.__name__=_D
_NwAtFwdIfCtrReset_Object=MibTableColumn
nwAtFwdIfCtrReset=_NwAtFwdIfCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1,3),_NwAtFwdIfCtrReset_Type())
nwAtFwdIfCtrReset.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtFwdIfCtrReset.setStatus(_A)
_NwAtFwdIfCtrOperationalTime_Type=TimeTicks
_NwAtFwdIfCtrOperationalTime_Object=MibTableColumn
nwAtFwdIfCtrOperationalTime=_NwAtFwdIfCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1,4),_NwAtFwdIfCtrOperationalTime_Type())
nwAtFwdIfCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCtrOperationalTime.setStatus(_A)
_NwAtFwdIfCtrInPkts_Type=Counter32
_NwAtFwdIfCtrInPkts_Object=MibTableColumn
nwAtFwdIfCtrInPkts=_NwAtFwdIfCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1,5),_NwAtFwdIfCtrInPkts_Type())
nwAtFwdIfCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCtrInPkts.setStatus(_A)
_NwAtFwdIfCtrOutPkts_Type=Counter32
_NwAtFwdIfCtrOutPkts_Object=MibTableColumn
nwAtFwdIfCtrOutPkts=_NwAtFwdIfCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1,6),_NwAtFwdIfCtrOutPkts_Type())
nwAtFwdIfCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCtrOutPkts.setStatus(_A)
_NwAtFwdIfCtrFwdPkts_Type=Counter32
_NwAtFwdIfCtrFwdPkts_Object=MibTableColumn
nwAtFwdIfCtrFwdPkts=_NwAtFwdIfCtrFwdPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1,7),_NwAtFwdIfCtrFwdPkts_Type())
nwAtFwdIfCtrFwdPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCtrFwdPkts.setStatus(_A)
_NwAtFwdIfCtrFilteredPkts_Type=Counter32
_NwAtFwdIfCtrFilteredPkts_Object=MibTableColumn
nwAtFwdIfCtrFilteredPkts=_NwAtFwdIfCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1,8),_NwAtFwdIfCtrFilteredPkts_Type())
nwAtFwdIfCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCtrFilteredPkts.setStatus(_A)
_NwAtFwdIfCtrDiscardPkts_Type=Counter32
_NwAtFwdIfCtrDiscardPkts_Object=MibTableColumn
nwAtFwdIfCtrDiscardPkts=_NwAtFwdIfCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1,9),_NwAtFwdIfCtrDiscardPkts_Type())
nwAtFwdIfCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCtrDiscardPkts.setStatus(_A)
_NwAtFwdIfCtrAddrErrPkts_Type=Counter32
_NwAtFwdIfCtrAddrErrPkts_Object=MibTableColumn
nwAtFwdIfCtrAddrErrPkts=_NwAtFwdIfCtrAddrErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1,10),_NwAtFwdIfCtrAddrErrPkts_Type())
nwAtFwdIfCtrAddrErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCtrAddrErrPkts.setStatus(_A)
_NwAtFwdIfCtrLenErrPkts_Type=Counter32
_NwAtFwdIfCtrLenErrPkts_Object=MibTableColumn
nwAtFwdIfCtrLenErrPkts=_NwAtFwdIfCtrLenErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1,11),_NwAtFwdIfCtrLenErrPkts_Type())
nwAtFwdIfCtrLenErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCtrLenErrPkts.setStatus(_A)
_NwAtFwdIfCtrHdrErrPkts_Type=Counter32
_NwAtFwdIfCtrHdrErrPkts_Object=MibTableColumn
nwAtFwdIfCtrHdrErrPkts=_NwAtFwdIfCtrHdrErrPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1,12),_NwAtFwdIfCtrHdrErrPkts_Type())
nwAtFwdIfCtrHdrErrPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCtrHdrErrPkts.setStatus(_A)
_NwAtFwdIfCtrInBytes_Type=Counter32
_NwAtFwdIfCtrInBytes_Object=MibTableColumn
nwAtFwdIfCtrInBytes=_NwAtFwdIfCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1,13),_NwAtFwdIfCtrInBytes_Type())
nwAtFwdIfCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCtrInBytes.setStatus(_A)
_NwAtFwdIfCtrOutBytes_Type=Counter32
_NwAtFwdIfCtrOutBytes_Object=MibTableColumn
nwAtFwdIfCtrOutBytes=_NwAtFwdIfCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1,14),_NwAtFwdIfCtrOutBytes_Type())
nwAtFwdIfCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCtrOutBytes.setStatus(_A)
_NwAtFwdIfCtrFwdBytes_Type=Counter32
_NwAtFwdIfCtrFwdBytes_Object=MibTableColumn
nwAtFwdIfCtrFwdBytes=_NwAtFwdIfCtrFwdBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1,15),_NwAtFwdIfCtrFwdBytes_Type())
nwAtFwdIfCtrFwdBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCtrFwdBytes.setStatus(_A)
_NwAtFwdIfCtrFilteredBytes_Type=Counter32
_NwAtFwdIfCtrFilteredBytes_Object=MibTableColumn
nwAtFwdIfCtrFilteredBytes=_NwAtFwdIfCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1,16),_NwAtFwdIfCtrFilteredBytes_Type())
nwAtFwdIfCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCtrFilteredBytes.setStatus(_A)
_NwAtFwdIfCtrDiscardBytes_Type=Counter32
_NwAtFwdIfCtrDiscardBytes_Object=MibTableColumn
nwAtFwdIfCtrDiscardBytes=_NwAtFwdIfCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1,17),_NwAtFwdIfCtrDiscardBytes_Type())
nwAtFwdIfCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCtrDiscardBytes.setStatus(_A)
_NwAtFwdIfCtrHostInPkts_Type=Counter32
_NwAtFwdIfCtrHostInPkts_Object=MibTableColumn
nwAtFwdIfCtrHostInPkts=_NwAtFwdIfCtrHostInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1,18),_NwAtFwdIfCtrHostInPkts_Type())
nwAtFwdIfCtrHostInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCtrHostInPkts.setStatus(_A)
_NwAtFwdIfCtrHostOutPkts_Type=Counter32
_NwAtFwdIfCtrHostOutPkts_Object=MibTableColumn
nwAtFwdIfCtrHostOutPkts=_NwAtFwdIfCtrHostOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1,19),_NwAtFwdIfCtrHostOutPkts_Type())
nwAtFwdIfCtrHostOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCtrHostOutPkts.setStatus(_A)
_NwAtFwdIfCtrHostDiscardPkts_Type=Counter32
_NwAtFwdIfCtrHostDiscardPkts_Object=MibTableColumn
nwAtFwdIfCtrHostDiscardPkts=_NwAtFwdIfCtrHostDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1,20),_NwAtFwdIfCtrHostDiscardPkts_Type())
nwAtFwdIfCtrHostDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCtrHostDiscardPkts.setStatus(_A)
_NwAtFwdIfCtrHostInBytes_Type=Counter32
_NwAtFwdIfCtrHostInBytes_Object=MibTableColumn
nwAtFwdIfCtrHostInBytes=_NwAtFwdIfCtrHostInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1,21),_NwAtFwdIfCtrHostInBytes_Type())
nwAtFwdIfCtrHostInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCtrHostInBytes.setStatus(_A)
_NwAtFwdIfCtrHostOutBytes_Type=Counter32
_NwAtFwdIfCtrHostOutBytes_Object=MibTableColumn
nwAtFwdIfCtrHostOutBytes=_NwAtFwdIfCtrHostOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1,22),_NwAtFwdIfCtrHostOutBytes_Type())
nwAtFwdIfCtrHostOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCtrHostOutBytes.setStatus(_A)
_NwAtFwdIfCtrHostDiscardBytes_Type=Counter32
_NwAtFwdIfCtrHostDiscardBytes_Object=MibTableColumn
nwAtFwdIfCtrHostDiscardBytes=_NwAtFwdIfCtrHostDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,2,2,2,1,1,23),_NwAtFwdIfCtrHostDiscardBytes_Type())
nwAtFwdIfCtrHostDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFwdIfCtrHostDiscardBytes.setStatus(_A)
_NwAtTopology_ObjectIdentity=ObjectIdentity
nwAtTopology=_NwAtTopology_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4))
_NwAtDistanceVector_ObjectIdentity=ObjectIdentity
nwAtDistanceVector=_NwAtDistanceVector_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1))
_NwAtProto_ObjectIdentity=ObjectIdentity
nwAtProto=_NwAtProto_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1))
_NwAtProtoSystem_ObjectIdentity=ObjectIdentity
nwAtProtoSystem=_NwAtProtoSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1))
_NwAtProtoConfig_ObjectIdentity=ObjectIdentity
nwAtProtoConfig=_NwAtProtoConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1,1))
class _NwAtProtoAdminSTATUS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwAtProtoAdminSTATUS_Type.__name__=_D
_NwAtProtoAdminSTATUS_Object=MibScalar
nwAtProtoAdminSTATUS=_NwAtProtoAdminSTATUS_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1,1,1),_NwAtProtoAdminSTATUS_Type())
nwAtProtoAdminSTATUS.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoAdminSTATUS.setStatus(_A)
class _NwAtProtoOperSTATUS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_J,4),(_K,5)))
_NwAtProtoOperSTATUS_Type.__name__=_D
_NwAtProtoOperSTATUS_Object=MibScalar
nwAtProtoOperSTATUS=_NwAtProtoOperSTATUS_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1,1,2),_NwAtProtoOperSTATUS_Type())
nwAtProtoOperSTATUS.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoOperSTATUS.setStatus(_A)
class _NwAtProtoAdminReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwAtProtoAdminReset_Type.__name__=_D
_NwAtProtoAdminReset_Object=MibScalar
nwAtProtoAdminReset=_NwAtProtoAdminReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1,1,3),_NwAtProtoAdminReset_Type())
nwAtProtoAdminReset.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoAdminReset.setStatus(_A)
_NwAtProtoOperationalTime_Type=TimeTicks
_NwAtProtoOperationalTime_Object=MibScalar
nwAtProtoOperationalTime=_NwAtProtoOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1,1,4),_NwAtProtoOperationalTime_Type())
nwAtProtoOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoOperationalTime.setStatus(_A)
_NwAtProtoVersion_Type=DisplayString
_NwAtProtoVersion_Object=MibScalar
nwAtProtoVersion=_NwAtProtoVersion_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1,1,5),_NwAtProtoVersion_Type())
nwAtProtoVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoVersion.setStatus(_A)
_NwAtProtoStackSize_Type=Integer32
_NwAtProtoStackSize_Object=MibScalar
nwAtProtoStackSize=_NwAtProtoStackSize_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1,1,6),_NwAtProtoStackSize_Type())
nwAtProtoStackSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoStackSize.setStatus(_A)
_NwAtProtoThreadPriority_Type=Integer32
_NwAtProtoThreadPriority_Object=MibScalar
nwAtProtoThreadPriority=_NwAtProtoThreadPriority_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1,1,7),_NwAtProtoThreadPriority_Type())
nwAtProtoThreadPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoThreadPriority.setStatus(_A)
_NwAtProtoDatabaseThreshold_Type=Integer32
_NwAtProtoDatabaseThreshold_Object=MibScalar
nwAtProtoDatabaseThreshold=_NwAtProtoDatabaseThreshold_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1,1,8),_NwAtProtoDatabaseThreshold_Type())
nwAtProtoDatabaseThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoDatabaseThreshold.setStatus(_A)
_NwAtProtoAgeOut_Type=Integer32
_NwAtProtoAgeOut_Object=MibScalar
nwAtProtoAgeOut=_NwAtProtoAgeOut_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1,1,9),_NwAtProtoAgeOut_Type())
nwAtProtoAgeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoAgeOut.setStatus(_A)
_NwAtProtoHoldDown_Type=Integer32
_NwAtProtoHoldDown_Object=MibScalar
nwAtProtoHoldDown=_NwAtProtoHoldDown_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1,1,10),_NwAtProtoHoldDown_Type())
nwAtProtoHoldDown.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoHoldDown.setStatus(_A)
_NwAtProtoCounters_ObjectIdentity=ObjectIdentity
nwAtProtoCounters=_NwAtProtoCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1,2))
class _NwAtProtoCtrAdminSTATUS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwAtProtoCtrAdminSTATUS_Type.__name__=_D
_NwAtProtoCtrAdminSTATUS_Object=MibScalar
nwAtProtoCtrAdminSTATUS=_NwAtProtoCtrAdminSTATUS_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1,2,1),_NwAtProtoCtrAdminSTATUS_Type())
nwAtProtoCtrAdminSTATUS.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoCtrAdminSTATUS.setStatus(_A)
class _NwAtProtoCtrReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwAtProtoCtrReset_Type.__name__=_D
_NwAtProtoCtrReset_Object=MibScalar
nwAtProtoCtrReset=_NwAtProtoCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1,2,2),_NwAtProtoCtrReset_Type())
nwAtProtoCtrReset.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoCtrReset.setStatus(_A)
_NwAtProtoCtrOperationalTime_Type=TimeTicks
_NwAtProtoCtrOperationalTime_Object=MibScalar
nwAtProtoCtrOperationalTime=_NwAtProtoCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1,2,3),_NwAtProtoCtrOperationalTime_Type())
nwAtProtoCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoCtrOperationalTime.setStatus(_A)
_NwAtProtoCtrInPkts_Type=Counter32
_NwAtProtoCtrInPkts_Object=MibScalar
nwAtProtoCtrInPkts=_NwAtProtoCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1,2,4),_NwAtProtoCtrInPkts_Type())
nwAtProtoCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoCtrInPkts.setStatus(_A)
_NwAtProtoCtrOutPkts_Type=Counter32
_NwAtProtoCtrOutPkts_Object=MibScalar
nwAtProtoCtrOutPkts=_NwAtProtoCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1,2,5),_NwAtProtoCtrOutPkts_Type())
nwAtProtoCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoCtrOutPkts.setStatus(_A)
_NwAtProtoCtrFilteredPkts_Type=Counter32
_NwAtProtoCtrFilteredPkts_Object=MibScalar
nwAtProtoCtrFilteredPkts=_NwAtProtoCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1,2,6),_NwAtProtoCtrFilteredPkts_Type())
nwAtProtoCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoCtrFilteredPkts.setStatus(_A)
_NwAtProtoCtrDiscardPkts_Type=Counter32
_NwAtProtoCtrDiscardPkts_Object=MibScalar
nwAtProtoCtrDiscardPkts=_NwAtProtoCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1,2,7),_NwAtProtoCtrDiscardPkts_Type())
nwAtProtoCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoCtrDiscardPkts.setStatus(_A)
_NwAtProtoCtrInBytes_Type=Counter32
_NwAtProtoCtrInBytes_Object=MibScalar
nwAtProtoCtrInBytes=_NwAtProtoCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1,2,8),_NwAtProtoCtrInBytes_Type())
nwAtProtoCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoCtrInBytes.setStatus(_A)
_NwAtProtoCtrOutBytes_Type=Counter32
_NwAtProtoCtrOutBytes_Object=MibScalar
nwAtProtoCtrOutBytes=_NwAtProtoCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1,2,9),_NwAtProtoCtrOutBytes_Type())
nwAtProtoCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoCtrOutBytes.setStatus(_A)
_NwAtProtoCtrFilteredBytes_Type=Counter32
_NwAtProtoCtrFilteredBytes_Object=MibScalar
nwAtProtoCtrFilteredBytes=_NwAtProtoCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1,2,10),_NwAtProtoCtrFilteredBytes_Type())
nwAtProtoCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoCtrFilteredBytes.setStatus(_A)
_NwAtProtoCtrDiscardBytes_Type=Counter32
_NwAtProtoCtrDiscardBytes_Object=MibScalar
nwAtProtoCtrDiscardBytes=_NwAtProtoCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,1,2,11),_NwAtProtoCtrDiscardBytes_Type())
nwAtProtoCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoCtrDiscardBytes.setStatus(_A)
_NwAtProtoInterface_ObjectIdentity=ObjectIdentity
nwAtProtoInterface=_NwAtProtoInterface_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2))
_NwAtProtoIfConfig_ObjectIdentity=ObjectIdentity
nwAtProtoIfConfig=_NwAtProtoIfConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,1))
_NwAtProtoIfTable_Object=MibTable
nwAtProtoIfTable=_NwAtProtoIfTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,1,1))
if mibBuilder.loadTexts:nwAtProtoIfTable.setStatus(_A)
_NwAtProtoIfEntry_Object=MibTableRow
nwAtProtoIfEntry=_NwAtProtoIfEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,1,1,1))
nwAtProtoIfEntry.setIndexNames((0,_H,_j))
if mibBuilder.loadTexts:nwAtProtoIfEntry.setStatus(_A)
_NwAtProtoIfIndex_Type=Integer32
_NwAtProtoIfIndex_Object=MibTableColumn
nwAtProtoIfIndex=_NwAtProtoIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,1,1,1,1),_NwAtProtoIfIndex_Type())
nwAtProtoIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoIfIndex.setStatus(_A)
class _NwAtProtoIfAdminSTATUS_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwAtProtoIfAdminSTATUS_Type.__name__=_D
_NwAtProtoIfAdminSTATUS_Object=MibTableColumn
nwAtProtoIfAdminSTATUS=_NwAtProtoIfAdminSTATUS_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,1,1,1,2),_NwAtProtoIfAdminSTATUS_Type())
nwAtProtoIfAdminSTATUS.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoIfAdminSTATUS.setStatus(_A)
class _NwAtProtoIfOperSTATUS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_J,4),(_K,5)))
_NwAtProtoIfOperSTATUS_Type.__name__=_D
_NwAtProtoIfOperSTATUS_Object=MibTableColumn
nwAtProtoIfOperSTATUS=_NwAtProtoIfOperSTATUS_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,1,1,1,3),_NwAtProtoIfOperSTATUS_Type())
nwAtProtoIfOperSTATUS.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoIfOperSTATUS.setStatus(_A)
_NwAtProtoIfOperationalTime_Type=TimeTicks
_NwAtProtoIfOperationalTime_Object=MibTableColumn
nwAtProtoIfOperationalTime=_NwAtProtoIfOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,1,1,1,4),_NwAtProtoIfOperationalTime_Type())
nwAtProtoIfOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoIfOperationalTime.setStatus(_A)
_NwAtProtoIfVersion_Type=Integer32
_NwAtProtoIfVersion_Object=MibTableColumn
nwAtProtoIfVersion=_NwAtProtoIfVersion_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,1,1,1,5),_NwAtProtoIfVersion_Type())
nwAtProtoIfVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoIfVersion.setStatus(_A)
class _NwAtProtoIfAdvertisement_Type(Integer32):defaultValue=60
_NwAtProtoIfAdvertisement_Type.__name__=_D
_NwAtProtoIfAdvertisement_Object=MibTableColumn
nwAtProtoIfAdvertisement=_NwAtProtoIfAdvertisement_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,1,1,1,6),_NwAtProtoIfAdvertisement_Type())
nwAtProtoIfAdvertisement.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoIfAdvertisement.setStatus(_A)
_NwAtProtoIfFloodDelay_Type=Integer32
_NwAtProtoIfFloodDelay_Object=MibTableColumn
nwAtProtoIfFloodDelay=_NwAtProtoIfFloodDelay_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,1,1,1,7),_NwAtProtoIfFloodDelay_Type())
nwAtProtoIfFloodDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoIfFloodDelay.setStatus(_A)
_NwAtProtoIfRequestDelay_Type=Integer32
_NwAtProtoIfRequestDelay_Object=MibTableColumn
nwAtProtoIfRequestDelay=_NwAtProtoIfRequestDelay_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,1,1,1,8),_NwAtProtoIfRequestDelay_Type())
nwAtProtoIfRequestDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoIfRequestDelay.setStatus(_A)
_NwAtProtoIfPriority_Type=Integer32
_NwAtProtoIfPriority_Object=MibTableColumn
nwAtProtoIfPriority=_NwAtProtoIfPriority_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,1,1,1,9),_NwAtProtoIfPriority_Type())
nwAtProtoIfPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoIfPriority.setStatus(_A)
_NwAtProtoIfHelloTimer_Type=Integer32
_NwAtProtoIfHelloTimer_Object=MibTableColumn
nwAtProtoIfHelloTimer=_NwAtProtoIfHelloTimer_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,1,1,1,10),_NwAtProtoIfHelloTimer_Type())
nwAtProtoIfHelloTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoIfHelloTimer.setStatus(_A)
class _NwAtProtoIfSplitHorizon_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwAtProtoIfSplitHorizon_Type.__name__=_D
_NwAtProtoIfSplitHorizon_Object=MibTableColumn
nwAtProtoIfSplitHorizon=_NwAtProtoIfSplitHorizon_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,1,1,1,11),_NwAtProtoIfSplitHorizon_Type())
nwAtProtoIfSplitHorizon.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoIfSplitHorizon.setStatus(_A)
class _NwAtProtoIfPoisonReverse_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwAtProtoIfPoisonReverse_Type.__name__=_D
_NwAtProtoIfPoisonReverse_Object=MibTableColumn
nwAtProtoIfPoisonReverse=_NwAtProtoIfPoisonReverse_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,1,1,1,12),_NwAtProtoIfPoisonReverse_Type())
nwAtProtoIfPoisonReverse.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoIfPoisonReverse.setStatus(_A)
class _NwAtProtoIfSnooping_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwAtProtoIfSnooping_Type.__name__=_D
_NwAtProtoIfSnooping_Object=MibTableColumn
nwAtProtoIfSnooping=_NwAtProtoIfSnooping_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,1,1,1,13),_NwAtProtoIfSnooping_Type())
nwAtProtoIfSnooping.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoIfSnooping.setStatus(_A)
class _NwAtProtoIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('bma',2),('nbma',3)))
_NwAtProtoIfType_Type.__name__=_D
_NwAtProtoIfType_Object=MibTableColumn
nwAtProtoIfType=_NwAtProtoIfType_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,1,1,1,14),_NwAtProtoIfType_Type())
nwAtProtoIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoIfType.setStatus(_A)
_NwAtProtoIfXmitCost_Type=Integer32
_NwAtProtoIfXmitCost_Object=MibTableColumn
nwAtProtoIfXmitCost=_NwAtProtoIfXmitCost_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,1,1,1,15),_NwAtProtoIfXmitCost_Type())
nwAtProtoIfXmitCost.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoIfXmitCost.setStatus(_A)
_NwAtProtoIfAclIdentifier_Type=Integer32
_NwAtProtoIfAclIdentifier_Object=MibTableColumn
nwAtProtoIfAclIdentifier=_NwAtProtoIfAclIdentifier_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,1,1,1,16),_NwAtProtoIfAclIdentifier_Type())
nwAtProtoIfAclIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoIfAclIdentifier.setStatus(_A)
class _NwAtProtoIfAclSTATUS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwAtProtoIfAclSTATUS_Type.__name__=_D
_NwAtProtoIfAclSTATUS_Object=MibTableColumn
nwAtProtoIfAclSTATUS=_NwAtProtoIfAclSTATUS_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,1,1,1,17),_NwAtProtoIfAclSTATUS_Type())
nwAtProtoIfAclSTATUS.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoIfAclSTATUS.setStatus(_A)
_NwAtProtoIfCounters_ObjectIdentity=ObjectIdentity
nwAtProtoIfCounters=_NwAtProtoIfCounters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,2))
_NwAtProtoIfCtrTable_Object=MibTable
nwAtProtoIfCtrTable=_NwAtProtoIfCtrTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,2,1))
if mibBuilder.loadTexts:nwAtProtoIfCtrTable.setStatus(_A)
_NwAtProtoIfCtrEntry_Object=MibTableRow
nwAtProtoIfCtrEntry=_NwAtProtoIfCtrEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,2,1,1))
nwAtProtoIfCtrEntry.setIndexNames((0,_H,_k))
if mibBuilder.loadTexts:nwAtProtoIfCtrEntry.setStatus(_A)
_NwAtProtoIfCtrIfIndex_Type=Integer32
_NwAtProtoIfCtrIfIndex_Object=MibTableColumn
nwAtProtoIfCtrIfIndex=_NwAtProtoIfCtrIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,2,1,1,1),_NwAtProtoIfCtrIfIndex_Type())
nwAtProtoIfCtrIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoIfCtrIfIndex.setStatus(_A)
class _NwAtProtoIfCtrAdminSTATUS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwAtProtoIfCtrAdminSTATUS_Type.__name__=_D
_NwAtProtoIfCtrAdminSTATUS_Object=MibTableColumn
nwAtProtoIfCtrAdminSTATUS=_NwAtProtoIfCtrAdminSTATUS_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,2,1,1,2),_NwAtProtoIfCtrAdminSTATUS_Type())
nwAtProtoIfCtrAdminSTATUS.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoIfCtrAdminSTATUS.setStatus(_A)
class _NwAtProtoIfCtrReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_I,2)))
_NwAtProtoIfCtrReset_Type.__name__=_D
_NwAtProtoIfCtrReset_Object=MibTableColumn
nwAtProtoIfCtrReset=_NwAtProtoIfCtrReset_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,2,1,1,3),_NwAtProtoIfCtrReset_Type())
nwAtProtoIfCtrReset.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtProtoIfCtrReset.setStatus(_A)
_NwAtProtoIfCtrOperationalTime_Type=TimeTicks
_NwAtProtoIfCtrOperationalTime_Object=MibTableColumn
nwAtProtoIfCtrOperationalTime=_NwAtProtoIfCtrOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,2,1,1,4),_NwAtProtoIfCtrOperationalTime_Type())
nwAtProtoIfCtrOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoIfCtrOperationalTime.setStatus(_A)
_NwAtProtoIfCtrInPkts_Type=Counter32
_NwAtProtoIfCtrInPkts_Object=MibTableColumn
nwAtProtoIfCtrInPkts=_NwAtProtoIfCtrInPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,2,1,1,5),_NwAtProtoIfCtrInPkts_Type())
nwAtProtoIfCtrInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoIfCtrInPkts.setStatus(_A)
_NwAtProtoIfCtrOutPkts_Type=Counter32
_NwAtProtoIfCtrOutPkts_Object=MibTableColumn
nwAtProtoIfCtrOutPkts=_NwAtProtoIfCtrOutPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,2,1,1,6),_NwAtProtoIfCtrOutPkts_Type())
nwAtProtoIfCtrOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoIfCtrOutPkts.setStatus(_A)
_NwAtProtoIfCtrFilteredPkts_Type=Counter32
_NwAtProtoIfCtrFilteredPkts_Object=MibTableColumn
nwAtProtoIfCtrFilteredPkts=_NwAtProtoIfCtrFilteredPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,2,1,1,7),_NwAtProtoIfCtrFilteredPkts_Type())
nwAtProtoIfCtrFilteredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoIfCtrFilteredPkts.setStatus(_A)
_NwAtProtoIfCtrDiscardPkts_Type=Counter32
_NwAtProtoIfCtrDiscardPkts_Object=MibTableColumn
nwAtProtoIfCtrDiscardPkts=_NwAtProtoIfCtrDiscardPkts_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,2,1,1,8),_NwAtProtoIfCtrDiscardPkts_Type())
nwAtProtoIfCtrDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoIfCtrDiscardPkts.setStatus(_A)
_NwAtProtoIfCtrInBytes_Type=Counter32
_NwAtProtoIfCtrInBytes_Object=MibTableColumn
nwAtProtoIfCtrInBytes=_NwAtProtoIfCtrInBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,2,1,1,9),_NwAtProtoIfCtrInBytes_Type())
nwAtProtoIfCtrInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoIfCtrInBytes.setStatus(_A)
_NwAtProtoIfCtrOutBytes_Type=Counter32
_NwAtProtoIfCtrOutBytes_Object=MibTableColumn
nwAtProtoIfCtrOutBytes=_NwAtProtoIfCtrOutBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,2,1,1,10),_NwAtProtoIfCtrOutBytes_Type())
nwAtProtoIfCtrOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoIfCtrOutBytes.setStatus(_A)
_NwAtProtoIfCtrFilteredBytes_Type=Counter32
_NwAtProtoIfCtrFilteredBytes_Object=MibTableColumn
nwAtProtoIfCtrFilteredBytes=_NwAtProtoIfCtrFilteredBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,2,1,1,11),_NwAtProtoIfCtrFilteredBytes_Type())
nwAtProtoIfCtrFilteredBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoIfCtrFilteredBytes.setStatus(_A)
_NwAtProtoIfCtrDiscardBytes_Type=Counter32
_NwAtProtoIfCtrDiscardBytes_Object=MibTableColumn
nwAtProtoIfCtrDiscardBytes=_NwAtProtoIfCtrDiscardBytes_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,1,1,2,2,1,1,12),_NwAtProtoIfCtrDiscardBytes_Type())
nwAtProtoIfCtrDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtProtoIfCtrDiscardBytes.setStatus(_A)
_NwAtLinkState_ObjectIdentity=ObjectIdentity
nwAtLinkState=_NwAtLinkState_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,4,2))
_NwAtFib_ObjectIdentity=ObjectIdentity
nwAtFib=_NwAtFib_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,5))
_NwAtFibTable_Object=MibTable
nwAtFibTable=_NwAtFibTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,5,1))
if mibBuilder.loadTexts:nwAtFibTable.setStatus(_A)
_NwAtFibEntry_Object=MibTableRow
nwAtFibEntry=_NwAtFibEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,5,1,1))
nwAtFibEntry.setIndexNames((0,_H,_l))
if mibBuilder.loadTexts:nwAtFibEntry.setStatus(_A)
_NwAtFibStartNet_Type=AtNetworkNumber
_NwAtFibStartNet_Object=MibTableColumn
nwAtFibStartNet=_NwAtFibStartNet_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,5,1,1,1),_NwAtFibStartNet_Type())
nwAtFibStartNet.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFibStartNet.setStatus(_A)
_NwAtFibEndNet_Type=AtNetworkNumber
_NwAtFibEndNet_Object=MibTableColumn
nwAtFibEndNet=_NwAtFibEndNet_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,5,1,1,2),_NwAtFibEndNet_Type())
nwAtFibEndNet.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFibEndNet.setStatus(_A)
_NwAtFibNextHop_Type=AtDdpNodeAddress
_NwAtFibNextHop_Object=MibTableColumn
nwAtFibNextHop=_NwAtFibNextHop_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,5,1,1,3),_NwAtFibNextHop_Type())
nwAtFibNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFibNextHop.setStatus(_A)
_NwAtFibNextHopIf_Type=Integer32
_NwAtFibNextHopIf_Object=MibTableColumn
nwAtFibNextHopIf=_NwAtFibNextHopIf_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,5,1,1,4),_NwAtFibNextHopIf_Type())
nwAtFibNextHopIf.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFibNextHopIf.setStatus(_A)
_NwAtFibHops_Type=Integer32
_NwAtFibHops_Object=MibTableColumn
nwAtFibHops=_NwAtFibHops_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,5,1,1,5),_NwAtFibHops_Type())
nwAtFibHops.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFibHops.setStatus(_A)
class _NwAtFibRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),('appleTalk',2)))
_NwAtFibRouteType_Type.__name__=_D
_NwAtFibRouteType_Object=MibTableColumn
nwAtFibRouteType=_NwAtFibRouteType_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,5,1,1,6),_NwAtFibRouteType_Type())
nwAtFibRouteType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtFibRouteType.setStatus(_A)
_NwAtEndSystems_ObjectIdentity=ObjectIdentity
nwAtEndSystems=_NwAtEndSystems_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6))
_NwAtHostsSystem_ObjectIdentity=ObjectIdentity
nwAtHostsSystem=_NwAtHostsSystem_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,1))
_NwAtHostsTimeToLive_Type=Integer32
_NwAtHostsTimeToLive_Object=MibScalar
nwAtHostsTimeToLive=_NwAtHostsTimeToLive_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,1,1),_NwAtHostsTimeToLive_Type())
nwAtHostsTimeToLive.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtHostsTimeToLive.setStatus(_A)
_NwAtHostsRetryCount_Type=Counter32
_NwAtHostsRetryCount_Object=MibScalar
nwAtHostsRetryCount=_NwAtHostsRetryCount_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,1,2),_NwAtHostsRetryCount_Type())
nwAtHostsRetryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtHostsRetryCount.setStatus(_A)
_NwAtHostsInterfaces_ObjectIdentity=ObjectIdentity
nwAtHostsInterfaces=_NwAtHostsInterfaces_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,2))
_NwAtHostCtlTable_Object=MibTable
nwAtHostCtlTable=_NwAtHostCtlTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,2,1))
if mibBuilder.loadTexts:nwAtHostCtlTable.setStatus(_A)
_NwAtHostCtlEntry_Object=MibTableRow
nwAtHostCtlEntry=_NwAtHostCtlEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,2,1,1))
nwAtHostCtlEntry.setIndexNames((0,_H,_m))
if mibBuilder.loadTexts:nwAtHostCtlEntry.setStatus(_A)
_NwAtHostCtlIfIndex_Type=Integer32
_NwAtHostCtlIfIndex_Object=MibTableColumn
nwAtHostCtlIfIndex=_NwAtHostCtlIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,2,1,1,1),_NwAtHostCtlIfIndex_Type())
nwAtHostCtlIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtHostCtlIfIndex.setStatus(_A)
class _NwAtHostCtlAdminSTATUS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_L,2),(_M,3)))
_NwAtHostCtlAdminSTATUS_Type.__name__=_D
_NwAtHostCtlAdminSTATUS_Object=MibTableColumn
nwAtHostCtlAdminSTATUS=_NwAtHostCtlAdminSTATUS_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,2,1,1,2),_NwAtHostCtlAdminSTATUS_Type())
nwAtHostCtlAdminSTATUS.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtHostCtlAdminSTATUS.setStatus(_A)
class _NwAtHostCtlOperSTATUS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_J,4),(_K,5)))
_NwAtHostCtlOperSTATUS_Type.__name__=_D
_NwAtHostCtlOperSTATUS_Object=MibTableColumn
nwAtHostCtlOperSTATUS=_NwAtHostCtlOperSTATUS_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,2,1,1,3),_NwAtHostCtlOperSTATUS_Type())
nwAtHostCtlOperSTATUS.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtHostCtlOperSTATUS.setStatus(_A)
_NwAtHostCtlOperationalTime_Type=TimeTicks
_NwAtHostCtlOperationalTime_Object=MibTableColumn
nwAtHostCtlOperationalTime=_NwAtHostCtlOperationalTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,2,1,1,4),_NwAtHostCtlOperationalTime_Type())
nwAtHostCtlOperationalTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtHostCtlOperationalTime.setStatus(_A)
class _NwAtHostCtlProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_L,2),(_M,3)))
_NwAtHostCtlProtocol_Type.__name__=_D
_NwAtHostCtlProtocol_Object=MibTableColumn
nwAtHostCtlProtocol=_NwAtHostCtlProtocol_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,2,1,1,5),_NwAtHostCtlProtocol_Type())
nwAtHostCtlProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtHostCtlProtocol.setStatus(_A)
class _NwAtHostCtlSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_L,2),(_M,3)))
_NwAtHostCtlSnooping_Type.__name__=_D
_NwAtHostCtlSnooping_Object=MibTableColumn
nwAtHostCtlSnooping=_NwAtHostCtlSnooping_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,2,1,1,6),_NwAtHostCtlSnooping_Type())
nwAtHostCtlSnooping.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtHostCtlSnooping.setStatus(_A)
class _NwAtHostCtlProxy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_L,2),(_M,3)))
_NwAtHostCtlProxy_Type.__name__=_D
_NwAtHostCtlProxy_Object=MibTableColumn
nwAtHostCtlProxy=_NwAtHostCtlProxy_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,2,1,1,7),_NwAtHostCtlProxy_Type())
nwAtHostCtlProxy.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtHostCtlProxy.setStatus(_A)
_NwAtHostCtlCacheMax_Type=Integer32
_NwAtHostCtlCacheMax_Object=MibTableColumn
nwAtHostCtlCacheMax=_NwAtHostCtlCacheMax_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,2,1,1,8),_NwAtHostCtlCacheMax_Type())
nwAtHostCtlCacheMax.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtHostCtlCacheMax.setStatus(_A)
_NwAtHostCtlCacheSize_Type=Integer32
_NwAtHostCtlCacheSize_Object=MibTableColumn
nwAtHostCtlCacheSize=_NwAtHostCtlCacheSize_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,2,1,1,9),_NwAtHostCtlCacheSize_Type())
nwAtHostCtlCacheSize.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtHostCtlCacheSize.setStatus(_A)
_NwAtHostCtlNumStatics_Type=Counter32
_NwAtHostCtlNumStatics_Object=MibTableColumn
nwAtHostCtlNumStatics=_NwAtHostCtlNumStatics_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,2,1,1,10),_NwAtHostCtlNumStatics_Type())
nwAtHostCtlNumStatics.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtHostCtlNumStatics.setStatus(_A)
_NwAtHostCtlNumDynamics_Type=Counter32
_NwAtHostCtlNumDynamics_Object=MibTableColumn
nwAtHostCtlNumDynamics=_NwAtHostCtlNumDynamics_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,2,1,1,11),_NwAtHostCtlNumDynamics_Type())
nwAtHostCtlNumDynamics.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtHostCtlNumDynamics.setStatus(_A)
_NwAtHostCtlCacheHits_Type=Counter32
_NwAtHostCtlCacheHits_Object=MibTableColumn
nwAtHostCtlCacheHits=_NwAtHostCtlCacheHits_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,2,1,1,12),_NwAtHostCtlCacheHits_Type())
nwAtHostCtlCacheHits.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtHostCtlCacheHits.setStatus(_A)
_NwAtHostCtlCacheMisses_Type=Counter32
_NwAtHostCtlCacheMisses_Object=MibTableColumn
nwAtHostCtlCacheMisses=_NwAtHostCtlCacheMisses_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,2,1,1,13),_NwAtHostCtlCacheMisses_Type())
nwAtHostCtlCacheMisses.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtHostCtlCacheMisses.setStatus(_A)
_NwAtHostsToMedia_ObjectIdentity=ObjectIdentity
nwAtHostsToMedia=_NwAtHostsToMedia_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,3))
_NwAtHostMapTable_Object=MibTable
nwAtHostMapTable=_NwAtHostMapTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,3,1))
if mibBuilder.loadTexts:nwAtHostMapTable.setStatus(_A)
_NwAtHostMapEntry_Object=MibTableRow
nwAtHostMapEntry=_NwAtHostMapEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,3,1,1))
nwAtHostMapEntry.setIndexNames((0,_H,_n),(0,_H,_o))
if mibBuilder.loadTexts:nwAtHostMapEntry.setStatus(_A)
_NwAtHostMapIfIndex_Type=Integer32
_NwAtHostMapIfIndex_Object=MibTableColumn
nwAtHostMapIfIndex=_NwAtHostMapIfIndex_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,3,1,1,1),_NwAtHostMapIfIndex_Type())
nwAtHostMapIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtHostMapIfIndex.setStatus(_A)
_NwAtHostMapAtAddr_Type=AtDdpNodeAddress
_NwAtHostMapAtAddr_Object=MibTableColumn
nwAtHostMapAtAddr=_NwAtHostMapAtAddr_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,3,1,1,2),_NwAtHostMapAtAddr_Type())
nwAtHostMapAtAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtHostMapAtAddr.setStatus(_A)
_NwAtHostMapPhysAddr_Type=PhysAddress
_NwAtHostMapPhysAddr_Object=MibTableColumn
nwAtHostMapPhysAddr=_NwAtHostMapPhysAddr_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,3,1,1,3),_NwAtHostMapPhysAddr_Type())
nwAtHostMapPhysAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtHostMapPhysAddr.setStatus(_A)
class _NwAtHostMapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_O,2),('dynamic',3),('static',4),(_N,5)))
_NwAtHostMapType_Type.__name__=_D
_NwAtHostMapType_Object=MibTableColumn
nwAtHostMapType=_NwAtHostMapType_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,3,1,1,4),_NwAtHostMapType_Type())
nwAtHostMapType.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtHostMapType.setStatus(_A)
_NwAtHostMapCircuitID_Type=Integer32
_NwAtHostMapCircuitID_Object=MibTableColumn
nwAtHostMapCircuitID=_NwAtHostMapCircuitID_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,3,1,1,5),_NwAtHostMapCircuitID_Type())
nwAtHostMapCircuitID.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtHostMapCircuitID.setStatus(_A)
class _NwAtHostMapFraming_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,8,9,11,16,17)));namedValues=NamedValues(*((_E,1),(_W,2),('snap',3),(_X,8),(_Y,9),(_Z,11),(_a,16),(_b,17)))
_NwAtHostMapFraming_Type.__name__=_D
_NwAtHostMapFraming_Object=MibTableColumn
nwAtHostMapFraming=_NwAtHostMapFraming_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,3,1,1,6),_NwAtHostMapFraming_Type())
nwAtHostMapFraming.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtHostMapFraming.setStatus(_A)
_NwAtHostMapPortNumber_Type=Integer32
_NwAtHostMapPortNumber_Object=MibTableColumn
nwAtHostMapPortNumber=_NwAtHostMapPortNumber_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,6,3,1,1,7),_NwAtHostMapPortNumber_Type())
nwAtHostMapPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtHostMapPortNumber.setStatus(_A)
_NwAtAccessControl_ObjectIdentity=ObjectIdentity
nwAtAccessControl=_NwAtAccessControl_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,7))
_NwAtAclValidEntries_Type=Gauge32
_NwAtAclValidEntries_Object=MibScalar
nwAtAclValidEntries=_NwAtAclValidEntries_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,7,1),_NwAtAclValidEntries_Type())
nwAtAclValidEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtAclValidEntries.setStatus(_A)
_NwAtAclTable_Object=MibTable
nwAtAclTable=_NwAtAclTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,7,2))
if mibBuilder.loadTexts:nwAtAclTable.setStatus(_A)
_NwAtAclEntry_Object=MibTableRow
nwAtAclEntry=_NwAtAclEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,7,2,1))
nwAtAclEntry.setIndexNames((0,_H,_p),(0,_H,_q))
if mibBuilder.loadTexts:nwAtAclEntry.setStatus(_A)
_NwAtAclIdentifier_Type=Integer32
_NwAtAclIdentifier_Object=MibTableColumn
nwAtAclIdentifier=_NwAtAclIdentifier_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,7,2,1,1),_NwAtAclIdentifier_Type())
nwAtAclIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtAclIdentifier.setStatus(_A)
_NwAtAclSequence_Type=Integer32
_NwAtAclSequence_Object=MibTableColumn
nwAtAclSequence=_NwAtAclSequence_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,7,2,1,2),_NwAtAclSequence_Type())
nwAtAclSequence.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtAclSequence.setStatus(_A)
class _NwAtAclPermission_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_O,2),('permit',3),('deny',4),('permit-bidirectional',5),('deny-bidirectional',6)))
_NwAtAclPermission_Type.__name__=_D
_NwAtAclPermission_Object=MibTableColumn
nwAtAclPermission=_NwAtAclPermission_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,7,2,1,3),_NwAtAclPermission_Type())
nwAtAclPermission.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtAclPermission.setStatus(_A)
_NwAtAclMatches_Type=Counter32
_NwAtAclMatches_Object=MibTableColumn
nwAtAclMatches=_NwAtAclMatches_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,7,2,1,4),_NwAtAclMatches_Type())
nwAtAclMatches.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtAclMatches.setStatus(_A)
_NwAtAclDestZone_Type=AtName
_NwAtAclDestZone_Object=MibTableColumn
nwAtAclDestZone=_NwAtAclDestZone_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,7,2,1,5),_NwAtAclDestZone_Type())
nwAtAclDestZone.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtAclDestZone.setStatus(_A)
_NwAtAclSrcZone_Type=AtName
_NwAtAclSrcZone_Object=MibTableColumn
nwAtAclSrcZone=_NwAtAclSrcZone_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,7,2,1,6),_NwAtAclSrcZone_Type())
nwAtAclSrcZone.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtAclSrcZone.setStatus(_A)
_NwAtFilters_ObjectIdentity=ObjectIdentity
nwAtFilters=_NwAtFilters_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,8))
_NwAtRedirector_ObjectIdentity=ObjectIdentity
nwAtRedirector=_NwAtRedirector_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,9))
_NwAtEvent_ObjectIdentity=ObjectIdentity
nwAtEvent=_NwAtEvent_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10))
_NwAtEventLogConfig_ObjectIdentity=ObjectIdentity
nwAtEventLogConfig=_NwAtEventLogConfig_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10,1))
class _NwAtEventAdminSTATUS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwAtEventAdminSTATUS_Type.__name__=_D
_NwAtEventAdminSTATUS_Object=MibScalar
nwAtEventAdminSTATUS=_NwAtEventAdminSTATUS_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10,1,1),_NwAtEventAdminSTATUS_Type())
nwAtEventAdminSTATUS.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtEventAdminSTATUS.setStatus(_A)
_NwAtEventMaxEntries_Type=Integer32
_NwAtEventMaxEntries_Object=MibScalar
nwAtEventMaxEntries=_NwAtEventMaxEntries_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10,1,2),_NwAtEventMaxEntries_Type())
nwAtEventMaxEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtEventMaxEntries.setStatus(_A)
class _NwAtEventTraceAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_NwAtEventTraceAll_Type.__name__=_D
_NwAtEventTraceAll_Object=MibScalar
nwAtEventTraceAll=_NwAtEventTraceAll_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10,1,3),_NwAtEventTraceAll_Type())
nwAtEventTraceAll.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtEventTraceAll.setStatus(_A)
_NwAtEventLogFilterTable_ObjectIdentity=ObjectIdentity
nwAtEventLogFilterTable=_NwAtEventLogFilterTable_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10,2))
_NwAtEventFilterTable_Object=MibTable
nwAtEventFilterTable=_NwAtEventFilterTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10,2,1))
if mibBuilder.loadTexts:nwAtEventFilterTable.setStatus(_A)
_NwAtEventFilterEntry_Object=MibTableRow
nwAtEventFilterEntry=_NwAtEventFilterEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10,2,1,1))
nwAtEventFilterEntry.setIndexNames((0,_H,_r),(0,_H,_s))
if mibBuilder.loadTexts:nwAtEventFilterEntry.setStatus(_A)
_NwAtEventFltrProtocol_Type=Integer32
_NwAtEventFltrProtocol_Object=MibTableColumn
nwAtEventFltrProtocol=_NwAtEventFltrProtocol_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10,2,1,1,1),_NwAtEventFltrProtocol_Type())
nwAtEventFltrProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtEventFltrProtocol.setStatus(_A)
_NwAtEventFltrIfNum_Type=Integer32
_NwAtEventFltrIfNum_Object=MibTableColumn
nwAtEventFltrIfNum=_NwAtEventFltrIfNum_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10,2,1,1,2),_NwAtEventFltrIfNum_Type())
nwAtEventFltrIfNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtEventFltrIfNum.setStatus(_A)
class _NwAtEventFltrControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_V,2),('add',3)))
_NwAtEventFltrControl_Type.__name__=_D
_NwAtEventFltrControl_Object=MibTableColumn
nwAtEventFltrControl=_NwAtEventFltrControl_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10,2,1,1,3),_NwAtEventFltrControl_Type())
nwAtEventFltrControl.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtEventFltrControl.setStatus(_A)
class _NwAtEventFltrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16,32)));namedValues=NamedValues(*(('misc',1),('timer',2),('rcv',4),('xmit',8),('event',16),('error',32)))
_NwAtEventFltrType_Type.__name__=_D
_NwAtEventFltrType_Object=MibTableColumn
nwAtEventFltrType=_NwAtEventFltrType_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10,2,1,1,4),_NwAtEventFltrType_Type())
nwAtEventFltrType.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtEventFltrType.setStatus(_A)
class _NwAtEventFltrSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_t,1),(_u,2),(_v,3)))
_NwAtEventFltrSeverity_Type.__name__=_D
_NwAtEventFltrSeverity_Object=MibTableColumn
nwAtEventFltrSeverity=_NwAtEventFltrSeverity_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10,2,1,1,5),_NwAtEventFltrSeverity_Type())
nwAtEventFltrSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtEventFltrSeverity.setStatus(_A)
class _NwAtEventFltrAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('log',1),('trap',2),('log-trap',3)))
_NwAtEventFltrAction_Type.__name__=_D
_NwAtEventFltrAction_Object=MibTableColumn
nwAtEventFltrAction=_NwAtEventFltrAction_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10,2,1,1,6),_NwAtEventFltrAction_Type())
nwAtEventFltrAction.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtEventFltrAction.setStatus(_A)
_NwAtEventLogTable_ObjectIdentity=ObjectIdentity
nwAtEventLogTable=_NwAtEventLogTable_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10,3))
_NwAtEventTable_Object=MibTable
nwAtEventTable=_NwAtEventTable_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10,3,1))
if mibBuilder.loadTexts:nwAtEventTable.setStatus(_A)
_NwAtEventEntry_Object=MibTableRow
nwAtEventEntry=_NwAtEventEntry_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10,3,1,1))
nwAtEventEntry.setIndexNames((0,_H,_w))
if mibBuilder.loadTexts:nwAtEventEntry.setStatus(_A)
_NwAtEventNumber_Type=Integer32
_NwAtEventNumber_Object=MibTableColumn
nwAtEventNumber=_NwAtEventNumber_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10,3,1,1,1),_NwAtEventNumber_Type())
nwAtEventNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtEventNumber.setStatus(_A)
_NwAtEventTime_Type=TimeTicks
_NwAtEventTime_Object=MibTableColumn
nwAtEventTime=_NwAtEventTime_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10,3,1,1,2),_NwAtEventTime_Type())
nwAtEventTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtEventTime.setStatus(_A)
class _NwAtEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16,32)));namedValues=NamedValues(*(('misc',1),('timer',2),('rcv',4),('xmit',8),('event',16),('error',32)))
_NwAtEventType_Type.__name__=_D
_NwAtEventType_Object=MibTableColumn
nwAtEventType=_NwAtEventType_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10,3,1,1,3),_NwAtEventType_Type())
nwAtEventType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtEventType.setStatus(_A)
class _NwAtEventSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_t,1),(_u,2),(_v,3)))
_NwAtEventSeverity_Type.__name__=_D
_NwAtEventSeverity_Object=MibTableColumn
nwAtEventSeverity=_NwAtEventSeverity_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10,3,1,1,4),_NwAtEventSeverity_Type())
nwAtEventSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtEventSeverity.setStatus(_A)
_NwAtEventProtocol_Type=Integer32
_NwAtEventProtocol_Object=MibTableColumn
nwAtEventProtocol=_NwAtEventProtocol_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10,3,1,1,5),_NwAtEventProtocol_Type())
nwAtEventProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtEventProtocol.setStatus(_A)
_NwAtEventIfNum_Type=Integer32
_NwAtEventIfNum_Object=MibTableColumn
nwAtEventIfNum=_NwAtEventIfNum_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10,3,1,1,6),_NwAtEventIfNum_Type())
nwAtEventIfNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtEventIfNum.setStatus(_A)
_NwAtEventTextString_Type=OctetString
_NwAtEventTextString_Object=MibTableColumn
nwAtEventTextString=_NwAtEventTextString_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,10,3,1,1,7),_NwAtEventTextString_Type())
nwAtEventTextString.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtEventTextString.setStatus(_A)
_NwAtWorkGroup_ObjectIdentity=ObjectIdentity
nwAtWorkGroup=_NwAtWorkGroup_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,11))
_NwAtNetDiag_ObjectIdentity=ObjectIdentity
nwAtNetDiag=_NwAtNetDiag_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12))
_NwAtNetDiagPing_ObjectIdentity=ObjectIdentity
nwAtNetDiagPing=_NwAtNetDiagPing_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,1))
_NwAtNetDiagTelnet_ObjectIdentity=ObjectIdentity
nwAtNetDiagTelnet=_NwAtNetDiagTelnet_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,2))
_NwAtNetDiagOutbound_ObjectIdentity=ObjectIdentity
nwAtNetDiagOutbound=_NwAtNetDiagOutbound_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3))
_NwAtNetDiagOutboundNetAddress_Type=AtDdpNodeAddress
_NwAtNetDiagOutboundNetAddress_Object=MibScalar
nwAtNetDiagOutboundNetAddress=_NwAtNetDiagOutboundNetAddress_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,1),_NwAtNetDiagOutboundNetAddress_Type())
nwAtNetDiagOutboundNetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundNetAddress.setStatus(_A)
_NwAtNetDiagOutboundPort_Type=Integer32
_NwAtNetDiagOutboundPort_Object=MibScalar
nwAtNetDiagOutboundPort=_NwAtNetDiagOutboundPort_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,2),_NwAtNetDiagOutboundPort_Type())
nwAtNetDiagOutboundPort.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundPort.setStatus(_A)
_NwAtNetDiagOutboundTimeout_Type=Integer32
_NwAtNetDiagOutboundTimeout_Object=MibScalar
nwAtNetDiagOutboundTimeout=_NwAtNetDiagOutboundTimeout_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,3),_NwAtNetDiagOutboundTimeout_Type())
nwAtNetDiagOutboundTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundTimeout.setStatus(_A)
_NwAtNetDiagOutboundRetries_Type=Integer32
_NwAtNetDiagOutboundRetries_Object=MibScalar
nwAtNetDiagOutboundRetries=_NwAtNetDiagOutboundRetries_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,4),_NwAtNetDiagOutboundRetries_Type())
nwAtNetDiagOutboundRetries.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundRetries.setStatus(_A)
class _NwAtNetDiagOutboundATEchoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),('sendEchoRequest',2),(_E,3)))
_NwAtNetDiagOutboundATEchoType_Type.__name__=_D
_NwAtNetDiagOutboundATEchoType_Object=MibScalar
nwAtNetDiagOutboundATEchoType=_NwAtNetDiagOutboundATEchoType_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,5),_NwAtNetDiagOutboundATEchoType_Type())
nwAtNetDiagOutboundATEchoType.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundATEchoType.setStatus(_A)
class _NwAtNetDiagOutboundATEchoStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_N,1),(_R,2),('timeout',3),('success',4)))
_NwAtNetDiagOutboundATEchoStatus_Type.__name__=_D
_NwAtNetDiagOutboundATEchoStatus_Object=MibScalar
nwAtNetDiagOutboundATEchoStatus=_NwAtNetDiagOutboundATEchoStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,6),_NwAtNetDiagOutboundATEchoStatus_Type())
nwAtNetDiagOutboundATEchoStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundATEchoStatus.setStatus(_A)
_NwAtNetDiagOutboundNBPEntityObject_Type=AtName
_NwAtNetDiagOutboundNBPEntityObject_Object=MibScalar
nwAtNetDiagOutboundNBPEntityObject=_NwAtNetDiagOutboundNBPEntityObject_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,7),_NwAtNetDiagOutboundNBPEntityObject_Type())
nwAtNetDiagOutboundNBPEntityObject.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundNBPEntityObject.setStatus(_A)
_NwAtNetDiagOutboundNBPEntityType_Type=AtName
_NwAtNetDiagOutboundNBPEntityType_Object=MibScalar
nwAtNetDiagOutboundNBPEntityType=_NwAtNetDiagOutboundNBPEntityType_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,8),_NwAtNetDiagOutboundNBPEntityType_Type())
nwAtNetDiagOutboundNBPEntityType.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundNBPEntityType.setStatus(_A)
_NwAtNetDiagOutboundNBPEntityZone_Type=AtName
_NwAtNetDiagOutboundNBPEntityZone_Object=MibScalar
nwAtNetDiagOutboundNBPEntityZone=_NwAtNetDiagOutboundNBPEntityZone_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,9),_NwAtNetDiagOutboundNBPEntityZone_Type())
nwAtNetDiagOutboundNBPEntityZone.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundNBPEntityZone.setStatus(_A)
class _NwAtNetDiagOutboundNBPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_P,1),('localRequest',2),('lookupMcast',3),('lookupBcast',4),('lookupDirect',5),('bcastRequestBcast',6),('bcastRequestDirect',7),('forwardRequestBcast',8),('forwardRequestDirect',9),(_E,10)))
_NwAtNetDiagOutboundNBPType_Type.__name__=_D
_NwAtNetDiagOutboundNBPType_Object=MibScalar
nwAtNetDiagOutboundNBPType=_NwAtNetDiagOutboundNBPType_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,10),_NwAtNetDiagOutboundNBPType_Type())
nwAtNetDiagOutboundNBPType.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundNBPType.setStatus(_A)
class _NwAtNetDiagOutboundNBPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_R,2),(_S,3)))
_NwAtNetDiagOutboundNBPStatus_Type.__name__=_D
_NwAtNetDiagOutboundNBPStatus_Object=MibScalar
nwAtNetDiagOutboundNBPStatus=_NwAtNetDiagOutboundNBPStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,11),_NwAtNetDiagOutboundNBPStatus_Type())
nwAtNetDiagOutboundNBPStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundNBPStatus.setStatus(_A)
class _NwAtNetDiagOutboundRTMPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_P,1),('sendRequest',2),('bcastRequest',3),('sendRDRequestSplitHorizon',4),('bcastRDRequestSplitHorizon',5),('sendRDRequestFullTable',6),('bcastRDRequestFullTable',7),(_E,8)))
_NwAtNetDiagOutboundRTMPType_Type.__name__=_D
_NwAtNetDiagOutboundRTMPType_Object=MibScalar
nwAtNetDiagOutboundRTMPType=_NwAtNetDiagOutboundRTMPType_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,12),_NwAtNetDiagOutboundRTMPType_Type())
nwAtNetDiagOutboundRTMPType.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundRTMPType.setStatus(_A)
class _NwAtNetDiagOutboundRTMPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_R,2),(_S,3)))
_NwAtNetDiagOutboundRTMPStatus_Type.__name__=_D
_NwAtNetDiagOutboundRTMPStatus_Object=MibScalar
nwAtNetDiagOutboundRTMPStatus=_NwAtNetDiagOutboundRTMPStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,13),_NwAtNetDiagOutboundRTMPStatus_Type())
nwAtNetDiagOutboundRTMPStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundRTMPStatus.setStatus(_A)
_NwAtNetDiagOutboundRTMPNetStart_Type=AtNetworkNumber
_NwAtNetDiagOutboundRTMPNetStart_Object=MibScalar
nwAtNetDiagOutboundRTMPNetStart=_NwAtNetDiagOutboundRTMPNetStart_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,14),_NwAtNetDiagOutboundRTMPNetStart_Type())
nwAtNetDiagOutboundRTMPNetStart.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundRTMPNetStart.setStatus(_A)
_NwAtNetDiagOutboundRTMPNetEnd_Type=AtNetworkNumber
_NwAtNetDiagOutboundRTMPNetEnd_Object=MibScalar
nwAtNetDiagOutboundRTMPNetEnd=_NwAtNetDiagOutboundRTMPNetEnd_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,15),_NwAtNetDiagOutboundRTMPNetEnd_Type())
nwAtNetDiagOutboundRTMPNetEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundRTMPNetEnd.setStatus(_A)
class _NwAtNetDiagOutboundZIPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_P,1),('sendQuery',2),('bcastQuery',3),('sendGetZonesList',4),('sendGetLocalZones',5),('sendGetMyZone',6),('sendGetNetInfo',7),('bcastGetNetInfo',8),(_E,9)))
_NwAtNetDiagOutboundZIPType_Type.__name__=_D
_NwAtNetDiagOutboundZIPType_Object=MibScalar
nwAtNetDiagOutboundZIPType=_NwAtNetDiagOutboundZIPType_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,16),_NwAtNetDiagOutboundZIPType_Type())
nwAtNetDiagOutboundZIPType.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundZIPType.setStatus(_A)
class _NwAtNetDiagOutboundZIPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_N,1),('queryInProgress',2),('atpInProgress',3),('gniInProgress',4),(_S,5)))
_NwAtNetDiagOutboundZIPStatus_Type.__name__=_D
_NwAtNetDiagOutboundZIPStatus_Object=MibScalar
nwAtNetDiagOutboundZIPStatus=_NwAtNetDiagOutboundZIPStatus_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,17),_NwAtNetDiagOutboundZIPStatus_Type())
nwAtNetDiagOutboundZIPStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundZIPStatus.setStatus(_A)
_NwAtNetDiagOutboundZIPQueryNet_Type=AtNetworkNumber
_NwAtNetDiagOutboundZIPQueryNet_Object=MibScalar
nwAtNetDiagOutboundZIPQueryNet=_NwAtNetDiagOutboundZIPQueryNet_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,18),_NwAtNetDiagOutboundZIPQueryNet_Type())
nwAtNetDiagOutboundZIPQueryNet.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundZIPQueryNet.setStatus(_A)
_NwAtNetDiagOutboundZIPQueryZone_Type=AtName
_NwAtNetDiagOutboundZIPQueryZone_Object=MibScalar
nwAtNetDiagOutboundZIPQueryZone=_NwAtNetDiagOutboundZIPQueryZone_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,19),_NwAtNetDiagOutboundZIPQueryZone_Type())
nwAtNetDiagOutboundZIPQueryZone.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundZIPQueryZone.setStatus(_A)
_NwAtNetDiagOutboundZIPGetNetInfoZone_Type=AtName
_NwAtNetDiagOutboundZIPGetNetInfoZone_Object=MibScalar
nwAtNetDiagOutboundZIPGetNetInfoZone=_NwAtNetDiagOutboundZIPGetNetInfoZone_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,20),_NwAtNetDiagOutboundZIPGetNetInfoZone_Type())
nwAtNetDiagOutboundZIPGetNetInfoZone.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundZIPGetNetInfoZone.setStatus(_A)
_NwAtNetDiagOutboundZIPGetNetInfoNetStart_Type=AtNetworkNumber
_NwAtNetDiagOutboundZIPGetNetInfoNetStart_Object=MibScalar
nwAtNetDiagOutboundZIPGetNetInfoNetStart=_NwAtNetDiagOutboundZIPGetNetInfoNetStart_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,21),_NwAtNetDiagOutboundZIPGetNetInfoNetStart_Type())
nwAtNetDiagOutboundZIPGetNetInfoNetStart.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundZIPGetNetInfoNetStart.setStatus(_A)
_NwAtNetDiagOutboundZIPGetNetInfoNetEnd_Type=AtNetworkNumber
_NwAtNetDiagOutboundZIPGetNetInfoNetEnd_Object=MibScalar
nwAtNetDiagOutboundZIPGetNetInfoNetEnd=_NwAtNetDiagOutboundZIPGetNetInfoNetEnd_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,22),_NwAtNetDiagOutboundZIPGetNetInfoNetEnd_Type())
nwAtNetDiagOutboundZIPGetNetInfoNetEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundZIPGetNetInfoNetEnd.setStatus(_A)
_NwAtNetDiagOutboundZIPGetNetInfoMulticast_Type=OctetString
_NwAtNetDiagOutboundZIPGetNetInfoMulticast_Object=MibScalar
nwAtNetDiagOutboundZIPGetNetInfoMulticast=_NwAtNetDiagOutboundZIPGetNetInfoMulticast_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,23),_NwAtNetDiagOutboundZIPGetNetInfoMulticast_Type())
nwAtNetDiagOutboundZIPGetNetInfoMulticast.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundZIPGetNetInfoMulticast.setStatus(_A)
_NwAtNetDiagOutboundZIPGetNetInfoDefaultZone_Type=AtName
_NwAtNetDiagOutboundZIPGetNetInfoDefaultZone_Object=MibScalar
nwAtNetDiagOutboundZIPGetNetInfoDefaultZone=_NwAtNetDiagOutboundZIPGetNetInfoDefaultZone_Object((1,3,6,1,4,1,52,4,2,2,2,3,4,2,12,3,24),_NwAtNetDiagOutboundZIPGetNetInfoDefaultZone_Type())
nwAtNetDiagOutboundZIPGetNetInfoDefaultZone.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtNetDiagOutboundZIPGetNetInfoDefaultZone.setStatus(_A)
_NwRtrExperimental_ObjectIdentity=ObjectIdentity
nwRtrExperimental=_NwRtrExperimental_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,4))
_NwAtportZoneTable_Object=MibTable
nwAtportZoneTable=_NwAtportZoneTable_Object((1,3,6,1,4,1,52,4,2,2,2,4,1))
if mibBuilder.loadTexts:nwAtportZoneTable.setStatus(_A)
_NwAtportZoneEntry_Object=MibTableRow
nwAtportZoneEntry=_NwAtportZoneEntry_Object((1,3,6,1,4,1,52,4,2,2,2,4,1,1))
nwAtportZoneEntry.setIndexNames((0,_H,_x),(0,_H,_y))
if mibBuilder.loadTexts:nwAtportZoneEntry.setStatus(_A)
_NwAtportZonePort_Type=Integer32
_NwAtportZonePort_Object=MibTableColumn
nwAtportZonePort=_NwAtportZonePort_Object((1,3,6,1,4,1,52,4,2,2,2,4,1,1,1),_NwAtportZonePort_Type())
nwAtportZonePort.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtportZonePort.setStatus(_A)
_NwAtportZoneName_Type=AtName
_NwAtportZoneName_Object=MibTableColumn
nwAtportZoneName=_NwAtportZoneName_Object((1,3,6,1,4,1,52,4,2,2,2,4,1,1,2),_NwAtportZoneName_Type())
nwAtportZoneName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwAtportZoneName.setStatus(_A)
class _NwAtportZoneStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_O,2)))
_NwAtportZoneStatus_Type.__name__=_D
_NwAtportZoneStatus_Object=MibTableColumn
nwAtportZoneStatus=_NwAtportZoneStatus_Object((1,3,6,1,4,1,52,4,2,2,2,4,1,1,3),_NwAtportZoneStatus_Type())
nwAtportZoneStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nwAtportZoneStatus.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'AtNetworkNumber':AtNetworkNumber,'AtDdpNodeAddress':AtDdpNodeAddress,'AtName':AtName,'nwAtRouter':nwAtRouter,'nwAtMibs':nwAtMibs,'nwAtMibRevText':nwAtMibRevText,'nwAtComponents':nwAtComponents,'nwAtSystem':nwAtSystem,'nwAtSysConfig':nwAtSysConfig,'nwAtSysRouterId':nwAtSysRouterId,'nwAtSysAdministration':nwAtSysAdministration,'nwAtSysAdminSTATUS':nwAtSysAdminSTATUS,'nwAtSysOperSTATUS':nwAtSysOperSTATUS,'nwAtSysAdminReset':nwAtSysAdminReset,'nwAtSysOperationalTime':nwAtSysOperationalTime,'nwAtSysVersion':nwAtSysVersion,'nwAtForwarding':nwAtForwarding,'nwAtFwdSystem':nwAtFwdSystem,'nwAtFwdCounters':nwAtFwdCounters,'nwAtFwdCtrAdminSTATUS':nwAtFwdCtrAdminSTATUS,'nwAtFwdCtrReset':nwAtFwdCtrReset,'nwAtFwdCtrOperationalTime':nwAtFwdCtrOperationalTime,'nwAtFwdCtrInPkts':nwAtFwdCtrInPkts,'nwAtFwdCtrOutPkts':nwAtFwdCtrOutPkts,'nwAtFwdCtrFwdPkts':nwAtFwdCtrFwdPkts,'nwAtFwdCtrFilteredPkts':nwAtFwdCtrFilteredPkts,'nwAtFwdCtrDiscardPkts':nwAtFwdCtrDiscardPkts,'nwAtFwdCtrAddrErrPkts':nwAtFwdCtrAddrErrPkts,'nwAtFwdCtrLenErrPkts':nwAtFwdCtrLenErrPkts,'nwAtFwdCtrHdrErrPkts':nwAtFwdCtrHdrErrPkts,'nwAtFwdCtrInBytes':nwAtFwdCtrInBytes,'nwAtFwdCtrOutBytes':nwAtFwdCtrOutBytes,'nwAtFwdCtrFwdBytes':nwAtFwdCtrFwdBytes,'nwAtFwdCtrFilteredBytes':nwAtFwdCtrFilteredBytes,'nwAtFwdCtrDiscardBytes':nwAtFwdCtrDiscardBytes,'nwAtFwdCtrHostInPkts':nwAtFwdCtrHostInPkts,'nwAtFwdCtrHostOutPkts':nwAtFwdCtrHostOutPkts,'nwAtFwdCtrHostDiscardPkts':nwAtFwdCtrHostDiscardPkts,'nwAtFwdCtrHostInBytes':nwAtFwdCtrHostInBytes,'nwAtFwdCtrHostOutBytes':nwAtFwdCtrHostOutBytes,'nwAtFwdCtrHostDiscardBytes':nwAtFwdCtrHostDiscardBytes,'nwAtFwdInterfaces':nwAtFwdInterfaces,'nwAtFwdIfConfig':nwAtFwdIfConfig,'nwAtFwdIfTable':nwAtFwdIfTable,'nwAtFwdIfEntry':nwAtFwdIfEntry,_U:nwAtFwdIfIndex,'nwAtFwdIfAdminSTATUS':nwAtFwdIfAdminSTATUS,'nwAtFwdIfOperSTATUS':nwAtFwdIfOperSTATUS,'nwAtFwdIfOperationalTime':nwAtFwdIfOperationalTime,'nwAtFwdIfControl':nwAtFwdIfControl,'nwAtFwdIfMtu':nwAtFwdIfMtu,'nwAtFwdIfForwarding':nwAtFwdIfForwarding,'nwAtFwdIfFrameType':nwAtFwdIfFrameType,'nwAtFwdIfAclIdentifier':nwAtFwdIfAclIdentifier,'nwAtFwdIfAclSTATUS':nwAtFwdIfAclSTATUS,'nwAtFwdIfCacheControl':nwAtFwdIfCacheControl,'nwAtFwdIfCacheEntries':nwAtFwdIfCacheEntries,'nwAtFwdIfCacheHits':nwAtFwdIfCacheHits,'nwAtFwdIfCacheMisses':nwAtFwdIfCacheMisses,'nwAtportTable':nwAtportTable,'nwAtportEntry':nwAtportEntry,_c:nwAtportIndex,'nwAtportDescr':nwAtportDescr,'nwAtportType':nwAtportType,'nwAtportNetStart':nwAtportNetStart,'nwAtportNetEnd':nwAtportNetEnd,'nwAtportNetAddress':nwAtportNetAddress,'nwAtportSTATUS':nwAtportSTATUS,'nwAtportNetConfig':nwAtportNetConfig,'nwAtportZoneConfig':nwAtportZoneConfig,'nwAtportZoneDefault':nwAtportZoneDefault,'nwAtportIfIndex':nwAtportIfIndex,'nwAtportNetFrom':nwAtportNetFrom,'nwAtportZoneFrom':nwAtportZoneFrom,'nwAtportInPkts':nwAtportInPkts,'nwAtportOutPkts':nwAtportOutPkts,'nwAtportHome':nwAtportHome,'nwAtportCurrentZone':nwAtportCurrentZone,'nwAtportConflictPhysAddr':nwAtportConflictPhysAddr,'nwAtFwdIfCounters':nwAtFwdIfCounters,'nwAtFwdIfCtrTable':nwAtFwdIfCtrTable,'nwAtFwdIfCtrEntry':nwAtFwdIfCtrEntry,_i:nwAtFwdIfCtrIfIndex,'nwAtFwdIfCtrAdminSTATUS':nwAtFwdIfCtrAdminSTATUS,'nwAtFwdIfCtrReset':nwAtFwdIfCtrReset,'nwAtFwdIfCtrOperationalTime':nwAtFwdIfCtrOperationalTime,'nwAtFwdIfCtrInPkts':nwAtFwdIfCtrInPkts,'nwAtFwdIfCtrOutPkts':nwAtFwdIfCtrOutPkts,'nwAtFwdIfCtrFwdPkts':nwAtFwdIfCtrFwdPkts,'nwAtFwdIfCtrFilteredPkts':nwAtFwdIfCtrFilteredPkts,'nwAtFwdIfCtrDiscardPkts':nwAtFwdIfCtrDiscardPkts,'nwAtFwdIfCtrAddrErrPkts':nwAtFwdIfCtrAddrErrPkts,'nwAtFwdIfCtrLenErrPkts':nwAtFwdIfCtrLenErrPkts,'nwAtFwdIfCtrHdrErrPkts':nwAtFwdIfCtrHdrErrPkts,'nwAtFwdIfCtrInBytes':nwAtFwdIfCtrInBytes,'nwAtFwdIfCtrOutBytes':nwAtFwdIfCtrOutBytes,'nwAtFwdIfCtrFwdBytes':nwAtFwdIfCtrFwdBytes,'nwAtFwdIfCtrFilteredBytes':nwAtFwdIfCtrFilteredBytes,'nwAtFwdIfCtrDiscardBytes':nwAtFwdIfCtrDiscardBytes,'nwAtFwdIfCtrHostInPkts':nwAtFwdIfCtrHostInPkts,'nwAtFwdIfCtrHostOutPkts':nwAtFwdIfCtrHostOutPkts,'nwAtFwdIfCtrHostDiscardPkts':nwAtFwdIfCtrHostDiscardPkts,'nwAtFwdIfCtrHostInBytes':nwAtFwdIfCtrHostInBytes,'nwAtFwdIfCtrHostOutBytes':nwAtFwdIfCtrHostOutBytes,'nwAtFwdIfCtrHostDiscardBytes':nwAtFwdIfCtrHostDiscardBytes,'nwAtTopology':nwAtTopology,'nwAtDistanceVector':nwAtDistanceVector,'nwAtProto':nwAtProto,'nwAtProtoSystem':nwAtProtoSystem,'nwAtProtoConfig':nwAtProtoConfig,'nwAtProtoAdminSTATUS':nwAtProtoAdminSTATUS,'nwAtProtoOperSTATUS':nwAtProtoOperSTATUS,'nwAtProtoAdminReset':nwAtProtoAdminReset,'nwAtProtoOperationalTime':nwAtProtoOperationalTime,'nwAtProtoVersion':nwAtProtoVersion,'nwAtProtoStackSize':nwAtProtoStackSize,'nwAtProtoThreadPriority':nwAtProtoThreadPriority,'nwAtProtoDatabaseThreshold':nwAtProtoDatabaseThreshold,'nwAtProtoAgeOut':nwAtProtoAgeOut,'nwAtProtoHoldDown':nwAtProtoHoldDown,'nwAtProtoCounters':nwAtProtoCounters,'nwAtProtoCtrAdminSTATUS':nwAtProtoCtrAdminSTATUS,'nwAtProtoCtrReset':nwAtProtoCtrReset,'nwAtProtoCtrOperationalTime':nwAtProtoCtrOperationalTime,'nwAtProtoCtrInPkts':nwAtProtoCtrInPkts,'nwAtProtoCtrOutPkts':nwAtProtoCtrOutPkts,'nwAtProtoCtrFilteredPkts':nwAtProtoCtrFilteredPkts,'nwAtProtoCtrDiscardPkts':nwAtProtoCtrDiscardPkts,'nwAtProtoCtrInBytes':nwAtProtoCtrInBytes,'nwAtProtoCtrOutBytes':nwAtProtoCtrOutBytes,'nwAtProtoCtrFilteredBytes':nwAtProtoCtrFilteredBytes,'nwAtProtoCtrDiscardBytes':nwAtProtoCtrDiscardBytes,'nwAtProtoInterface':nwAtProtoInterface,'nwAtProtoIfConfig':nwAtProtoIfConfig,'nwAtProtoIfTable':nwAtProtoIfTable,'nwAtProtoIfEntry':nwAtProtoIfEntry,_j:nwAtProtoIfIndex,'nwAtProtoIfAdminSTATUS':nwAtProtoIfAdminSTATUS,'nwAtProtoIfOperSTATUS':nwAtProtoIfOperSTATUS,'nwAtProtoIfOperationalTime':nwAtProtoIfOperationalTime,'nwAtProtoIfVersion':nwAtProtoIfVersion,'nwAtProtoIfAdvertisement':nwAtProtoIfAdvertisement,'nwAtProtoIfFloodDelay':nwAtProtoIfFloodDelay,'nwAtProtoIfRequestDelay':nwAtProtoIfRequestDelay,'nwAtProtoIfPriority':nwAtProtoIfPriority,'nwAtProtoIfHelloTimer':nwAtProtoIfHelloTimer,'nwAtProtoIfSplitHorizon':nwAtProtoIfSplitHorizon,'nwAtProtoIfPoisonReverse':nwAtProtoIfPoisonReverse,'nwAtProtoIfSnooping':nwAtProtoIfSnooping,'nwAtProtoIfType':nwAtProtoIfType,'nwAtProtoIfXmitCost':nwAtProtoIfXmitCost,'nwAtProtoIfAclIdentifier':nwAtProtoIfAclIdentifier,'nwAtProtoIfAclSTATUS':nwAtProtoIfAclSTATUS,'nwAtProtoIfCounters':nwAtProtoIfCounters,'nwAtProtoIfCtrTable':nwAtProtoIfCtrTable,'nwAtProtoIfCtrEntry':nwAtProtoIfCtrEntry,_k:nwAtProtoIfCtrIfIndex,'nwAtProtoIfCtrAdminSTATUS':nwAtProtoIfCtrAdminSTATUS,'nwAtProtoIfCtrReset':nwAtProtoIfCtrReset,'nwAtProtoIfCtrOperationalTime':nwAtProtoIfCtrOperationalTime,'nwAtProtoIfCtrInPkts':nwAtProtoIfCtrInPkts,'nwAtProtoIfCtrOutPkts':nwAtProtoIfCtrOutPkts,'nwAtProtoIfCtrFilteredPkts':nwAtProtoIfCtrFilteredPkts,'nwAtProtoIfCtrDiscardPkts':nwAtProtoIfCtrDiscardPkts,'nwAtProtoIfCtrInBytes':nwAtProtoIfCtrInBytes,'nwAtProtoIfCtrOutBytes':nwAtProtoIfCtrOutBytes,'nwAtProtoIfCtrFilteredBytes':nwAtProtoIfCtrFilteredBytes,'nwAtProtoIfCtrDiscardBytes':nwAtProtoIfCtrDiscardBytes,'nwAtLinkState':nwAtLinkState,'nwAtFib':nwAtFib,'nwAtFibTable':nwAtFibTable,'nwAtFibEntry':nwAtFibEntry,_l:nwAtFibStartNet,'nwAtFibEndNet':nwAtFibEndNet,'nwAtFibNextHop':nwAtFibNextHop,'nwAtFibNextHopIf':nwAtFibNextHopIf,'nwAtFibHops':nwAtFibHops,'nwAtFibRouteType':nwAtFibRouteType,'nwAtEndSystems':nwAtEndSystems,'nwAtHostsSystem':nwAtHostsSystem,'nwAtHostsTimeToLive':nwAtHostsTimeToLive,'nwAtHostsRetryCount':nwAtHostsRetryCount,'nwAtHostsInterfaces':nwAtHostsInterfaces,'nwAtHostCtlTable':nwAtHostCtlTable,'nwAtHostCtlEntry':nwAtHostCtlEntry,_m:nwAtHostCtlIfIndex,'nwAtHostCtlAdminSTATUS':nwAtHostCtlAdminSTATUS,'nwAtHostCtlOperSTATUS':nwAtHostCtlOperSTATUS,'nwAtHostCtlOperationalTime':nwAtHostCtlOperationalTime,'nwAtHostCtlProtocol':nwAtHostCtlProtocol,'nwAtHostCtlSnooping':nwAtHostCtlSnooping,'nwAtHostCtlProxy':nwAtHostCtlProxy,'nwAtHostCtlCacheMax':nwAtHostCtlCacheMax,'nwAtHostCtlCacheSize':nwAtHostCtlCacheSize,'nwAtHostCtlNumStatics':nwAtHostCtlNumStatics,'nwAtHostCtlNumDynamics':nwAtHostCtlNumDynamics,'nwAtHostCtlCacheHits':nwAtHostCtlCacheHits,'nwAtHostCtlCacheMisses':nwAtHostCtlCacheMisses,'nwAtHostsToMedia':nwAtHostsToMedia,'nwAtHostMapTable':nwAtHostMapTable,'nwAtHostMapEntry':nwAtHostMapEntry,_n:nwAtHostMapIfIndex,_o:nwAtHostMapAtAddr,'nwAtHostMapPhysAddr':nwAtHostMapPhysAddr,'nwAtHostMapType':nwAtHostMapType,'nwAtHostMapCircuitID':nwAtHostMapCircuitID,'nwAtHostMapFraming':nwAtHostMapFraming,'nwAtHostMapPortNumber':nwAtHostMapPortNumber,'nwAtAccessControl':nwAtAccessControl,'nwAtAclValidEntries':nwAtAclValidEntries,'nwAtAclTable':nwAtAclTable,'nwAtAclEntry':nwAtAclEntry,_p:nwAtAclIdentifier,_q:nwAtAclSequence,'nwAtAclPermission':nwAtAclPermission,'nwAtAclMatches':nwAtAclMatches,'nwAtAclDestZone':nwAtAclDestZone,'nwAtAclSrcZone':nwAtAclSrcZone,'nwAtFilters':nwAtFilters,'nwAtRedirector':nwAtRedirector,'nwAtEvent':nwAtEvent,'nwAtEventLogConfig':nwAtEventLogConfig,'nwAtEventAdminSTATUS':nwAtEventAdminSTATUS,'nwAtEventMaxEntries':nwAtEventMaxEntries,'nwAtEventTraceAll':nwAtEventTraceAll,'nwAtEventLogFilterTable':nwAtEventLogFilterTable,'nwAtEventFilterTable':nwAtEventFilterTable,'nwAtEventFilterEntry':nwAtEventFilterEntry,_r:nwAtEventFltrProtocol,_s:nwAtEventFltrIfNum,'nwAtEventFltrControl':nwAtEventFltrControl,'nwAtEventFltrType':nwAtEventFltrType,'nwAtEventFltrSeverity':nwAtEventFltrSeverity,'nwAtEventFltrAction':nwAtEventFltrAction,'nwAtEventLogTable':nwAtEventLogTable,'nwAtEventTable':nwAtEventTable,'nwAtEventEntry':nwAtEventEntry,_w:nwAtEventNumber,'nwAtEventTime':nwAtEventTime,'nwAtEventType':nwAtEventType,'nwAtEventSeverity':nwAtEventSeverity,'nwAtEventProtocol':nwAtEventProtocol,'nwAtEventIfNum':nwAtEventIfNum,'nwAtEventTextString':nwAtEventTextString,'nwAtWorkGroup':nwAtWorkGroup,'nwAtNetDiag':nwAtNetDiag,'nwAtNetDiagPing':nwAtNetDiagPing,'nwAtNetDiagTelnet':nwAtNetDiagTelnet,'nwAtNetDiagOutbound':nwAtNetDiagOutbound,'nwAtNetDiagOutboundNetAddress':nwAtNetDiagOutboundNetAddress,'nwAtNetDiagOutboundPort':nwAtNetDiagOutboundPort,'nwAtNetDiagOutboundTimeout':nwAtNetDiagOutboundTimeout,'nwAtNetDiagOutboundRetries':nwAtNetDiagOutboundRetries,'nwAtNetDiagOutboundATEchoType':nwAtNetDiagOutboundATEchoType,'nwAtNetDiagOutboundATEchoStatus':nwAtNetDiagOutboundATEchoStatus,'nwAtNetDiagOutboundNBPEntityObject':nwAtNetDiagOutboundNBPEntityObject,'nwAtNetDiagOutboundNBPEntityType':nwAtNetDiagOutboundNBPEntityType,'nwAtNetDiagOutboundNBPEntityZone':nwAtNetDiagOutboundNBPEntityZone,'nwAtNetDiagOutboundNBPType':nwAtNetDiagOutboundNBPType,'nwAtNetDiagOutboundNBPStatus':nwAtNetDiagOutboundNBPStatus,'nwAtNetDiagOutboundRTMPType':nwAtNetDiagOutboundRTMPType,'nwAtNetDiagOutboundRTMPStatus':nwAtNetDiagOutboundRTMPStatus,'nwAtNetDiagOutboundRTMPNetStart':nwAtNetDiagOutboundRTMPNetStart,'nwAtNetDiagOutboundRTMPNetEnd':nwAtNetDiagOutboundRTMPNetEnd,'nwAtNetDiagOutboundZIPType':nwAtNetDiagOutboundZIPType,'nwAtNetDiagOutboundZIPStatus':nwAtNetDiagOutboundZIPStatus,'nwAtNetDiagOutboundZIPQueryNet':nwAtNetDiagOutboundZIPQueryNet,'nwAtNetDiagOutboundZIPQueryZone':nwAtNetDiagOutboundZIPQueryZone,'nwAtNetDiagOutboundZIPGetNetInfoZone':nwAtNetDiagOutboundZIPGetNetInfoZone,'nwAtNetDiagOutboundZIPGetNetInfoNetStart':nwAtNetDiagOutboundZIPGetNetInfoNetStart,'nwAtNetDiagOutboundZIPGetNetInfoNetEnd':nwAtNetDiagOutboundZIPGetNetInfoNetEnd,'nwAtNetDiagOutboundZIPGetNetInfoMulticast':nwAtNetDiagOutboundZIPGetNetInfoMulticast,'nwAtNetDiagOutboundZIPGetNetInfoDefaultZone':nwAtNetDiagOutboundZIPGetNetInfoDefaultZone,'nwRtrExperimental':nwRtrExperimental,'nwAtportZoneTable':nwAtportZoneTable,'nwAtportZoneEntry':nwAtportZoneEntry,_x:nwAtportZonePort,_y:nwAtportZoneName,'nwAtportZoneStatus':nwAtportZoneStatus})