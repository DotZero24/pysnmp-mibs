_w='hmSrmRingOperState'
_v='hmSrmRingProtocol'
_u='hmRpcRingOperState'
_t='hmMrpMRMRealRingState'
_s='hmRingRedConfigOperState'
_r='hmRingCplPartnerIpAddr'
_q='hmRingCplPartnerInterconnIfOpState'
_p='hmRingCplInterconnIfOpState'
_o='hmRingRedOperState'
_n='singleManager'
_m='redundantManager'
_l='delay1000'
_k='hmRingCplInterconnIfIndex'
_j='hmRingCplInterconnGroupID'
_i='delay300'
_h='delay500'
_g='underCreation'
_f='inactive'
_e='not-available'
_d='hmRingRedPrimIfIndex'
_c='hmRingRedPrimGroupID'
_b='hmSrmRingID'
_a='hmRpcRingID'
_Z='hmRpcRingProtocol'
_Y='ringportLinkError'
_X='redNotGuaranteed'
_W='redGuaranteed'
_V='closed'
_U='open'
_T='hmMrpDomainID'
_S='standby'
_R='undefined'
_Q='enabled'
_P='client'
_O='read-create'
_N='OctetString'
_M='forwarding'
_L='blocked'
_K='disable'
_J='active'
_I='manager'
_H='noError'
_G='not-connected'
_F='disabled'
_E='HMRING-MGMT-SNMP-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmConfiguration,=mibBuilder.importSymbols('HMPRIV-MGMT-SNMP-MIB','hmConfiguration')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hmRingRedundancy=ModuleIdentity((1,3,6,1,4,1,248,14,5))
if mibBuilder.loadTexts:hmRingRedundancy.setRevisions(('2008-11-18 12:00','2007-09-13 12:00'))
_HmRingRedundancyEvent_ObjectIdentity=ObjectIdentity
hmRingRedundancyEvent=_HmRingRedundancyEvent_ObjectIdentity((1,3,6,1,4,1,248,14,5,0))
if mibBuilder.loadTexts:hmRingRedundancyEvent.setStatus(_A)
_HmRingRedTable_Object=MibTable
hmRingRedTable=_HmRingRedTable_Object((1,3,6,1,4,1,248,14,5,1))
if mibBuilder.loadTexts:hmRingRedTable.setStatus(_A)
_HmRingRedEntry_Object=MibTableRow
hmRingRedEntry=_HmRingRedEntry_Object((1,3,6,1,4,1,248,14,5,1,1))
hmRingRedEntry.setIndexNames((0,_E,_c),(0,_E,_d))
if mibBuilder.loadTexts:hmRingRedEntry.setStatus(_A)
class _HmRingRedPrimGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_HmRingRedPrimGroupID_Type.__name__=_B
_HmRingRedPrimGroupID_Object=MibTableColumn
hmRingRedPrimGroupID=_HmRingRedPrimGroupID_Object((1,3,6,1,4,1,248,14,5,1,1,1),_HmRingRedPrimGroupID_Type())
hmRingRedPrimGroupID.setMaxAccess(_C)
if mibBuilder.loadTexts:hmRingRedPrimGroupID.setStatus(_A)
class _HmRingRedPrimIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_HmRingRedPrimIfIndex_Type.__name__=_B
_HmRingRedPrimIfIndex_Object=MibTableColumn
hmRingRedPrimIfIndex=_HmRingRedPrimIfIndex_Object((1,3,6,1,4,1,248,14,5,1,1,2),_HmRingRedPrimIfIndex_Type())
hmRingRedPrimIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hmRingRedPrimIfIndex.setStatus(_A)
class _HmRingRedPrimIfOpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_e,1),(_J,2),(_f,3)))
_HmRingRedPrimIfOpState_Type.__name__=_B
_HmRingRedPrimIfOpState_Object=MibTableColumn
hmRingRedPrimIfOpState=_HmRingRedPrimIfOpState_Object((1,3,6,1,4,1,248,14,5,1,1,3),_HmRingRedPrimIfOpState_Type())
hmRingRedPrimIfOpState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmRingRedPrimIfOpState.setStatus(_A)
_HmRingRedRedGroupID_Type=Integer32
_HmRingRedRedGroupID_Object=MibTableColumn
hmRingRedRedGroupID=_HmRingRedRedGroupID_Object((1,3,6,1,4,1,248,14,5,1,1,4),_HmRingRedRedGroupID_Type())
hmRingRedRedGroupID.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRingRedRedGroupID.setStatus(_A)
_HmRingRedRedIfIndex_Type=Integer32
_HmRingRedRedIfIndex_Object=MibTableColumn
hmRingRedRedIfIndex=_HmRingRedRedIfIndex_Object((1,3,6,1,4,1,248,14,5,1,1,5),_HmRingRedRedIfIndex_Type())
hmRingRedRedIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRingRedRedIfIndex.setStatus(_A)
class _HmRingRedRedIfOpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_e,1),(_J,2),(_f,3)))
_HmRingRedRedIfOpState_Type.__name__=_B
_HmRingRedRedIfOpState_Object=MibTableColumn
hmRingRedRedIfOpState=_HmRingRedRedIfOpState_Object((1,3,6,1,4,1,248,14,5,1,1,6),_HmRingRedRedIfOpState_Type())
hmRingRedRedIfOpState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmRingRedRedIfOpState.setStatus(_A)
class _HmRingRedOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_g,1),('rmActive',2),('rmInactive',3),('rs',4),(_K,5)))
_HmRingRedOperState_Type.__name__=_B
_HmRingRedOperState_Object=MibTableColumn
hmRingRedOperState=_HmRingRedOperState_Object((1,3,6,1,4,1,248,14,5,1,1,7),_HmRingRedOperState_Type())
hmRingRedOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmRingRedOperState.setStatus(_A)
class _HmRingRedMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('create',1),('delete',2),('rm',3),('rs',4),(_K,5)))
_HmRingRedMode_Type.__name__=_B
_HmRingRedMode_Object=MibTableColumn
hmRingRedMode=_HmRingRedMode_Object((1,3,6,1,4,1,248,14,5,1,1,8),_HmRingRedMode_Type())
hmRingRedMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRingRedMode.setStatus(_A)
class _HmRingRedConfigOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('rmConfigError',2),('ringConfigError',3),('anotherRM',4)))
_HmRingRedConfigOperState_Type.__name__=_B
_HmRingRedConfigOperState_Object=MibTableColumn
hmRingRedConfigOperState=_HmRingRedConfigOperState_Object((1,3,6,1,4,1,248,14,5,1,1,9),_HmRingRedConfigOperState_Type())
hmRingRedConfigOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmRingRedConfigOperState.setStatus(_A)
class _HmRingRedRecoveryDelay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_i,2)))
_HmRingRedRecoveryDelay_Type.__name__=_B
_HmRingRedRecoveryDelay_Object=MibTableColumn
hmRingRedRecoveryDelay=_HmRingRedRecoveryDelay_Object((1,3,6,1,4,1,248,14,5,1,1,10),_HmRingRedRecoveryDelay_Type())
hmRingRedRecoveryDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRingRedRecoveryDelay.setStatus(_A)
_HmRingCouplingTable_Object=MibTable
hmRingCouplingTable=_HmRingCouplingTable_Object((1,3,6,1,4,1,248,14,5,2))
if mibBuilder.loadTexts:hmRingCouplingTable.setStatus(_A)
_HmRingCouplingEntry_Object=MibTableRow
hmRingCouplingEntry=_HmRingCouplingEntry_Object((1,3,6,1,4,1,248,14,5,2,1))
hmRingCouplingEntry.setIndexNames((0,_E,_j),(0,_E,_k))
if mibBuilder.loadTexts:hmRingCouplingEntry.setStatus(_A)
_HmRingCplInterconnGroupID_Type=Integer32
_HmRingCplInterconnGroupID_Object=MibTableColumn
hmRingCplInterconnGroupID=_HmRingCplInterconnGroupID_Object((1,3,6,1,4,1,248,14,5,2,1,1),_HmRingCplInterconnGroupID_Type())
hmRingCplInterconnGroupID.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRingCplInterconnGroupID.setStatus(_A)
_HmRingCplInterconnIfIndex_Type=Integer32
_HmRingCplInterconnIfIndex_Object=MibTableColumn
hmRingCplInterconnIfIndex=_HmRingCplInterconnIfIndex_Object((1,3,6,1,4,1,248,14,5,2,1,2),_HmRingCplInterconnIfIndex_Type())
hmRingCplInterconnIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRingCplInterconnIfIndex.setStatus(_A)
class _HmRingCplInterconnIfOpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_J,2),(_S,3)))
_HmRingCplInterconnIfOpState_Type.__name__=_B
_HmRingCplInterconnIfOpState_Object=MibTableColumn
hmRingCplInterconnIfOpState=_HmRingCplInterconnIfOpState_Object((1,3,6,1,4,1,248,14,5,2,1,3),_HmRingCplInterconnIfOpState_Type())
hmRingCplInterconnIfOpState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmRingCplInterconnIfOpState.setStatus(_A)
_HmRingCplControlGroupID_Type=Integer32
_HmRingCplControlGroupID_Object=MibTableColumn
hmRingCplControlGroupID=_HmRingCplControlGroupID_Object((1,3,6,1,4,1,248,14,5,2,1,4),_HmRingCplControlGroupID_Type())
hmRingCplControlGroupID.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRingCplControlGroupID.setStatus(_A)
_HmRingCplControlIfIndex_Type=Integer32
_HmRingCplControlIfIndex_Object=MibTableColumn
hmRingCplControlIfIndex=_HmRingCplControlIfIndex_Object((1,3,6,1,4,1,248,14,5,2,1,5),_HmRingCplControlIfIndex_Type())
hmRingCplControlIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRingCplControlIfIndex.setStatus(_A)
class _HmRingCplControlIfOpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_J,2),(_S,3)))
_HmRingCplControlIfOpState_Type.__name__=_B
_HmRingCplControlIfOpState_Object=MibTableColumn
hmRingCplControlIfOpState=_HmRingCplControlIfOpState_Object((1,3,6,1,4,1,248,14,5,2,1,6),_HmRingCplControlIfOpState_Type())
hmRingCplControlIfOpState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmRingCplControlIfOpState.setStatus(_A)
class _HmRingCplControlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('outband',1),('inband',2),('unknown',3),('local',4),(_K,5)))
_HmRingCplControlMode_Type.__name__=_B
_HmRingCplControlMode_Object=MibTableColumn
hmRingCplControlMode=_HmRingCplControlMode_Object((1,3,6,1,4,1,248,14,5,2,1,7),_HmRingCplControlMode_Type())
hmRingCplControlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRingCplControlMode.setStatus(_A)
_HmRingCplPartnerIpAddr_Type=IpAddress
_HmRingCplPartnerIpAddr_Object=MibTableColumn
hmRingCplPartnerIpAddr=_HmRingCplPartnerIpAddr_Object((1,3,6,1,4,1,248,14,5,2,1,8),_HmRingCplPartnerIpAddr_Type())
hmRingCplPartnerIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hmRingCplPartnerIpAddr.setStatus(_A)
_HmRingCplPartnerInterconnGroupID_Type=Integer32
_HmRingCplPartnerInterconnGroupID_Object=MibTableColumn
hmRingCplPartnerInterconnGroupID=_HmRingCplPartnerInterconnGroupID_Object((1,3,6,1,4,1,248,14,5,2,1,9),_HmRingCplPartnerInterconnGroupID_Type())
hmRingCplPartnerInterconnGroupID.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRingCplPartnerInterconnGroupID.setStatus(_A)
_HmRingCplPartnerInterconnIfIndex_Type=Integer32
_HmRingCplPartnerInterconnIfIndex_Object=MibTableColumn
hmRingCplPartnerInterconnIfIndex=_HmRingCplPartnerInterconnIfIndex_Object((1,3,6,1,4,1,248,14,5,2,1,10),_HmRingCplPartnerInterconnIfIndex_Type())
hmRingCplPartnerInterconnIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRingCplPartnerInterconnIfIndex.setStatus(_A)
class _HmRingCplPartnerInterconnIfOpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_J,2),(_S,3)))
_HmRingCplPartnerInterconnIfOpState_Type.__name__=_B
_HmRingCplPartnerInterconnIfOpState_Object=MibTableColumn
hmRingCplPartnerInterconnIfOpState=_HmRingCplPartnerInterconnIfOpState_Object((1,3,6,1,4,1,248,14,5,2,1,11),_HmRingCplPartnerInterconnIfOpState_Type())
hmRingCplPartnerInterconnIfOpState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmRingCplPartnerInterconnIfOpState.setStatus(_A)
class _HmRingCplOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_g,1),('slave',2),('master',3),('local',4),(_K,5)))
_HmRingCplOperState_Type.__name__=_B
_HmRingCplOperState_Object=MibTableColumn
hmRingCplOperState=_HmRingCplOperState_Object((1,3,6,1,4,1,248,14,5,2,1,12),_HmRingCplOperState_Type())
hmRingCplOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmRingCplOperState.setStatus(_A)
class _HmRingCplMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('slaveOff',1),('slaveOn',2),(_K,3)))
_HmRingCplMode_Type.__name__=_B
_HmRingCplMode_Object=MibTableColumn
hmRingCplMode=_HmRingCplMode_Object((1,3,6,1,4,1,248,14,5,2,1,13),_HmRingCplMode_Type())
hmRingCplMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRingCplMode.setStatus(_A)
_HmRingCplRowStatus_Type=RowStatus
_HmRingCplRowStatus_Object=MibTableColumn
hmRingCplRowStatus=_HmRingCplRowStatus_Object((1,3,6,1,4,1,248,14,5,2,1,14),_HmRingCplRowStatus_Type())
hmRingCplRowStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:hmRingCplRowStatus.setStatus(_A)
class _HmRingCplConfigOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_H,1),('slaveCouplingLinkError',2),('slaveControlLinkError',3),('masterControlLinkError',4),('twoSlaves',5),('localPartnerLinkError',6),('localInvalidCouplingPort',7),('couplingPortNotAvailable',8),('controlPortNotAvailable',9),('partnerPortNotAvailable',10)))
_HmRingCplConfigOperState_Type.__name__=_B
_HmRingCplConfigOperState_Object=MibTableColumn
hmRingCplConfigOperState=_HmRingCplConfigOperState_Object((1,3,6,1,4,1,248,14,5,2,1,15),_HmRingCplConfigOperState_Type())
hmRingCplConfigOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmRingCplConfigOperState.setStatus(_A)
class _HmRingCplCouplingLinks_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('basicRedundancy',1),('extendedRedundancy',2)))
_HmRingCplCouplingLinks_Type.__name__=_B
_HmRingCplCouplingLinks_Object=MibTableColumn
hmRingCplCouplingLinks=_HmRingCplCouplingLinks_Object((1,3,6,1,4,1,248,14,5,2,1,16),_HmRingCplCouplingLinks_Type())
hmRingCplCouplingLinks.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRingCplCouplingLinks.setStatus(_A)
class _HmRingCplExtendedDiag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('basicRedundancyInactive',2)))
_HmRingCplExtendedDiag_Type.__name__=_B
_HmRingCplExtendedDiag_Object=MibTableColumn
hmRingCplExtendedDiag=_HmRingCplExtendedDiag_Object((1,3,6,1,4,1,248,14,5,2,1,17),_HmRingCplExtendedDiag_Type())
hmRingCplExtendedDiag.setMaxAccess(_C)
if mibBuilder.loadTexts:hmRingCplExtendedDiag.setStatus(_A)
class _HmRingCplNetCoupling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ringCoupling',1),('netCoupling',2)))
_HmRingCplNetCoupling_Type.__name__=_B
_HmRingCplNetCoupling_Object=MibTableColumn
hmRingCplNetCoupling=_HmRingCplNetCoupling_Object((1,3,6,1,4,1,248,14,5,2,1,18),_HmRingCplNetCoupling_Type())
hmRingCplNetCoupling.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRingCplNetCoupling.setStatus(_A)
class _HmRingCplConfigSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dipSwitch',1),('management',2)))
_HmRingCplConfigSource_Type.__name__=_B
_HmRingCplConfigSource_Object=MibTableColumn
hmRingCplConfigSource=_HmRingCplConfigSource_Object((1,3,6,1,4,1,248,14,5,2,1,19),_HmRingCplConfigSource_Type())
hmRingCplConfigSource.setMaxAccess(_C)
if mibBuilder.loadTexts:hmRingCplConfigSource.setStatus(_A)
_HmMrpTable_Object=MibTable
hmMrpTable=_HmMrpTable_Object((1,3,6,1,4,1,248,14,5,3))
if mibBuilder.loadTexts:hmMrpTable.setStatus(_A)
_HmMrpEntry_Object=MibTableRow
hmMrpEntry=_HmMrpEntry_Object((1,3,6,1,4,1,248,14,5,3,1))
hmMrpEntry.setIndexNames((1,_E,_T))
if mibBuilder.loadTexts:hmMrpEntry.setStatus(_A)
class _HmMrpDomainID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_HmMrpDomainID_Type.__name__=_N
_HmMrpDomainID_Object=MibTableColumn
hmMrpDomainID=_HmMrpDomainID_Object((1,3,6,1,4,1,248,14,5,3,1,1),_HmMrpDomainID_Type())
hmMrpDomainID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hmMrpDomainID.setStatus(_A)
_HmMrpRingport1GroupID_Type=Integer32
_HmMrpRingport1GroupID_Object=MibTableColumn
hmMrpRingport1GroupID=_HmMrpRingport1GroupID_Object((1,3,6,1,4,1,248,14,5,3,1,2),_HmMrpRingport1GroupID_Type())
hmMrpRingport1GroupID.setMaxAccess(_D)
if mibBuilder.loadTexts:hmMrpRingport1GroupID.setStatus(_A)
_HmMrpRingport1IfIndex_Type=Integer32
_HmMrpRingport1IfIndex_Object=MibTableColumn
hmMrpRingport1IfIndex=_HmMrpRingport1IfIndex_Object((1,3,6,1,4,1,248,14,5,3,1,3),_HmMrpRingport1IfIndex_Type())
hmMrpRingport1IfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hmMrpRingport1IfIndex.setStatus(_A)
class _HmMrpRingport1OperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_L,2),(_M,3),(_G,4)))
_HmMrpRingport1OperState_Type.__name__=_B
_HmMrpRingport1OperState_Object=MibTableColumn
hmMrpRingport1OperState=_HmMrpRingport1OperState_Object((1,3,6,1,4,1,248,14,5,3,1,4),_HmMrpRingport1OperState_Type())
hmMrpRingport1OperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMrpRingport1OperState.setStatus(_A)
_HmMrpRingport2GroupID_Type=Integer32
_HmMrpRingport2GroupID_Object=MibTableColumn
hmMrpRingport2GroupID=_HmMrpRingport2GroupID_Object((1,3,6,1,4,1,248,14,5,3,1,5),_HmMrpRingport2GroupID_Type())
hmMrpRingport2GroupID.setMaxAccess(_D)
if mibBuilder.loadTexts:hmMrpRingport2GroupID.setStatus(_A)
_HmMrpRingport2IfIndex_Type=Integer32
_HmMrpRingport2IfIndex_Object=MibTableColumn
hmMrpRingport2IfIndex=_HmMrpRingport2IfIndex_Object((1,3,6,1,4,1,248,14,5,3,1,6),_HmMrpRingport2IfIndex_Type())
hmMrpRingport2IfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hmMrpRingport2IfIndex.setStatus(_A)
class _HmMrpRingport2OperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_L,2),(_M,3),(_G,4)))
_HmMrpRingport2OperState_Type.__name__=_B
_HmMrpRingport2OperState_Object=MibTableColumn
hmMrpRingport2OperState=_HmMrpRingport2OperState_Object((1,3,6,1,4,1,248,14,5,3,1,7),_HmMrpRingport2OperState_Type())
hmMrpRingport2OperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMrpRingport2OperState.setStatus(_A)
_HmMrpVlanID_Type=Integer32
_HmMrpVlanID_Object=MibTableColumn
hmMrpVlanID=_HmMrpVlanID_Object((1,3,6,1,4,1,248,14,5,3,1,8),_HmMrpVlanID_Type())
hmMrpVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:hmMrpVlanID.setStatus(_A)
class _HmMrpExpectedRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_I,2)))
_HmMrpExpectedRole_Type.__name__=_B
_HmMrpExpectedRole_Object=MibTableColumn
hmMrpExpectedRole=_HmMrpExpectedRole_Object((1,3,6,1,4,1,248,14,5,3,1,9),_HmMrpExpectedRole_Type())
hmMrpExpectedRole.setMaxAccess(_D)
if mibBuilder.loadTexts:hmMrpExpectedRole.setStatus(_A)
_HmMrpMRCLinkDownInterval_Type=Integer32
_HmMrpMRCLinkDownInterval_Object=MibTableColumn
hmMrpMRCLinkDownInterval=_HmMrpMRCLinkDownInterval_Object((1,3,6,1,4,1,248,14,5,3,1,10),_HmMrpMRCLinkDownInterval_Type())
hmMrpMRCLinkDownInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMrpMRCLinkDownInterval.setStatus(_A)
_HmMrpMRCLinkUpInterval_Type=Integer32
_HmMrpMRCLinkUpInterval_Object=MibTableColumn
hmMrpMRCLinkUpInterval=_HmMrpMRCLinkUpInterval_Object((1,3,6,1,4,1,248,14,5,3,1,11),_HmMrpMRCLinkUpInterval_Type())
hmMrpMRCLinkUpInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMrpMRCLinkUpInterval.setStatus(_A)
_HmMrpMRCLinkChangeCount_Type=Integer32
_HmMrpMRCLinkChangeCount_Object=MibTableColumn
hmMrpMRCLinkChangeCount=_HmMrpMRCLinkChangeCount_Object((1,3,6,1,4,1,248,14,5,3,1,12),_HmMrpMRCLinkChangeCount_Type())
hmMrpMRCLinkChangeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMrpMRCLinkChangeCount.setStatus(_A)
class _HmMrpMRCBlockedSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_F,2)))
_HmMrpMRCBlockedSupported_Type.__name__=_B
_HmMrpMRCBlockedSupported_Object=MibTableColumn
hmMrpMRCBlockedSupported=_HmMrpMRCBlockedSupported_Object((1,3,6,1,4,1,248,14,5,3,1,13),_HmMrpMRCBlockedSupported_Type())
hmMrpMRCBlockedSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMrpMRCBlockedSupported.setStatus(_A)
class _HmMrpMRMPriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HmMrpMRMPriority_Type.__name__=_B
_HmMrpMRMPriority_Object=MibTableColumn
hmMrpMRMPriority=_HmMrpMRMPriority_Object((1,3,6,1,4,1,248,14,5,3,1,14),_HmMrpMRMPriority_Type())
hmMrpMRMPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:hmMrpMRMPriority.setStatus(_A)
_HmMrpMRMTopologyChangeInterval_Type=Integer32
_HmMrpMRMTopologyChangeInterval_Object=MibTableColumn
hmMrpMRMTopologyChangeInterval=_HmMrpMRMTopologyChangeInterval_Object((1,3,6,1,4,1,248,14,5,3,1,15),_HmMrpMRMTopologyChangeInterval_Type())
hmMrpMRMTopologyChangeInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMrpMRMTopologyChangeInterval.setStatus(_A)
_HmMrpMRMTopologyChangeRepeatCount_Type=Integer32
_HmMrpMRMTopologyChangeRepeatCount_Object=MibTableColumn
hmMrpMRMTopologyChangeRepeatCount=_HmMrpMRMTopologyChangeRepeatCount_Object((1,3,6,1,4,1,248,14,5,3,1,16),_HmMrpMRMTopologyChangeRepeatCount_Type())
hmMrpMRMTopologyChangeRepeatCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMrpMRMTopologyChangeRepeatCount.setStatus(_A)
_HmMrpMRMShortTestInterval_Type=Integer32
_HmMrpMRMShortTestInterval_Object=MibTableColumn
hmMrpMRMShortTestInterval=_HmMrpMRMShortTestInterval_Object((1,3,6,1,4,1,248,14,5,3,1,17),_HmMrpMRMShortTestInterval_Type())
hmMrpMRMShortTestInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMrpMRMShortTestInterval.setStatus(_A)
_HmMrpMRMDefaultTestInterval_Type=Integer32
_HmMrpMRMDefaultTestInterval_Object=MibTableColumn
hmMrpMRMDefaultTestInterval=_HmMrpMRMDefaultTestInterval_Object((1,3,6,1,4,1,248,14,5,3,1,18),_HmMrpMRMDefaultTestInterval_Type())
hmMrpMRMDefaultTestInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMrpMRMDefaultTestInterval.setStatus(_A)
_HmMrpMRMTestMonitoringCount_Type=Integer32
_HmMrpMRMTestMonitoringCount_Object=MibTableColumn
hmMrpMRMTestMonitoringCount=_HmMrpMRMTestMonitoringCount_Object((1,3,6,1,4,1,248,14,5,3,1,19),_HmMrpMRMTestMonitoringCount_Type())
hmMrpMRMTestMonitoringCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMrpMRMTestMonitoringCount.setStatus(_A)
class _HmMrpMRMNonBlockingMRCSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_F,2)))
_HmMrpMRMNonBlockingMRCSupported_Type.__name__=_B
_HmMrpMRMNonBlockingMRCSupported_Object=MibTableColumn
hmMrpMRMNonBlockingMRCSupported=_HmMrpMRMNonBlockingMRCSupported_Object((1,3,6,1,4,1,248,14,5,3,1,20),_HmMrpMRMNonBlockingMRCSupported_Type())
hmMrpMRMNonBlockingMRCSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMrpMRMNonBlockingMRCSupported.setStatus(_A)
_HmMrpMRMTestMonitoringExtendedCount_Type=Integer32
_HmMrpMRMTestMonitoringExtendedCount_Object=MibTableColumn
hmMrpMRMTestMonitoringExtendedCount=_HmMrpMRMTestMonitoringExtendedCount_Object((1,3,6,1,4,1,248,14,5,3,1,21),_HmMrpMRMTestMonitoringExtendedCount_Type())
hmMrpMRMTestMonitoringExtendedCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMrpMRMTestMonitoringExtendedCount.setStatus(_A)
class _HmMrpMRMReactOnLinkChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_F,2)))
_HmMrpMRMReactOnLinkChange_Type.__name__=_B
_HmMrpMRMReactOnLinkChange_Object=MibTableColumn
hmMrpMRMReactOnLinkChange=_HmMrpMRMReactOnLinkChange_Object((1,3,6,1,4,1,248,14,5,3,1,22),_HmMrpMRMReactOnLinkChange_Type())
hmMrpMRMReactOnLinkChange.setMaxAccess(_D)
if mibBuilder.loadTexts:hmMrpMRMReactOnLinkChange.setStatus(_A)
class _HmMrpMRMCheckMediaRedundancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_F,2)))
_HmMrpMRMCheckMediaRedundancy_Type.__name__=_B
_HmMrpMRMCheckMediaRedundancy_Object=MibTableColumn
hmMrpMRMCheckMediaRedundancy=_HmMrpMRMCheckMediaRedundancy_Object((1,3,6,1,4,1,248,14,5,3,1,23),_HmMrpMRMCheckMediaRedundancy_Type())
hmMrpMRMCheckMediaRedundancy.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMrpMRMCheckMediaRedundancy.setStatus(_A)
class _HmMrpMRMRealRoleState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_I,2),(_R,3)))
_HmMrpMRMRealRoleState_Type.__name__=_B
_HmMrpMRMRealRoleState_Object=MibTableColumn
hmMrpMRMRealRoleState=_HmMrpMRMRealRoleState_Object((1,3,6,1,4,1,248,14,5,3,1,24),_HmMrpMRMRealRoleState_Type())
hmMrpMRMRealRoleState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMrpMRMRealRoleState.setStatus(_A)
class _HmMrpMRMRealRingState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),(_V,2),(_R,3)))
_HmMrpMRMRealRingState_Type.__name__=_B
_HmMrpMRMRealRingState_Object=MibTableColumn
hmMrpMRMRealRingState=_HmMrpMRMRealRingState_Object((1,3,6,1,4,1,248,14,5,3,1,25),_HmMrpMRMRealRingState_Type())
hmMrpMRMRealRingState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMrpMRMRealRingState.setStatus(_A)
_HmMrpRowStatus_Type=RowStatus
_HmMrpRowStatus_Object=MibTableColumn
hmMrpRowStatus=_HmMrpRowStatus_Object((1,3,6,1,4,1,248,14,5,3,1,26),_HmMrpRowStatus_Type())
hmMrpRowStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:hmMrpRowStatus.setStatus(_A)
class _HmMrpRedOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_HmMrpRedOperState_Type.__name__=_B
_HmMrpRedOperState_Object=MibTableColumn
hmMrpRedOperState=_HmMrpRedOperState_Object((1,3,6,1,4,1,248,14,5,3,1,27),_HmMrpRedOperState_Type())
hmMrpRedOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMrpRedOperState.setStatus(_A)
class _HmMrpConfigOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_Y,2)))
_HmMrpConfigOperState_Type.__name__=_B
_HmMrpConfigOperState_Object=MibTableColumn
hmMrpConfigOperState=_HmMrpConfigOperState_Object((1,3,6,1,4,1,248,14,5,3,1,28),_HmMrpConfigOperState_Type())
hmMrpConfigOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmMrpConfigOperState.setStatus(_A)
_HmMrpDomainName_Type=DisplayString
_HmMrpDomainName_Object=MibTableColumn
hmMrpDomainName=_HmMrpDomainName_Object((1,3,6,1,4,1,248,14,5,3,1,29),_HmMrpDomainName_Type())
hmMrpDomainName.setMaxAccess(_D)
if mibBuilder.loadTexts:hmMrpDomainName.setStatus(_A)
class _HmMrpMRMRecoveryDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_h,1),('delay200',2),(_l,3)))
_HmMrpMRMRecoveryDelay_Type.__name__=_B
_HmMrpMRMRecoveryDelay_Object=MibTableColumn
hmMrpMRMRecoveryDelay=_HmMrpMRMRecoveryDelay_Object((1,3,6,1,4,1,248,14,5,3,1,30),_HmMrpMRMRecoveryDelay_Type())
hmMrpMRMRecoveryDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:hmMrpMRMRecoveryDelay.setStatus(_A)
_HmRpcTable_Object=MibTable
hmRpcTable=_HmRpcTable_Object((1,3,6,1,4,1,248,14,5,4))
if mibBuilder.loadTexts:hmRpcTable.setStatus(_A)
_HmRpcEntry_Object=MibTableRow
hmRpcEntry=_HmRpcEntry_Object((1,3,6,1,4,1,248,14,5,4,1))
hmRpcEntry.setIndexNames((0,_E,_Z),(0,_E,_a))
if mibBuilder.loadTexts:hmRpcEntry.setStatus(_A)
class _HmRpcRingProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(3));namedValues=NamedValues(('fastHiperRing',3))
_HmRpcRingProtocol_Type.__name__=_B
_HmRpcRingProtocol_Object=MibTableColumn
hmRpcRingProtocol=_HmRpcRingProtocol_Object((1,3,6,1,4,1,248,14,5,4,1,1),_HmRpcRingProtocol_Type())
hmRpcRingProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRpcRingProtocol.setStatus(_A)
_HmRpcRingID_Type=Integer32
_HmRpcRingID_Object=MibTableColumn
hmRpcRingID=_HmRpcRingID_Object((1,3,6,1,4,1,248,14,5,4,1,2),_HmRpcRingID_Type())
hmRpcRingID.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRpcRingID.setStatus(_A)
_HmRpcRingName_Type=DisplayString
_HmRpcRingName_Object=MibTableColumn
hmRpcRingName=_HmRpcRingName_Object((1,3,6,1,4,1,248,14,5,4,1,3),_HmRpcRingName_Type())
hmRpcRingName.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRpcRingName.setStatus(_A)
_HmRpcRingport1GroupID_Type=Integer32
_HmRpcRingport1GroupID_Object=MibTableColumn
hmRpcRingport1GroupID=_HmRpcRingport1GroupID_Object((1,3,6,1,4,1,248,14,5,4,1,4),_HmRpcRingport1GroupID_Type())
hmRpcRingport1GroupID.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRpcRingport1GroupID.setStatus(_A)
_HmRpcRingport1IfIndex_Type=Integer32
_HmRpcRingport1IfIndex_Object=MibTableColumn
hmRpcRingport1IfIndex=_HmRpcRingport1IfIndex_Object((1,3,6,1,4,1,248,14,5,4,1,5),_HmRpcRingport1IfIndex_Type())
hmRpcRingport1IfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRpcRingport1IfIndex.setStatus(_A)
class _HmRpcRingport1OperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_L,2),(_M,3),(_G,4)))
_HmRpcRingport1OperState_Type.__name__=_B
_HmRpcRingport1OperState_Object=MibTableColumn
hmRpcRingport1OperState=_HmRpcRingport1OperState_Object((1,3,6,1,4,1,248,14,5,4,1,6),_HmRpcRingport1OperState_Type())
hmRpcRingport1OperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmRpcRingport1OperState.setStatus(_A)
_HmRpcRingport2GroupID_Type=Integer32
_HmRpcRingport2GroupID_Object=MibTableColumn
hmRpcRingport2GroupID=_HmRpcRingport2GroupID_Object((1,3,6,1,4,1,248,14,5,4,1,7),_HmRpcRingport2GroupID_Type())
hmRpcRingport2GroupID.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRpcRingport2GroupID.setStatus(_A)
_HmRpcRingport2IfIndex_Type=Integer32
_HmRpcRingport2IfIndex_Object=MibTableColumn
hmRpcRingport2IfIndex=_HmRpcRingport2IfIndex_Object((1,3,6,1,4,1,248,14,5,4,1,8),_HmRpcRingport2IfIndex_Type())
hmRpcRingport2IfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRpcRingport2IfIndex.setStatus(_A)
class _HmRpcRingport2OperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_L,2),(_M,3),(_G,4)))
_HmRpcRingport2OperState_Type.__name__=_B
_HmRpcRingport2OperState_Object=MibTableColumn
hmRpcRingport2OperState=_HmRpcRingport2OperState_Object((1,3,6,1,4,1,248,14,5,4,1,9),_HmRpcRingport2OperState_Type())
hmRpcRingport2OperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmRpcRingport2OperState.setStatus(_A)
_HmRpcVlanID_Type=Integer32
_HmRpcVlanID_Object=MibTableColumn
hmRpcVlanID=_HmRpcVlanID_Object((1,3,6,1,4,1,248,14,5,4,1,10),_HmRpcVlanID_Type())
hmRpcVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRpcVlanID.setStatus(_A)
class _HmRpcAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_I,2)))
_HmRpcAdminState_Type.__name__=_B
_HmRpcAdminState_Object=MibTableColumn
hmRpcAdminState=_HmRpcAdminState_Object((1,3,6,1,4,1,248,14,5,4,1,11),_HmRpcAdminState_Type())
hmRpcAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRpcAdminState.setStatus(_A)
class _HmRpcOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_I,2),(_F,3)))
_HmRpcOperState_Type.__name__=_B
_HmRpcOperState_Object=MibTableColumn
hmRpcOperState=_HmRpcOperState_Object((1,3,6,1,4,1,248,14,5,4,1,12),_HmRpcOperState_Type())
hmRpcOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmRpcOperState.setStatus(_A)
class _HmRpcRingOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_U,2),(_V,3)))
_HmRpcRingOperState_Type.__name__=_B
_HmRpcRingOperState_Object=MibTableColumn
hmRpcRingOperState=_HmRpcRingOperState_Object((1,3,6,1,4,1,248,14,5,4,1,13),_HmRpcRingOperState_Type())
hmRpcRingOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmRpcRingOperState.setStatus(_A)
class _HmRpcRedundancyOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_HmRpcRedundancyOperState_Type.__name__=_B
_HmRpcRedundancyOperState_Object=MibTableColumn
hmRpcRedundancyOperState=_HmRpcRedundancyOperState_Object((1,3,6,1,4,1,248,14,5,4,1,14),_HmRpcRedundancyOperState_Type())
hmRpcRedundancyOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmRpcRedundancyOperState.setStatus(_A)
class _HmRpcConfigOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),(_Y,2),('singleSideReceive',3),('multipleRM',4)))
_HmRpcConfigOperState_Type.__name__=_B
_HmRpcConfigOperState_Object=MibTableColumn
hmRpcConfigOperState=_HmRpcConfigOperState_Object((1,3,6,1,4,1,248,14,5,4,1,15),_HmRpcConfigOperState_Type())
hmRpcConfigOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmRpcConfigOperState.setStatus(_A)
_HmRpcRowStatus_Type=RowStatus
_HmRpcRowStatus_Object=MibTableColumn
hmRpcRowStatus=_HmRpcRowStatus_Object((1,3,6,1,4,1,248,14,5,4,1,16),_HmRpcRowStatus_Type())
hmRpcRowStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:hmRpcRowStatus.setStatus(_A)
_HmRpcNodes_Type=Integer32
_HmRpcNodes_Object=MibTableColumn
hmRpcNodes=_HmRpcNodes_Object((1,3,6,1,4,1,248,14,5,4,1,17),_HmRpcNodes_Type())
hmRpcNodes.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRpcNodes.setStatus(_A)
_HmRpcRoundTripDelay_Type=Unsigned32
_HmRpcRoundTripDelay_Object=MibTableColumn
hmRpcRoundTripDelay=_HmRpcRoundTripDelay_Object((1,3,6,1,4,1,248,14,5,4,1,18),_HmRpcRoundTripDelay_Type())
hmRpcRoundTripDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hmRpcRoundTripDelay.setStatus(_A)
_HmMultiHiperRing_ObjectIdentity=ObjectIdentity
hmMultiHiperRing=_HmMultiHiperRing_ObjectIdentity((1,3,6,1,4,1,248,14,5,5))
_HmSrmMaxInstances_Type=Integer32
_HmSrmMaxInstances_Object=MibScalar
hmSrmMaxInstances=_HmSrmMaxInstances_Object((1,3,6,1,4,1,248,14,5,5,1),_HmSrmMaxInstances_Type())
hmSrmMaxInstances.setMaxAccess(_C)
if mibBuilder.loadTexts:hmSrmMaxInstances.setStatus(_A)
_HmSrmTable_Object=MibTable
hmSrmTable=_HmSrmTable_Object((1,3,6,1,4,1,248,14,5,5,5))
if mibBuilder.loadTexts:hmSrmTable.setStatus(_A)
_HmSrmEntry_Object=MibTableRow
hmSrmEntry=_HmSrmEntry_Object((1,3,6,1,4,1,248,14,5,5,5,1))
hmSrmEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:hmSrmEntry.setStatus(_A)
_HmSrmRingID_Type=Integer32
_HmSrmRingID_Object=MibTableColumn
hmSrmRingID=_HmSrmRingID_Object((1,3,6,1,4,1,248,14,5,5,5,1,1),_HmSrmRingID_Type())
hmSrmRingID.setMaxAccess(_D)
if mibBuilder.loadTexts:hmSrmRingID.setStatus(_A)
class _HmSrmRingProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(4));namedValues=NamedValues(('standardMRP',4))
_HmSrmRingProtocol_Type.__name__=_B
_HmSrmRingProtocol_Object=MibTableColumn
hmSrmRingProtocol=_HmSrmRingProtocol_Object((1,3,6,1,4,1,248,14,5,5,5,1,2),_HmSrmRingProtocol_Type())
hmSrmRingProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:hmSrmRingProtocol.setStatus(_A)
_HmSrmRingName_Type=DisplayString
_HmSrmRingName_Object=MibTableColumn
hmSrmRingName=_HmSrmRingName_Object((1,3,6,1,4,1,248,14,5,5,5,1,3),_HmSrmRingName_Type())
hmSrmRingName.setMaxAccess(_D)
if mibBuilder.loadTexts:hmSrmRingName.setStatus(_A)
_HmSrmRingport1GroupID_Type=Integer32
_HmSrmRingport1GroupID_Object=MibTableColumn
hmSrmRingport1GroupID=_HmSrmRingport1GroupID_Object((1,3,6,1,4,1,248,14,5,5,5,1,4),_HmSrmRingport1GroupID_Type())
hmSrmRingport1GroupID.setMaxAccess(_D)
if mibBuilder.loadTexts:hmSrmRingport1GroupID.setStatus(_A)
_HmSrmRingport1IfIndex_Type=Integer32
_HmSrmRingport1IfIndex_Object=MibTableColumn
hmSrmRingport1IfIndex=_HmSrmRingport1IfIndex_Object((1,3,6,1,4,1,248,14,5,5,5,1,5),_HmSrmRingport1IfIndex_Type())
hmSrmRingport1IfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hmSrmRingport1IfIndex.setStatus(_A)
class _HmSrmRingport1OperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_L,2),(_M,3),(_G,4)))
_HmSrmRingport1OperState_Type.__name__=_B
_HmSrmRingport1OperState_Object=MibTableColumn
hmSrmRingport1OperState=_HmSrmRingport1OperState_Object((1,3,6,1,4,1,248,14,5,5,5,1,6),_HmSrmRingport1OperState_Type())
hmSrmRingport1OperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmSrmRingport1OperState.setStatus(_A)
class _HmSrmVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4042))
_HmSrmVlanID_Type.__name__=_B
_HmSrmVlanID_Object=MibTableColumn
hmSrmVlanID=_HmSrmVlanID_Object((1,3,6,1,4,1,248,14,5,5,5,1,7),_HmSrmVlanID_Type())
hmSrmVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:hmSrmVlanID.setStatus(_A)
class _HmSrmAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_m,2),(_n,3)))
_HmSrmAdminState_Type.__name__=_B
_HmSrmAdminState_Object=MibTableColumn
hmSrmAdminState=_HmSrmAdminState_Object((1,3,6,1,4,1,248,14,5,5,5,1,8),_HmSrmAdminState_Type())
hmSrmAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:hmSrmAdminState.setStatus(_A)
class _HmSrmOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_m,2),(_n,3),(_F,4)))
_HmSrmOperState_Type.__name__=_B
_HmSrmOperState_Object=MibTableColumn
hmSrmOperState=_HmSrmOperState_Object((1,3,6,1,4,1,248,14,5,5,5,1,9),_HmSrmOperState_Type())
hmSrmOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmSrmOperState.setStatus(_A)
class _HmSrmRingOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_U,2),(_V,3)))
_HmSrmRingOperState_Type.__name__=_B
_HmSrmRingOperState_Object=MibTableColumn
hmSrmRingOperState=_HmSrmRingOperState_Object((1,3,6,1,4,1,248,14,5,5,5,1,10),_HmSrmRingOperState_Type())
hmSrmRingOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmSrmRingOperState.setStatus(_A)
class _HmSrmRedundancyOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_HmSrmRedundancyOperState_Type.__name__=_B
_HmSrmRedundancyOperState_Object=MibTableColumn
hmSrmRedundancyOperState=_HmSrmRedundancyOperState_Object((1,3,6,1,4,1,248,14,5,5,5,1,11),_HmSrmRedundancyOperState_Type())
hmSrmRedundancyOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmSrmRedundancyOperState.setStatus(_A)
class _HmSrmConfigOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_H,1),(_Y,2),('multipleSRM',3),('noPartnerManager',4),('concurrentVLAN',5),('concurrentPort',6),('concurrentRedundancy',7),('trunkMember',8),('sharedVLAN',9)))
_HmSrmConfigOperState_Type.__name__=_B
_HmSrmConfigOperState_Object=MibTableColumn
hmSrmConfigOperState=_HmSrmConfigOperState_Object((1,3,6,1,4,1,248,14,5,5,5,1,12),_HmSrmConfigOperState_Type())
hmSrmConfigOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:hmSrmConfigOperState.setStatus(_A)
_HmSrmRowStatus_Type=RowStatus
_HmSrmRowStatus_Object=MibTableColumn
hmSrmRowStatus=_HmSrmRowStatus_Object((1,3,6,1,4,1,248,14,5,5,5,1,13),_HmSrmRowStatus_Type())
hmSrmRowStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:hmSrmRowStatus.setStatus(_A)
class _HmSrmNodes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HmSrmNodes_Type.__name__=_B
_HmSrmNodes_Object=MibTableColumn
hmSrmNodes=_HmSrmNodes_Object((1,3,6,1,4,1,248,14,5,5,5,1,14),_HmSrmNodes_Type())
hmSrmNodes.setMaxAccess(_D)
if mibBuilder.loadTexts:hmSrmNodes.setStatus(_A)
class _HmSrmMRPDomainID_Type(OctetString):defaultHexValue='FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_HmSrmMRPDomainID_Type.__name__=_N
_HmSrmMRPDomainID_Object=MibTableColumn
hmSrmMRPDomainID=_HmSrmMRPDomainID_Object((1,3,6,1,4,1,248,14,5,5,5,1,15),_HmSrmMRPDomainID_Type())
hmSrmMRPDomainID.setMaxAccess(_D)
if mibBuilder.loadTexts:hmSrmMRPDomainID.setStatus(_A)
class _HmSrmPartnerMAC_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HmSrmPartnerMAC_Type.__name__=_N
_HmSrmPartnerMAC_Object=MibTableColumn
hmSrmPartnerMAC=_HmSrmPartnerMAC_Object((1,3,6,1,4,1,248,14,5,5,5,1,16),_HmSrmPartnerMAC_Type())
hmSrmPartnerMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:hmSrmPartnerMAC.setStatus(_A)
class _HmSrmRecoveryDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_i,1),(_l,2)))
_HmSrmRecoveryDelay_Type.__name__=_B
_HmSrmRecoveryDelay_Object=MibTableColumn
hmSrmRecoveryDelay=_HmSrmRecoveryDelay_Object((1,3,6,1,4,1,248,14,5,5,5,1,17),_HmSrmRecoveryDelay_Type())
hmSrmRecoveryDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:hmSrmRecoveryDelay.setStatus(_A)
hmRingRedReconfig=NotificationType((1,3,6,1,4,1,248,14,5,0,1))
hmRingRedReconfig.setObjects((_E,_o))
if mibBuilder.loadTexts:hmRingRedReconfig.setStatus(_A)
hmRingCplReconfig=NotificationType((1,3,6,1,4,1,248,14,5,0,2))
hmRingCplReconfig.setObjects(*((_E,_p),(_E,_q),(_E,_r)))
if mibBuilder.loadTexts:hmRingCplReconfig.setStatus(_A)
hmRingRedConfigChanged=NotificationType((1,3,6,1,4,1,248,14,5,0,3))
hmRingRedConfigChanged.setObjects((_E,_s))
if mibBuilder.loadTexts:hmRingRedConfigChanged.setStatus(_A)
hmMrpReconfig=NotificationType((1,3,6,1,4,1,248,14,5,0,4))
hmMrpReconfig.setObjects(*((_E,_T),(_E,_t)))
if mibBuilder.loadTexts:hmMrpReconfig.setStatus(_A)
hmRpcReconfig=NotificationType((1,3,6,1,4,1,248,14,5,0,5))
hmRpcReconfig.setObjects(*((_E,_Z),(_E,_a),(_E,_u)))
if mibBuilder.loadTexts:hmRpcReconfig.setStatus(_A)
hmSrmReconfig=NotificationType((1,3,6,1,4,1,248,14,5,0,6))
hmSrmReconfig.setObjects(*((_E,_b),(_E,_v),(_E,_w)))
if mibBuilder.loadTexts:hmSrmReconfig.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hmRingRedundancy':hmRingRedundancy,'hmRingRedundancyEvent':hmRingRedundancyEvent,'hmRingRedReconfig':hmRingRedReconfig,'hmRingCplReconfig':hmRingCplReconfig,'hmRingRedConfigChanged':hmRingRedConfigChanged,'hmMrpReconfig':hmMrpReconfig,'hmRpcReconfig':hmRpcReconfig,'hmSrmReconfig':hmSrmReconfig,'hmRingRedTable':hmRingRedTable,'hmRingRedEntry':hmRingRedEntry,_c:hmRingRedPrimGroupID,_d:hmRingRedPrimIfIndex,'hmRingRedPrimIfOpState':hmRingRedPrimIfOpState,'hmRingRedRedGroupID':hmRingRedRedGroupID,'hmRingRedRedIfIndex':hmRingRedRedIfIndex,'hmRingRedRedIfOpState':hmRingRedRedIfOpState,_o:hmRingRedOperState,'hmRingRedMode':hmRingRedMode,_s:hmRingRedConfigOperState,'hmRingRedRecoveryDelay':hmRingRedRecoveryDelay,'hmRingCouplingTable':hmRingCouplingTable,'hmRingCouplingEntry':hmRingCouplingEntry,_j:hmRingCplInterconnGroupID,_k:hmRingCplInterconnIfIndex,_p:hmRingCplInterconnIfOpState,'hmRingCplControlGroupID':hmRingCplControlGroupID,'hmRingCplControlIfIndex':hmRingCplControlIfIndex,'hmRingCplControlIfOpState':hmRingCplControlIfOpState,'hmRingCplControlMode':hmRingCplControlMode,_r:hmRingCplPartnerIpAddr,'hmRingCplPartnerInterconnGroupID':hmRingCplPartnerInterconnGroupID,'hmRingCplPartnerInterconnIfIndex':hmRingCplPartnerInterconnIfIndex,_q:hmRingCplPartnerInterconnIfOpState,'hmRingCplOperState':hmRingCplOperState,'hmRingCplMode':hmRingCplMode,'hmRingCplRowStatus':hmRingCplRowStatus,'hmRingCplConfigOperState':hmRingCplConfigOperState,'hmRingCplCouplingLinks':hmRingCplCouplingLinks,'hmRingCplExtendedDiag':hmRingCplExtendedDiag,'hmRingCplNetCoupling':hmRingCplNetCoupling,'hmRingCplConfigSource':hmRingCplConfigSource,'hmMrpTable':hmMrpTable,'hmMrpEntry':hmMrpEntry,_T:hmMrpDomainID,'hmMrpRingport1GroupID':hmMrpRingport1GroupID,'hmMrpRingport1IfIndex':hmMrpRingport1IfIndex,'hmMrpRingport1OperState':hmMrpRingport1OperState,'hmMrpRingport2GroupID':hmMrpRingport2GroupID,'hmMrpRingport2IfIndex':hmMrpRingport2IfIndex,'hmMrpRingport2OperState':hmMrpRingport2OperState,'hmMrpVlanID':hmMrpVlanID,'hmMrpExpectedRole':hmMrpExpectedRole,'hmMrpMRCLinkDownInterval':hmMrpMRCLinkDownInterval,'hmMrpMRCLinkUpInterval':hmMrpMRCLinkUpInterval,'hmMrpMRCLinkChangeCount':hmMrpMRCLinkChangeCount,'hmMrpMRCBlockedSupported':hmMrpMRCBlockedSupported,'hmMrpMRMPriority':hmMrpMRMPriority,'hmMrpMRMTopologyChangeInterval':hmMrpMRMTopologyChangeInterval,'hmMrpMRMTopologyChangeRepeatCount':hmMrpMRMTopologyChangeRepeatCount,'hmMrpMRMShortTestInterval':hmMrpMRMShortTestInterval,'hmMrpMRMDefaultTestInterval':hmMrpMRMDefaultTestInterval,'hmMrpMRMTestMonitoringCount':hmMrpMRMTestMonitoringCount,'hmMrpMRMNonBlockingMRCSupported':hmMrpMRMNonBlockingMRCSupported,'hmMrpMRMTestMonitoringExtendedCount':hmMrpMRMTestMonitoringExtendedCount,'hmMrpMRMReactOnLinkChange':hmMrpMRMReactOnLinkChange,'hmMrpMRMCheckMediaRedundancy':hmMrpMRMCheckMediaRedundancy,'hmMrpMRMRealRoleState':hmMrpMRMRealRoleState,_t:hmMrpMRMRealRingState,'hmMrpRowStatus':hmMrpRowStatus,'hmMrpRedOperState':hmMrpRedOperState,'hmMrpConfigOperState':hmMrpConfigOperState,'hmMrpDomainName':hmMrpDomainName,'hmMrpMRMRecoveryDelay':hmMrpMRMRecoveryDelay,'hmRpcTable':hmRpcTable,'hmRpcEntry':hmRpcEntry,_Z:hmRpcRingProtocol,_a:hmRpcRingID,'hmRpcRingName':hmRpcRingName,'hmRpcRingport1GroupID':hmRpcRingport1GroupID,'hmRpcRingport1IfIndex':hmRpcRingport1IfIndex,'hmRpcRingport1OperState':hmRpcRingport1OperState,'hmRpcRingport2GroupID':hmRpcRingport2GroupID,'hmRpcRingport2IfIndex':hmRpcRingport2IfIndex,'hmRpcRingport2OperState':hmRpcRingport2OperState,'hmRpcVlanID':hmRpcVlanID,'hmRpcAdminState':hmRpcAdminState,'hmRpcOperState':hmRpcOperState,_u:hmRpcRingOperState,'hmRpcRedundancyOperState':hmRpcRedundancyOperState,'hmRpcConfigOperState':hmRpcConfigOperState,'hmRpcRowStatus':hmRpcRowStatus,'hmRpcNodes':hmRpcNodes,'hmRpcRoundTripDelay':hmRpcRoundTripDelay,'hmMultiHiperRing':hmMultiHiperRing,'hmSrmMaxInstances':hmSrmMaxInstances,'hmSrmTable':hmSrmTable,'hmSrmEntry':hmSrmEntry,_b:hmSrmRingID,_v:hmSrmRingProtocol,'hmSrmRingName':hmSrmRingName,'hmSrmRingport1GroupID':hmSrmRingport1GroupID,'hmSrmRingport1IfIndex':hmSrmRingport1IfIndex,'hmSrmRingport1OperState':hmSrmRingport1OperState,'hmSrmVlanID':hmSrmVlanID,'hmSrmAdminState':hmSrmAdminState,'hmSrmOperState':hmSrmOperState,_w:hmSrmRingOperState,'hmSrmRedundancyOperState':hmSrmRedundancyOperState,'hmSrmConfigOperState':hmSrmConfigOperState,'hmSrmRowStatus':hmSrmRowStatus,'hmSrmNodes':hmSrmNodes,'hmSrmMRPDomainID':hmSrmMRPDomainID,'hmSrmPartnerMAC':hmSrmPartnerMAC,'hmSrmRecoveryDelay':hmSrmRecoveryDelay})