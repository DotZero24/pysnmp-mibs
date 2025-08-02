_AM='hm2MrpDomainDiagGroup'
_AL='hm2MrpNotificationsGroup'
_AK='hm2MrpDomainManagerGroup'
_AJ='hm2MrpDomainBasicGroup'
_AI='hm2MrpReconfig'
_AH='hm2RedundantCplState'
_AG='hm2RedundantCplCurrentRole'
_AF='hm2RingCplPartnerIpAddr'
_AE='hm2RingCplPartnerIpAddrType'
_AD='hm2RingCplPartnerInterconnIfOpState'
_AC='hm2RingCplInterconnIfOpState'
_AB='hm2SrmSubRingOperState'
_AA='hm2MrpMRMRoundTripDelayReset'
_A9='hm2MrpMRMRoundTripDelayMin'
_A8='hm2MrpMRMRoundTripDelayMax'
_A7='hm2MrpMRMLastRingOpenChange'
_A6='hm2MrpMRMRingOpenCount'
_A5='hm2MrpMRMNonBlockingMRCSupported'
_A4='hm2MrpMRMReactOnLinkChange'
_A3='hm2MrpMRMPriority'
_A2='hm2MrpRowStatus'
_A1='hm2MrpConfigOperState'
_A0='hm2MrpRedundancyOperState'
_z='hm2MrpMRCBlockedSupported'
_y='hm2MrpVlanID'
_x='hm2MrpRecoveryDelaySupported'
_w='hm2MrpRecoveryDelay'
_v='hm2MrpRoleOperState'
_u='hm2MrpRoleAdminState'
_t='hm2MrpRingport2OperState'
_s='hm2MrpRingport2IfIndex'
_r='hm2MrpRingport1OperState'
_q='hm2MrpRingport1IfIndex'
_p='hm2MrpDomainName'
_o='unknown'
_n='hm2RingCplInterconnIfIndex'
_m='inactive'
_l='not-available'
_k='redNotGuaranteed'
_j='redGuaranteed'
_i='singleManager'
_h='redundantManager'
_g='closed'
_f='client'
_e='notConnected'
_d='obsolete'
_c='accessible-for-notify'
_b='not-connected'
_a='Unsigned32'
_Z='SnmpAdminString'
_Y='InetAddressType'
_X='InetAddress'
_W='hm2MrpRingOperState'
_V='master'
_U='slave'
_T='single'
_S='hm2SrmRingID'
_R='enabled'
_Q='undefined'
_P='blocked'
_O='hm2MrpDomainID'
_N='active'
_M='OctetString'
_L='noError'
_K='manager'
_J='forwarding'
_I='HmEnabledStatus'
_H='InterfaceIndexOrZero'
_G='disabled'
_F='read-write'
_E='read-create'
_D='Integer32'
_C='HM2-L2REDUNDANCY-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HmEnabledStatus,hm2ConfigurationMibs=mibBuilder.importSymbols('HM2-TC-MIB',_I,'hm2ConfigurationMibs')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_H)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_X,_Y)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_Z)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_a,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
hm2L2RedundancyMib=ModuleIdentity((1,3,6,1,4,1,248,11,40))
if mibBuilder.loadTexts:hm2L2RedundancyMib.setRevisions(('2011-11-23 00:00',))
class Hm2CplPortOpState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_b,1),(_N,2),('standby',3),('not-applicable',4)))
class Hm2CplRingActiveProt(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('error',1),('rstp',2),('drstp',3),('mrp',4),('dlr',5),('hiper-ring',6)))
_Hm2L2RedundancyMibNotifications_ObjectIdentity=ObjectIdentity
hm2L2RedundancyMibNotifications=_Hm2L2RedundancyMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,40,0))
_Hm2L2RedundancyMibObjects_ObjectIdentity=ObjectIdentity
hm2L2RedundancyMibObjects=_Hm2L2RedundancyMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,40,1))
_Hm2MrpMibGroup_ObjectIdentity=ObjectIdentity
hm2MrpMibGroup=_Hm2MrpMibGroup_ObjectIdentity((1,3,6,1,4,1,248,11,40,1,1))
_Hm2MrpTable_Object=MibTable
hm2MrpTable=_Hm2MrpTable_Object((1,3,6,1,4,1,248,11,40,1,1,1))
if mibBuilder.loadTexts:hm2MrpTable.setStatus(_A)
_Hm2MrpEntry_Object=MibTableRow
hm2MrpEntry=_Hm2MrpEntry_Object((1,3,6,1,4,1,248,11,40,1,1,1,1))
hm2MrpEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:hm2MrpEntry.setStatus(_A)
class _Hm2MrpDomainID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Hm2MrpDomainID_Type.__name__=_M
_Hm2MrpDomainID_Object=MibTableColumn
hm2MrpDomainID=_Hm2MrpDomainID_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,1),_Hm2MrpDomainID_Type())
hm2MrpDomainID.setMaxAccess(_c)
if mibBuilder.loadTexts:hm2MrpDomainID.setStatus(_A)
class _Hm2MrpDomainName_Type(SnmpAdminString):defaultValue=OctetString('')
_Hm2MrpDomainName_Type.__name__=_Z
_Hm2MrpDomainName_Object=MibTableColumn
hm2MrpDomainName=_Hm2MrpDomainName_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,2),_Hm2MrpDomainName_Type())
hm2MrpDomainName.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2MrpDomainName.setStatus(_A)
_Hm2MrpRingport1GroupID_Type=Integer32
_Hm2MrpRingport1GroupID_Object=MibTableColumn
hm2MrpRingport1GroupID=_Hm2MrpRingport1GroupID_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,3),_Hm2MrpRingport1GroupID_Type())
hm2MrpRingport1GroupID.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2MrpRingport1GroupID.setStatus(_d)
_Hm2MrpRingport1IfIndex_Type=Integer32
_Hm2MrpRingport1IfIndex_Object=MibTableColumn
hm2MrpRingport1IfIndex=_Hm2MrpRingport1IfIndex_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,4),_Hm2MrpRingport1IfIndex_Type())
hm2MrpRingport1IfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2MrpRingport1IfIndex.setStatus(_A)
class _Hm2MrpRingport1OperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_P,2),(_J,3),(_e,4)))
_Hm2MrpRingport1OperState_Type.__name__=_D
_Hm2MrpRingport1OperState_Object=MibTableColumn
hm2MrpRingport1OperState=_Hm2MrpRingport1OperState_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,5),_Hm2MrpRingport1OperState_Type())
hm2MrpRingport1OperState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2MrpRingport1OperState.setStatus(_A)
_Hm2MrpRingport2GroupID_Type=Integer32
_Hm2MrpRingport2GroupID_Object=MibTableColumn
hm2MrpRingport2GroupID=_Hm2MrpRingport2GroupID_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,6),_Hm2MrpRingport2GroupID_Type())
hm2MrpRingport2GroupID.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2MrpRingport2GroupID.setStatus(_d)
_Hm2MrpRingport2IfIndex_Type=Integer32
_Hm2MrpRingport2IfIndex_Object=MibTableColumn
hm2MrpRingport2IfIndex=_Hm2MrpRingport2IfIndex_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,7),_Hm2MrpRingport2IfIndex_Type())
hm2MrpRingport2IfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2MrpRingport2IfIndex.setStatus(_A)
class _Hm2MrpRingport2OperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_P,2),(_J,3),(_e,4)))
_Hm2MrpRingport2OperState_Type.__name__=_D
_Hm2MrpRingport2OperState_Object=MibTableColumn
hm2MrpRingport2OperState=_Hm2MrpRingport2OperState_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,8),_Hm2MrpRingport2OperState_Type())
hm2MrpRingport2OperState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2MrpRingport2OperState.setStatus(_A)
class _Hm2MrpRoleAdminState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),(_K,2)))
_Hm2MrpRoleAdminState_Type.__name__=_D
_Hm2MrpRoleAdminState_Object=MibTableColumn
hm2MrpRoleAdminState=_Hm2MrpRoleAdminState_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,9),_Hm2MrpRoleAdminState_Type())
hm2MrpRoleAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2MrpRoleAdminState.setStatus(_A)
class _Hm2MrpRoleOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_f,1),(_K,2),(_Q,3)))
_Hm2MrpRoleOperState_Type.__name__=_D
_Hm2MrpRoleOperState_Object=MibTableColumn
hm2MrpRoleOperState=_Hm2MrpRoleOperState_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,10),_Hm2MrpRoleOperState_Type())
hm2MrpRoleOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2MrpRoleOperState.setStatus(_A)
class _Hm2MrpRecoveryDelay_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('delay500',1),('delay200',2),('delay30',3),('delay10',4)))
_Hm2MrpRecoveryDelay_Type.__name__=_D
_Hm2MrpRecoveryDelay_Object=MibTableColumn
hm2MrpRecoveryDelay=_Hm2MrpRecoveryDelay_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,11),_Hm2MrpRecoveryDelay_Type())
hm2MrpRecoveryDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2MrpRecoveryDelay.setStatus(_A)
class _Hm2MrpRecoveryDelaySupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('supportedAll',1),('supported200500',2)))
_Hm2MrpRecoveryDelaySupported_Type.__name__=_D
_Hm2MrpRecoveryDelaySupported_Object=MibTableColumn
hm2MrpRecoveryDelaySupported=_Hm2MrpRecoveryDelaySupported_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,12),_Hm2MrpRecoveryDelaySupported_Type())
hm2MrpRecoveryDelaySupported.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2MrpRecoveryDelaySupported.setStatus(_A)
class _Hm2MrpVlanID_Type(Integer32):defaultValue=0
_Hm2MrpVlanID_Type.__name__=_D
_Hm2MrpVlanID_Object=MibTableColumn
hm2MrpVlanID=_Hm2MrpVlanID_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,13),_Hm2MrpVlanID_Type())
hm2MrpVlanID.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2MrpVlanID.setStatus(_A)
class _Hm2MrpMRMPriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Hm2MrpMRMPriority_Type.__name__=_D
_Hm2MrpMRMPriority_Object=MibTableColumn
hm2MrpMRMPriority=_Hm2MrpMRMPriority_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,14),_Hm2MrpMRMPriority_Type())
hm2MrpMRMPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2MrpMRMPriority.setStatus(_A)
class _Hm2MrpMRMReactOnLinkChange_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_G,2)))
_Hm2MrpMRMReactOnLinkChange_Type.__name__=_D
_Hm2MrpMRMReactOnLinkChange_Object=MibTableColumn
hm2MrpMRMReactOnLinkChange=_Hm2MrpMRMReactOnLinkChange_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,15),_Hm2MrpMRMReactOnLinkChange_Type())
hm2MrpMRMReactOnLinkChange.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2MrpMRMReactOnLinkChange.setStatus(_A)
_Hm2MrpMRMRingOpenCount_Type=Counter32
_Hm2MrpMRMRingOpenCount_Object=MibTableColumn
hm2MrpMRMRingOpenCount=_Hm2MrpMRMRingOpenCount_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,16),_Hm2MrpMRMRingOpenCount_Type())
hm2MrpMRMRingOpenCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2MrpMRMRingOpenCount.setStatus(_A)
_Hm2MrpMRMLastRingOpenChange_Type=Unsigned32
_Hm2MrpMRMLastRingOpenChange_Object=MibTableColumn
hm2MrpMRMLastRingOpenChange=_Hm2MrpMRMLastRingOpenChange_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,17),_Hm2MrpMRMLastRingOpenChange_Type())
hm2MrpMRMLastRingOpenChange.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2MrpMRMLastRingOpenChange.setStatus(_A)
_Hm2MrpMRMRoundTripDelayMax_Type=Unsigned32
_Hm2MrpMRMRoundTripDelayMax_Object=MibTableColumn
hm2MrpMRMRoundTripDelayMax=_Hm2MrpMRMRoundTripDelayMax_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,18),_Hm2MrpMRMRoundTripDelayMax_Type())
hm2MrpMRMRoundTripDelayMax.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2MrpMRMRoundTripDelayMax.setStatus(_A)
_Hm2MrpMRMRoundTripDelayMin_Type=Unsigned32
_Hm2MrpMRMRoundTripDelayMin_Object=MibTableColumn
hm2MrpMRMRoundTripDelayMin=_Hm2MrpMRMRoundTripDelayMin_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,19),_Hm2MrpMRMRoundTripDelayMin_Type())
hm2MrpMRMRoundTripDelayMin.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2MrpMRMRoundTripDelayMin.setStatus(_A)
class _Hm2MrpMRMRoundTripDelayReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_Hm2MrpMRMRoundTripDelayReset_Type.__name__=_D
_Hm2MrpMRMRoundTripDelayReset_Object=MibTableColumn
hm2MrpMRMRoundTripDelayReset=_Hm2MrpMRMRoundTripDelayReset_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,20),_Hm2MrpMRMRoundTripDelayReset_Type())
hm2MrpMRMRoundTripDelayReset.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2MrpMRMRoundTripDelayReset.setStatus(_A)
class _Hm2MrpMRMNonBlockingMRCSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_G,2)))
_Hm2MrpMRMNonBlockingMRCSupported_Type.__name__=_D
_Hm2MrpMRMNonBlockingMRCSupported_Object=MibTableColumn
hm2MrpMRMNonBlockingMRCSupported=_Hm2MrpMRMNonBlockingMRCSupported_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,21),_Hm2MrpMRMNonBlockingMRCSupported_Type())
hm2MrpMRMNonBlockingMRCSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2MrpMRMNonBlockingMRCSupported.setStatus(_A)
class _Hm2MrpMRCBlockedSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_G,2)))
_Hm2MrpMRCBlockedSupported_Type.__name__=_D
_Hm2MrpMRCBlockedSupported_Object=MibTableColumn
hm2MrpMRCBlockedSupported=_Hm2MrpMRCBlockedSupported_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,22),_Hm2MrpMRCBlockedSupported_Type())
hm2MrpMRCBlockedSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2MrpMRCBlockedSupported.setStatus(_A)
class _Hm2MrpRingOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('open',1),(_g,2),(_Q,3)))
_Hm2MrpRingOperState_Type.__name__=_D
_Hm2MrpRingOperState_Object=MibTableColumn
hm2MrpRingOperState=_Hm2MrpRingOperState_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,23),_Hm2MrpRingOperState_Type())
hm2MrpRingOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2MrpRingOperState.setStatus(_A)
class _Hm2MrpRedundancyOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('available',1),('notAvailable',2)))
_Hm2MrpRedundancyOperState_Type.__name__=_D
_Hm2MrpRedundancyOperState_Object=MibTableColumn
hm2MrpRedundancyOperState=_Hm2MrpRedundancyOperState_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,24),_Hm2MrpRedundancyOperState_Type())
hm2MrpRedundancyOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2MrpRedundancyOperState.setStatus(_A)
class _Hm2MrpConfigOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),('ringportLinkError',2),('multipleMRM',3),('singleSideReceive',4)))
_Hm2MrpConfigOperState_Type.__name__=_D
_Hm2MrpConfigOperState_Object=MibTableColumn
hm2MrpConfigOperState=_Hm2MrpConfigOperState_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,25),_Hm2MrpConfigOperState_Type())
hm2MrpConfigOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2MrpConfigOperState.setStatus(_A)
_Hm2MrpRowStatus_Type=RowStatus
_Hm2MrpRowStatus_Object=MibTableColumn
hm2MrpRowStatus=_Hm2MrpRowStatus_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,26),_Hm2MrpRowStatus_Type())
hm2MrpRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2MrpRowStatus.setStatus(_A)
class _Hm2MrpRingport2FixedBackup_Type(HmEnabledStatus):defaultValue=2
_Hm2MrpRingport2FixedBackup_Type.__name__=_I
_Hm2MrpRingport2FixedBackup_Object=MibTableColumn
hm2MrpRingport2FixedBackup=_Hm2MrpRingport2FixedBackup_Object((1,3,6,1,4,1,248,11,40,1,1,1,1,27),_Hm2MrpRingport2FixedBackup_Type())
hm2MrpRingport2FixedBackup.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2MrpRingport2FixedBackup.setStatus(_A)
_Hm2MrpConformance_ObjectIdentity=ObjectIdentity
hm2MrpConformance=_Hm2MrpConformance_ObjectIdentity((1,3,6,1,4,1,248,11,40,1,1,2))
_Hm2MrpCompliances_ObjectIdentity=ObjectIdentity
hm2MrpCompliances=_Hm2MrpCompliances_ObjectIdentity((1,3,6,1,4,1,248,11,40,1,1,2,1))
_Hm2MrpGroups_ObjectIdentity=ObjectIdentity
hm2MrpGroups=_Hm2MrpGroups_ObjectIdentity((1,3,6,1,4,1,248,11,40,1,1,2,2))
class _Hm2MrpFastMrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('supported',1),('notSupported',2)))
_Hm2MrpFastMrp_Type.__name__=_D
_Hm2MrpFastMrp_Object=MibScalar
hm2MrpFastMrp=_Hm2MrpFastMrp_Object((1,3,6,1,4,1,248,11,40,1,1,3),_Hm2MrpFastMrp_Type())
hm2MrpFastMrp.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2MrpFastMrp.setStatus(_A)
_Hm2SrmMibGroup_ObjectIdentity=ObjectIdentity
hm2SrmMibGroup=_Hm2SrmMibGroup_ObjectIdentity((1,3,6,1,4,1,248,11,40,1,4))
class _Hm2SrmGlobalAdminState_Type(HmEnabledStatus):defaultValue=2
_Hm2SrmGlobalAdminState_Type.__name__=_I
_Hm2SrmGlobalAdminState_Object=MibScalar
hm2SrmGlobalAdminState=_Hm2SrmGlobalAdminState_Object((1,3,6,1,4,1,248,11,40,1,4,1),_Hm2SrmGlobalAdminState_Type())
hm2SrmGlobalAdminState.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2SrmGlobalAdminState.setStatus(_A)
_Hm2SrmMaxInstances_Type=Integer32
_Hm2SrmMaxInstances_Object=MibScalar
hm2SrmMaxInstances=_Hm2SrmMaxInstances_Object((1,3,6,1,4,1,248,11,40,1,4,2),_Hm2SrmMaxInstances_Type())
hm2SrmMaxInstances.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SrmMaxInstances.setStatus(_A)
_Hm2SrmTable_Object=MibTable
hm2SrmTable=_Hm2SrmTable_Object((1,3,6,1,4,1,248,11,40,1,4,3))
if mibBuilder.loadTexts:hm2SrmTable.setStatus(_A)
_Hm2SrmEntry_Object=MibTableRow
hm2SrmEntry=_Hm2SrmEntry_Object((1,3,6,1,4,1,248,11,40,1,4,3,1))
hm2SrmEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:hm2SrmEntry.setStatus(_A)
_Hm2SrmRingID_Type=Integer32
_Hm2SrmRingID_Object=MibTableColumn
hm2SrmRingID=_Hm2SrmRingID_Object((1,3,6,1,4,1,248,11,40,1,4,3,1,1),_Hm2SrmRingID_Type())
hm2SrmRingID.setMaxAccess(_c)
if mibBuilder.loadTexts:hm2SrmRingID.setStatus(_A)
class _Hm2SrmAdminState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_h,2),(_i,3)))
_Hm2SrmAdminState_Type.__name__=_D
_Hm2SrmAdminState_Object=MibTableColumn
hm2SrmAdminState=_Hm2SrmAdminState_Object((1,3,6,1,4,1,248,11,40,1,4,3,1,2),_Hm2SrmAdminState_Type())
hm2SrmAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2SrmAdminState.setStatus(_A)
class _Hm2SrmOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_h,2),(_i,3),(_G,4)))
_Hm2SrmOperState_Type.__name__=_D
_Hm2SrmOperState_Object=MibTableColumn
hm2SrmOperState=_Hm2SrmOperState_Object((1,3,6,1,4,1,248,11,40,1,4,3,1,3),_Hm2SrmOperState_Type())
hm2SrmOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SrmOperState.setStatus(_A)
class _Hm2SrmVlanID_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4042))
_Hm2SrmVlanID_Type.__name__=_D
_Hm2SrmVlanID_Object=MibTableColumn
hm2SrmVlanID=_Hm2SrmVlanID_Object((1,3,6,1,4,1,248,11,40,1,4,3,1,4),_Hm2SrmVlanID_Type())
hm2SrmVlanID.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2SrmVlanID.setStatus(_A)
class _Hm2SrmMRPDomainID_Type(OctetString):defaultHexValue='FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Hm2SrmMRPDomainID_Type.__name__=_M
_Hm2SrmMRPDomainID_Object=MibTableColumn
hm2SrmMRPDomainID=_Hm2SrmMRPDomainID_Object((1,3,6,1,4,1,248,11,40,1,4,3,1,5),_Hm2SrmMRPDomainID_Type())
hm2SrmMRPDomainID.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2SrmMRPDomainID.setStatus(_A)
_Hm2SrmPartnerMAC_Type=MacAddress
_Hm2SrmPartnerMAC_Object=MibTableColumn
hm2SrmPartnerMAC=_Hm2SrmPartnerMAC_Object((1,3,6,1,4,1,248,11,40,1,4,3,1,6),_Hm2SrmPartnerMAC_Type())
hm2SrmPartnerMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SrmPartnerMAC.setStatus(_A)
class _Hm2SrmSubRingProtocol_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(4));namedValues=NamedValues(('iec-62439-mrp',4))
_Hm2SrmSubRingProtocol_Type.__name__=_D
_Hm2SrmSubRingProtocol_Object=MibTableColumn
hm2SrmSubRingProtocol=_Hm2SrmSubRingProtocol_Object((1,3,6,1,4,1,248,11,40,1,4,3,1,7),_Hm2SrmSubRingProtocol_Type())
hm2SrmSubRingProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2SrmSubRingProtocol.setStatus(_A)
_Hm2SrmSubRingName_Type=SnmpAdminString
_Hm2SrmSubRingName_Object=MibTableColumn
hm2SrmSubRingName=_Hm2SrmSubRingName_Object((1,3,6,1,4,1,248,11,40,1,4,3,1,8),_Hm2SrmSubRingName_Type())
hm2SrmSubRingName.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2SrmSubRingName.setStatus(_A)
_Hm2SrmSubRingPortIfIndex_Type=Integer32
_Hm2SrmSubRingPortIfIndex_Object=MibTableColumn
hm2SrmSubRingPortIfIndex=_Hm2SrmSubRingPortIfIndex_Object((1,3,6,1,4,1,248,11,40,1,4,3,1,9),_Hm2SrmSubRingPortIfIndex_Type())
hm2SrmSubRingPortIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2SrmSubRingPortIfIndex.setStatus(_A)
class _Hm2SrmSubRingPortOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_P,2),(_J,3),(_b,4)))
_Hm2SrmSubRingPortOperState_Type.__name__=_D
_Hm2SrmSubRingPortOperState_Object=MibTableColumn
hm2SrmSubRingPortOperState=_Hm2SrmSubRingPortOperState_Object((1,3,6,1,4,1,248,11,40,1,4,3,1,10),_Hm2SrmSubRingPortOperState_Type())
hm2SrmSubRingPortOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SrmSubRingPortOperState.setStatus(_A)
class _Hm2SrmSubRingOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),('open',2),(_g,3)))
_Hm2SrmSubRingOperState_Type.__name__=_D
_Hm2SrmSubRingOperState_Object=MibTableColumn
hm2SrmSubRingOperState=_Hm2SrmSubRingOperState_Object((1,3,6,1,4,1,248,11,40,1,4,3,1,11),_Hm2SrmSubRingOperState_Type())
hm2SrmSubRingOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SrmSubRingOperState.setStatus(_A)
class _Hm2SrmRedundancyOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_j,1),(_k,2)))
_Hm2SrmRedundancyOperState_Type.__name__=_D
_Hm2SrmRedundancyOperState_Object=MibTableColumn
hm2SrmRedundancyOperState=_Hm2SrmRedundancyOperState_Object((1,3,6,1,4,1,248,11,40,1,4,3,1,12),_Hm2SrmRedundancyOperState_Type())
hm2SrmRedundancyOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SrmRedundancyOperState.setStatus(_A)
class _Hm2SrmConfigOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_L,1),('ringPortLinkError',2),('multipleSRM',3),('noPartnerManager',4),('concurrentVLAN',5),('concurrentPort',6),('concurrentRedundancy',7),('trunkMember',8),('sharedVLAN',9)))
_Hm2SrmConfigOperState_Type.__name__=_D
_Hm2SrmConfigOperState_Object=MibTableColumn
hm2SrmConfigOperState=_Hm2SrmConfigOperState_Object((1,3,6,1,4,1,248,11,40,1,4,3,1,13),_Hm2SrmConfigOperState_Type())
hm2SrmConfigOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2SrmConfigOperState.setStatus(_A)
_Hm2SrmRowStatus_Type=RowStatus
_Hm2SrmRowStatus_Object=MibTableColumn
hm2SrmRowStatus=_Hm2SrmRowStatus_Object((1,3,6,1,4,1,248,11,40,1,4,3,1,20),_Hm2SrmRowStatus_Type())
hm2SrmRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2SrmRowStatus.setStatus(_A)
_Hm2RingRedMibGroup_ObjectIdentity=ObjectIdentity
hm2RingRedMibGroup=_Hm2RingRedMibGroup_ObjectIdentity((1,3,6,1,4,1,248,11,40,1,7))
class _Hm2RingRedAdminState_Type(HmEnabledStatus):defaultValue=2
_Hm2RingRedAdminState_Type.__name__=_I
_Hm2RingRedAdminState_Object=MibScalar
hm2RingRedAdminState=_Hm2RingRedAdminState_Object((1,3,6,1,4,1,248,11,40,1,7,1),_Hm2RingRedAdminState_Type())
hm2RingRedAdminState.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2RingRedAdminState.setStatus(_A)
class _Hm2RingRedMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('ring-switch',1))
_Hm2RingRedMode_Type.__name__=_D
_Hm2RingRedMode_Object=MibScalar
hm2RingRedMode=_Hm2RingRedMode_Object((1,3,6,1,4,1,248,11,40,1,7,2),_Hm2RingRedMode_Type())
hm2RingRedMode.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2RingRedMode.setStatus(_A)
class _Hm2RingRedPrimaryIntf_Type(InterfaceIndexOrZero):defaultValue=0
_Hm2RingRedPrimaryIntf_Type.__name__=_H
_Hm2RingRedPrimaryIntf_Object=MibScalar
hm2RingRedPrimaryIntf=_Hm2RingRedPrimaryIntf_Object((1,3,6,1,4,1,248,11,40,1,7,3),_Hm2RingRedPrimaryIntf_Type())
hm2RingRedPrimaryIntf.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2RingRedPrimaryIntf.setStatus(_A)
class _Hm2RingRedPrimaryIntfState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_l,1),(_N,2),(_m,3)))
_Hm2RingRedPrimaryIntfState_Type.__name__=_D
_Hm2RingRedPrimaryIntfState_Object=MibScalar
hm2RingRedPrimaryIntfState=_Hm2RingRedPrimaryIntfState_Object((1,3,6,1,4,1,248,11,40,1,7,4),_Hm2RingRedPrimaryIntfState_Type())
hm2RingRedPrimaryIntfState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2RingRedPrimaryIntfState.setStatus(_A)
class _Hm2RingRedSecondaryIntf_Type(InterfaceIndexOrZero):defaultValue=0
_Hm2RingRedSecondaryIntf_Type.__name__=_H
_Hm2RingRedSecondaryIntf_Object=MibScalar
hm2RingRedSecondaryIntf=_Hm2RingRedSecondaryIntf_Object((1,3,6,1,4,1,248,11,40,1,7,5),_Hm2RingRedSecondaryIntf_Type())
hm2RingRedSecondaryIntf.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2RingRedSecondaryIntf.setStatus(_A)
class _Hm2RingRedSecondaryIntfState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_l,1),(_N,2),(_m,3)))
_Hm2RingRedSecondaryIntfState_Type.__name__=_D
_Hm2RingRedSecondaryIntfState_Object=MibScalar
hm2RingRedSecondaryIntfState=_Hm2RingRedSecondaryIntfState_Object((1,3,6,1,4,1,248,11,40,1,7,6),_Hm2RingRedSecondaryIntfState_Type())
hm2RingRedSecondaryIntfState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2RingRedSecondaryIntfState.setStatus(_A)
_Hm2RingCouplingMibGroup_ObjectIdentity=ObjectIdentity
hm2RingCouplingMibGroup=_Hm2RingCouplingMibGroup_ObjectIdentity((1,3,6,1,4,1,248,11,40,1,8))
_Hm2RingCouplingTable_Object=MibTable
hm2RingCouplingTable=_Hm2RingCouplingTable_Object((1,3,6,1,4,1,248,11,40,1,8,1))
if mibBuilder.loadTexts:hm2RingCouplingTable.setStatus(_A)
_Hm2RingCouplingEntry_Object=MibTableRow
hm2RingCouplingEntry=_Hm2RingCouplingEntry_Object((1,3,6,1,4,1,248,11,40,1,8,1,1))
hm2RingCouplingEntry.setIndexNames((0,_C,_n))
if mibBuilder.loadTexts:hm2RingCouplingEntry.setStatus(_A)
_Hm2RingCplInterconnIfIndex_Type=InterfaceIndexOrZero
_Hm2RingCplInterconnIfIndex_Object=MibTableColumn
hm2RingCplInterconnIfIndex=_Hm2RingCplInterconnIfIndex_Object((1,3,6,1,4,1,248,11,40,1,8,1,1,1),_Hm2RingCplInterconnIfIndex_Type())
hm2RingCplInterconnIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2RingCplInterconnIfIndex.setStatus(_A)
_Hm2RingCplInterconnIfOpState_Type=Hm2CplPortOpState
_Hm2RingCplInterconnIfOpState_Object=MibTableColumn
hm2RingCplInterconnIfOpState=_Hm2RingCplInterconnIfOpState_Object((1,3,6,1,4,1,248,11,40,1,8,1,1,2),_Hm2RingCplInterconnIfOpState_Type())
hm2RingCplInterconnIfOpState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2RingCplInterconnIfOpState.setStatus(_A)
_Hm2RingCplControlIfIndex_Type=InterfaceIndexOrZero
_Hm2RingCplControlIfIndex_Object=MibTableColumn
hm2RingCplControlIfIndex=_Hm2RingCplControlIfIndex_Object((1,3,6,1,4,1,248,11,40,1,8,1,1,3),_Hm2RingCplControlIfIndex_Type())
hm2RingCplControlIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2RingCplControlIfIndex.setStatus(_A)
_Hm2RingCplControlIfOpState_Type=Hm2CplPortOpState
_Hm2RingCplControlIfOpState_Object=MibTableColumn
hm2RingCplControlIfOpState=_Hm2RingCplControlIfOpState_Object((1,3,6,1,4,1,248,11,40,1,8,1,1,4),_Hm2RingCplControlIfOpState_Type())
hm2RingCplControlIfOpState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2RingCplControlIfOpState.setStatus(_A)
_Hm2RingCplPartnerInterconnIfIndex_Type=InterfaceIndexOrZero
_Hm2RingCplPartnerInterconnIfIndex_Object=MibTableColumn
hm2RingCplPartnerInterconnIfIndex=_Hm2RingCplPartnerInterconnIfIndex_Object((1,3,6,1,4,1,248,11,40,1,8,1,1,5),_Hm2RingCplPartnerInterconnIfIndex_Type())
hm2RingCplPartnerInterconnIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2RingCplPartnerInterconnIfIndex.setStatus(_A)
_Hm2RingCplPartnerInterconnIfOpState_Type=Hm2CplPortOpState
_Hm2RingCplPartnerInterconnIfOpState_Object=MibTableColumn
hm2RingCplPartnerInterconnIfOpState=_Hm2RingCplPartnerInterconnIfOpState_Object((1,3,6,1,4,1,248,11,40,1,8,1,1,6),_Hm2RingCplPartnerInterconnIfOpState_Type())
hm2RingCplPartnerInterconnIfOpState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2RingCplPartnerInterconnIfOpState.setStatus(_A)
class _Hm2RingCplPartnerIpAddrType_Type(InetAddressType):defaultValue=1
_Hm2RingCplPartnerIpAddrType_Type.__name__=_Y
_Hm2RingCplPartnerIpAddrType_Object=MibTableColumn
hm2RingCplPartnerIpAddrType=_Hm2RingCplPartnerIpAddrType_Object((1,3,6,1,4,1,248,11,40,1,8,1,1,7),_Hm2RingCplPartnerIpAddrType_Type())
hm2RingCplPartnerIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2RingCplPartnerIpAddrType.setStatus(_A)
class _Hm2RingCplPartnerIpAddr_Type(InetAddress):defaultHexValue='00000000'
_Hm2RingCplPartnerIpAddr_Type.__name__=_X
_Hm2RingCplPartnerIpAddr_Object=MibTableColumn
hm2RingCplPartnerIpAddr=_Hm2RingCplPartnerIpAddr_Object((1,3,6,1,4,1,248,11,40,1,8,1,1,8),_Hm2RingCplPartnerIpAddr_Type())
hm2RingCplPartnerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2RingCplPartnerIpAddr.setStatus(_A)
class _Hm2RingCplCouplingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_T,1),('dual-master-inband',2),('dual-master-outband',3),('dual-slave-inband',4),('dual-slave-outband',5),(_o,6)))
_Hm2RingCplCouplingMode_Type.__name__=_D
_Hm2RingCplCouplingMode_Object=MibTableColumn
hm2RingCplCouplingMode=_Hm2RingCplCouplingMode_Object((1,3,6,1,4,1,248,11,40,1,8,1,1,9),_Hm2RingCplCouplingMode_Type())
hm2RingCplCouplingMode.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2RingCplCouplingMode.setStatus(_A)
class _Hm2RingCplControlModeOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('outband',1),('inband',2),(_o,3),('local',4)))
_Hm2RingCplControlModeOperState_Type.__name__=_D
_Hm2RingCplControlModeOperState_Object=MibTableColumn
hm2RingCplControlModeOperState=_Hm2RingCplControlModeOperState_Object((1,3,6,1,4,1,248,11,40,1,8,1,1,10),_Hm2RingCplControlModeOperState_Type())
hm2RingCplControlModeOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2RingCplControlModeOperState.setStatus(_A)
class _Hm2RingCplModeOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('slaveOff',1),('slaveOn',2)))
_Hm2RingCplModeOperState_Type.__name__=_D
_Hm2RingCplModeOperState_Object=MibTableColumn
hm2RingCplModeOperState=_Hm2RingCplModeOperState_Object((1,3,6,1,4,1,248,11,40,1,8,1,1,11),_Hm2RingCplModeOperState_Type())
hm2RingCplModeOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2RingCplModeOperState.setStatus(_A)
class _Hm2RingCplOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('underCreation',1),(_U,2),(_V,3),('local',4)))
_Hm2RingCplOperState_Type.__name__=_D
_Hm2RingCplOperState_Object=MibTableColumn
hm2RingCplOperState=_Hm2RingCplOperState_Object((1,3,6,1,4,1,248,11,40,1,8,1,1,12),_Hm2RingCplOperState_Type())
hm2RingCplOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2RingCplOperState.setStatus(_A)
class _Hm2RingCplConfigOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_L,1),('slaveCouplingLinkError',2),('slaveControlLinkError',3),('masterControlLinkError',4),('twoSlaves',5),('localPartnerLinkError',6),('localInvalidCouplingPort',7),('couplingPortNotAvailable',8),('controlPortNotAvailable',9),('partnerPortNotAvailable',10)))
_Hm2RingCplConfigOperState_Type.__name__=_D
_Hm2RingCplConfigOperState_Object=MibTableColumn
hm2RingCplConfigOperState=_Hm2RingCplConfigOperState_Object((1,3,6,1,4,1,248,11,40,1,8,1,1,13),_Hm2RingCplConfigOperState_Type())
hm2RingCplConfigOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2RingCplConfigOperState.setStatus(_A)
class _Hm2RingCplCouplingLinks_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('basicRedundancy',1),('extendedRedundancy',2)))
_Hm2RingCplCouplingLinks_Type.__name__=_D
_Hm2RingCplCouplingLinks_Object=MibTableColumn
hm2RingCplCouplingLinks=_Hm2RingCplCouplingLinks_Object((1,3,6,1,4,1,248,11,40,1,8,1,1,14),_Hm2RingCplCouplingLinks_Type())
hm2RingCplCouplingLinks.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2RingCplCouplingLinks.setStatus(_A)
class _Hm2RingCplExtendedDiag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('basicRedundancyInactive',2)))
_Hm2RingCplExtendedDiag_Type.__name__=_D
_Hm2RingCplExtendedDiag_Object=MibTableColumn
hm2RingCplExtendedDiag=_Hm2RingCplExtendedDiag_Object((1,3,6,1,4,1,248,11,40,1,8,1,1,15),_Hm2RingCplExtendedDiag_Type())
hm2RingCplExtendedDiag.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2RingCplExtendedDiag.setStatus(_A)
class _Hm2RingCplNetCoupling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ringCoupling',1),('netCoupling',2)))
_Hm2RingCplNetCoupling_Type.__name__=_D
_Hm2RingCplNetCoupling_Object=MibTableColumn
hm2RingCplNetCoupling=_Hm2RingCplNetCoupling_Object((1,3,6,1,4,1,248,11,40,1,8,1,1,16),_Hm2RingCplNetCoupling_Type())
hm2RingCplNetCoupling.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2RingCplNetCoupling.setStatus(_A)
class _Hm2RingCplRedOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_j,1),(_k,2)))
_Hm2RingCplRedOperState_Type.__name__=_D
_Hm2RingCplRedOperState_Object=MibTableColumn
hm2RingCplRedOperState=_Hm2RingCplRedOperState_Object((1,3,6,1,4,1,248,11,40,1,8,1,1,17),_Hm2RingCplRedOperState_Type())
hm2RingCplRedOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2RingCplRedOperState.setStatus(_A)
_Hm2RingCplRowStatus_Type=RowStatus
_Hm2RingCplRowStatus_Object=MibTableColumn
hm2RingCplRowStatus=_Hm2RingCplRowStatus_Object((1,3,6,1,4,1,248,11,40,1,8,1,1,22),_Hm2RingCplRowStatus_Type())
hm2RingCplRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hm2RingCplRowStatus.setStatus(_A)
_Hm2RedundantCplConfigMibGroup_ObjectIdentity=ObjectIdentity
hm2RedundantCplConfigMibGroup=_Hm2RedundantCplConfigMibGroup_ObjectIdentity((1,3,6,1,4,1,248,11,40,1,9))
class _Hm2RedundantCplAdminState_Type(HmEnabledStatus):defaultValue=2
_Hm2RedundantCplAdminState_Type.__name__=_I
_Hm2RedundantCplAdminState_Object=MibScalar
hm2RedundantCplAdminState=_Hm2RedundantCplAdminState_Object((1,3,6,1,4,1,248,11,40,1,9,1),_Hm2RedundantCplAdminState_Type())
hm2RedundantCplAdminState.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2RedundantCplAdminState.setStatus(_A)
class _Hm2RedundantCplInPrimaryPort_Type(InterfaceIndexOrZero):defaultValue=0
_Hm2RedundantCplInPrimaryPort_Type.__name__=_H
_Hm2RedundantCplInPrimaryPort_Object=MibScalar
hm2RedundantCplInPrimaryPort=_Hm2RedundantCplInPrimaryPort_Object((1,3,6,1,4,1,248,11,40,1,9,2),_Hm2RedundantCplInPrimaryPort_Type())
hm2RedundantCplInPrimaryPort.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2RedundantCplInPrimaryPort.setStatus(_A)
class _Hm2RedundantCplOutPrimaryPort_Type(InterfaceIndexOrZero):defaultValue=0
_Hm2RedundantCplOutPrimaryPort_Type.__name__=_H
_Hm2RedundantCplOutPrimaryPort_Object=MibScalar
hm2RedundantCplOutPrimaryPort=_Hm2RedundantCplOutPrimaryPort_Object((1,3,6,1,4,1,248,11,40,1,9,3),_Hm2RedundantCplOutPrimaryPort_Type())
hm2RedundantCplOutPrimaryPort.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2RedundantCplOutPrimaryPort.setStatus(_A)
class _Hm2RedundantCplInSecondaryPort_Type(InterfaceIndexOrZero):defaultValue=0
_Hm2RedundantCplInSecondaryPort_Type.__name__=_H
_Hm2RedundantCplInSecondaryPort_Object=MibScalar
hm2RedundantCplInSecondaryPort=_Hm2RedundantCplInSecondaryPort_Object((1,3,6,1,4,1,248,11,40,1,9,4),_Hm2RedundantCplInSecondaryPort_Type())
hm2RedundantCplInSecondaryPort.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2RedundantCplInSecondaryPort.setStatus(_A)
class _Hm2RedundantCplOutSecondaryPort_Type(InterfaceIndexOrZero):defaultValue=0
_Hm2RedundantCplOutSecondaryPort_Type.__name__=_H
_Hm2RedundantCplOutSecondaryPort_Object=MibScalar
hm2RedundantCplOutSecondaryPort=_Hm2RedundantCplOutSecondaryPort_Object((1,3,6,1,4,1,248,11,40,1,9,5),_Hm2RedundantCplOutSecondaryPort_Type())
hm2RedundantCplOutSecondaryPort.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2RedundantCplOutSecondaryPort.setStatus(_A)
class _Hm2RedundantCplRole_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_V,1),(_U,2),(_T,3),('auto',4)))
_Hm2RedundantCplRole_Type.__name__=_D
_Hm2RedundantCplRole_Object=MibScalar
hm2RedundantCplRole=_Hm2RedundantCplRole_Object((1,3,6,1,4,1,248,11,40,1,9,6),_Hm2RedundantCplRole_Type())
hm2RedundantCplRole.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2RedundantCplRole.setStatus(_A)
class _Hm2RedundantCplCurrentRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_V,1),(_U,2),('listening',3),('error',4),(_G,5),(_T,6)))
_Hm2RedundantCplCurrentRole_Type.__name__=_D
_Hm2RedundantCplCurrentRole_Object=MibScalar
hm2RedundantCplCurrentRole=_Hm2RedundantCplCurrentRole_Object((1,3,6,1,4,1,248,11,40,1,9,7),_Hm2RedundantCplCurrentRole_Type())
hm2RedundantCplCurrentRole.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2RedundantCplCurrentRole.setStatus(_A)
class _Hm2RedundantCplTimeout_Type(Unsigned32):defaultValue=250;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,60000))
_Hm2RedundantCplTimeout_Type.__name__=_a
_Hm2RedundantCplTimeout_Object=MibScalar
hm2RedundantCplTimeout=_Hm2RedundantCplTimeout_Object((1,3,6,1,4,1,248,11,40,1,9,8),_Hm2RedundantCplTimeout_Type())
hm2RedundantCplTimeout.setMaxAccess(_F)
if mibBuilder.loadTexts:hm2RedundantCplTimeout.setStatus(_A)
_Hm2RedundantCplPartner_Type=MacAddress
_Hm2RedundantCplPartner_Object=MibScalar
hm2RedundantCplPartner=_Hm2RedundantCplPartner_Object((1,3,6,1,4,1,248,11,40,1,9,9),_Hm2RedundantCplPartner_Type())
hm2RedundantCplPartner.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2RedundantCplPartner.setStatus(_A)
_Hm2RedundantCplPartnerPrimaryPort_Type=InterfaceIndexOrZero
_Hm2RedundantCplPartnerPrimaryPort_Object=MibScalar
hm2RedundantCplPartnerPrimaryPort=_Hm2RedundantCplPartnerPrimaryPort_Object((1,3,6,1,4,1,248,11,40,1,9,10),_Hm2RedundantCplPartnerPrimaryPort_Type())
hm2RedundantCplPartnerPrimaryPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2RedundantCplPartnerPrimaryPort.setStatus(_A)
_Hm2RedundantCplPartnerSecondaryPort_Type=InterfaceIndexOrZero
_Hm2RedundantCplPartnerSecondaryPort_Object=MibScalar
hm2RedundantCplPartnerSecondaryPort=_Hm2RedundantCplPartnerSecondaryPort_Object((1,3,6,1,4,1,248,11,40,1,9,11),_Hm2RedundantCplPartnerSecondaryPort_Type())
hm2RedundantCplPartnerSecondaryPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2RedundantCplPartnerSecondaryPort.setStatus(_A)
class _Hm2RedundantCplState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),('blocking',2)))
_Hm2RedundantCplState_Type.__name__=_D
_Hm2RedundantCplState_Object=MibScalar
hm2RedundantCplState=_Hm2RedundantCplState_Object((1,3,6,1,4,1,248,11,40,1,9,12),_Hm2RedundantCplState_Type())
hm2RedundantCplState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2RedundantCplState.setStatus(_A)
class _Hm2RedundantCplRedundancyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('redAvailable',1),('redNotAvailable',2)))
_Hm2RedundantCplRedundancyState_Type.__name__=_D
_Hm2RedundantCplRedundancyState_Object=MibScalar
hm2RedundantCplRedundancyState=_Hm2RedundantCplRedundancyState_Object((1,3,6,1,4,1,248,11,40,1,9,13),_Hm2RedundantCplRedundancyState_Type())
hm2RedundantCplRedundancyState.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2RedundantCplRedundancyState.setStatus(_A)
_Hm2RedundantCplPartnerIPAddrType_Type=InetAddressType
_Hm2RedundantCplPartnerIPAddrType_Object=MibScalar
hm2RedundantCplPartnerIPAddrType=_Hm2RedundantCplPartnerIPAddrType_Object((1,3,6,1,4,1,248,11,40,1,9,14),_Hm2RedundantCplPartnerIPAddrType_Type())
hm2RedundantCplPartnerIPAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2RedundantCplPartnerIPAddrType.setStatus(_A)
_Hm2RedundantCplPartnerIPAddr_Type=InetAddress
_Hm2RedundantCplPartnerIPAddr_Object=MibScalar
hm2RedundantCplPartnerIPAddr=_Hm2RedundantCplPartnerIPAddr_Object((1,3,6,1,4,1,248,11,40,1,9,15),_Hm2RedundantCplPartnerIPAddr_Type())
hm2RedundantCplPartnerIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2RedundantCplPartnerIPAddr.setStatus(_A)
_Hm2RedundantCplActiveProtPrimaryRing_Type=Hm2CplRingActiveProt
_Hm2RedundantCplActiveProtPrimaryRing_Object=MibScalar
hm2RedundantCplActiveProtPrimaryRing=_Hm2RedundantCplActiveProtPrimaryRing_Object((1,3,6,1,4,1,248,11,40,1,9,16),_Hm2RedundantCplActiveProtPrimaryRing_Type())
hm2RedundantCplActiveProtPrimaryRing.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2RedundantCplActiveProtPrimaryRing.setStatus(_A)
_Hm2RedundantCplActiveProtSecondaryRing_Type=Hm2CplRingActiveProt
_Hm2RedundantCplActiveProtSecondaryRing_Object=MibScalar
hm2RedundantCplActiveProtSecondaryRing=_Hm2RedundantCplActiveProtSecondaryRing_Object((1,3,6,1,4,1,248,11,40,1,9,17),_Hm2RedundantCplActiveProtSecondaryRing_Type())
hm2RedundantCplActiveProtSecondaryRing.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2RedundantCplActiveProtSecondaryRing.setStatus(_A)
_Hm2L2RedundancyMibSNMPExtensionGroup_ObjectIdentity=ObjectIdentity
hm2L2RedundancyMibSNMPExtensionGroup=_Hm2L2RedundancyMibSNMPExtensionGroup_ObjectIdentity((1,3,6,1,4,1,248,11,40,3))
_Hm2RingCouplingMibSESGroup_ObjectIdentity=ObjectIdentity
hm2RingCouplingMibSESGroup=_Hm2RingCouplingMibSESGroup_ObjectIdentity((1,3,6,1,4,1,248,11,40,3,8))
_Hm2RingCouplingInvalidPortConfiguration_ObjectIdentity=ObjectIdentity
hm2RingCouplingInvalidPortConfiguration=_Hm2RingCouplingInvalidPortConfiguration_ObjectIdentity((1,3,6,1,4,1,248,11,40,3,8,1))
if mibBuilder.loadTexts:hm2RingCouplingInvalidPortConfiguration.setStatus(_A)
_Hm2RedundantCplSESGroup_ObjectIdentity=ObjectIdentity
hm2RedundantCplSESGroup=_Hm2RedundantCplSESGroup_ObjectIdentity((1,3,6,1,4,1,248,11,40,3,9))
_Hm2RedundantCplPortsMissing_ObjectIdentity=ObjectIdentity
hm2RedundantCplPortsMissing=_Hm2RedundantCplPortsMissing_ObjectIdentity((1,3,6,1,4,1,248,11,40,3,9,1))
if mibBuilder.loadTexts:hm2RedundantCplPortsMissing.setStatus(_A)
_Hm2RedundantCplSecondaryGroupUnitMismatched_ObjectIdentity=ObjectIdentity
hm2RedundantCplSecondaryGroupUnitMismatched=_Hm2RedundantCplSecondaryGroupUnitMismatched_ObjectIdentity((1,3,6,1,4,1,248,11,40,3,9,2))
if mibBuilder.loadTexts:hm2RedundantCplSecondaryGroupUnitMismatched.setStatus(_A)
hm2MrpDomainBasicGroup=ObjectGroup((1,3,6,1,4,1,248,11,40,1,1,2,2,1))
hm2MrpDomainBasicGroup.setObjects(*((_C,_O),(_C,_p),(_C,_q),(_C,_r),(_C,_s),(_C,_t),(_C,_u),(_C,_v),(_C,_w),(_C,_x),(_C,_y),(_C,_z),(_C,_A0),(_C,_A1),(_C,_A2)))
if mibBuilder.loadTexts:hm2MrpDomainBasicGroup.setStatus(_A)
hm2MrpDomainManagerGroup=ObjectGroup((1,3,6,1,4,1,248,11,40,1,1,2,2,2))
hm2MrpDomainManagerGroup.setObjects(*((_C,_A3),(_C,_A4),(_C,_A5),(_C,_W)))
if mibBuilder.loadTexts:hm2MrpDomainManagerGroup.setStatus(_A)
hm2MrpDomainDiagGroup=ObjectGroup((1,3,6,1,4,1,248,11,40,1,1,2,2,3))
hm2MrpDomainDiagGroup.setObjects(*((_C,_A6),(_C,_A7),(_C,_A8),(_C,_A9),(_C,_AA)))
if mibBuilder.loadTexts:hm2MrpDomainDiagGroup.setStatus(_A)
hm2MrpReconfig=NotificationType((1,3,6,1,4,1,248,11,40,0,1))
hm2MrpReconfig.setObjects((_C,_W))
if mibBuilder.loadTexts:hm2MrpReconfig.setStatus(_A)
hm2SrmReconfig=NotificationType((1,3,6,1,4,1,248,11,40,0,2))
hm2SrmReconfig.setObjects(*((_C,_S),(_C,_AB)))
if mibBuilder.loadTexts:hm2SrmReconfig.setStatus(_A)
hm2RingCplReconfig=NotificationType((1,3,6,1,4,1,248,11,40,0,3))
hm2RingCplReconfig.setObjects(*((_C,_AC),(_C,_AD),(_C,_AE),(_C,_AF)))
if mibBuilder.loadTexts:hm2RingCplReconfig.setStatus(_A)
hm2RedundantCplReconfig=NotificationType((1,3,6,1,4,1,248,11,40,0,4))
hm2RedundantCplReconfig.setObjects(*((_C,_AG),(_C,_AH)))
if mibBuilder.loadTexts:hm2RedundantCplReconfig.setStatus(_A)
hm2MrpNotificationsGroup=NotificationGroup((1,3,6,1,4,1,248,11,40,1,1,2,2,4))
hm2MrpNotificationsGroup.setObjects((_C,_AI))
if mibBuilder.loadTexts:hm2MrpNotificationsGroup.setStatus(_A)
hm2MrpCompliance=ModuleCompliance((1,3,6,1,4,1,248,11,40,1,1,2,1,1))
hm2MrpCompliance.setObjects(*((_C,_AJ),(_C,_AK),(_C,_AL),(_C,_AM)))
if mibBuilder.loadTexts:hm2MrpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'Hm2CplPortOpState':Hm2CplPortOpState,'Hm2CplRingActiveProt':Hm2CplRingActiveProt,'hm2L2RedundancyMib':hm2L2RedundancyMib,'hm2L2RedundancyMibNotifications':hm2L2RedundancyMibNotifications,_AI:hm2MrpReconfig,'hm2SrmReconfig':hm2SrmReconfig,'hm2RingCplReconfig':hm2RingCplReconfig,'hm2RedundantCplReconfig':hm2RedundantCplReconfig,'hm2L2RedundancyMibObjects':hm2L2RedundancyMibObjects,'hm2MrpMibGroup':hm2MrpMibGroup,'hm2MrpTable':hm2MrpTable,'hm2MrpEntry':hm2MrpEntry,_O:hm2MrpDomainID,_p:hm2MrpDomainName,'hm2MrpRingport1GroupID':hm2MrpRingport1GroupID,_q:hm2MrpRingport1IfIndex,_r:hm2MrpRingport1OperState,'hm2MrpRingport2GroupID':hm2MrpRingport2GroupID,_s:hm2MrpRingport2IfIndex,_t:hm2MrpRingport2OperState,_u:hm2MrpRoleAdminState,_v:hm2MrpRoleOperState,_w:hm2MrpRecoveryDelay,_x:hm2MrpRecoveryDelaySupported,_y:hm2MrpVlanID,_A3:hm2MrpMRMPriority,_A4:hm2MrpMRMReactOnLinkChange,_A6:hm2MrpMRMRingOpenCount,_A7:hm2MrpMRMLastRingOpenChange,_A8:hm2MrpMRMRoundTripDelayMax,_A9:hm2MrpMRMRoundTripDelayMin,_AA:hm2MrpMRMRoundTripDelayReset,_A5:hm2MrpMRMNonBlockingMRCSupported,_z:hm2MrpMRCBlockedSupported,_W:hm2MrpRingOperState,_A0:hm2MrpRedundancyOperState,_A1:hm2MrpConfigOperState,_A2:hm2MrpRowStatus,'hm2MrpRingport2FixedBackup':hm2MrpRingport2FixedBackup,'hm2MrpConformance':hm2MrpConformance,'hm2MrpCompliances':hm2MrpCompliances,'hm2MrpCompliance':hm2MrpCompliance,'hm2MrpGroups':hm2MrpGroups,_AJ:hm2MrpDomainBasicGroup,_AK:hm2MrpDomainManagerGroup,_AM:hm2MrpDomainDiagGroup,_AL:hm2MrpNotificationsGroup,'hm2MrpFastMrp':hm2MrpFastMrp,'hm2SrmMibGroup':hm2SrmMibGroup,'hm2SrmGlobalAdminState':hm2SrmGlobalAdminState,'hm2SrmMaxInstances':hm2SrmMaxInstances,'hm2SrmTable':hm2SrmTable,'hm2SrmEntry':hm2SrmEntry,_S:hm2SrmRingID,'hm2SrmAdminState':hm2SrmAdminState,'hm2SrmOperState':hm2SrmOperState,'hm2SrmVlanID':hm2SrmVlanID,'hm2SrmMRPDomainID':hm2SrmMRPDomainID,'hm2SrmPartnerMAC':hm2SrmPartnerMAC,'hm2SrmSubRingProtocol':hm2SrmSubRingProtocol,'hm2SrmSubRingName':hm2SrmSubRingName,'hm2SrmSubRingPortIfIndex':hm2SrmSubRingPortIfIndex,'hm2SrmSubRingPortOperState':hm2SrmSubRingPortOperState,_AB:hm2SrmSubRingOperState,'hm2SrmRedundancyOperState':hm2SrmRedundancyOperState,'hm2SrmConfigOperState':hm2SrmConfigOperState,'hm2SrmRowStatus':hm2SrmRowStatus,'hm2RingRedMibGroup':hm2RingRedMibGroup,'hm2RingRedAdminState':hm2RingRedAdminState,'hm2RingRedMode':hm2RingRedMode,'hm2RingRedPrimaryIntf':hm2RingRedPrimaryIntf,'hm2RingRedPrimaryIntfState':hm2RingRedPrimaryIntfState,'hm2RingRedSecondaryIntf':hm2RingRedSecondaryIntf,'hm2RingRedSecondaryIntfState':hm2RingRedSecondaryIntfState,'hm2RingCouplingMibGroup':hm2RingCouplingMibGroup,'hm2RingCouplingTable':hm2RingCouplingTable,'hm2RingCouplingEntry':hm2RingCouplingEntry,_n:hm2RingCplInterconnIfIndex,_AC:hm2RingCplInterconnIfOpState,'hm2RingCplControlIfIndex':hm2RingCplControlIfIndex,'hm2RingCplControlIfOpState':hm2RingCplControlIfOpState,'hm2RingCplPartnerInterconnIfIndex':hm2RingCplPartnerInterconnIfIndex,_AD:hm2RingCplPartnerInterconnIfOpState,_AE:hm2RingCplPartnerIpAddrType,_AF:hm2RingCplPartnerIpAddr,'hm2RingCplCouplingMode':hm2RingCplCouplingMode,'hm2RingCplControlModeOperState':hm2RingCplControlModeOperState,'hm2RingCplModeOperState':hm2RingCplModeOperState,'hm2RingCplOperState':hm2RingCplOperState,'hm2RingCplConfigOperState':hm2RingCplConfigOperState,'hm2RingCplCouplingLinks':hm2RingCplCouplingLinks,'hm2RingCplExtendedDiag':hm2RingCplExtendedDiag,'hm2RingCplNetCoupling':hm2RingCplNetCoupling,'hm2RingCplRedOperState':hm2RingCplRedOperState,'hm2RingCplRowStatus':hm2RingCplRowStatus,'hm2RedundantCplConfigMibGroup':hm2RedundantCplConfigMibGroup,'hm2RedundantCplAdminState':hm2RedundantCplAdminState,'hm2RedundantCplInPrimaryPort':hm2RedundantCplInPrimaryPort,'hm2RedundantCplOutPrimaryPort':hm2RedundantCplOutPrimaryPort,'hm2RedundantCplInSecondaryPort':hm2RedundantCplInSecondaryPort,'hm2RedundantCplOutSecondaryPort':hm2RedundantCplOutSecondaryPort,'hm2RedundantCplRole':hm2RedundantCplRole,_AG:hm2RedundantCplCurrentRole,'hm2RedundantCplTimeout':hm2RedundantCplTimeout,'hm2RedundantCplPartner':hm2RedundantCplPartner,'hm2RedundantCplPartnerPrimaryPort':hm2RedundantCplPartnerPrimaryPort,'hm2RedundantCplPartnerSecondaryPort':hm2RedundantCplPartnerSecondaryPort,_AH:hm2RedundantCplState,'hm2RedundantCplRedundancyState':hm2RedundantCplRedundancyState,'hm2RedundantCplPartnerIPAddrType':hm2RedundantCplPartnerIPAddrType,'hm2RedundantCplPartnerIPAddr':hm2RedundantCplPartnerIPAddr,'hm2RedundantCplActiveProtPrimaryRing':hm2RedundantCplActiveProtPrimaryRing,'hm2RedundantCplActiveProtSecondaryRing':hm2RedundantCplActiveProtSecondaryRing,'hm2L2RedundancyMibSNMPExtensionGroup':hm2L2RedundancyMibSNMPExtensionGroup,'hm2RingCouplingMibSESGroup':hm2RingCouplingMibSESGroup,'hm2RingCouplingInvalidPortConfiguration':hm2RingCouplingInvalidPortConfiguration,'hm2RedundantCplSESGroup':hm2RedundantCplSESGroup,'hm2RedundantCplPortsMissing':hm2RedundantCplPortsMissing,'hm2RedundantCplSecondaryGroupUnitMismatched':hm2RedundantCplSecondaryGroupUnitMismatched})