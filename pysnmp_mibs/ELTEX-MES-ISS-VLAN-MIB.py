_b='eltMesIssPortSecLastViolationAddress'
_a='eltMesIssVlanPortMacMapEntry'
_Z='eltMesIssVlanPortEntry'
_Y='eltMesIssVoiceVlanOUIPrefix'
_X='eltMesIssMacBasedVlanMacMask'
_W='eltMesIssMacBasedVlanMacAddress'
_V='eltMesIssMacBasedVlanPortGroupId'
_U='eltMesIssVlanFdbPortMacAddress'
_T='eltMesIssVlanFdbPortVlanId'
_S='DisplayString'
_R='Unsigned32'
_Q='fsDot1qVlanContextId'
_P='ARICENTQ-BRIDGE-MIB'
_O='OctetString'
_N='deprecated'
_M='dot1qVlanIndex'
_L='VlanIndex'
_K='Q-BRIDGE-MIB'
_J='read-create'
_I='read-only'
_H='ifIndex'
_G='IF-MIB'
_F='not-accessible'
_E='Integer32'
_D='TruthValue'
_C='ELTEX-MES-ISS-VLAN-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1qFutureVlanPortEntry,dot1qFutureVlanPortMacMapEntry=mibBuilder.importSymbols('ARICENT-VLAN-MIB','dot1qFutureVlanPortEntry','dot1qFutureVlanPortMacMapEntry')
fsDot1qVlanContextId,=mibBuilder.importSymbols(_P,_Q)
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
ifIndex,=mibBuilder.importSymbols(_G,_H)
VlanIndex,dot1qVlanIndex=mibBuilder.importSymbols(_K,_L,_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_R,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_S,'MacAddress','PhysAddress','RowStatus','TextualConvention',_D)
eltMesIssVlanMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,3))
if mibBuilder.loadTexts:eltMesIssVlanMIB.setRevisions(('2023-02-15 00:00','2022-12-06 00:00','2022-10-10 00:00','2022-08-05 00:00','2021-06-29 00:00','2019-12-12 00:00','2018-12-08 00:00'))
class EltMesIssPortSecurityMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('disabled',1),('dynamic',2),('secure-permanent',3),('secure-delete-on-reset',4)))
_EltMesIssVlanObjects_ObjectIdentity=ObjectIdentity
eltMesIssVlanObjects=_EltMesIssVlanObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,3,1))
_EltMesIssVlanGlobals_ObjectIdentity=ObjectIdentity
eltMesIssVlanGlobals=_EltMesIssVlanGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,139,3,1,1))
_EltMesIssVlanFdbPortTable_Object=MibTable
eltMesIssVlanFdbPortTable=_EltMesIssVlanFdbPortTable_Object((1,3,6,1,4,1,35265,1,139,3,1,1,1))
if mibBuilder.loadTexts:eltMesIssVlanFdbPortTable.setStatus(_A)
_EltMesIssVlanFdbPortEntry_Object=MibTableRow
eltMesIssVlanFdbPortEntry=_EltMesIssVlanFdbPortEntry_Object((1,3,6,1,4,1,35265,1,139,3,1,1,1,1))
eltMesIssVlanFdbPortEntry.setIndexNames((0,_G,_H),(0,_C,_T),(0,_C,_U))
if mibBuilder.loadTexts:eltMesIssVlanFdbPortEntry.setStatus(_A)
_EltMesIssVlanFdbPortVlanId_Type=VlanIndex
_EltMesIssVlanFdbPortVlanId_Object=MibTableColumn
eltMesIssVlanFdbPortVlanId=_EltMesIssVlanFdbPortVlanId_Object((1,3,6,1,4,1,35265,1,139,3,1,1,1,1,1),_EltMesIssVlanFdbPortVlanId_Type())
eltMesIssVlanFdbPortVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:eltMesIssVlanFdbPortVlanId.setStatus(_A)
_EltMesIssVlanFdbPortMacAddress_Type=MacAddress
_EltMesIssVlanFdbPortMacAddress_Object=MibTableColumn
eltMesIssVlanFdbPortMacAddress=_EltMesIssVlanFdbPortMacAddress_Object((1,3,6,1,4,1,35265,1,139,3,1,1,1,1,2),_EltMesIssVlanFdbPortMacAddress_Type())
eltMesIssVlanFdbPortMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:eltMesIssVlanFdbPortMacAddress.setStatus(_A)
class _EltMesIssVlanFdbPortEntryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('invalid',2),('learned',3),('self',4),('mgmt',5)))
_EltMesIssVlanFdbPortEntryStatus_Type.__name__=_E
_EltMesIssVlanFdbPortEntryStatus_Object=MibTableColumn
eltMesIssVlanFdbPortEntryStatus=_EltMesIssVlanFdbPortEntryStatus_Object((1,3,6,1,4,1,35265,1,139,3,1,1,1,1,3),_EltMesIssVlanFdbPortEntryStatus_Type())
eltMesIssVlanFdbPortEntryStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:eltMesIssVlanFdbPortEntryStatus.setStatus(_A)
class _EltMesIssVoiceVlanGlobalVlanIndex_Type(VlanIndex):defaultValue=0
_EltMesIssVoiceVlanGlobalVlanIndex_Type.__name__=_L
_EltMesIssVoiceVlanGlobalVlanIndex_Object=MibScalar
eltMesIssVoiceVlanGlobalVlanIndex=_EltMesIssVoiceVlanGlobalVlanIndex_Object((1,3,6,1,4,1,35265,1,139,3,1,1,2),_EltMesIssVoiceVlanGlobalVlanIndex_Type())
eltMesIssVoiceVlanGlobalVlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssVoiceVlanGlobalVlanIndex.setStatus(_A)
_EltMesIssVlanPortConfig_ObjectIdentity=ObjectIdentity
eltMesIssVlanPortConfig=_EltMesIssVlanPortConfig_ObjectIdentity((1,3,6,1,4,1,35265,1,139,3,1,2))
_EltMesIssVlanPortTable_Object=MibTable
eltMesIssVlanPortTable=_EltMesIssVlanPortTable_Object((1,3,6,1,4,1,35265,1,139,3,1,2,1))
if mibBuilder.loadTexts:eltMesIssVlanPortTable.setStatus(_A)
_EltMesIssVlanPortEntry_Object=MibTableRow
eltMesIssVlanPortEntry=_EltMesIssVlanPortEntry_Object((1,3,6,1,4,1,35265,1,139,3,1,2,1,1))
if mibBuilder.loadTexts:eltMesIssVlanPortEntry.setStatus(_A)
class _EltMesIssVlanDot1qTunnelStatus_Type(TruthValue):defaultValue=2
_EltMesIssVlanDot1qTunnelStatus_Type.__name__=_D
_EltMesIssVlanDot1qTunnelStatus_Object=MibTableColumn
eltMesIssVlanDot1qTunnelStatus=_EltMesIssVlanDot1qTunnelStatus_Object((1,3,6,1,4,1,35265,1,139,3,1,2,1,1,1),_EltMesIssVlanDot1qTunnelStatus_Type())
eltMesIssVlanDot1qTunnelStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssVlanDot1qTunnelStatus.setStatus(_A)
_EltMesIssVlanPortSecurityMacLimit_Type=Unsigned32
_EltMesIssVlanPortSecurityMacLimit_Object=MibTableColumn
eltMesIssVlanPortSecurityMacLimit=_EltMesIssVlanPortSecurityMacLimit_Object((1,3,6,1,4,1,35265,1,139,3,1,2,1,1,2),_EltMesIssVlanPortSecurityMacLimit_Type())
eltMesIssVlanPortSecurityMacLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssVlanPortSecurityMacLimit.setStatus(_A)
class _EltMesIssVlanPortSecurityStatus_Type(TruthValue):defaultValue=2
_EltMesIssVlanPortSecurityStatus_Type.__name__=_D
_EltMesIssVlanPortSecurityStatus_Object=MibTableColumn
eltMesIssVlanPortSecurityStatus=_EltMesIssVlanPortSecurityStatus_Object((1,3,6,1,4,1,35265,1,139,3,1,2,1,1,3),_EltMesIssVlanPortSecurityStatus_Type())
eltMesIssVlanPortSecurityStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssVlanPortSecurityStatus.setStatus(_A)
_EltMesIssVlanPortSecurityMode_Type=EltMesIssPortSecurityMode
_EltMesIssVlanPortSecurityMode_Object=MibTableColumn
eltMesIssVlanPortSecurityMode=_EltMesIssVlanPortSecurityMode_Object((1,3,6,1,4,1,35265,1,139,3,1,2,1,1,4),_EltMesIssVlanPortSecurityMode_Type())
eltMesIssVlanPortSecurityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssVlanPortSecurityMode.setStatus(_A)
class _EltMesIssVlanPortDefaultVlanTagged_Type(TruthValue):defaultValue=2
_EltMesIssVlanPortDefaultVlanTagged_Type.__name__=_D
_EltMesIssVlanPortDefaultVlanTagged_Object=MibTableColumn
eltMesIssVlanPortDefaultVlanTagged=_EltMesIssVlanPortDefaultVlanTagged_Object((1,3,6,1,4,1,35265,1,139,3,1,2,1,1,5),_EltMesIssVlanPortDefaultVlanTagged_Type())
eltMesIssVlanPortDefaultVlanTagged.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssVlanPortDefaultVlanTagged.setStatus(_A)
class _EltMesIssVlanPortMvrVlanId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_EltMesIssVlanPortMvrVlanId_Type.__name__=_R
_EltMesIssVlanPortMvrVlanId_Object=MibTableColumn
eltMesIssVlanPortMvrVlanId=_EltMesIssVlanPortMvrVlanId_Object((1,3,6,1,4,1,35265,1,139,3,1,2,1,1,6),_EltMesIssVlanPortMvrVlanId_Type())
eltMesIssVlanPortMvrVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssVlanPortMvrVlanId.setStatus(_A)
class _EltMesIssVlanPortMvrVlanTagged_Type(TruthValue):defaultValue=2
_EltMesIssVlanPortMvrVlanTagged_Type.__name__=_D
_EltMesIssVlanPortMvrVlanTagged_Object=MibTableColumn
eltMesIssVlanPortMvrVlanTagged=_EltMesIssVlanPortMvrVlanTagged_Object((1,3,6,1,4,1,35265,1,139,3,1,2,1,1,7),_EltMesIssVlanPortMvrVlanTagged_Type())
eltMesIssVlanPortMvrVlanTagged.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssVlanPortMvrVlanTagged.setStatus(_A)
class _EltMesIssVlanPortDefaultVlanForbidden_Type(TruthValue):defaultValue=2
_EltMesIssVlanPortDefaultVlanForbidden_Type.__name__=_D
_EltMesIssVlanPortDefaultVlanForbidden_Object=MibTableColumn
eltMesIssVlanPortDefaultVlanForbidden=_EltMesIssVlanPortDefaultVlanForbidden_Object((1,3,6,1,4,1,35265,1,139,3,1,2,1,1,8),_EltMesIssVlanPortDefaultVlanForbidden_Type())
eltMesIssVlanPortDefaultVlanForbidden.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssVlanPortDefaultVlanForbidden.setStatus(_A)
class _EltMesIssVlanPortEgressFiltering_Type(TruthValue):defaultValue=1
_EltMesIssVlanPortEgressFiltering_Type.__name__=_D
_EltMesIssVlanPortEgressFiltering_Object=MibTableColumn
eltMesIssVlanPortEgressFiltering=_EltMesIssVlanPortEgressFiltering_Object((1,3,6,1,4,1,35265,1,139,3,1,2,1,1,9),_EltMesIssVlanPortEgressFiltering_Type())
eltMesIssVlanPortEgressFiltering.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssVlanPortEgressFiltering.setStatus(_A)
_EltMesIssVlanPortMacMapTable_Object=MibTable
eltMesIssVlanPortMacMapTable=_EltMesIssVlanPortMacMapTable_Object((1,3,6,1,4,1,35265,1,139,3,1,2,2))
if mibBuilder.loadTexts:eltMesIssVlanPortMacMapTable.setStatus(_N)
_EltMesIssVlanPortMacMapEntry_Object=MibTableRow
eltMesIssVlanPortMacMapEntry=_EltMesIssVlanPortMacMapEntry_Object((1,3,6,1,4,1,35265,1,139,3,1,2,2,1))
if mibBuilder.loadTexts:eltMesIssVlanPortMacMapEntry.setStatus(_N)
_EltMesIssVlanPortMacMapMask_Type=MacAddress
_EltMesIssVlanPortMacMapMask_Object=MibTableColumn
eltMesIssVlanPortMacMapMask=_EltMesIssVlanPortMacMapMask_Object((1,3,6,1,4,1,35265,1,139,3,1,2,2,1,1),_EltMesIssVlanPortMacMapMask_Type())
eltMesIssVlanPortMacMapMask.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssVlanPortMacMapMask.setStatus(_N)
_EltMesIssMacBasedVlanPortTable_Object=MibTable
eltMesIssMacBasedVlanPortTable=_EltMesIssMacBasedVlanPortTable_Object((1,3,6,1,4,1,35265,1,139,3,1,2,3))
if mibBuilder.loadTexts:eltMesIssMacBasedVlanPortTable.setStatus(_A)
_EltMesIssMacBasedVlanPortEntry_Object=MibTableRow
eltMesIssMacBasedVlanPortEntry=_EltMesIssMacBasedVlanPortEntry_Object((1,3,6,1,4,1,35265,1,139,3,1,2,3,1))
eltMesIssMacBasedVlanPortEntry.setIndexNames((0,_G,_H),(0,_C,_V))
if mibBuilder.loadTexts:eltMesIssMacBasedVlanPortEntry.setStatus(_A)
class _EltMesIssMacBasedVlanPortGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EltMesIssMacBasedVlanPortGroupId_Type.__name__=_E
_EltMesIssMacBasedVlanPortGroupId_Object=MibTableColumn
eltMesIssMacBasedVlanPortGroupId=_EltMesIssMacBasedVlanPortGroupId_Object((1,3,6,1,4,1,35265,1,139,3,1,2,3,1,1),_EltMesIssMacBasedVlanPortGroupId_Type())
eltMesIssMacBasedVlanPortGroupId.setMaxAccess(_F)
if mibBuilder.loadTexts:eltMesIssMacBasedVlanPortGroupId.setStatus(_A)
_EltMesIssMacBasedVlanPortGroupVid_Type=VlanIndex
_EltMesIssMacBasedVlanPortGroupVid_Object=MibTableColumn
eltMesIssMacBasedVlanPortGroupVid=_EltMesIssMacBasedVlanPortGroupVid_Object((1,3,6,1,4,1,35265,1,139,3,1,2,3,1,2),_EltMesIssMacBasedVlanPortGroupVid_Type())
eltMesIssMacBasedVlanPortGroupVid.setMaxAccess(_J)
if mibBuilder.loadTexts:eltMesIssMacBasedVlanPortGroupVid.setStatus(_A)
class _EltMesIssMacBasedVlanPortMcastBcastOption_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allow',1),('suppress',2)))
_EltMesIssMacBasedVlanPortMcastBcastOption_Type.__name__=_E
_EltMesIssMacBasedVlanPortMcastBcastOption_Object=MibTableColumn
eltMesIssMacBasedVlanPortMcastBcastOption=_EltMesIssMacBasedVlanPortMcastBcastOption_Object((1,3,6,1,4,1,35265,1,139,3,1,2,3,1,3),_EltMesIssMacBasedVlanPortMcastBcastOption_Type())
eltMesIssMacBasedVlanPortMcastBcastOption.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssMacBasedVlanPortMcastBcastOption.setStatus(_A)
_EltMesIssMacBasedVlanPortRowStatus_Type=RowStatus
_EltMesIssMacBasedVlanPortRowStatus_Object=MibTableColumn
eltMesIssMacBasedVlanPortRowStatus=_EltMesIssMacBasedVlanPortRowStatus_Object((1,3,6,1,4,1,35265,1,139,3,1,2,3,1,4),_EltMesIssMacBasedVlanPortRowStatus_Type())
eltMesIssMacBasedVlanPortRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:eltMesIssMacBasedVlanPortRowStatus.setStatus(_A)
_EltMesIssVoiceVlanPortTable_Object=MibTable
eltMesIssVoiceVlanPortTable=_EltMesIssVoiceVlanPortTable_Object((1,3,6,1,4,1,35265,1,139,3,1,2,4))
if mibBuilder.loadTexts:eltMesIssVoiceVlanPortTable.setStatus(_A)
_EltMesIssVoiceVlanPortEntry_Object=MibTableRow
eltMesIssVoiceVlanPortEntry=_EltMesIssVoiceVlanPortEntry_Object((1,3,6,1,4,1,35265,1,139,3,1,2,4,1))
eltMesIssVoiceVlanPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:eltMesIssVoiceVlanPortEntry.setStatus(_A)
class _EltMesIssVoiceVlanPortEnable_Type(TruthValue):defaultValue=2
_EltMesIssVoiceVlanPortEnable_Type.__name__=_D
_EltMesIssVoiceVlanPortEnable_Object=MibTableColumn
eltMesIssVoiceVlanPortEnable=_EltMesIssVoiceVlanPortEnable_Object((1,3,6,1,4,1,35265,1,139,3,1,2,4,1,1),_EltMesIssVoiceVlanPortEnable_Type())
eltMesIssVoiceVlanPortEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssVoiceVlanPortEnable.setStatus(_A)
class _EltMesIssVoiceVlanPortVlanIndex_Type(VlanIndex):defaultValue=0
_EltMesIssVoiceVlanPortVlanIndex_Type.__name__=_L
_EltMesIssVoiceVlanPortVlanIndex_Object=MibTableColumn
eltMesIssVoiceVlanPortVlanIndex=_EltMesIssVoiceVlanPortVlanIndex_Object((1,3,6,1,4,1,35265,1,139,3,1,2,4,1,2),_EltMesIssVoiceVlanPortVlanIndex_Type())
eltMesIssVoiceVlanPortVlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssVoiceVlanPortVlanIndex.setStatus(_A)
class _EltMesIssVoiceVlanPortAuthenticationBypass_Type(TruthValue):defaultValue=2
_EltMesIssVoiceVlanPortAuthenticationBypass_Type.__name__=_D
_EltMesIssVoiceVlanPortAuthenticationBypass_Object=MibTableColumn
eltMesIssVoiceVlanPortAuthenticationBypass=_EltMesIssVoiceVlanPortAuthenticationBypass_Object((1,3,6,1,4,1,35265,1,139,3,1,2,4,1,3),_EltMesIssVoiceVlanPortAuthenticationBypass_Type())
eltMesIssVoiceVlanPortAuthenticationBypass.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssVoiceVlanPortAuthenticationBypass.setStatus(_A)
_EltMesIssVlanConfig_ObjectIdentity=ObjectIdentity
eltMesIssVlanConfig=_EltMesIssVlanConfig_ObjectIdentity((1,3,6,1,4,1,35265,1,139,3,1,3))
_EltMesIssDot1qVlanStaticTable_Object=MibTable
eltMesIssDot1qVlanStaticTable=_EltMesIssDot1qVlanStaticTable_Object((1,3,6,1,4,1,35265,1,139,3,1,3,1))
if mibBuilder.loadTexts:eltMesIssDot1qVlanStaticTable.setStatus(_A)
_EltMesIssDot1qVlanStaticEntry_Object=MibTableRow
eltMesIssDot1qVlanStaticEntry=_EltMesIssDot1qVlanStaticEntry_Object((1,3,6,1,4,1,35265,1,139,3,1,3,1,1))
eltMesIssDot1qVlanStaticEntry.setIndexNames((0,_K,_M))
if mibBuilder.loadTexts:eltMesIssDot1qVlanStaticEntry.setStatus(_A)
class _EltMesIssDot1qVlanStaticCos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_EltMesIssDot1qVlanStaticCos_Type.__name__=_E
_EltMesIssDot1qVlanStaticCos_Object=MibTableColumn
eltMesIssDot1qVlanStaticCos=_EltMesIssDot1qVlanStaticCos_Object((1,3,6,1,4,1,35265,1,139,3,1,3,1,1,1),_EltMesIssDot1qVlanStaticCos_Type())
eltMesIssDot1qVlanStaticCos.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssDot1qVlanStaticCos.setStatus(_A)
_EltMesIssMacBasedVlanGroupTable_Object=MibTable
eltMesIssMacBasedVlanGroupTable=_EltMesIssMacBasedVlanGroupTable_Object((1,3,6,1,4,1,35265,1,139,3,1,3,2))
if mibBuilder.loadTexts:eltMesIssMacBasedVlanGroupTable.setStatus(_A)
_EltMesIssMacBasedVlanGroupEntry_Object=MibTableRow
eltMesIssMacBasedVlanGroupEntry=_EltMesIssMacBasedVlanGroupEntry_Object((1,3,6,1,4,1,35265,1,139,3,1,3,2,1))
eltMesIssMacBasedVlanGroupEntry.setIndexNames((0,_C,_W),(0,_C,_X))
if mibBuilder.loadTexts:eltMesIssMacBasedVlanGroupEntry.setStatus(_A)
_EltMesIssMacBasedVlanMacAddress_Type=MacAddress
_EltMesIssMacBasedVlanMacAddress_Object=MibTableColumn
eltMesIssMacBasedVlanMacAddress=_EltMesIssMacBasedVlanMacAddress_Object((1,3,6,1,4,1,35265,1,139,3,1,3,2,1,1),_EltMesIssMacBasedVlanMacAddress_Type())
eltMesIssMacBasedVlanMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:eltMesIssMacBasedVlanMacAddress.setStatus(_A)
_EltMesIssMacBasedVlanMacMask_Type=MacAddress
_EltMesIssMacBasedVlanMacMask_Object=MibTableColumn
eltMesIssMacBasedVlanMacMask=_EltMesIssMacBasedVlanMacMask_Object((1,3,6,1,4,1,35265,1,139,3,1,3,2,1,2),_EltMesIssMacBasedVlanMacMask_Type())
eltMesIssMacBasedVlanMacMask.setMaxAccess(_F)
if mibBuilder.loadTexts:eltMesIssMacBasedVlanMacMask.setStatus(_A)
class _EltMesIssMacBasedVlanGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EltMesIssMacBasedVlanGroupId_Type.__name__=_E
_EltMesIssMacBasedVlanGroupId_Object=MibTableColumn
eltMesIssMacBasedVlanGroupId=_EltMesIssMacBasedVlanGroupId_Object((1,3,6,1,4,1,35265,1,139,3,1,3,2,1,3),_EltMesIssMacBasedVlanGroupId_Type())
eltMesIssMacBasedVlanGroupId.setMaxAccess(_J)
if mibBuilder.loadTexts:eltMesIssMacBasedVlanGroupId.setStatus(_A)
_EltMesIssMacBasedVlanGroupRowStatus_Type=RowStatus
_EltMesIssMacBasedVlanGroupRowStatus_Object=MibTableColumn
eltMesIssMacBasedVlanGroupRowStatus=_EltMesIssMacBasedVlanGroupRowStatus_Object((1,3,6,1,4,1,35265,1,139,3,1,3,2,1,4),_EltMesIssMacBasedVlanGroupRowStatus_Type())
eltMesIssMacBasedVlanGroupRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:eltMesIssMacBasedVlanGroupRowStatus.setStatus(_A)
_EltMesIssVoiceVlanOUITable_Object=MibTable
eltMesIssVoiceVlanOUITable=_EltMesIssVoiceVlanOUITable_Object((1,3,6,1,4,1,35265,1,139,3,1,3,3))
if mibBuilder.loadTexts:eltMesIssVoiceVlanOUITable.setStatus(_A)
_EltMesIssVoiceVlanOUIEntry_Object=MibTableRow
eltMesIssVoiceVlanOUIEntry=_EltMesIssVoiceVlanOUIEntry_Object((1,3,6,1,4,1,35265,1,139,3,1,3,3,1))
eltMesIssVoiceVlanOUIEntry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:eltMesIssVoiceVlanOUIEntry.setStatus(_A)
class _EltMesIssVoiceVlanOUIPrefix_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_EltMesIssVoiceVlanOUIPrefix_Type.__name__=_O
_EltMesIssVoiceVlanOUIPrefix_Object=MibTableColumn
eltMesIssVoiceVlanOUIPrefix=_EltMesIssVoiceVlanOUIPrefix_Object((1,3,6,1,4,1,35265,1,139,3,1,3,3,1,1),_EltMesIssVoiceVlanOUIPrefix_Type())
eltMesIssVoiceVlanOUIPrefix.setMaxAccess(_F)
if mibBuilder.loadTexts:eltMesIssVoiceVlanOUIPrefix.setStatus(_A)
class _EltMesIssVoiceVlanOUIDescription_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EltMesIssVoiceVlanOUIDescription_Type.__name__=_S
_EltMesIssVoiceVlanOUIDescription_Object=MibTableColumn
eltMesIssVoiceVlanOUIDescription=_EltMesIssVoiceVlanOUIDescription_Object((1,3,6,1,4,1,35265,1,139,3,1,3,3,1,2),_EltMesIssVoiceVlanOUIDescription_Type())
eltMesIssVoiceVlanOUIDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssVoiceVlanOUIDescription.setStatus(_A)
_EltMesIssVoiceVlanOUIEntryRowStatus_Type=RowStatus
_EltMesIssVoiceVlanOUIEntryRowStatus_Object=MibTableColumn
eltMesIssVoiceVlanOUIEntryRowStatus=_EltMesIssVoiceVlanOUIEntryRowStatus_Object((1,3,6,1,4,1,35265,1,139,3,1,3,3,1,3),_EltMesIssVoiceVlanOUIEntryRowStatus_Type())
eltMesIssVoiceVlanOUIEntryRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:eltMesIssVoiceVlanOUIEntryRowStatus.setStatus(_A)
_EltMesIssVlanStatistics_ObjectIdentity=ObjectIdentity
eltMesIssVlanStatistics=_EltMesIssVlanStatistics_ObjectIdentity((1,3,6,1,4,1,35265,1,139,3,1,4))
_EltMesIssVlanCurrentTable_Object=MibTable
eltMesIssVlanCurrentTable=_EltMesIssVlanCurrentTable_Object((1,3,6,1,4,1,35265,1,139,3,1,4,1))
if mibBuilder.loadTexts:eltMesIssVlanCurrentTable.setStatus(_A)
_EltMesIssVlanCurrentEntry_Object=MibTableRow
eltMesIssVlanCurrentEntry=_EltMesIssVlanCurrentEntry_Object((1,3,6,1,4,1,35265,1,139,3,1,4,1,1))
eltMesIssVlanCurrentEntry.setIndexNames((0,_P,_Q),(0,_K,_M))
if mibBuilder.loadTexts:eltMesIssVlanCurrentEntry.setStatus(_A)
_EltMesIssVlanFdbId_Type=Unsigned32
_EltMesIssVlanFdbId_Object=MibTableColumn
eltMesIssVlanFdbId=_EltMesIssVlanFdbId_Object((1,3,6,1,4,1,35265,1,139,3,1,4,1,1,1),_EltMesIssVlanFdbId_Type())
eltMesIssVlanFdbId.setMaxAccess(_I)
if mibBuilder.loadTexts:eltMesIssVlanFdbId.setStatus(_A)
class _EltMesIssVlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('permanent',2),('dynamicGvrp',3)))
_EltMesIssVlanStatus_Type.__name__=_E
_EltMesIssVlanStatus_Object=MibTableColumn
eltMesIssVlanStatus=_EltMesIssVlanStatus_Object((1,3,6,1,4,1,35265,1,139,3,1,4,1,1,2),_EltMesIssVlanStatus_Type())
eltMesIssVlanStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:eltMesIssVlanStatus.setStatus(_A)
_EltMesIssVlanCreationTime_Type=TimeTicks
_EltMesIssVlanCreationTime_Object=MibTableColumn
eltMesIssVlanCreationTime=_EltMesIssVlanCreationTime_Object((1,3,6,1,4,1,35265,1,139,3,1,4,1,1,3),_EltMesIssVlanCreationTime_Type())
eltMesIssVlanCreationTime.setMaxAccess(_I)
if mibBuilder.loadTexts:eltMesIssVlanCreationTime.setStatus(_A)
_EltMesIssPortSecViolationObjects_ObjectIdentity=ObjectIdentity
eltMesIssPortSecViolationObjects=_EltMesIssPortSecViolationObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,3,1,5))
_EltMesIssPortSecLastViolationAddress_Type=MacAddress
_EltMesIssPortSecLastViolationAddress_Object=MibScalar
eltMesIssPortSecLastViolationAddress=_EltMesIssPortSecLastViolationAddress_Object((1,3,6,1,4,1,35265,1,139,3,1,5,1),_EltMesIssPortSecLastViolationAddress_Type())
eltMesIssPortSecLastViolationAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:eltMesIssPortSecLastViolationAddress.setStatus(_A)
_EltMesIssPortSecViolationNotifications_ObjectIdentity=ObjectIdentity
eltMesIssPortSecViolationNotifications=_EltMesIssPortSecViolationNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,139,3,1,6))
_EltMesIssPortSecViolationNotificationsPrefix_ObjectIdentity=ObjectIdentity
eltMesIssPortSecViolationNotificationsPrefix=_EltMesIssPortSecViolationNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,35265,1,139,3,1,6,0))
dot1qFutureVlanPortEntry.registerAugmentions((_C,_Z))
eltMesIssVlanPortEntry.setIndexNames(*dot1qFutureVlanPortEntry.getIndexNames())
dot1qFutureVlanPortMacMapEntry.registerAugmentions((_C,_a))
eltMesIssVlanPortMacMapEntry.setIndexNames(*dot1qFutureVlanPortMacMapEntry.getIndexNames())
eltMesIssVlanLastMacConstraintTrap=NotificationType((1,3,6,1,4,1,35265,1,139,3,1,6,0,1))
eltMesIssVlanLastMacConstraintTrap.setObjects(*((_C,_b),(_G,_H)))
if mibBuilder.loadTexts:eltMesIssVlanLastMacConstraintTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'EltMesIssPortSecurityMode':EltMesIssPortSecurityMode,'eltMesIssVlanMIB':eltMesIssVlanMIB,'eltMesIssVlanObjects':eltMesIssVlanObjects,'eltMesIssVlanGlobals':eltMesIssVlanGlobals,'eltMesIssVlanFdbPortTable':eltMesIssVlanFdbPortTable,'eltMesIssVlanFdbPortEntry':eltMesIssVlanFdbPortEntry,_T:eltMesIssVlanFdbPortVlanId,_U:eltMesIssVlanFdbPortMacAddress,'eltMesIssVlanFdbPortEntryStatus':eltMesIssVlanFdbPortEntryStatus,'eltMesIssVoiceVlanGlobalVlanIndex':eltMesIssVoiceVlanGlobalVlanIndex,'eltMesIssVlanPortConfig':eltMesIssVlanPortConfig,'eltMesIssVlanPortTable':eltMesIssVlanPortTable,_Z:eltMesIssVlanPortEntry,'eltMesIssVlanDot1qTunnelStatus':eltMesIssVlanDot1qTunnelStatus,'eltMesIssVlanPortSecurityMacLimit':eltMesIssVlanPortSecurityMacLimit,'eltMesIssVlanPortSecurityStatus':eltMesIssVlanPortSecurityStatus,'eltMesIssVlanPortSecurityMode':eltMesIssVlanPortSecurityMode,'eltMesIssVlanPortDefaultVlanTagged':eltMesIssVlanPortDefaultVlanTagged,'eltMesIssVlanPortMvrVlanId':eltMesIssVlanPortMvrVlanId,'eltMesIssVlanPortMvrVlanTagged':eltMesIssVlanPortMvrVlanTagged,'eltMesIssVlanPortDefaultVlanForbidden':eltMesIssVlanPortDefaultVlanForbidden,'eltMesIssVlanPortEgressFiltering':eltMesIssVlanPortEgressFiltering,'eltMesIssVlanPortMacMapTable':eltMesIssVlanPortMacMapTable,_a:eltMesIssVlanPortMacMapEntry,'eltMesIssVlanPortMacMapMask':eltMesIssVlanPortMacMapMask,'eltMesIssMacBasedVlanPortTable':eltMesIssMacBasedVlanPortTable,'eltMesIssMacBasedVlanPortEntry':eltMesIssMacBasedVlanPortEntry,_V:eltMesIssMacBasedVlanPortGroupId,'eltMesIssMacBasedVlanPortGroupVid':eltMesIssMacBasedVlanPortGroupVid,'eltMesIssMacBasedVlanPortMcastBcastOption':eltMesIssMacBasedVlanPortMcastBcastOption,'eltMesIssMacBasedVlanPortRowStatus':eltMesIssMacBasedVlanPortRowStatus,'eltMesIssVoiceVlanPortTable':eltMesIssVoiceVlanPortTable,'eltMesIssVoiceVlanPortEntry':eltMesIssVoiceVlanPortEntry,'eltMesIssVoiceVlanPortEnable':eltMesIssVoiceVlanPortEnable,'eltMesIssVoiceVlanPortVlanIndex':eltMesIssVoiceVlanPortVlanIndex,'eltMesIssVoiceVlanPortAuthenticationBypass':eltMesIssVoiceVlanPortAuthenticationBypass,'eltMesIssVlanConfig':eltMesIssVlanConfig,'eltMesIssDot1qVlanStaticTable':eltMesIssDot1qVlanStaticTable,'eltMesIssDot1qVlanStaticEntry':eltMesIssDot1qVlanStaticEntry,'eltMesIssDot1qVlanStaticCos':eltMesIssDot1qVlanStaticCos,'eltMesIssMacBasedVlanGroupTable':eltMesIssMacBasedVlanGroupTable,'eltMesIssMacBasedVlanGroupEntry':eltMesIssMacBasedVlanGroupEntry,_W:eltMesIssMacBasedVlanMacAddress,_X:eltMesIssMacBasedVlanMacMask,'eltMesIssMacBasedVlanGroupId':eltMesIssMacBasedVlanGroupId,'eltMesIssMacBasedVlanGroupRowStatus':eltMesIssMacBasedVlanGroupRowStatus,'eltMesIssVoiceVlanOUITable':eltMesIssVoiceVlanOUITable,'eltMesIssVoiceVlanOUIEntry':eltMesIssVoiceVlanOUIEntry,_Y:eltMesIssVoiceVlanOUIPrefix,'eltMesIssVoiceVlanOUIDescription':eltMesIssVoiceVlanOUIDescription,'eltMesIssVoiceVlanOUIEntryRowStatus':eltMesIssVoiceVlanOUIEntryRowStatus,'eltMesIssVlanStatistics':eltMesIssVlanStatistics,'eltMesIssVlanCurrentTable':eltMesIssVlanCurrentTable,'eltMesIssVlanCurrentEntry':eltMesIssVlanCurrentEntry,'eltMesIssVlanFdbId':eltMesIssVlanFdbId,'eltMesIssVlanStatus':eltMesIssVlanStatus,'eltMesIssVlanCreationTime':eltMesIssVlanCreationTime,'eltMesIssPortSecViolationObjects':eltMesIssPortSecViolationObjects,_b:eltMesIssPortSecLastViolationAddress,'eltMesIssPortSecViolationNotifications':eltMesIssPortSecViolationNotifications,'eltMesIssPortSecViolationNotificationsPrefix':eltMesIssPortSecViolationNotificationsPrefix,'eltMesIssVlanLastMacConstraintTrap':eltMesIssVlanLastMacConstraintTrap})