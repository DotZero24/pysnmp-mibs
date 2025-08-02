_L='backup'
_K='snVsrpVirRtrId'
_J='snVsrpVirRtrVlanId'
_I='snVsrpIfVlanId'
_H='OctetString'
_G='HP-SN-VSRP-MIB'
_F='enabled'
_E='disabled'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
snVsrp,=mibBuilder.importSymbols('HP-SN-SWITCH-GROUP-MIB','snVsrp')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SnVsrpGlobal_ObjectIdentity=ObjectIdentity
snVsrpGlobal=_SnVsrpGlobal_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,1))
class _SnVsrpGroupOperModeVsrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_SnVsrpGroupOperModeVsrp_Type.__name__=_B
_SnVsrpGroupOperModeVsrp_Object=MibScalar
snVsrpGroupOperModeVsrp=_SnVsrpGroupOperModeVsrp_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,1,1),_SnVsrpGroupOperModeVsrp_Type())
snVsrpGroupOperModeVsrp.setMaxAccess(_D)
if mibBuilder.loadTexts:snVsrpGroupOperModeVsrp.setStatus(_A)
class _SnVsrpIfStateChangeTrap_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_SnVsrpIfStateChangeTrap_Type.__name__=_B
_SnVsrpIfStateChangeTrap_Object=MibScalar
snVsrpIfStateChangeTrap=_SnVsrpIfStateChangeTrap_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,1,2),_SnVsrpIfStateChangeTrap_Type())
snVsrpIfStateChangeTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:snVsrpIfStateChangeTrap.setStatus(_A)
_SnVsrpIfMaxNumVridPerIntf_Type=Integer32
_SnVsrpIfMaxNumVridPerIntf_Object=MibScalar
snVsrpIfMaxNumVridPerIntf=_SnVsrpIfMaxNumVridPerIntf_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,1,3),_SnVsrpIfMaxNumVridPerIntf_Type())
snVsrpIfMaxNumVridPerIntf.setMaxAccess(_C)
if mibBuilder.loadTexts:snVsrpIfMaxNumVridPerIntf.setStatus(_A)
_SnVsrpIfMaxNumVridPerSystem_Type=Integer32
_SnVsrpIfMaxNumVridPerSystem_Object=MibScalar
snVsrpIfMaxNumVridPerSystem=_SnVsrpIfMaxNumVridPerSystem_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,1,4),_SnVsrpIfMaxNumVridPerSystem_Type())
snVsrpIfMaxNumVridPerSystem.setMaxAccess(_C)
if mibBuilder.loadTexts:snVsrpIfMaxNumVridPerSystem.setStatus(_A)
class _SnVsrpClearVrrpStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('clear',1)))
_SnVsrpClearVrrpStat_Type.__name__=_B
_SnVsrpClearVrrpStat_Object=MibScalar
snVsrpClearVrrpStat=_SnVsrpClearVrrpStat_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,1,5),_SnVsrpClearVrrpStat_Type())
snVsrpClearVrrpStat.setMaxAccess(_D)
if mibBuilder.loadTexts:snVsrpClearVrrpStat.setStatus(_A)
_SnVsrpIfIntf_ObjectIdentity=ObjectIdentity
snVsrpIfIntf=_SnVsrpIfIntf_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,2))
_SnVsrpIfTable_Object=MibTable
snVsrpIfTable=_SnVsrpIfTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,2,1))
if mibBuilder.loadTexts:snVsrpIfTable.setStatus(_A)
_SnVsrpIfEntry_Object=MibTableRow
snVsrpIfEntry=_SnVsrpIfEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,2,1,1))
snVsrpIfEntry.setIndexNames((0,_G,_I))
if mibBuilder.loadTexts:snVsrpIfEntry.setStatus(_A)
_SnVsrpIfVlanId_Type=Integer32
_SnVsrpIfVlanId_Object=MibTableColumn
snVsrpIfVlanId=_SnVsrpIfVlanId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,2,1,1,1),_SnVsrpIfVlanId_Type())
snVsrpIfVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:snVsrpIfVlanId.setStatus(_A)
class _SnVsrpIfAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('noAuth',0),('simpleTextPasswd',1),('ipAuthHeader',2)))
_SnVsrpIfAuthType_Type.__name__=_B
_SnVsrpIfAuthType_Object=MibTableColumn
snVsrpIfAuthType=_SnVsrpIfAuthType_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,2,1,1,2),_SnVsrpIfAuthType_Type())
snVsrpIfAuthType.setMaxAccess(_D)
if mibBuilder.loadTexts:snVsrpIfAuthType.setStatus(_A)
class _SnVsrpIfAuthPassword_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_SnVsrpIfAuthPassword_Type.__name__=_H
_SnVsrpIfAuthPassword_Object=MibTableColumn
snVsrpIfAuthPassword=_SnVsrpIfAuthPassword_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,2,1,1,3),_SnVsrpIfAuthPassword_Type())
snVsrpIfAuthPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:snVsrpIfAuthPassword.setStatus(_A)
_SnVsrpVirRtr_ObjectIdentity=ObjectIdentity
snVsrpVirRtr=_SnVsrpVirRtr_ObjectIdentity((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3))
_SnVsrpVirRtrTable_Object=MibTable
snVsrpVirRtrTable=_SnVsrpVirRtrTable_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1))
if mibBuilder.loadTexts:snVsrpVirRtrTable.setStatus(_A)
_SnVsrpVirRtrEntry_Object=MibTableRow
snVsrpVirRtrEntry=_SnVsrpVirRtrEntry_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1))
snVsrpVirRtrEntry.setIndexNames((0,_G,_J),(0,_G,_K))
if mibBuilder.loadTexts:snVsrpVirRtrEntry.setStatus(_A)
_SnVsrpVirRtrVlanId_Type=Integer32
_SnVsrpVirRtrVlanId_Object=MibTableColumn
snVsrpVirRtrVlanId=_SnVsrpVirRtrVlanId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,1),_SnVsrpVirRtrVlanId_Type())
snVsrpVirRtrVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:snVsrpVirRtrVlanId.setStatus(_A)
class _SnVsrpVirRtrId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SnVsrpVirRtrId_Type.__name__=_B
_SnVsrpVirRtrId_Object=MibTableColumn
snVsrpVirRtrId=_SnVsrpVirRtrId_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,2),_SnVsrpVirRtrId_Type())
snVsrpVirRtrId.setMaxAccess(_C)
if mibBuilder.loadTexts:snVsrpVirRtrId.setStatus(_A)
class _SnVsrpVirRtrOwnership_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('incomplete',0),('owner',1),(_L,2)))
_SnVsrpVirRtrOwnership_Type.__name__=_B
_SnVsrpVirRtrOwnership_Object=MibTableColumn
snVsrpVirRtrOwnership=_SnVsrpVirRtrOwnership_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,3),_SnVsrpVirRtrOwnership_Type())
snVsrpVirRtrOwnership.setMaxAccess(_D)
if mibBuilder.loadTexts:snVsrpVirRtrOwnership.setStatus(_A)
class _SnVsrpVirRtrCfgPriority_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_SnVsrpVirRtrCfgPriority_Type.__name__=_B
_SnVsrpVirRtrCfgPriority_Object=MibTableColumn
snVsrpVirRtrCfgPriority=_SnVsrpVirRtrCfgPriority_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,4),_SnVsrpVirRtrCfgPriority_Type())
snVsrpVirRtrCfgPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:snVsrpVirRtrCfgPriority.setStatus(_A)
class _SnVsrpVirRtrTrackPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_SnVsrpVirRtrTrackPriority_Type.__name__=_B
_SnVsrpVirRtrTrackPriority_Object=MibTableColumn
snVsrpVirRtrTrackPriority=_SnVsrpVirRtrTrackPriority_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,5),_SnVsrpVirRtrTrackPriority_Type())
snVsrpVirRtrTrackPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:snVsrpVirRtrTrackPriority.setStatus(_A)
class _SnVsrpVirRtrCurrPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_SnVsrpVirRtrCurrPriority_Type.__name__=_B
_SnVsrpVirRtrCurrPriority_Object=MibTableColumn
snVsrpVirRtrCurrPriority=_SnVsrpVirRtrCurrPriority_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,6),_SnVsrpVirRtrCurrPriority_Type())
snVsrpVirRtrCurrPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:snVsrpVirRtrCurrPriority.setStatus(_A)
class _SnVsrpVirRtrHelloInt_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,84))
_SnVsrpVirRtrHelloInt_Type.__name__=_B
_SnVsrpVirRtrHelloInt_Object=MibTableColumn
snVsrpVirRtrHelloInt=_SnVsrpVirRtrHelloInt_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,7),_SnVsrpVirRtrHelloInt_Type())
snVsrpVirRtrHelloInt.setMaxAccess(_D)
if mibBuilder.loadTexts:snVsrpVirRtrHelloInt.setStatus(_A)
class _SnVsrpVirRtrDeadInt_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,84))
_SnVsrpVirRtrDeadInt_Type.__name__=_B
_SnVsrpVirRtrDeadInt_Object=MibTableColumn
snVsrpVirRtrDeadInt=_SnVsrpVirRtrDeadInt_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,8),_SnVsrpVirRtrDeadInt_Type())
snVsrpVirRtrDeadInt.setMaxAccess(_D)
if mibBuilder.loadTexts:snVsrpVirRtrDeadInt.setStatus(_A)
class _SnVsrpVirRtrPreemptMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_SnVsrpVirRtrPreemptMode_Type.__name__=_B
_SnVsrpVirRtrPreemptMode_Object=MibTableColumn
snVsrpVirRtrPreemptMode=_SnVsrpVirRtrPreemptMode_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,9),_SnVsrpVirRtrPreemptMode_Type())
snVsrpVirRtrPreemptMode.setMaxAccess(_D)
if mibBuilder.loadTexts:snVsrpVirRtrPreemptMode.setStatus(_A)
class _SnVsrpVirRtrState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('init',0),('master',1),(_L,2)))
_SnVsrpVirRtrState_Type.__name__=_B
_SnVsrpVirRtrState_Object=MibTableColumn
snVsrpVirRtrState=_SnVsrpVirRtrState_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,10),_SnVsrpVirRtrState_Type())
snVsrpVirRtrState.setMaxAccess(_C)
if mibBuilder.loadTexts:snVsrpVirRtrState.setStatus(_A)
class _SnVsrpVirRtrIpAddrMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_SnVsrpVirRtrIpAddrMask_Type.__name__=_H
_SnVsrpVirRtrIpAddrMask_Object=MibTableColumn
snVsrpVirRtrIpAddrMask=_SnVsrpVirRtrIpAddrMask_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,11),_SnVsrpVirRtrIpAddrMask_Type())
snVsrpVirRtrIpAddrMask.setMaxAccess(_D)
if mibBuilder.loadTexts:snVsrpVirRtrIpAddrMask.setStatus(_A)
class _SnVsrpVirRtrActivate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_SnVsrpVirRtrActivate_Type.__name__=_B
_SnVsrpVirRtrActivate_Object=MibTableColumn
snVsrpVirRtrActivate=_SnVsrpVirRtrActivate_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,12),_SnVsrpVirRtrActivate_Type())
snVsrpVirRtrActivate.setMaxAccess(_D)
if mibBuilder.loadTexts:snVsrpVirRtrActivate.setStatus(_A)
_SnVsrpVirRtrTrackPortList_Type=OctetString
_SnVsrpVirRtrTrackPortList_Object=MibTableColumn
snVsrpVirRtrTrackPortList=_SnVsrpVirRtrTrackPortList_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,13),_SnVsrpVirRtrTrackPortList_Type())
snVsrpVirRtrTrackPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:snVsrpVirRtrTrackPortList.setStatus(_A)
class _SnVsrpVirRtrAdvertiseBackup_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_SnVsrpVirRtrAdvertiseBackup_Type.__name__=_B
_SnVsrpVirRtrAdvertiseBackup_Object=MibTableColumn
snVsrpVirRtrAdvertiseBackup=_SnVsrpVirRtrAdvertiseBackup_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,14),_SnVsrpVirRtrAdvertiseBackup_Type())
snVsrpVirRtrAdvertiseBackup.setMaxAccess(_D)
if mibBuilder.loadTexts:snVsrpVirRtrAdvertiseBackup.setStatus(_A)
class _SnVsrpVirRtrHoldDownInt_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,84))
_SnVsrpVirRtrHoldDownInt_Type.__name__=_B
_SnVsrpVirRtrHoldDownInt_Object=MibTableColumn
snVsrpVirRtrHoldDownInt=_SnVsrpVirRtrHoldDownInt_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,15),_SnVsrpVirRtrHoldDownInt_Type())
snVsrpVirRtrHoldDownInt.setMaxAccess(_D)
if mibBuilder.loadTexts:snVsrpVirRtrHoldDownInt.setStatus(_A)
class _SnVsrpVirRtrInitTtl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SnVsrpVirRtrInitTtl_Type.__name__=_B
_SnVsrpVirRtrInitTtl_Object=MibTableColumn
snVsrpVirRtrInitTtl=_SnVsrpVirRtrInitTtl_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,16),_SnVsrpVirRtrInitTtl_Type())
snVsrpVirRtrInitTtl.setMaxAccess(_D)
if mibBuilder.loadTexts:snVsrpVirRtrInitTtl.setStatus(_A)
_SnVsrpVirRtrIncPortList_Type=OctetString
_SnVsrpVirRtrIncPortList_Object=MibTableColumn
snVsrpVirRtrIncPortList=_SnVsrpVirRtrIncPortList_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,17),_SnVsrpVirRtrIncPortList_Type())
snVsrpVirRtrIncPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:snVsrpVirRtrIncPortList.setStatus(_A)
class _SnVsrpVirRtrSave_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_SnVsrpVirRtrSave_Type.__name__=_B
_SnVsrpVirRtrSave_Object=MibTableColumn
snVsrpVirRtrSave=_SnVsrpVirRtrSave_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,18),_SnVsrpVirRtrSave_Type())
snVsrpVirRtrSave.setMaxAccess(_D)
if mibBuilder.loadTexts:snVsrpVirRtrSave.setStatus(_A)
class _SnVsrpVirRtrBackupInt_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,3600))
_SnVsrpVirRtrBackupInt_Type.__name__=_B
_SnVsrpVirRtrBackupInt_Object=MibTableColumn
snVsrpVirRtrBackupInt=_SnVsrpVirRtrBackupInt_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,19),_SnVsrpVirRtrBackupInt_Type())
snVsrpVirRtrBackupInt.setMaxAccess(_D)
if mibBuilder.loadTexts:snVsrpVirRtrBackupInt.setStatus(_A)
class _SnVsrpVirRtrRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('invalid',1),('valid',2),('delete',3),('create',4),('modify',5)))
_SnVsrpVirRtrRowStatus_Type.__name__=_B
_SnVsrpVirRtrRowStatus_Object=MibTableColumn
snVsrpVirRtrRowStatus=_SnVsrpVirRtrRowStatus_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,20),_SnVsrpVirRtrRowStatus_Type())
snVsrpVirRtrRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:snVsrpVirRtrRowStatus.setStatus(_A)
_SnVsrpVirRtrRxArpPktDropCnts_Type=Counter32
_SnVsrpVirRtrRxArpPktDropCnts_Object=MibTableColumn
snVsrpVirRtrRxArpPktDropCnts=_SnVsrpVirRtrRxArpPktDropCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,21),_SnVsrpVirRtrRxArpPktDropCnts_Type())
snVsrpVirRtrRxArpPktDropCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:snVsrpVirRtrRxArpPktDropCnts.setStatus(_A)
_SnVsrpVirRtrRxIpPktDropCnts_Type=Counter32
_SnVsrpVirRtrRxIpPktDropCnts_Object=MibTableColumn
snVsrpVirRtrRxIpPktDropCnts=_SnVsrpVirRtrRxIpPktDropCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,22),_SnVsrpVirRtrRxIpPktDropCnts_Type())
snVsrpVirRtrRxIpPktDropCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:snVsrpVirRtrRxIpPktDropCnts.setStatus(_A)
_SnVsrpVirRtrRxPortMismatchCnts_Type=Counter32
_SnVsrpVirRtrRxPortMismatchCnts_Object=MibTableColumn
snVsrpVirRtrRxPortMismatchCnts=_SnVsrpVirRtrRxPortMismatchCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,23),_SnVsrpVirRtrRxPortMismatchCnts_Type())
snVsrpVirRtrRxPortMismatchCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:snVsrpVirRtrRxPortMismatchCnts.setStatus(_A)
_SnVsrpVirRtrRxNumOfIpMismatchCnts_Type=Counter32
_SnVsrpVirRtrRxNumOfIpMismatchCnts_Object=MibTableColumn
snVsrpVirRtrRxNumOfIpMismatchCnts=_SnVsrpVirRtrRxNumOfIpMismatchCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,24),_SnVsrpVirRtrRxNumOfIpMismatchCnts_Type())
snVsrpVirRtrRxNumOfIpMismatchCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:snVsrpVirRtrRxNumOfIpMismatchCnts.setStatus(_A)
_SnVsrpVirRtrRxIpMismatchCnts_Type=Counter32
_SnVsrpVirRtrRxIpMismatchCnts_Object=MibTableColumn
snVsrpVirRtrRxIpMismatchCnts=_SnVsrpVirRtrRxIpMismatchCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,25),_SnVsrpVirRtrRxIpMismatchCnts_Type())
snVsrpVirRtrRxIpMismatchCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:snVsrpVirRtrRxIpMismatchCnts.setStatus(_A)
_SnVsrpVirRtrRxHelloIntMismatchCnts_Type=Counter32
_SnVsrpVirRtrRxHelloIntMismatchCnts_Object=MibTableColumn
snVsrpVirRtrRxHelloIntMismatchCnts=_SnVsrpVirRtrRxHelloIntMismatchCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,26),_SnVsrpVirRtrRxHelloIntMismatchCnts_Type())
snVsrpVirRtrRxHelloIntMismatchCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:snVsrpVirRtrRxHelloIntMismatchCnts.setStatus(_A)
_SnVsrpVirRtrRxPriorityZeroFromMasterCnts_Type=Counter32
_SnVsrpVirRtrRxPriorityZeroFromMasterCnts_Object=MibTableColumn
snVsrpVirRtrRxPriorityZeroFromMasterCnts=_SnVsrpVirRtrRxPriorityZeroFromMasterCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,27),_SnVsrpVirRtrRxPriorityZeroFromMasterCnts_Type())
snVsrpVirRtrRxPriorityZeroFromMasterCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:snVsrpVirRtrRxPriorityZeroFromMasterCnts.setStatus(_A)
_SnVsrpVirRtrRxHigherPriorityCnts_Type=Counter32
_SnVsrpVirRtrRxHigherPriorityCnts_Object=MibTableColumn
snVsrpVirRtrRxHigherPriorityCnts=_SnVsrpVirRtrRxHigherPriorityCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,28),_SnVsrpVirRtrRxHigherPriorityCnts_Type())
snVsrpVirRtrRxHigherPriorityCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:snVsrpVirRtrRxHigherPriorityCnts.setStatus(_A)
_SnVsrpVirRtrTransToMasterStateCnts_Type=Counter32
_SnVsrpVirRtrTransToMasterStateCnts_Object=MibTableColumn
snVsrpVirRtrTransToMasterStateCnts=_SnVsrpVirRtrTransToMasterStateCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,29),_SnVsrpVirRtrTransToMasterStateCnts_Type())
snVsrpVirRtrTransToMasterStateCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:snVsrpVirRtrTransToMasterStateCnts.setStatus(_A)
_SnVsrpVirRtrTransToBackupStateCnts_Type=Counter32
_SnVsrpVirRtrTransToBackupStateCnts_Object=MibTableColumn
snVsrpVirRtrTransToBackupStateCnts=_SnVsrpVirRtrTransToBackupStateCnts_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,30),_SnVsrpVirRtrTransToBackupStateCnts_Type())
snVsrpVirRtrTransToBackupStateCnts.setMaxAccess(_C)
if mibBuilder.loadTexts:snVsrpVirRtrTransToBackupStateCnts.setStatus(_A)
_SnVsrpVirRtrCurrDeadInt_Type=Integer32
_SnVsrpVirRtrCurrDeadInt_Object=MibTableColumn
snVsrpVirRtrCurrDeadInt=_SnVsrpVirRtrCurrDeadInt_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,31),_SnVsrpVirRtrCurrDeadInt_Type())
snVsrpVirRtrCurrDeadInt.setMaxAccess(_C)
if mibBuilder.loadTexts:snVsrpVirRtrCurrDeadInt.setStatus(_A)
class _SnVsrpVirRtrCurHelloInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,84))
_SnVsrpVirRtrCurHelloInt_Type.__name__=_B
_SnVsrpVirRtrCurHelloInt_Object=MibTableColumn
snVsrpVirRtrCurHelloInt=_SnVsrpVirRtrCurHelloInt_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,32),_SnVsrpVirRtrCurHelloInt_Type())
snVsrpVirRtrCurHelloInt.setMaxAccess(_C)
if mibBuilder.loadTexts:snVsrpVirRtrCurHelloInt.setStatus(_A)
class _SnVsrpVirRtrCurHoldDownInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,84))
_SnVsrpVirRtrCurHoldDownInt_Type.__name__=_B
_SnVsrpVirRtrCurHoldDownInt_Object=MibTableColumn
snVsrpVirRtrCurHoldDownInt=_SnVsrpVirRtrCurHoldDownInt_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,33),_SnVsrpVirRtrCurHoldDownInt_Type())
snVsrpVirRtrCurHoldDownInt.setMaxAccess(_C)
if mibBuilder.loadTexts:snVsrpVirRtrCurHoldDownInt.setStatus(_A)
class _SnVsrpVirRtrCurInitTtl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SnVsrpVirRtrCurInitTtl_Type.__name__=_B
_SnVsrpVirRtrCurInitTtl_Object=MibTableColumn
snVsrpVirRtrCurInitTtl=_SnVsrpVirRtrCurInitTtl_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,34),_SnVsrpVirRtrCurInitTtl_Type())
snVsrpVirRtrCurInitTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:snVsrpVirRtrCurInitTtl.setStatus(_A)
_SnVsrpVirRtrHelloMacAddress_Type=MacAddress
_SnVsrpVirRtrHelloMacAddress_Object=MibTableColumn
snVsrpVirRtrHelloMacAddress=_SnVsrpVirRtrHelloMacAddress_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,35),_SnVsrpVirRtrHelloMacAddress_Type())
snVsrpVirRtrHelloMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:snVsrpVirRtrHelloMacAddress.setStatus(_A)
_SnVsrpVirRtrMasterIpAddr_Type=IpAddress
_SnVsrpVirRtrMasterIpAddr_Object=MibTableColumn
snVsrpVirRtrMasterIpAddr=_SnVsrpVirRtrMasterIpAddr_Object((1,3,6,1,4,1,11,2,3,7,11,12,1,3,21,3,1,1,36),_SnVsrpVirRtrMasterIpAddr_Type())
snVsrpVirRtrMasterIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:snVsrpVirRtrMasterIpAddr.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'MacAddress':MacAddress,'snVsrpGlobal':snVsrpGlobal,'snVsrpGroupOperModeVsrp':snVsrpGroupOperModeVsrp,'snVsrpIfStateChangeTrap':snVsrpIfStateChangeTrap,'snVsrpIfMaxNumVridPerIntf':snVsrpIfMaxNumVridPerIntf,'snVsrpIfMaxNumVridPerSystem':snVsrpIfMaxNumVridPerSystem,'snVsrpClearVrrpStat':snVsrpClearVrrpStat,'snVsrpIfIntf':snVsrpIfIntf,'snVsrpIfTable':snVsrpIfTable,'snVsrpIfEntry':snVsrpIfEntry,_I:snVsrpIfVlanId,'snVsrpIfAuthType':snVsrpIfAuthType,'snVsrpIfAuthPassword':snVsrpIfAuthPassword,'snVsrpVirRtr':snVsrpVirRtr,'snVsrpVirRtrTable':snVsrpVirRtrTable,'snVsrpVirRtrEntry':snVsrpVirRtrEntry,_J:snVsrpVirRtrVlanId,_K:snVsrpVirRtrId,'snVsrpVirRtrOwnership':snVsrpVirRtrOwnership,'snVsrpVirRtrCfgPriority':snVsrpVirRtrCfgPriority,'snVsrpVirRtrTrackPriority':snVsrpVirRtrTrackPriority,'snVsrpVirRtrCurrPriority':snVsrpVirRtrCurrPriority,'snVsrpVirRtrHelloInt':snVsrpVirRtrHelloInt,'snVsrpVirRtrDeadInt':snVsrpVirRtrDeadInt,'snVsrpVirRtrPreemptMode':snVsrpVirRtrPreemptMode,'snVsrpVirRtrState':snVsrpVirRtrState,'snVsrpVirRtrIpAddrMask':snVsrpVirRtrIpAddrMask,'snVsrpVirRtrActivate':snVsrpVirRtrActivate,'snVsrpVirRtrTrackPortList':snVsrpVirRtrTrackPortList,'snVsrpVirRtrAdvertiseBackup':snVsrpVirRtrAdvertiseBackup,'snVsrpVirRtrHoldDownInt':snVsrpVirRtrHoldDownInt,'snVsrpVirRtrInitTtl':snVsrpVirRtrInitTtl,'snVsrpVirRtrIncPortList':snVsrpVirRtrIncPortList,'snVsrpVirRtrSave':snVsrpVirRtrSave,'snVsrpVirRtrBackupInt':snVsrpVirRtrBackupInt,'snVsrpVirRtrRowStatus':snVsrpVirRtrRowStatus,'snVsrpVirRtrRxArpPktDropCnts':snVsrpVirRtrRxArpPktDropCnts,'snVsrpVirRtrRxIpPktDropCnts':snVsrpVirRtrRxIpPktDropCnts,'snVsrpVirRtrRxPortMismatchCnts':snVsrpVirRtrRxPortMismatchCnts,'snVsrpVirRtrRxNumOfIpMismatchCnts':snVsrpVirRtrRxNumOfIpMismatchCnts,'snVsrpVirRtrRxIpMismatchCnts':snVsrpVirRtrRxIpMismatchCnts,'snVsrpVirRtrRxHelloIntMismatchCnts':snVsrpVirRtrRxHelloIntMismatchCnts,'snVsrpVirRtrRxPriorityZeroFromMasterCnts':snVsrpVirRtrRxPriorityZeroFromMasterCnts,'snVsrpVirRtrRxHigherPriorityCnts':snVsrpVirRtrRxHigherPriorityCnts,'snVsrpVirRtrTransToMasterStateCnts':snVsrpVirRtrTransToMasterStateCnts,'snVsrpVirRtrTransToBackupStateCnts':snVsrpVirRtrTransToBackupStateCnts,'snVsrpVirRtrCurrDeadInt':snVsrpVirRtrCurrDeadInt,'snVsrpVirRtrCurHelloInt':snVsrpVirRtrCurHelloInt,'snVsrpVirRtrCurHoldDownInt':snVsrpVirRtrCurHoldDownInt,'snVsrpVirRtrCurInitTtl':snVsrpVirRtrCurInitTtl,'snVsrpVirRtrHelloMacAddress':snVsrpVirRtrHelloMacAddress,'snVsrpVirRtrMasterIpAddr':snVsrpVirRtrMasterIpAddr})