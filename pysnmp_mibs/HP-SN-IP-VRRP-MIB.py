_Y='snVrrpVirRtr2Id'
_X='modify'
_W='create'
_V='delete'
_U='invalid'
_T='master'
_S='incomplete'
_R='snVrrpVirRtrId'
_Q='snVrrpVirRtrPort'
_P='ipAuthHeader'
_O='simpleTextPasswd'
_N='noAuth'
_M='snVrrpIfPort'
_L='ifIndex'
_K='IF-MIB'
_J='backup'
_I='HP-SN-IP-VRRP-MIB'
_H='OctetString'
_G='enabled'
_F='disabled'
_E='Integer32'
_D='read-write'
_C='deprecated'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
snVrrp,=mibBuilder.importSymbols('HP-SN-ROOT-MIB','snVrrp')
ifIndex,=mibBuilder.importSymbols(_K,_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SnVrrpGlobal_ObjectIdentity=ObjectIdentity
snVrrpGlobal=_SnVrrpGlobal_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,2,12,1))
class _SnVrrpGroupOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_SnVrrpGroupOperMode_Type.__name__=_E
_SnVrrpGroupOperMode_Object=MibScalar
snVrrpGroupOperMode=_SnVrrpGroupOperMode_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,1,1),_SnVrrpGroupOperMode_Type())
snVrrpGroupOperMode.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpGroupOperMode.setStatus(_A)
class _SnVrrpIfStateChangeTrap_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_SnVrrpIfStateChangeTrap_Type.__name__=_E
_SnVrrpIfStateChangeTrap_Object=MibScalar
snVrrpIfStateChangeTrap=_SnVrrpIfStateChangeTrap_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,1,2),_SnVrrpIfStateChangeTrap_Type())
snVrrpIfStateChangeTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpIfStateChangeTrap.setStatus(_A)
_SnVrrpIfMaxNumVridPerIntf_Type=Integer32
_SnVrrpIfMaxNumVridPerIntf_Object=MibScalar
snVrrpIfMaxNumVridPerIntf=_SnVrrpIfMaxNumVridPerIntf_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,1,3),_SnVrrpIfMaxNumVridPerIntf_Type())
snVrrpIfMaxNumVridPerIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpIfMaxNumVridPerIntf.setStatus(_A)
_SnVrrpIfMaxNumVridPerSystem_Type=Integer32
_SnVrrpIfMaxNumVridPerSystem_Object=MibScalar
snVrrpIfMaxNumVridPerSystem=_SnVrrpIfMaxNumVridPerSystem_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,1,4),_SnVrrpIfMaxNumVridPerSystem_Type())
snVrrpIfMaxNumVridPerSystem.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpIfMaxNumVridPerSystem.setStatus(_A)
class _SnVrrpClearVrrpStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('clear',1)))
_SnVrrpClearVrrpStat_Type.__name__=_E
_SnVrrpClearVrrpStat_Object=MibScalar
snVrrpClearVrrpStat=_SnVrrpClearVrrpStat_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,1,5),_SnVrrpClearVrrpStat_Type())
snVrrpClearVrrpStat.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpClearVrrpStat.setStatus(_A)
class _SnVrrpGroupOperModeVrrpextended_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_SnVrrpGroupOperModeVrrpextended_Type.__name__=_E
_SnVrrpGroupOperModeVrrpextended_Object=MibScalar
snVrrpGroupOperModeVrrpextended=_SnVrrpGroupOperModeVrrpextended_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,1,6),_SnVrrpGroupOperModeVrrpextended_Type())
snVrrpGroupOperModeVrrpextended.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpGroupOperModeVrrpextended.setStatus(_A)
_SnVrrpIntf_ObjectIdentity=ObjectIdentity
snVrrpIntf=_SnVrrpIntf_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,2,12,2))
_SnVrrpIfTable_Object=MibTable
snVrrpIfTable=_SnVrrpIfTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,2,1))
if mibBuilder.loadTexts:snVrrpIfTable.setStatus(_C)
_SnVrrpIfEntry_Object=MibTableRow
snVrrpIfEntry=_SnVrrpIfEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,2,1,1))
snVrrpIfEntry.setIndexNames((0,_I,_M))
if mibBuilder.loadTexts:snVrrpIfEntry.setStatus(_C)
_SnVrrpIfPort_Type=Integer32
_SnVrrpIfPort_Object=MibTableColumn
snVrrpIfPort=_SnVrrpIfPort_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,2,1,1,1),_SnVrrpIfPort_Type())
snVrrpIfPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpIfPort.setStatus(_C)
class _SnVrrpIfAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2)))
_SnVrrpIfAuthType_Type.__name__=_E
_SnVrrpIfAuthType_Object=MibTableColumn
snVrrpIfAuthType=_SnVrrpIfAuthType_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,2,1,1,2),_SnVrrpIfAuthType_Type())
snVrrpIfAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpIfAuthType.setStatus(_C)
class _SnVrrpIfAuthPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_SnVrrpIfAuthPassword_Type.__name__=_H
_SnVrrpIfAuthPassword_Object=MibTableColumn
snVrrpIfAuthPassword=_SnVrrpIfAuthPassword_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,2,1,1,3),_SnVrrpIfAuthPassword_Type())
snVrrpIfAuthPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpIfAuthPassword.setStatus(_C)
_SnVrrpIfRxHeaderErrCnts_Type=Counter32
_SnVrrpIfRxHeaderErrCnts_Object=MibTableColumn
snVrrpIfRxHeaderErrCnts=_SnVrrpIfRxHeaderErrCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,2,1,1,4),_SnVrrpIfRxHeaderErrCnts_Type())
snVrrpIfRxHeaderErrCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpIfRxHeaderErrCnts.setStatus(_C)
_SnVrrpIfRxAuthTypeErrCnts_Type=Counter32
_SnVrrpIfRxAuthTypeErrCnts_Object=MibTableColumn
snVrrpIfRxAuthTypeErrCnts=_SnVrrpIfRxAuthTypeErrCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,2,1,1,5),_SnVrrpIfRxAuthTypeErrCnts_Type())
snVrrpIfRxAuthTypeErrCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpIfRxAuthTypeErrCnts.setStatus(_C)
_SnVrrpIfRxAuthPwdMismatchErrCnts_Type=Counter32
_SnVrrpIfRxAuthPwdMismatchErrCnts_Object=MibTableColumn
snVrrpIfRxAuthPwdMismatchErrCnts=_SnVrrpIfRxAuthPwdMismatchErrCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,2,1,1,6),_SnVrrpIfRxAuthPwdMismatchErrCnts_Type())
snVrrpIfRxAuthPwdMismatchErrCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpIfRxAuthPwdMismatchErrCnts.setStatus(_C)
_SnVrrpIfRxVridErrCnts_Type=Counter32
_SnVrrpIfRxVridErrCnts_Object=MibTableColumn
snVrrpIfRxVridErrCnts=_SnVrrpIfRxVridErrCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,2,1,1,7),_SnVrrpIfRxVridErrCnts_Type())
snVrrpIfRxVridErrCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpIfRxVridErrCnts.setStatus(_C)
_SnVrrpVirRtr_ObjectIdentity=ObjectIdentity
snVrrpVirRtr=_SnVrrpVirRtr_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3))
_SnVrrpVirRtrTable_Object=MibTable
snVrrpVirRtrTable=_SnVrrpVirRtrTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1))
if mibBuilder.loadTexts:snVrrpVirRtrTable.setStatus(_C)
_SnVrrpVirRtrEntry_Object=MibTableRow
snVrrpVirRtrEntry=_SnVrrpVirRtrEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1))
snVrrpVirRtrEntry.setIndexNames((0,_I,_Q),(0,_I,_R))
if mibBuilder.loadTexts:snVrrpVirRtrEntry.setStatus(_C)
_SnVrrpVirRtrPort_Type=Integer32
_SnVrrpVirRtrPort_Object=MibTableColumn
snVrrpVirRtrPort=_SnVrrpVirRtrPort_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,1),_SnVrrpVirRtrPort_Type())
snVrrpVirRtrPort.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtrPort.setStatus(_C)
class _SnVrrpVirRtrId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SnVrrpVirRtrId_Type.__name__=_E
_SnVrrpVirRtrId_Object=MibTableColumn
snVrrpVirRtrId=_SnVrrpVirRtrId_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,2),_SnVrrpVirRtrId_Type())
snVrrpVirRtrId.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtrId.setStatus(_C)
class _SnVrrpVirRtrOwnership_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_S,0),('owner',1),(_J,2)))
_SnVrrpVirRtrOwnership_Type.__name__=_E
_SnVrrpVirRtrOwnership_Object=MibTableColumn
snVrrpVirRtrOwnership=_SnVrrpVirRtrOwnership_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,3),_SnVrrpVirRtrOwnership_Type())
snVrrpVirRtrOwnership.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtrOwnership.setStatus(_C)
class _SnVrrpVirRtrCfgPriority_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,254))
_SnVrrpVirRtrCfgPriority_Type.__name__=_E
_SnVrrpVirRtrCfgPriority_Object=MibTableColumn
snVrrpVirRtrCfgPriority=_SnVrrpVirRtrCfgPriority_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,4),_SnVrrpVirRtrCfgPriority_Type())
snVrrpVirRtrCfgPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtrCfgPriority.setStatus(_C)
class _SnVrrpVirRtrTrackPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_SnVrrpVirRtrTrackPriority_Type.__name__=_E
_SnVrrpVirRtrTrackPriority_Object=MibTableColumn
snVrrpVirRtrTrackPriority=_SnVrrpVirRtrTrackPriority_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,5),_SnVrrpVirRtrTrackPriority_Type())
snVrrpVirRtrTrackPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtrTrackPriority.setStatus(_C)
class _SnVrrpVirRtrCurrPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_SnVrrpVirRtrCurrPriority_Type.__name__=_E
_SnVrrpVirRtrCurrPriority_Object=MibTableColumn
snVrrpVirRtrCurrPriority=_SnVrrpVirRtrCurrPriority_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,6),_SnVrrpVirRtrCurrPriority_Type())
snVrrpVirRtrCurrPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtrCurrPriority.setStatus(_C)
class _SnVrrpVirRtrHelloInt_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,84))
_SnVrrpVirRtrHelloInt_Type.__name__=_E
_SnVrrpVirRtrHelloInt_Object=MibTableColumn
snVrrpVirRtrHelloInt=_SnVrrpVirRtrHelloInt_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,7),_SnVrrpVirRtrHelloInt_Type())
snVrrpVirRtrHelloInt.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtrHelloInt.setStatus(_C)
class _SnVrrpVirRtrDeadInt_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,84))
_SnVrrpVirRtrDeadInt_Type.__name__=_E
_SnVrrpVirRtrDeadInt_Object=MibTableColumn
snVrrpVirRtrDeadInt=_SnVrrpVirRtrDeadInt_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,8),_SnVrrpVirRtrDeadInt_Type())
snVrrpVirRtrDeadInt.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtrDeadInt.setStatus(_C)
class _SnVrrpVirRtrPreemptMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_SnVrrpVirRtrPreemptMode_Type.__name__=_E
_SnVrrpVirRtrPreemptMode_Object=MibTableColumn
snVrrpVirRtrPreemptMode=_SnVrrpVirRtrPreemptMode_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,9),_SnVrrpVirRtrPreemptMode_Type())
snVrrpVirRtrPreemptMode.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtrPreemptMode.setStatus(_C)
class _SnVrrpVirRtrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('init',0),(_T,1),(_J,2)))
_SnVrrpVirRtrState_Type.__name__=_E
_SnVrrpVirRtrState_Object=MibTableColumn
snVrrpVirRtrState=_SnVrrpVirRtrState_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,10),_SnVrrpVirRtrState_Type())
snVrrpVirRtrState.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtrState.setStatus(_C)
class _SnVrrpVirRtrActivate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_SnVrrpVirRtrActivate_Type.__name__=_E
_SnVrrpVirRtrActivate_Object=MibTableColumn
snVrrpVirRtrActivate=_SnVrrpVirRtrActivate_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,11),_SnVrrpVirRtrActivate_Type())
snVrrpVirRtrActivate.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtrActivate.setStatus(_C)
class _SnVrrpVirRtrIpAddrMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SnVrrpVirRtrIpAddrMask_Type.__name__=_H
_SnVrrpVirRtrIpAddrMask_Object=MibTableColumn
snVrrpVirRtrIpAddrMask=_SnVrrpVirRtrIpAddrMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,12),_SnVrrpVirRtrIpAddrMask_Type())
snVrrpVirRtrIpAddrMask.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtrIpAddrMask.setStatus(_C)
class _SnVrrpVirRtrTrackPortMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,32))
_SnVrrpVirRtrTrackPortMask_Type.__name__=_H
_SnVrrpVirRtrTrackPortMask_Object=MibTableColumn
snVrrpVirRtrTrackPortMask=_SnVrrpVirRtrTrackPortMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,13),_SnVrrpVirRtrTrackPortMask_Type())
snVrrpVirRtrTrackPortMask.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtrTrackPortMask.setStatus(_C)
class _SnVrrpVirRtrTrackVifMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,512))
_SnVrrpVirRtrTrackVifMask_Type.__name__=_H
_SnVrrpVirRtrTrackVifMask_Object=MibTableColumn
snVrrpVirRtrTrackVifMask=_SnVrrpVirRtrTrackVifMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,14),_SnVrrpVirRtrTrackVifMask_Type())
snVrrpVirRtrTrackVifMask.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtrTrackVifMask.setStatus(_C)
class _SnVrrpVirRtrRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_U,1),('valid',2),(_V,3),(_W,4),(_X,5)))
_SnVrrpVirRtrRowStatus_Type.__name__=_E
_SnVrrpVirRtrRowStatus_Object=MibTableColumn
snVrrpVirRtrRowStatus=_SnVrrpVirRtrRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,15),_SnVrrpVirRtrRowStatus_Type())
snVrrpVirRtrRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtrRowStatus.setStatus(_C)
_SnVrrpVirRtrRxArpPktDropCnts_Type=Counter32
_SnVrrpVirRtrRxArpPktDropCnts_Object=MibTableColumn
snVrrpVirRtrRxArpPktDropCnts=_SnVrrpVirRtrRxArpPktDropCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,16),_SnVrrpVirRtrRxArpPktDropCnts_Type())
snVrrpVirRtrRxArpPktDropCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtrRxArpPktDropCnts.setStatus(_C)
_SnVrrpVirRtrRxIpPktDropCnts_Type=Counter32
_SnVrrpVirRtrRxIpPktDropCnts_Object=MibTableColumn
snVrrpVirRtrRxIpPktDropCnts=_SnVrrpVirRtrRxIpPktDropCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,17),_SnVrrpVirRtrRxIpPktDropCnts_Type())
snVrrpVirRtrRxIpPktDropCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtrRxIpPktDropCnts.setStatus(_C)
_SnVrrpVirRtrRxPortMismatchCnts_Type=Counter32
_SnVrrpVirRtrRxPortMismatchCnts_Object=MibTableColumn
snVrrpVirRtrRxPortMismatchCnts=_SnVrrpVirRtrRxPortMismatchCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,18),_SnVrrpVirRtrRxPortMismatchCnts_Type())
snVrrpVirRtrRxPortMismatchCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtrRxPortMismatchCnts.setStatus(_C)
_SnVrrpVirRtrRxNumOfIpMismatchCnts_Type=Counter32
_SnVrrpVirRtrRxNumOfIpMismatchCnts_Object=MibTableColumn
snVrrpVirRtrRxNumOfIpMismatchCnts=_SnVrrpVirRtrRxNumOfIpMismatchCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,19),_SnVrrpVirRtrRxNumOfIpMismatchCnts_Type())
snVrrpVirRtrRxNumOfIpMismatchCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtrRxNumOfIpMismatchCnts.setStatus(_C)
_SnVrrpVirRtrRxIpMismatchCnts_Type=Counter32
_SnVrrpVirRtrRxIpMismatchCnts_Object=MibTableColumn
snVrrpVirRtrRxIpMismatchCnts=_SnVrrpVirRtrRxIpMismatchCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,20),_SnVrrpVirRtrRxIpMismatchCnts_Type())
snVrrpVirRtrRxIpMismatchCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtrRxIpMismatchCnts.setStatus(_C)
_SnVrrpVirRtrRxHelloIntMismatchCnts_Type=Counter32
_SnVrrpVirRtrRxHelloIntMismatchCnts_Object=MibTableColumn
snVrrpVirRtrRxHelloIntMismatchCnts=_SnVrrpVirRtrRxHelloIntMismatchCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,21),_SnVrrpVirRtrRxHelloIntMismatchCnts_Type())
snVrrpVirRtrRxHelloIntMismatchCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtrRxHelloIntMismatchCnts.setStatus(_C)
_SnVrrpVirRtrRxPriorityZeroFromMasterCnts_Type=Counter32
_SnVrrpVirRtrRxPriorityZeroFromMasterCnts_Object=MibTableColumn
snVrrpVirRtrRxPriorityZeroFromMasterCnts=_SnVrrpVirRtrRxPriorityZeroFromMasterCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,22),_SnVrrpVirRtrRxPriorityZeroFromMasterCnts_Type())
snVrrpVirRtrRxPriorityZeroFromMasterCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtrRxPriorityZeroFromMasterCnts.setStatus(_C)
_SnVrrpVirRtrRxHigherPriorityCnts_Type=Counter32
_SnVrrpVirRtrRxHigherPriorityCnts_Object=MibTableColumn
snVrrpVirRtrRxHigherPriorityCnts=_SnVrrpVirRtrRxHigherPriorityCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,23),_SnVrrpVirRtrRxHigherPriorityCnts_Type())
snVrrpVirRtrRxHigherPriorityCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtrRxHigherPriorityCnts.setStatus(_C)
_SnVrrpVirRtrTransToMasterStateCnts_Type=Counter32
_SnVrrpVirRtrTransToMasterStateCnts_Object=MibTableColumn
snVrrpVirRtrTransToMasterStateCnts=_SnVrrpVirRtrTransToMasterStateCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,24),_SnVrrpVirRtrTransToMasterStateCnts_Type())
snVrrpVirRtrTransToMasterStateCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtrTransToMasterStateCnts.setStatus(_C)
_SnVrrpVirRtrTransToBackupStateCnts_Type=Counter32
_SnVrrpVirRtrTransToBackupStateCnts_Object=MibTableColumn
snVrrpVirRtrTransToBackupStateCnts=_SnVrrpVirRtrTransToBackupStateCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,25),_SnVrrpVirRtrTransToBackupStateCnts_Type())
snVrrpVirRtrTransToBackupStateCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtrTransToBackupStateCnts.setStatus(_C)
_SnVrrpVirRtrCurrDeadInt_Type=Integer32
_SnVrrpVirRtrCurrDeadInt_Object=MibTableColumn
snVrrpVirRtrCurrDeadInt=_SnVrrpVirRtrCurrDeadInt_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,26),_SnVrrpVirRtrCurrDeadInt_Type())
snVrrpVirRtrCurrDeadInt.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtrCurrDeadInt.setStatus(_C)
_SnVrrpVirRtrTrackPortList_Type=OctetString
_SnVrrpVirRtrTrackPortList_Object=MibTableColumn
snVrrpVirRtrTrackPortList=_SnVrrpVirRtrTrackPortList_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,27),_SnVrrpVirRtrTrackPortList_Type())
snVrrpVirRtrTrackPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtrTrackPortList.setStatus(_C)
_SnVrrpVirRtrTrackVifPortList_Type=OctetString
_SnVrrpVirRtrTrackVifPortList_Object=MibTableColumn
snVrrpVirRtrTrackVifPortList=_SnVrrpVirRtrTrackVifPortList_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,3,1,1,28),_SnVrrpVirRtrTrackVifPortList_Type())
snVrrpVirRtrTrackVifPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtrTrackVifPortList.setStatus(_C)
_SnVrrpIntf2_ObjectIdentity=ObjectIdentity
snVrrpIntf2=_SnVrrpIntf2_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,2,12,4))
_SnVrrpIf2Table_Object=MibTable
snVrrpIf2Table=_SnVrrpIf2Table_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,4,1))
if mibBuilder.loadTexts:snVrrpIf2Table.setStatus(_A)
_SnVrrpIf2Entry_Object=MibTableRow
snVrrpIf2Entry=_SnVrrpIf2Entry_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,4,1,1))
snVrrpIf2Entry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:snVrrpIf2Entry.setStatus(_A)
class _SnVrrpIf2AuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2)))
_SnVrrpIf2AuthType_Type.__name__=_E
_SnVrrpIf2AuthType_Object=MibTableColumn
snVrrpIf2AuthType=_SnVrrpIf2AuthType_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,4,1,1,1),_SnVrrpIf2AuthType_Type())
snVrrpIf2AuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpIf2AuthType.setStatus(_A)
class _SnVrrpIf2AuthPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_SnVrrpIf2AuthPassword_Type.__name__=_H
_SnVrrpIf2AuthPassword_Object=MibTableColumn
snVrrpIf2AuthPassword=_SnVrrpIf2AuthPassword_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,4,1,1,2),_SnVrrpIf2AuthPassword_Type())
snVrrpIf2AuthPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpIf2AuthPassword.setStatus(_A)
_SnVrrpIf2RxHeaderErrCnts_Type=Counter32
_SnVrrpIf2RxHeaderErrCnts_Object=MibTableColumn
snVrrpIf2RxHeaderErrCnts=_SnVrrpIf2RxHeaderErrCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,4,1,1,3),_SnVrrpIf2RxHeaderErrCnts_Type())
snVrrpIf2RxHeaderErrCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpIf2RxHeaderErrCnts.setStatus(_A)
_SnVrrpIf2RxAuthTypeErrCnts_Type=Counter32
_SnVrrpIf2RxAuthTypeErrCnts_Object=MibTableColumn
snVrrpIf2RxAuthTypeErrCnts=_SnVrrpIf2RxAuthTypeErrCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,4,1,1,4),_SnVrrpIf2RxAuthTypeErrCnts_Type())
snVrrpIf2RxAuthTypeErrCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpIf2RxAuthTypeErrCnts.setStatus(_A)
_SnVrrpIf2RxAuthPwdMismatchErrCnts_Type=Counter32
_SnVrrpIf2RxAuthPwdMismatchErrCnts_Object=MibTableColumn
snVrrpIf2RxAuthPwdMismatchErrCnts=_SnVrrpIf2RxAuthPwdMismatchErrCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,4,1,1,5),_SnVrrpIf2RxAuthPwdMismatchErrCnts_Type())
snVrrpIf2RxAuthPwdMismatchErrCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpIf2RxAuthPwdMismatchErrCnts.setStatus(_A)
_SnVrrpIf2RxVridErrCnts_Type=Counter32
_SnVrrpIf2RxVridErrCnts_Object=MibTableColumn
snVrrpIf2RxVridErrCnts=_SnVrrpIf2RxVridErrCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,4,1,1,6),_SnVrrpIf2RxVridErrCnts_Type())
snVrrpIf2RxVridErrCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpIf2RxVridErrCnts.setStatus(_A)
_SnVrrpVirRtr2_ObjectIdentity=ObjectIdentity
snVrrpVirRtr2=_SnVrrpVirRtr2_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5))
_SnVrrpVirRtr2Table_Object=MibTable
snVrrpVirRtr2Table=_SnVrrpVirRtr2Table_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1))
if mibBuilder.loadTexts:snVrrpVirRtr2Table.setStatus(_A)
_SnVrrpVirRtr2Entry_Object=MibTableRow
snVrrpVirRtr2Entry=_SnVrrpVirRtr2Entry_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1))
snVrrpVirRtr2Entry.setIndexNames((0,_K,_L),(0,_I,_Y))
if mibBuilder.loadTexts:snVrrpVirRtr2Entry.setStatus(_A)
class _SnVrrpVirRtr2Id_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SnVrrpVirRtr2Id_Type.__name__=_E
_SnVrrpVirRtr2Id_Object=MibTableColumn
snVrrpVirRtr2Id=_SnVrrpVirRtr2Id_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,1),_SnVrrpVirRtr2Id_Type())
snVrrpVirRtr2Id.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtr2Id.setStatus(_A)
class _SnVrrpVirRtr2Ownership_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_S,0),('owner',1),(_J,2)))
_SnVrrpVirRtr2Ownership_Type.__name__=_E
_SnVrrpVirRtr2Ownership_Object=MibTableColumn
snVrrpVirRtr2Ownership=_SnVrrpVirRtr2Ownership_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,2),_SnVrrpVirRtr2Ownership_Type())
snVrrpVirRtr2Ownership.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtr2Ownership.setStatus(_A)
class _SnVrrpVirRtr2CfgPriority_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnVrrpVirRtr2CfgPriority_Type.__name__=_E
_SnVrrpVirRtr2CfgPriority_Object=MibTableColumn
snVrrpVirRtr2CfgPriority=_SnVrrpVirRtr2CfgPriority_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,3),_SnVrrpVirRtr2CfgPriority_Type())
snVrrpVirRtr2CfgPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtr2CfgPriority.setStatus(_A)
class _SnVrrpVirRtr2TrackPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_SnVrrpVirRtr2TrackPriority_Type.__name__=_E
_SnVrrpVirRtr2TrackPriority_Object=MibTableColumn
snVrrpVirRtr2TrackPriority=_SnVrrpVirRtr2TrackPriority_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,4),_SnVrrpVirRtr2TrackPriority_Type())
snVrrpVirRtr2TrackPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtr2TrackPriority.setStatus(_A)
class _SnVrrpVirRtr2CurrPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_SnVrrpVirRtr2CurrPriority_Type.__name__=_E
_SnVrrpVirRtr2CurrPriority_Object=MibTableColumn
snVrrpVirRtr2CurrPriority=_SnVrrpVirRtr2CurrPriority_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,5),_SnVrrpVirRtr2CurrPriority_Type())
snVrrpVirRtr2CurrPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtr2CurrPriority.setStatus(_A)
class _SnVrrpVirRtr2HelloInt_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,84))
_SnVrrpVirRtr2HelloInt_Type.__name__=_E
_SnVrrpVirRtr2HelloInt_Object=MibTableColumn
snVrrpVirRtr2HelloInt=_SnVrrpVirRtr2HelloInt_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,6),_SnVrrpVirRtr2HelloInt_Type())
snVrrpVirRtr2HelloInt.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtr2HelloInt.setStatus(_A)
class _SnVrrpVirRtr2DeadInt_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,84))
_SnVrrpVirRtr2DeadInt_Type.__name__=_E
_SnVrrpVirRtr2DeadInt_Object=MibTableColumn
snVrrpVirRtr2DeadInt=_SnVrrpVirRtr2DeadInt_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,7),_SnVrrpVirRtr2DeadInt_Type())
snVrrpVirRtr2DeadInt.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtr2DeadInt.setStatus(_A)
class _SnVrrpVirRtr2PreemptMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_SnVrrpVirRtr2PreemptMode_Type.__name__=_E
_SnVrrpVirRtr2PreemptMode_Object=MibTableColumn
snVrrpVirRtr2PreemptMode=_SnVrrpVirRtr2PreemptMode_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,8),_SnVrrpVirRtr2PreemptMode_Type())
snVrrpVirRtr2PreemptMode.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtr2PreemptMode.setStatus(_A)
class _SnVrrpVirRtr2State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('init',0),(_T,1),(_J,2)))
_SnVrrpVirRtr2State_Type.__name__=_E
_SnVrrpVirRtr2State_Object=MibTableColumn
snVrrpVirRtr2State=_SnVrrpVirRtr2State_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,9),_SnVrrpVirRtr2State_Type())
snVrrpVirRtr2State.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtr2State.setStatus(_A)
class _SnVrrpVirRtr2IpAddrMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SnVrrpVirRtr2IpAddrMask_Type.__name__=_H
_SnVrrpVirRtr2IpAddrMask_Object=MibTableColumn
snVrrpVirRtr2IpAddrMask=_SnVrrpVirRtr2IpAddrMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,10),_SnVrrpVirRtr2IpAddrMask_Type())
snVrrpVirRtr2IpAddrMask.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtr2IpAddrMask.setStatus(_A)
class _SnVrrpVirRtr2Activate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_SnVrrpVirRtr2Activate_Type.__name__=_E
_SnVrrpVirRtr2Activate_Object=MibTableColumn
snVrrpVirRtr2Activate=_SnVrrpVirRtr2Activate_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,11),_SnVrrpVirRtr2Activate_Type())
snVrrpVirRtr2Activate.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtr2Activate.setStatus(_A)
class _SnVrrpVirRtr2BackupInt_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,3600))
_SnVrrpVirRtr2BackupInt_Type.__name__=_E
_SnVrrpVirRtr2BackupInt_Object=MibTableColumn
snVrrpVirRtr2BackupInt=_SnVrrpVirRtr2BackupInt_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,12),_SnVrrpVirRtr2BackupInt_Type())
snVrrpVirRtr2BackupInt.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtr2BackupInt.setStatus(_A)
class _SnVrrpVirRtr2RowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_U,1),('valid',2),(_V,3),(_W,4),(_X,5)))
_SnVrrpVirRtr2RowStatus_Type.__name__=_E
_SnVrrpVirRtr2RowStatus_Object=MibTableColumn
snVrrpVirRtr2RowStatus=_SnVrrpVirRtr2RowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,13),_SnVrrpVirRtr2RowStatus_Type())
snVrrpVirRtr2RowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtr2RowStatus.setStatus(_A)
_SnVrrpVirRtr2RxArpPktDropCnts_Type=Counter32
_SnVrrpVirRtr2RxArpPktDropCnts_Object=MibTableColumn
snVrrpVirRtr2RxArpPktDropCnts=_SnVrrpVirRtr2RxArpPktDropCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,14),_SnVrrpVirRtr2RxArpPktDropCnts_Type())
snVrrpVirRtr2RxArpPktDropCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtr2RxArpPktDropCnts.setStatus(_A)
_SnVrrpVirRtr2RxIpPktDropCnts_Type=Counter32
_SnVrrpVirRtr2RxIpPktDropCnts_Object=MibTableColumn
snVrrpVirRtr2RxIpPktDropCnts=_SnVrrpVirRtr2RxIpPktDropCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,15),_SnVrrpVirRtr2RxIpPktDropCnts_Type())
snVrrpVirRtr2RxIpPktDropCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtr2RxIpPktDropCnts.setStatus(_A)
_SnVrrpVirRtr2RxPortMismatchCnts_Type=Counter32
_SnVrrpVirRtr2RxPortMismatchCnts_Object=MibTableColumn
snVrrpVirRtr2RxPortMismatchCnts=_SnVrrpVirRtr2RxPortMismatchCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,16),_SnVrrpVirRtr2RxPortMismatchCnts_Type())
snVrrpVirRtr2RxPortMismatchCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtr2RxPortMismatchCnts.setStatus(_A)
_SnVrrpVirRtr2RxNumOfIpMismatchCnts_Type=Counter32
_SnVrrpVirRtr2RxNumOfIpMismatchCnts_Object=MibTableColumn
snVrrpVirRtr2RxNumOfIpMismatchCnts=_SnVrrpVirRtr2RxNumOfIpMismatchCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,17),_SnVrrpVirRtr2RxNumOfIpMismatchCnts_Type())
snVrrpVirRtr2RxNumOfIpMismatchCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtr2RxNumOfIpMismatchCnts.setStatus(_A)
_SnVrrpVirRtr2RxIpMismatchCnts_Type=Counter32
_SnVrrpVirRtr2RxIpMismatchCnts_Object=MibTableColumn
snVrrpVirRtr2RxIpMismatchCnts=_SnVrrpVirRtr2RxIpMismatchCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,18),_SnVrrpVirRtr2RxIpMismatchCnts_Type())
snVrrpVirRtr2RxIpMismatchCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtr2RxIpMismatchCnts.setStatus(_A)
_SnVrrpVirRtr2RxHelloIntMismatchCnts_Type=Counter32
_SnVrrpVirRtr2RxHelloIntMismatchCnts_Object=MibTableColumn
snVrrpVirRtr2RxHelloIntMismatchCnts=_SnVrrpVirRtr2RxHelloIntMismatchCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,19),_SnVrrpVirRtr2RxHelloIntMismatchCnts_Type())
snVrrpVirRtr2RxHelloIntMismatchCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtr2RxHelloIntMismatchCnts.setStatus(_A)
_SnVrrpVirRtr2RxPriorityZeroFromMasterCnts_Type=Counter32
_SnVrrpVirRtr2RxPriorityZeroFromMasterCnts_Object=MibTableColumn
snVrrpVirRtr2RxPriorityZeroFromMasterCnts=_SnVrrpVirRtr2RxPriorityZeroFromMasterCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,20),_SnVrrpVirRtr2RxPriorityZeroFromMasterCnts_Type())
snVrrpVirRtr2RxPriorityZeroFromMasterCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtr2RxPriorityZeroFromMasterCnts.setStatus(_A)
_SnVrrpVirRtr2RxHigherPriorityCnts_Type=Counter32
_SnVrrpVirRtr2RxHigherPriorityCnts_Object=MibTableColumn
snVrrpVirRtr2RxHigherPriorityCnts=_SnVrrpVirRtr2RxHigherPriorityCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,21),_SnVrrpVirRtr2RxHigherPriorityCnts_Type())
snVrrpVirRtr2RxHigherPriorityCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtr2RxHigherPriorityCnts.setStatus(_A)
_SnVrrpVirRtr2TransToMasterStateCnts_Type=Counter32
_SnVrrpVirRtr2TransToMasterStateCnts_Object=MibTableColumn
snVrrpVirRtr2TransToMasterStateCnts=_SnVrrpVirRtr2TransToMasterStateCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,22),_SnVrrpVirRtr2TransToMasterStateCnts_Type())
snVrrpVirRtr2TransToMasterStateCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtr2TransToMasterStateCnts.setStatus(_A)
_SnVrrpVirRtr2TransToBackupStateCnts_Type=Counter32
_SnVrrpVirRtr2TransToBackupStateCnts_Object=MibTableColumn
snVrrpVirRtr2TransToBackupStateCnts=_SnVrrpVirRtr2TransToBackupStateCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,23),_SnVrrpVirRtr2TransToBackupStateCnts_Type())
snVrrpVirRtr2TransToBackupStateCnts.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtr2TransToBackupStateCnts.setStatus(_A)
_SnVrrpVirRtr2CurrDeadInt_Type=Integer32
_SnVrrpVirRtr2CurrDeadInt_Object=MibTableColumn
snVrrpVirRtr2CurrDeadInt=_SnVrrpVirRtr2CurrDeadInt_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,24),_SnVrrpVirRtr2CurrDeadInt_Type())
snVrrpVirRtr2CurrDeadInt.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtr2CurrDeadInt.setStatus(_A)
_SnVrrpVirRtr2TrackPortList_Type=OctetString
_SnVrrpVirRtr2TrackPortList_Object=MibTableColumn
snVrrpVirRtr2TrackPortList=_SnVrrpVirRtr2TrackPortList_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,25),_SnVrrpVirRtr2TrackPortList_Type())
snVrrpVirRtr2TrackPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtr2TrackPortList.setStatus(_A)
class _SnVrrpVirRtr2AdvertiseBackup_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_SnVrrpVirRtr2AdvertiseBackup_Type.__name__=_E
_SnVrrpVirRtr2AdvertiseBackup_Object=MibTableColumn
snVrrpVirRtr2AdvertiseBackup=_SnVrrpVirRtr2AdvertiseBackup_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,26),_SnVrrpVirRtr2AdvertiseBackup_Type())
snVrrpVirRtr2AdvertiseBackup.setMaxAccess(_D)
if mibBuilder.loadTexts:snVrrpVirRtr2AdvertiseBackup.setStatus(_A)
_SnVrrpVirRtr2MasterIpAddr_Type=IpAddress
_SnVrrpVirRtr2MasterIpAddr_Object=MibTableColumn
snVrrpVirRtr2MasterIpAddr=_SnVrrpVirRtr2MasterIpAddr_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,27),_SnVrrpVirRtr2MasterIpAddr_Type())
snVrrpVirRtr2MasterIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtr2MasterIpAddr.setStatus(_A)
class _SnVrrpVirRtr2IpAddrCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnVrrpVirRtr2IpAddrCount_Type.__name__=_E
_SnVrrpVirRtr2IpAddrCount_Object=MibTableColumn
snVrrpVirRtr2IpAddrCount=_SnVrrpVirRtr2IpAddrCount_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,28),_SnVrrpVirRtr2IpAddrCount_Type())
snVrrpVirRtr2IpAddrCount.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtr2IpAddrCount.setStatus(_A)
_SnVrrpVirRtr2VirtualMacAddr_Type=MacAddress
_SnVrrpVirRtr2VirtualMacAddr_Object=MibTableColumn
snVrrpVirRtr2VirtualMacAddr=_SnVrrpVirRtr2VirtualMacAddr_Object((1,3,6,1,4,1,11,2,3,7,11,12,2,12,5,1,1,29),_SnVrrpVirRtr2VirtualMacAddr_Type())
snVrrpVirRtr2VirtualMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:snVrrpVirRtr2VirtualMacAddr.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'MacAddress':MacAddress,'snVrrpGlobal':snVrrpGlobal,'snVrrpGroupOperMode':snVrrpGroupOperMode,'snVrrpIfStateChangeTrap':snVrrpIfStateChangeTrap,'snVrrpIfMaxNumVridPerIntf':snVrrpIfMaxNumVridPerIntf,'snVrrpIfMaxNumVridPerSystem':snVrrpIfMaxNumVridPerSystem,'snVrrpClearVrrpStat':snVrrpClearVrrpStat,'snVrrpGroupOperModeVrrpextended':snVrrpGroupOperModeVrrpextended,'snVrrpIntf':snVrrpIntf,'snVrrpIfTable':snVrrpIfTable,'snVrrpIfEntry':snVrrpIfEntry,_M:snVrrpIfPort,'snVrrpIfAuthType':snVrrpIfAuthType,'snVrrpIfAuthPassword':snVrrpIfAuthPassword,'snVrrpIfRxHeaderErrCnts':snVrrpIfRxHeaderErrCnts,'snVrrpIfRxAuthTypeErrCnts':snVrrpIfRxAuthTypeErrCnts,'snVrrpIfRxAuthPwdMismatchErrCnts':snVrrpIfRxAuthPwdMismatchErrCnts,'snVrrpIfRxVridErrCnts':snVrrpIfRxVridErrCnts,'snVrrpVirRtr':snVrrpVirRtr,'snVrrpVirRtrTable':snVrrpVirRtrTable,'snVrrpVirRtrEntry':snVrrpVirRtrEntry,_Q:snVrrpVirRtrPort,_R:snVrrpVirRtrId,'snVrrpVirRtrOwnership':snVrrpVirRtrOwnership,'snVrrpVirRtrCfgPriority':snVrrpVirRtrCfgPriority,'snVrrpVirRtrTrackPriority':snVrrpVirRtrTrackPriority,'snVrrpVirRtrCurrPriority':snVrrpVirRtrCurrPriority,'snVrrpVirRtrHelloInt':snVrrpVirRtrHelloInt,'snVrrpVirRtrDeadInt':snVrrpVirRtrDeadInt,'snVrrpVirRtrPreemptMode':snVrrpVirRtrPreemptMode,'snVrrpVirRtrState':snVrrpVirRtrState,'snVrrpVirRtrActivate':snVrrpVirRtrActivate,'snVrrpVirRtrIpAddrMask':snVrrpVirRtrIpAddrMask,'snVrrpVirRtrTrackPortMask':snVrrpVirRtrTrackPortMask,'snVrrpVirRtrTrackVifMask':snVrrpVirRtrTrackVifMask,'snVrrpVirRtrRowStatus':snVrrpVirRtrRowStatus,'snVrrpVirRtrRxArpPktDropCnts':snVrrpVirRtrRxArpPktDropCnts,'snVrrpVirRtrRxIpPktDropCnts':snVrrpVirRtrRxIpPktDropCnts,'snVrrpVirRtrRxPortMismatchCnts':snVrrpVirRtrRxPortMismatchCnts,'snVrrpVirRtrRxNumOfIpMismatchCnts':snVrrpVirRtrRxNumOfIpMismatchCnts,'snVrrpVirRtrRxIpMismatchCnts':snVrrpVirRtrRxIpMismatchCnts,'snVrrpVirRtrRxHelloIntMismatchCnts':snVrrpVirRtrRxHelloIntMismatchCnts,'snVrrpVirRtrRxPriorityZeroFromMasterCnts':snVrrpVirRtrRxPriorityZeroFromMasterCnts,'snVrrpVirRtrRxHigherPriorityCnts':snVrrpVirRtrRxHigherPriorityCnts,'snVrrpVirRtrTransToMasterStateCnts':snVrrpVirRtrTransToMasterStateCnts,'snVrrpVirRtrTransToBackupStateCnts':snVrrpVirRtrTransToBackupStateCnts,'snVrrpVirRtrCurrDeadInt':snVrrpVirRtrCurrDeadInt,'snVrrpVirRtrTrackPortList':snVrrpVirRtrTrackPortList,'snVrrpVirRtrTrackVifPortList':snVrrpVirRtrTrackVifPortList,'snVrrpIntf2':snVrrpIntf2,'snVrrpIf2Table':snVrrpIf2Table,'snVrrpIf2Entry':snVrrpIf2Entry,'snVrrpIf2AuthType':snVrrpIf2AuthType,'snVrrpIf2AuthPassword':snVrrpIf2AuthPassword,'snVrrpIf2RxHeaderErrCnts':snVrrpIf2RxHeaderErrCnts,'snVrrpIf2RxAuthTypeErrCnts':snVrrpIf2RxAuthTypeErrCnts,'snVrrpIf2RxAuthPwdMismatchErrCnts':snVrrpIf2RxAuthPwdMismatchErrCnts,'snVrrpIf2RxVridErrCnts':snVrrpIf2RxVridErrCnts,'snVrrpVirRtr2':snVrrpVirRtr2,'snVrrpVirRtr2Table':snVrrpVirRtr2Table,'snVrrpVirRtr2Entry':snVrrpVirRtr2Entry,_Y:snVrrpVirRtr2Id,'snVrrpVirRtr2Ownership':snVrrpVirRtr2Ownership,'snVrrpVirRtr2CfgPriority':snVrrpVirRtr2CfgPriority,'snVrrpVirRtr2TrackPriority':snVrrpVirRtr2TrackPriority,'snVrrpVirRtr2CurrPriority':snVrrpVirRtr2CurrPriority,'snVrrpVirRtr2HelloInt':snVrrpVirRtr2HelloInt,'snVrrpVirRtr2DeadInt':snVrrpVirRtr2DeadInt,'snVrrpVirRtr2PreemptMode':snVrrpVirRtr2PreemptMode,'snVrrpVirRtr2State':snVrrpVirRtr2State,'snVrrpVirRtr2IpAddrMask':snVrrpVirRtr2IpAddrMask,'snVrrpVirRtr2Activate':snVrrpVirRtr2Activate,'snVrrpVirRtr2BackupInt':snVrrpVirRtr2BackupInt,'snVrrpVirRtr2RowStatus':snVrrpVirRtr2RowStatus,'snVrrpVirRtr2RxArpPktDropCnts':snVrrpVirRtr2RxArpPktDropCnts,'snVrrpVirRtr2RxIpPktDropCnts':snVrrpVirRtr2RxIpPktDropCnts,'snVrrpVirRtr2RxPortMismatchCnts':snVrrpVirRtr2RxPortMismatchCnts,'snVrrpVirRtr2RxNumOfIpMismatchCnts':snVrrpVirRtr2RxNumOfIpMismatchCnts,'snVrrpVirRtr2RxIpMismatchCnts':snVrrpVirRtr2RxIpMismatchCnts,'snVrrpVirRtr2RxHelloIntMismatchCnts':snVrrpVirRtr2RxHelloIntMismatchCnts,'snVrrpVirRtr2RxPriorityZeroFromMasterCnts':snVrrpVirRtr2RxPriorityZeroFromMasterCnts,'snVrrpVirRtr2RxHigherPriorityCnts':snVrrpVirRtr2RxHigherPriorityCnts,'snVrrpVirRtr2TransToMasterStateCnts':snVrrpVirRtr2TransToMasterStateCnts,'snVrrpVirRtr2TransToBackupStateCnts':snVrrpVirRtr2TransToBackupStateCnts,'snVrrpVirRtr2CurrDeadInt':snVrrpVirRtr2CurrDeadInt,'snVrrpVirRtr2TrackPortList':snVrrpVirRtr2TrackPortList,'snVrrpVirRtr2AdvertiseBackup':snVrrpVirRtr2AdvertiseBackup,'snVrrpVirRtr2MasterIpAddr':snVrrpVirRtr2MasterIpAddr,'snVrrpVirRtr2IpAddrCount':snVrrpVirRtr2IpAddrCount,'snVrrpVirRtr2VirtualMacAddr':snVrrpVirRtr2VirtualMacAddr})