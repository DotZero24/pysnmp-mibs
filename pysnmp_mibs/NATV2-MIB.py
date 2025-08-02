_B9='natv2CGNInstanceLevelGroup'
_B8='natv2CGNDeviceLevelGroup'
_B7='natv2CGNNotificationGroup'
_B6='natv2NotificationSubscriberPortMappingEntriesHigh'
_B5='natv2NotificationPoolUsageHigh'
_B4='natv2NotificationPoolUsageLow'
_B3='natv2NotificationInstancePortMapEntriesHigh'
_B2='natv2NotificationInstanceAddressMapEntriesHigh'
_B1='natv2PortMapSubscriberIndex'
_B0='natv2PortMapInternalMappedAddress'
_A_='natv2PortMapInternalMappedAddressType'
_Az='natv2AddressMapSubscriberIndex'
_Ay='natv2AddressMapInternalMappedAddress'
_Ax='natv2AddressMapInternalMappedAddressType'
_Aw='natv2InstanceLimitSubscriberActives'
_Av='natv2InstanceSubscriberActiveLimitDrops'
_Au='natv2SubscriberNotificationInterval'
_At='natv2SubscriberThresholdPortMapEntriesHigh'
_As='natv2SubscriberLimitPortMapEntries'
_Ar='natv2SubscriberDiscontinuityTime'
_Aq='natv2SubscriberPortMapFailureDrops'
_Ap='natv2SubscriberAddressMapFailureDrops'
_Ao='natv2SubscriberAddressMapCreations'
_An='natv2SubscriberTranslations'
_Am='natv2SubscriberAddressMapEntries'
_Al='natv2SubscriberInternalPrefixLength'
_Ak='natv2SubscriberInternalPrefix'
_Aj='natv2SubscriberInternalPrefixType'
_Ai='natv2SubscriberInternalRealm'
_Ah='natv2PortMapExternalPoolIndex'
_Ag='natv2AddressMapExternalPoolIndex'
_Af='natv2PoolRangeEnd'
_Ae='natv2PoolRangeBegin'
_Ad='natv2PoolNotificationInterval'
_Ac='natv2PoolThresholdUsageHigh'
_Ab='natv2PoolThresholdUsageLow'
_Aa='natv2PoolDiscontinuityTime'
_AZ='natv2PoolPortMapFailureDrops'
_AY='natv2PoolAddressMapFailureDrops'
_AX='natv2PoolPortMapCreations'
_AW='natv2PoolAddressMapCreations'
_AV='natv2PoolPortMapEntries'
_AU='natv2PoolAddressMapEntries'
_AT='natv2PoolMaximumPort'
_AS='natv2PoolMinimumPort'
_AR='natv2PoolAddressType'
_AQ='natv2PoolRealm'
_AP='natv2InstancePoolingBehavior'
_AO='natv2PortMapInternalPort'
_AN='natv2PortMapInternalAddress'
_AM='natv2PortMapInternalAddressType'
_AL='natv2PortMapInternalRealm'
_AK='natv2AddressMapExternalAddress'
_AJ='natv2AddressMapExternalAddressType'
_AI='natv2AddressMapExternalRealm'
_AH='natv2ProtocolPortMapFailureDrops'
_AG='natv2ProtocolPortMapCreations'
_AF='natv2ProtocolTranslations'
_AE='natv2ProtocolPortMapEntries'
_AD='natv2InstanceLimitPendingFragments'
_AC='natv2InstanceLimitPortMapEntries'
_AB='natv2InstanceLimitAddressMapEntries'
_AA='natv2InstanceNotificationInterval'
_A9='natv2InstanceThresholdPortMapEntriesHigh'
_A8='natv2InstanceThresholdAddressMapEntriesHigh'
_A7='natv2InstanceDiscontinuityTime'
_A6='natv2InstanceOtherResourceFailureDrops'
_A5='natv2InstanceFragmentDrops'
_A4='natv2InstancePortMapFailureDrops'
_A3='natv2InstancePortMapEntryLimitDrops'
_A2='natv2InstanceAddressMapFailureDrops'
_A1='natv2InstanceAddressMapEntryLimitDrops'
_A0='natv2InstanceTranslations'
_z='natv2InstanceFragmentBehavior'
_y='natv2InstanceFilteringBehavior'
_x='natv2InstancePortMappingBehavior'
_w='natv2InstanceAlias'
_v='natv2PortMapExternalPort'
_u='natv2PortMapExternalAddress'
_t='natv2PortMapExternalAddressType'
_s='natv2PortMapExternalRealm'
_r='natv2PortMapProtocol'
_q='natv2PortMapInstanceIndex'
_p='natv2AddressMapRowIndex'
_o='natv2AddressMapInternalAddress'
_n='natv2AddressMapInternalAddressType'
_m='natv2AddressMapInternalRealm'
_l='natv2AddressMapInstanceIndex'
_k='natv2PoolRangeRowIndex'
_j='natv2PoolRangePoolIndex'
_i='natv2PoolRangeInstanceIndex'
_h='accessible-for-notify'
_g='Percent'
_f='natv2PoolIndex'
_e='natv2PoolInstanceIndex'
_d='natv2ProtocolNumber'
_c='natv2ProtocolInstanceIndex'
_b='addressAndPortDependent'
_a='addressDependent'
_Z='endpointIndependent'
_Y='natv2InstanceIndex'
_X='natv2SubscriberIndex'
_W='DisplayString'
_V='natv2PooledInstanceLevelGroup'
_U='natv2PooledNotificationGroup'
_T='natv2SubscriberPortMapCreations'
_S='natv2SubscriberPortMapEntries'
_R='natv2InstancePortMapCreations'
_Q='natv2InstanceAddressMapCreations'
_P='natv2InstancePortMapEntries'
_O='natv2InstanceAddressMapEntries'
_N='Seconds'
_M='InetAddress'
_L='natv2BasicInstanceLevelGroup'
_K='natv2BasicNotificationGroup'
_J='natv2PoolNotifiedPortMapProtocol'
_I='natv2PoolNotifiedPortMapEntries'
_H='SnmpAdminString'
_G='Unsigned32'
_F='Integer32'
_E='read-write'
_D='not-accessible'
_C='read-only'
_B='NATV2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressPrefixLength,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_M,'InetAddressPrefixLength','InetAddressType','InetPortNumber')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_W,'PhysAddress','TextualConvention','TimeStamp')
natv2MIB=ModuleIdentity((1,3,6,1,2,1,234))
if mibBuilder.loadTexts:natv2MIB.setRevisions(('2015-10-02 00:00',))
class ProtocolNumber(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class Natv2SubscriberIndex(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class Natv2SubscriberIndexOrZero(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295))
class Natv2InstanceIndex(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class Natv2PoolIndex(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class Natv2PoolIndexOrZero(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295))
_Natv2MIBNotifications_ObjectIdentity=ObjectIdentity
natv2MIBNotifications=_Natv2MIBNotifications_ObjectIdentity((1,3,6,1,2,1,234,0))
_Natv2MIBDeviceObjects_ObjectIdentity=ObjectIdentity
natv2MIBDeviceObjects=_Natv2MIBDeviceObjects_ObjectIdentity((1,3,6,1,2,1,234,1))
_Natv2SubscriberTable_Object=MibTable
natv2SubscriberTable=_Natv2SubscriberTable_Object((1,3,6,1,2,1,234,1,1))
if mibBuilder.loadTexts:natv2SubscriberTable.setStatus(_A)
_Natv2SubscriberEntry_Object=MibTableRow
natv2SubscriberEntry=_Natv2SubscriberEntry_Object((1,3,6,1,2,1,234,1,1,1))
natv2SubscriberEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:natv2SubscriberEntry.setStatus(_A)
_Natv2SubscriberIndex_Type=Natv2SubscriberIndex
_Natv2SubscriberIndex_Object=MibTableColumn
natv2SubscriberIndex=_Natv2SubscriberIndex_Object((1,3,6,1,2,1,234,1,1,1,1),_Natv2SubscriberIndex_Type())
natv2SubscriberIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:natv2SubscriberIndex.setStatus(_A)
class _Natv2SubscriberInternalRealm_Type(SnmpAdminString):defaultValue=OctetString('internal');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Natv2SubscriberInternalRealm_Type.__name__=_H
_Natv2SubscriberInternalRealm_Object=MibTableColumn
natv2SubscriberInternalRealm=_Natv2SubscriberInternalRealm_Object((1,3,6,1,2,1,234,1,1,1,2),_Natv2SubscriberInternalRealm_Type())
natv2SubscriberInternalRealm.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2SubscriberInternalRealm.setStatus(_A)
_Natv2SubscriberInternalPrefixType_Type=InetAddressType
_Natv2SubscriberInternalPrefixType_Object=MibTableColumn
natv2SubscriberInternalPrefixType=_Natv2SubscriberInternalPrefixType_Object((1,3,6,1,2,1,234,1,1,1,3),_Natv2SubscriberInternalPrefixType_Type())
natv2SubscriberInternalPrefixType.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2SubscriberInternalPrefixType.setStatus(_A)
_Natv2SubscriberInternalPrefix_Type=InetAddress
_Natv2SubscriberInternalPrefix_Object=MibTableColumn
natv2SubscriberInternalPrefix=_Natv2SubscriberInternalPrefix_Object((1,3,6,1,2,1,234,1,1,1,4),_Natv2SubscriberInternalPrefix_Type())
natv2SubscriberInternalPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2SubscriberInternalPrefix.setStatus(_A)
_Natv2SubscriberInternalPrefixLength_Type=InetAddressPrefixLength
_Natv2SubscriberInternalPrefixLength_Object=MibTableColumn
natv2SubscriberInternalPrefixLength=_Natv2SubscriberInternalPrefixLength_Object((1,3,6,1,2,1,234,1,1,1,5),_Natv2SubscriberInternalPrefixLength_Type())
natv2SubscriberInternalPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2SubscriberInternalPrefixLength.setStatus(_A)
_Natv2SubscriberAddressMapEntries_Type=Unsigned32
_Natv2SubscriberAddressMapEntries_Object=MibTableColumn
natv2SubscriberAddressMapEntries=_Natv2SubscriberAddressMapEntries_Object((1,3,6,1,2,1,234,1,1,1,6),_Natv2SubscriberAddressMapEntries_Type())
natv2SubscriberAddressMapEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2SubscriberAddressMapEntries.setStatus(_A)
_Natv2SubscriberPortMapEntries_Type=Unsigned32
_Natv2SubscriberPortMapEntries_Object=MibTableColumn
natv2SubscriberPortMapEntries=_Natv2SubscriberPortMapEntries_Object((1,3,6,1,2,1,234,1,1,1,7),_Natv2SubscriberPortMapEntries_Type())
natv2SubscriberPortMapEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2SubscriberPortMapEntries.setStatus(_A)
_Natv2SubscriberTranslations_Type=Counter64
_Natv2SubscriberTranslations_Object=MibTableColumn
natv2SubscriberTranslations=_Natv2SubscriberTranslations_Object((1,3,6,1,2,1,234,1,1,1,8),_Natv2SubscriberTranslations_Type())
natv2SubscriberTranslations.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2SubscriberTranslations.setStatus(_A)
_Natv2SubscriberAddressMapCreations_Type=Counter64
_Natv2SubscriberAddressMapCreations_Object=MibTableColumn
natv2SubscriberAddressMapCreations=_Natv2SubscriberAddressMapCreations_Object((1,3,6,1,2,1,234,1,1,1,9),_Natv2SubscriberAddressMapCreations_Type())
natv2SubscriberAddressMapCreations.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2SubscriberAddressMapCreations.setStatus(_A)
_Natv2SubscriberPortMapCreations_Type=Counter64
_Natv2SubscriberPortMapCreations_Object=MibTableColumn
natv2SubscriberPortMapCreations=_Natv2SubscriberPortMapCreations_Object((1,3,6,1,2,1,234,1,1,1,10),_Natv2SubscriberPortMapCreations_Type())
natv2SubscriberPortMapCreations.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2SubscriberPortMapCreations.setStatus(_A)
_Natv2SubscriberAddressMapFailureDrops_Type=Counter64
_Natv2SubscriberAddressMapFailureDrops_Object=MibTableColumn
natv2SubscriberAddressMapFailureDrops=_Natv2SubscriberAddressMapFailureDrops_Object((1,3,6,1,2,1,234,1,1,1,11),_Natv2SubscriberAddressMapFailureDrops_Type())
natv2SubscriberAddressMapFailureDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2SubscriberAddressMapFailureDrops.setStatus(_A)
_Natv2SubscriberPortMapFailureDrops_Type=Counter64
_Natv2SubscriberPortMapFailureDrops_Object=MibTableColumn
natv2SubscriberPortMapFailureDrops=_Natv2SubscriberPortMapFailureDrops_Object((1,3,6,1,2,1,234,1,1,1,12),_Natv2SubscriberPortMapFailureDrops_Type())
natv2SubscriberPortMapFailureDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2SubscriberPortMapFailureDrops.setStatus(_A)
_Natv2SubscriberDiscontinuityTime_Type=TimeStamp
_Natv2SubscriberDiscontinuityTime_Object=MibTableColumn
natv2SubscriberDiscontinuityTime=_Natv2SubscriberDiscontinuityTime_Object((1,3,6,1,2,1,234,1,1,1,14),_Natv2SubscriberDiscontinuityTime_Type())
natv2SubscriberDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2SubscriberDiscontinuityTime.setStatus(_A)
class _Natv2SubscriberLimitPortMapEntries_Type(Unsigned32):defaultValue=0
_Natv2SubscriberLimitPortMapEntries_Type.__name__=_G
_Natv2SubscriberLimitPortMapEntries_Object=MibTableColumn
natv2SubscriberLimitPortMapEntries=_Natv2SubscriberLimitPortMapEntries_Object((1,3,6,1,2,1,234,1,1,1,15),_Natv2SubscriberLimitPortMapEntries_Type())
natv2SubscriberLimitPortMapEntries.setMaxAccess(_E)
if mibBuilder.loadTexts:natv2SubscriberLimitPortMapEntries.setStatus(_A)
class _Natv2SubscriberThresholdPortMapEntriesHigh_Type(Integer32):defaultValue=-1
_Natv2SubscriberThresholdPortMapEntriesHigh_Type.__name__=_F
_Natv2SubscriberThresholdPortMapEntriesHigh_Object=MibTableColumn
natv2SubscriberThresholdPortMapEntriesHigh=_Natv2SubscriberThresholdPortMapEntriesHigh_Object((1,3,6,1,2,1,234,1,1,1,16),_Natv2SubscriberThresholdPortMapEntriesHigh_Type())
natv2SubscriberThresholdPortMapEntriesHigh.setMaxAccess(_E)
if mibBuilder.loadTexts:natv2SubscriberThresholdPortMapEntriesHigh.setStatus(_A)
class _Natv2SubscriberNotificationInterval_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_Natv2SubscriberNotificationInterval_Type.__name__=_G
_Natv2SubscriberNotificationInterval_Object=MibTableColumn
natv2SubscriberNotificationInterval=_Natv2SubscriberNotificationInterval_Object((1,3,6,1,2,1,234,1,1,1,17),_Natv2SubscriberNotificationInterval_Type())
natv2SubscriberNotificationInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:natv2SubscriberNotificationInterval.setStatus(_A)
if mibBuilder.loadTexts:natv2SubscriberNotificationInterval.setUnits(_N)
_Natv2MIBInstanceObjects_ObjectIdentity=ObjectIdentity
natv2MIBInstanceObjects=_Natv2MIBInstanceObjects_ObjectIdentity((1,3,6,1,2,1,234,2))
_Natv2InstanceTable_Object=MibTable
natv2InstanceTable=_Natv2InstanceTable_Object((1,3,6,1,2,1,234,2,1))
if mibBuilder.loadTexts:natv2InstanceTable.setStatus(_A)
_Natv2InstanceEntry_Object=MibTableRow
natv2InstanceEntry=_Natv2InstanceEntry_Object((1,3,6,1,2,1,234,2,1,1))
natv2InstanceEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:natv2InstanceEntry.setStatus(_A)
_Natv2InstanceIndex_Type=Natv2InstanceIndex
_Natv2InstanceIndex_Object=MibTableColumn
natv2InstanceIndex=_Natv2InstanceIndex_Object((1,3,6,1,2,1,234,2,1,1,1),_Natv2InstanceIndex_Type())
natv2InstanceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:natv2InstanceIndex.setStatus(_A)
class _Natv2InstanceAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Natv2InstanceAlias_Type.__name__=_W
_Natv2InstanceAlias_Object=MibTableColumn
natv2InstanceAlias=_Natv2InstanceAlias_Object((1,3,6,1,2,1,234,2,1,1,2),_Natv2InstanceAlias_Type())
natv2InstanceAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2InstanceAlias.setStatus(_A)
class _Natv2InstancePortMappingBehavior_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Z,0),(_a,1),(_b,2)))
_Natv2InstancePortMappingBehavior_Type.__name__=_F
_Natv2InstancePortMappingBehavior_Object=MibTableColumn
natv2InstancePortMappingBehavior=_Natv2InstancePortMappingBehavior_Object((1,3,6,1,2,1,234,2,1,1,3),_Natv2InstancePortMappingBehavior_Type())
natv2InstancePortMappingBehavior.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2InstancePortMappingBehavior.setStatus(_A)
class _Natv2InstanceFilteringBehavior_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Z,0),(_a,1),(_b,2)))
_Natv2InstanceFilteringBehavior_Type.__name__=_F
_Natv2InstanceFilteringBehavior_Object=MibTableColumn
natv2InstanceFilteringBehavior=_Natv2InstanceFilteringBehavior_Object((1,3,6,1,2,1,234,2,1,1,4),_Natv2InstanceFilteringBehavior_Type())
natv2InstanceFilteringBehavior.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2InstanceFilteringBehavior.setStatus(_A)
class _Natv2InstancePoolingBehavior_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('arbitrary',0),('paired',1)))
_Natv2InstancePoolingBehavior_Type.__name__=_F
_Natv2InstancePoolingBehavior_Object=MibTableColumn
natv2InstancePoolingBehavior=_Natv2InstancePoolingBehavior_Object((1,3,6,1,2,1,234,2,1,1,5),_Natv2InstancePoolingBehavior_Type())
natv2InstancePoolingBehavior.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2InstancePoolingBehavior.setStatus(_A)
class _Natv2InstanceFragmentBehavior_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('fragmentNone',0),('fragmentInOrder',1),('fragmentOutOfOrder',2)))
_Natv2InstanceFragmentBehavior_Type.__name__=_F
_Natv2InstanceFragmentBehavior_Object=MibTableColumn
natv2InstanceFragmentBehavior=_Natv2InstanceFragmentBehavior_Object((1,3,6,1,2,1,234,2,1,1,6),_Natv2InstanceFragmentBehavior_Type())
natv2InstanceFragmentBehavior.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2InstanceFragmentBehavior.setStatus(_A)
_Natv2InstanceAddressMapEntries_Type=Unsigned32
_Natv2InstanceAddressMapEntries_Object=MibTableColumn
natv2InstanceAddressMapEntries=_Natv2InstanceAddressMapEntries_Object((1,3,6,1,2,1,234,2,1,1,7),_Natv2InstanceAddressMapEntries_Type())
natv2InstanceAddressMapEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2InstanceAddressMapEntries.setStatus(_A)
_Natv2InstancePortMapEntries_Type=Unsigned32
_Natv2InstancePortMapEntries_Object=MibTableColumn
natv2InstancePortMapEntries=_Natv2InstancePortMapEntries_Object((1,3,6,1,2,1,234,2,1,1,8),_Natv2InstancePortMapEntries_Type())
natv2InstancePortMapEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2InstancePortMapEntries.setStatus(_A)
_Natv2InstanceTranslations_Type=Counter64
_Natv2InstanceTranslations_Object=MibTableColumn
natv2InstanceTranslations=_Natv2InstanceTranslations_Object((1,3,6,1,2,1,234,2,1,1,9),_Natv2InstanceTranslations_Type())
natv2InstanceTranslations.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2InstanceTranslations.setStatus(_A)
_Natv2InstanceAddressMapCreations_Type=Counter64
_Natv2InstanceAddressMapCreations_Object=MibTableColumn
natv2InstanceAddressMapCreations=_Natv2InstanceAddressMapCreations_Object((1,3,6,1,2,1,234,2,1,1,10),_Natv2InstanceAddressMapCreations_Type())
natv2InstanceAddressMapCreations.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2InstanceAddressMapCreations.setStatus(_A)
_Natv2InstancePortMapCreations_Type=Counter64
_Natv2InstancePortMapCreations_Object=MibTableColumn
natv2InstancePortMapCreations=_Natv2InstancePortMapCreations_Object((1,3,6,1,2,1,234,2,1,1,11),_Natv2InstancePortMapCreations_Type())
natv2InstancePortMapCreations.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2InstancePortMapCreations.setStatus(_A)
_Natv2InstanceAddressMapEntryLimitDrops_Type=Counter64
_Natv2InstanceAddressMapEntryLimitDrops_Object=MibTableColumn
natv2InstanceAddressMapEntryLimitDrops=_Natv2InstanceAddressMapEntryLimitDrops_Object((1,3,6,1,2,1,234,2,1,1,12),_Natv2InstanceAddressMapEntryLimitDrops_Type())
natv2InstanceAddressMapEntryLimitDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2InstanceAddressMapEntryLimitDrops.setStatus(_A)
_Natv2InstancePortMapEntryLimitDrops_Type=Counter64
_Natv2InstancePortMapEntryLimitDrops_Object=MibTableColumn
natv2InstancePortMapEntryLimitDrops=_Natv2InstancePortMapEntryLimitDrops_Object((1,3,6,1,2,1,234,2,1,1,13),_Natv2InstancePortMapEntryLimitDrops_Type())
natv2InstancePortMapEntryLimitDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2InstancePortMapEntryLimitDrops.setStatus(_A)
_Natv2InstanceSubscriberActiveLimitDrops_Type=Counter64
_Natv2InstanceSubscriberActiveLimitDrops_Object=MibTableColumn
natv2InstanceSubscriberActiveLimitDrops=_Natv2InstanceSubscriberActiveLimitDrops_Object((1,3,6,1,2,1,234,2,1,1,14),_Natv2InstanceSubscriberActiveLimitDrops_Type())
natv2InstanceSubscriberActiveLimitDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2InstanceSubscriberActiveLimitDrops.setStatus(_A)
_Natv2InstanceAddressMapFailureDrops_Type=Counter64
_Natv2InstanceAddressMapFailureDrops_Object=MibTableColumn
natv2InstanceAddressMapFailureDrops=_Natv2InstanceAddressMapFailureDrops_Object((1,3,6,1,2,1,234,2,1,1,15),_Natv2InstanceAddressMapFailureDrops_Type())
natv2InstanceAddressMapFailureDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2InstanceAddressMapFailureDrops.setStatus(_A)
_Natv2InstancePortMapFailureDrops_Type=Counter64
_Natv2InstancePortMapFailureDrops_Object=MibTableColumn
natv2InstancePortMapFailureDrops=_Natv2InstancePortMapFailureDrops_Object((1,3,6,1,2,1,234,2,1,1,16),_Natv2InstancePortMapFailureDrops_Type())
natv2InstancePortMapFailureDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2InstancePortMapFailureDrops.setStatus(_A)
_Natv2InstanceFragmentDrops_Type=Counter64
_Natv2InstanceFragmentDrops_Object=MibTableColumn
natv2InstanceFragmentDrops=_Natv2InstanceFragmentDrops_Object((1,3,6,1,2,1,234,2,1,1,17),_Natv2InstanceFragmentDrops_Type())
natv2InstanceFragmentDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2InstanceFragmentDrops.setStatus(_A)
_Natv2InstanceOtherResourceFailureDrops_Type=Counter64
_Natv2InstanceOtherResourceFailureDrops_Object=MibTableColumn
natv2InstanceOtherResourceFailureDrops=_Natv2InstanceOtherResourceFailureDrops_Object((1,3,6,1,2,1,234,2,1,1,18),_Natv2InstanceOtherResourceFailureDrops_Type())
natv2InstanceOtherResourceFailureDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2InstanceOtherResourceFailureDrops.setStatus(_A)
_Natv2InstanceDiscontinuityTime_Type=TimeStamp
_Natv2InstanceDiscontinuityTime_Object=MibTableColumn
natv2InstanceDiscontinuityTime=_Natv2InstanceDiscontinuityTime_Object((1,3,6,1,2,1,234,2,1,1,19),_Natv2InstanceDiscontinuityTime_Type())
natv2InstanceDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2InstanceDiscontinuityTime.setStatus(_A)
class _Natv2InstanceThresholdAddressMapEntriesHigh_Type(Integer32):defaultValue=-1
_Natv2InstanceThresholdAddressMapEntriesHigh_Type.__name__=_F
_Natv2InstanceThresholdAddressMapEntriesHigh_Object=MibTableColumn
natv2InstanceThresholdAddressMapEntriesHigh=_Natv2InstanceThresholdAddressMapEntriesHigh_Object((1,3,6,1,2,1,234,2,1,1,20),_Natv2InstanceThresholdAddressMapEntriesHigh_Type())
natv2InstanceThresholdAddressMapEntriesHigh.setMaxAccess(_E)
if mibBuilder.loadTexts:natv2InstanceThresholdAddressMapEntriesHigh.setStatus(_A)
class _Natv2InstanceThresholdPortMapEntriesHigh_Type(Integer32):defaultValue=-1
_Natv2InstanceThresholdPortMapEntriesHigh_Type.__name__=_F
_Natv2InstanceThresholdPortMapEntriesHigh_Object=MibTableColumn
natv2InstanceThresholdPortMapEntriesHigh=_Natv2InstanceThresholdPortMapEntriesHigh_Object((1,3,6,1,2,1,234,2,1,1,21),_Natv2InstanceThresholdPortMapEntriesHigh_Type())
natv2InstanceThresholdPortMapEntriesHigh.setMaxAccess(_E)
if mibBuilder.loadTexts:natv2InstanceThresholdPortMapEntriesHigh.setStatus(_A)
class _Natv2InstanceNotificationInterval_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_Natv2InstanceNotificationInterval_Type.__name__=_G
_Natv2InstanceNotificationInterval_Object=MibTableColumn
natv2InstanceNotificationInterval=_Natv2InstanceNotificationInterval_Object((1,3,6,1,2,1,234,2,1,1,22),_Natv2InstanceNotificationInterval_Type())
natv2InstanceNotificationInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:natv2InstanceNotificationInterval.setStatus(_A)
if mibBuilder.loadTexts:natv2InstanceNotificationInterval.setUnits(_N)
class _Natv2InstanceLimitAddressMapEntries_Type(Unsigned32):defaultValue=0
_Natv2InstanceLimitAddressMapEntries_Type.__name__=_G
_Natv2InstanceLimitAddressMapEntries_Object=MibTableColumn
natv2InstanceLimitAddressMapEntries=_Natv2InstanceLimitAddressMapEntries_Object((1,3,6,1,2,1,234,2,1,1,23),_Natv2InstanceLimitAddressMapEntries_Type())
natv2InstanceLimitAddressMapEntries.setMaxAccess(_E)
if mibBuilder.loadTexts:natv2InstanceLimitAddressMapEntries.setStatus(_A)
class _Natv2InstanceLimitPortMapEntries_Type(Unsigned32):defaultValue=0
_Natv2InstanceLimitPortMapEntries_Type.__name__=_G
_Natv2InstanceLimitPortMapEntries_Object=MibTableColumn
natv2InstanceLimitPortMapEntries=_Natv2InstanceLimitPortMapEntries_Object((1,3,6,1,2,1,234,2,1,1,24),_Natv2InstanceLimitPortMapEntries_Type())
natv2InstanceLimitPortMapEntries.setMaxAccess(_E)
if mibBuilder.loadTexts:natv2InstanceLimitPortMapEntries.setStatus(_A)
class _Natv2InstanceLimitPendingFragments_Type(Unsigned32):defaultValue=0
_Natv2InstanceLimitPendingFragments_Type.__name__=_G
_Natv2InstanceLimitPendingFragments_Object=MibTableColumn
natv2InstanceLimitPendingFragments=_Natv2InstanceLimitPendingFragments_Object((1,3,6,1,2,1,234,2,1,1,25),_Natv2InstanceLimitPendingFragments_Type())
natv2InstanceLimitPendingFragments.setMaxAccess(_E)
if mibBuilder.loadTexts:natv2InstanceLimitPendingFragments.setStatus(_A)
class _Natv2InstanceLimitSubscriberActives_Type(Unsigned32):defaultValue=0
_Natv2InstanceLimitSubscriberActives_Type.__name__=_G
_Natv2InstanceLimitSubscriberActives_Object=MibTableColumn
natv2InstanceLimitSubscriberActives=_Natv2InstanceLimitSubscriberActives_Object((1,3,6,1,2,1,234,2,1,1,26),_Natv2InstanceLimitSubscriberActives_Type())
natv2InstanceLimitSubscriberActives.setMaxAccess(_E)
if mibBuilder.loadTexts:natv2InstanceLimitSubscriberActives.setStatus(_A)
_Natv2ProtocolTable_Object=MibTable
natv2ProtocolTable=_Natv2ProtocolTable_Object((1,3,6,1,2,1,234,2,2))
if mibBuilder.loadTexts:natv2ProtocolTable.setStatus(_A)
_Natv2ProtocolEntry_Object=MibTableRow
natv2ProtocolEntry=_Natv2ProtocolEntry_Object((1,3,6,1,2,1,234,2,2,1))
natv2ProtocolEntry.setIndexNames((0,_B,_c),(0,_B,_d))
if mibBuilder.loadTexts:natv2ProtocolEntry.setStatus(_A)
_Natv2ProtocolInstanceIndex_Type=Natv2InstanceIndex
_Natv2ProtocolInstanceIndex_Object=MibTableColumn
natv2ProtocolInstanceIndex=_Natv2ProtocolInstanceIndex_Object((1,3,6,1,2,1,234,2,2,1,1),_Natv2ProtocolInstanceIndex_Type())
natv2ProtocolInstanceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:natv2ProtocolInstanceIndex.setStatus(_A)
_Natv2ProtocolNumber_Type=ProtocolNumber
_Natv2ProtocolNumber_Object=MibTableColumn
natv2ProtocolNumber=_Natv2ProtocolNumber_Object((1,3,6,1,2,1,234,2,2,1,2),_Natv2ProtocolNumber_Type())
natv2ProtocolNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:natv2ProtocolNumber.setStatus(_A)
_Natv2ProtocolPortMapEntries_Type=Unsigned32
_Natv2ProtocolPortMapEntries_Object=MibTableColumn
natv2ProtocolPortMapEntries=_Natv2ProtocolPortMapEntries_Object((1,3,6,1,2,1,234,2,2,1,3),_Natv2ProtocolPortMapEntries_Type())
natv2ProtocolPortMapEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2ProtocolPortMapEntries.setStatus(_A)
_Natv2ProtocolTranslations_Type=Counter64
_Natv2ProtocolTranslations_Object=MibTableColumn
natv2ProtocolTranslations=_Natv2ProtocolTranslations_Object((1,3,6,1,2,1,234,2,2,1,4),_Natv2ProtocolTranslations_Type())
natv2ProtocolTranslations.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2ProtocolTranslations.setStatus(_A)
_Natv2ProtocolPortMapCreations_Type=Counter64
_Natv2ProtocolPortMapCreations_Object=MibTableColumn
natv2ProtocolPortMapCreations=_Natv2ProtocolPortMapCreations_Object((1,3,6,1,2,1,234,2,2,1,5),_Natv2ProtocolPortMapCreations_Type())
natv2ProtocolPortMapCreations.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2ProtocolPortMapCreations.setStatus(_A)
_Natv2ProtocolPortMapFailureDrops_Type=Counter64
_Natv2ProtocolPortMapFailureDrops_Object=MibTableColumn
natv2ProtocolPortMapFailureDrops=_Natv2ProtocolPortMapFailureDrops_Object((1,3,6,1,2,1,234,2,2,1,6),_Natv2ProtocolPortMapFailureDrops_Type())
natv2ProtocolPortMapFailureDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2ProtocolPortMapFailureDrops.setStatus(_A)
_Natv2PoolTable_Object=MibTable
natv2PoolTable=_Natv2PoolTable_Object((1,3,6,1,2,1,234,2,3))
if mibBuilder.loadTexts:natv2PoolTable.setStatus(_A)
_Natv2PoolEntry_Object=MibTableRow
natv2PoolEntry=_Natv2PoolEntry_Object((1,3,6,1,2,1,234,2,3,1))
natv2PoolEntry.setIndexNames((0,_B,_e),(0,_B,_f))
if mibBuilder.loadTexts:natv2PoolEntry.setStatus(_A)
_Natv2PoolInstanceIndex_Type=Natv2InstanceIndex
_Natv2PoolInstanceIndex_Object=MibTableColumn
natv2PoolInstanceIndex=_Natv2PoolInstanceIndex_Object((1,3,6,1,2,1,234,2,3,1,1),_Natv2PoolInstanceIndex_Type())
natv2PoolInstanceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:natv2PoolInstanceIndex.setStatus(_A)
_Natv2PoolIndex_Type=Natv2PoolIndex
_Natv2PoolIndex_Object=MibTableColumn
natv2PoolIndex=_Natv2PoolIndex_Object((1,3,6,1,2,1,234,2,3,1,2),_Natv2PoolIndex_Type())
natv2PoolIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:natv2PoolIndex.setStatus(_A)
class _Natv2PoolRealm_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Natv2PoolRealm_Type.__name__=_H
_Natv2PoolRealm_Object=MibTableColumn
natv2PoolRealm=_Natv2PoolRealm_Object((1,3,6,1,2,1,234,2,3,1,3),_Natv2PoolRealm_Type())
natv2PoolRealm.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2PoolRealm.setStatus(_A)
_Natv2PoolAddressType_Type=InetAddressType
_Natv2PoolAddressType_Object=MibTableColumn
natv2PoolAddressType=_Natv2PoolAddressType_Object((1,3,6,1,2,1,234,2,3,1,4),_Natv2PoolAddressType_Type())
natv2PoolAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2PoolAddressType.setStatus(_A)
_Natv2PoolMinimumPort_Type=InetPortNumber
_Natv2PoolMinimumPort_Object=MibTableColumn
natv2PoolMinimumPort=_Natv2PoolMinimumPort_Object((1,3,6,1,2,1,234,2,3,1,5),_Natv2PoolMinimumPort_Type())
natv2PoolMinimumPort.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2PoolMinimumPort.setStatus(_A)
_Natv2PoolMaximumPort_Type=InetPortNumber
_Natv2PoolMaximumPort_Object=MibTableColumn
natv2PoolMaximumPort=_Natv2PoolMaximumPort_Object((1,3,6,1,2,1,234,2,3,1,6),_Natv2PoolMaximumPort_Type())
natv2PoolMaximumPort.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2PoolMaximumPort.setStatus(_A)
_Natv2PoolAddressMapEntries_Type=Unsigned32
_Natv2PoolAddressMapEntries_Object=MibTableColumn
natv2PoolAddressMapEntries=_Natv2PoolAddressMapEntries_Object((1,3,6,1,2,1,234,2,3,1,7),_Natv2PoolAddressMapEntries_Type())
natv2PoolAddressMapEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2PoolAddressMapEntries.setStatus(_A)
_Natv2PoolPortMapEntries_Type=Unsigned32
_Natv2PoolPortMapEntries_Object=MibTableColumn
natv2PoolPortMapEntries=_Natv2PoolPortMapEntries_Object((1,3,6,1,2,1,234,2,3,1,8),_Natv2PoolPortMapEntries_Type())
natv2PoolPortMapEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2PoolPortMapEntries.setStatus(_A)
_Natv2PoolAddressMapCreations_Type=Counter64
_Natv2PoolAddressMapCreations_Object=MibTableColumn
natv2PoolAddressMapCreations=_Natv2PoolAddressMapCreations_Object((1,3,6,1,2,1,234,2,3,1,9),_Natv2PoolAddressMapCreations_Type())
natv2PoolAddressMapCreations.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2PoolAddressMapCreations.setStatus(_A)
_Natv2PoolPortMapCreations_Type=Counter64
_Natv2PoolPortMapCreations_Object=MibTableColumn
natv2PoolPortMapCreations=_Natv2PoolPortMapCreations_Object((1,3,6,1,2,1,234,2,3,1,10),_Natv2PoolPortMapCreations_Type())
natv2PoolPortMapCreations.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2PoolPortMapCreations.setStatus(_A)
_Natv2PoolAddressMapFailureDrops_Type=Counter64
_Natv2PoolAddressMapFailureDrops_Object=MibTableColumn
natv2PoolAddressMapFailureDrops=_Natv2PoolAddressMapFailureDrops_Object((1,3,6,1,2,1,234,2,3,1,11),_Natv2PoolAddressMapFailureDrops_Type())
natv2PoolAddressMapFailureDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2PoolAddressMapFailureDrops.setStatus(_A)
_Natv2PoolPortMapFailureDrops_Type=Counter64
_Natv2PoolPortMapFailureDrops_Object=MibTableColumn
natv2PoolPortMapFailureDrops=_Natv2PoolPortMapFailureDrops_Object((1,3,6,1,2,1,234,2,3,1,12),_Natv2PoolPortMapFailureDrops_Type())
natv2PoolPortMapFailureDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2PoolPortMapFailureDrops.setStatus(_A)
_Natv2PoolDiscontinuityTime_Type=TimeStamp
_Natv2PoolDiscontinuityTime_Object=MibTableColumn
natv2PoolDiscontinuityTime=_Natv2PoolDiscontinuityTime_Object((1,3,6,1,2,1,234,2,3,1,13),_Natv2PoolDiscontinuityTime_Type())
natv2PoolDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2PoolDiscontinuityTime.setStatus(_A)
class _Natv2PoolThresholdUsageLow_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,100))
_Natv2PoolThresholdUsageLow_Type.__name__=_F
_Natv2PoolThresholdUsageLow_Object=MibTableColumn
natv2PoolThresholdUsageLow=_Natv2PoolThresholdUsageLow_Object((1,3,6,1,2,1,234,2,3,1,14),_Natv2PoolThresholdUsageLow_Type())
natv2PoolThresholdUsageLow.setMaxAccess(_E)
if mibBuilder.loadTexts:natv2PoolThresholdUsageLow.setStatus(_A)
if mibBuilder.loadTexts:natv2PoolThresholdUsageLow.setUnits(_g)
class _Natv2PoolThresholdUsageHigh_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,100))
_Natv2PoolThresholdUsageHigh_Type.__name__=_F
_Natv2PoolThresholdUsageHigh_Object=MibTableColumn
natv2PoolThresholdUsageHigh=_Natv2PoolThresholdUsageHigh_Object((1,3,6,1,2,1,234,2,3,1,15),_Natv2PoolThresholdUsageHigh_Type())
natv2PoolThresholdUsageHigh.setMaxAccess(_E)
if mibBuilder.loadTexts:natv2PoolThresholdUsageHigh.setStatus(_A)
if mibBuilder.loadTexts:natv2PoolThresholdUsageHigh.setUnits(_g)
_Natv2PoolNotifiedPortMapEntries_Type=Unsigned32
_Natv2PoolNotifiedPortMapEntries_Object=MibTableColumn
natv2PoolNotifiedPortMapEntries=_Natv2PoolNotifiedPortMapEntries_Object((1,3,6,1,2,1,234,2,3,1,16),_Natv2PoolNotifiedPortMapEntries_Type())
natv2PoolNotifiedPortMapEntries.setMaxAccess(_h)
if mibBuilder.loadTexts:natv2PoolNotifiedPortMapEntries.setStatus(_A)
_Natv2PoolNotifiedPortMapProtocol_Type=ProtocolNumber
_Natv2PoolNotifiedPortMapProtocol_Object=MibTableColumn
natv2PoolNotifiedPortMapProtocol=_Natv2PoolNotifiedPortMapProtocol_Object((1,3,6,1,2,1,234,2,3,1,17),_Natv2PoolNotifiedPortMapProtocol_Type())
natv2PoolNotifiedPortMapProtocol.setMaxAccess(_h)
if mibBuilder.loadTexts:natv2PoolNotifiedPortMapProtocol.setStatus(_A)
class _Natv2PoolNotificationInterval_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_Natv2PoolNotificationInterval_Type.__name__=_G
_Natv2PoolNotificationInterval_Object=MibTableColumn
natv2PoolNotificationInterval=_Natv2PoolNotificationInterval_Object((1,3,6,1,2,1,234,2,3,1,18),_Natv2PoolNotificationInterval_Type())
natv2PoolNotificationInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:natv2PoolNotificationInterval.setStatus(_A)
if mibBuilder.loadTexts:natv2PoolNotificationInterval.setUnits(_N)
_Natv2PoolRangeTable_Object=MibTable
natv2PoolRangeTable=_Natv2PoolRangeTable_Object((1,3,6,1,2,1,234,2,4))
if mibBuilder.loadTexts:natv2PoolRangeTable.setStatus(_A)
_Natv2PoolRangeEntry_Object=MibTableRow
natv2PoolRangeEntry=_Natv2PoolRangeEntry_Object((1,3,6,1,2,1,234,2,4,1))
natv2PoolRangeEntry.setIndexNames((0,_B,_i),(0,_B,_j),(0,_B,_k))
if mibBuilder.loadTexts:natv2PoolRangeEntry.setStatus(_A)
_Natv2PoolRangeInstanceIndex_Type=Natv2InstanceIndex
_Natv2PoolRangeInstanceIndex_Object=MibTableColumn
natv2PoolRangeInstanceIndex=_Natv2PoolRangeInstanceIndex_Object((1,3,6,1,2,1,234,2,4,1,1),_Natv2PoolRangeInstanceIndex_Type())
natv2PoolRangeInstanceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:natv2PoolRangeInstanceIndex.setStatus(_A)
_Natv2PoolRangePoolIndex_Type=Natv2PoolIndex
_Natv2PoolRangePoolIndex_Object=MibTableColumn
natv2PoolRangePoolIndex=_Natv2PoolRangePoolIndex_Object((1,3,6,1,2,1,234,2,4,1,2),_Natv2PoolRangePoolIndex_Type())
natv2PoolRangePoolIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:natv2PoolRangePoolIndex.setStatus(_A)
_Natv2PoolRangeRowIndex_Type=Unsigned32
_Natv2PoolRangeRowIndex_Object=MibTableColumn
natv2PoolRangeRowIndex=_Natv2PoolRangeRowIndex_Object((1,3,6,1,2,1,234,2,4,1,3),_Natv2PoolRangeRowIndex_Type())
natv2PoolRangeRowIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:natv2PoolRangeRowIndex.setStatus(_A)
_Natv2PoolRangeBegin_Type=InetAddress
_Natv2PoolRangeBegin_Object=MibTableColumn
natv2PoolRangeBegin=_Natv2PoolRangeBegin_Object((1,3,6,1,2,1,234,2,4,1,4),_Natv2PoolRangeBegin_Type())
natv2PoolRangeBegin.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2PoolRangeBegin.setStatus(_A)
_Natv2PoolRangeEnd_Type=InetAddress
_Natv2PoolRangeEnd_Object=MibTableColumn
natv2PoolRangeEnd=_Natv2PoolRangeEnd_Object((1,3,6,1,2,1,234,2,4,1,5),_Natv2PoolRangeEnd_Type())
natv2PoolRangeEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2PoolRangeEnd.setStatus(_A)
_Natv2AddressMapTable_Object=MibTable
natv2AddressMapTable=_Natv2AddressMapTable_Object((1,3,6,1,2,1,234,2,5))
if mibBuilder.loadTexts:natv2AddressMapTable.setStatus(_A)
_Natv2AddressMapEntry_Object=MibTableRow
natv2AddressMapEntry=_Natv2AddressMapEntry_Object((1,3,6,1,2,1,234,2,5,1))
natv2AddressMapEntry.setIndexNames((0,_B,_l),(0,_B,_m),(0,_B,_n),(0,_B,_o),(0,_B,_p))
if mibBuilder.loadTexts:natv2AddressMapEntry.setStatus(_A)
_Natv2AddressMapInstanceIndex_Type=Natv2InstanceIndex
_Natv2AddressMapInstanceIndex_Object=MibTableColumn
natv2AddressMapInstanceIndex=_Natv2AddressMapInstanceIndex_Object((1,3,6,1,2,1,234,2,5,1,1),_Natv2AddressMapInstanceIndex_Type())
natv2AddressMapInstanceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:natv2AddressMapInstanceIndex.setStatus(_A)
class _Natv2AddressMapInternalRealm_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Natv2AddressMapInternalRealm_Type.__name__=_H
_Natv2AddressMapInternalRealm_Object=MibTableColumn
natv2AddressMapInternalRealm=_Natv2AddressMapInternalRealm_Object((1,3,6,1,2,1,234,2,5,1,2),_Natv2AddressMapInternalRealm_Type())
natv2AddressMapInternalRealm.setMaxAccess(_D)
if mibBuilder.loadTexts:natv2AddressMapInternalRealm.setStatus(_A)
_Natv2AddressMapInternalAddressType_Type=InetAddressType
_Natv2AddressMapInternalAddressType_Object=MibTableColumn
natv2AddressMapInternalAddressType=_Natv2AddressMapInternalAddressType_Object((1,3,6,1,2,1,234,2,5,1,3),_Natv2AddressMapInternalAddressType_Type())
natv2AddressMapInternalAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:natv2AddressMapInternalAddressType.setStatus(_A)
class _Natv2AddressMapInternalAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Natv2AddressMapInternalAddress_Type.__name__=_M
_Natv2AddressMapInternalAddress_Object=MibTableColumn
natv2AddressMapInternalAddress=_Natv2AddressMapInternalAddress_Object((1,3,6,1,2,1,234,2,5,1,4),_Natv2AddressMapInternalAddress_Type())
natv2AddressMapInternalAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:natv2AddressMapInternalAddress.setStatus(_A)
_Natv2AddressMapRowIndex_Type=Unsigned32
_Natv2AddressMapRowIndex_Object=MibTableColumn
natv2AddressMapRowIndex=_Natv2AddressMapRowIndex_Object((1,3,6,1,2,1,234,2,5,1,5),_Natv2AddressMapRowIndex_Type())
natv2AddressMapRowIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:natv2AddressMapRowIndex.setStatus(_A)
_Natv2AddressMapInternalMappedAddressType_Type=InetAddressType
_Natv2AddressMapInternalMappedAddressType_Object=MibTableColumn
natv2AddressMapInternalMappedAddressType=_Natv2AddressMapInternalMappedAddressType_Object((1,3,6,1,2,1,234,2,5,1,6),_Natv2AddressMapInternalMappedAddressType_Type())
natv2AddressMapInternalMappedAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2AddressMapInternalMappedAddressType.setStatus(_A)
_Natv2AddressMapInternalMappedAddress_Type=InetAddress
_Natv2AddressMapInternalMappedAddress_Object=MibTableColumn
natv2AddressMapInternalMappedAddress=_Natv2AddressMapInternalMappedAddress_Object((1,3,6,1,2,1,234,2,5,1,7),_Natv2AddressMapInternalMappedAddress_Type())
natv2AddressMapInternalMappedAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2AddressMapInternalMappedAddress.setStatus(_A)
class _Natv2AddressMapExternalRealm_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Natv2AddressMapExternalRealm_Type.__name__=_H
_Natv2AddressMapExternalRealm_Object=MibTableColumn
natv2AddressMapExternalRealm=_Natv2AddressMapExternalRealm_Object((1,3,6,1,2,1,234,2,5,1,8),_Natv2AddressMapExternalRealm_Type())
natv2AddressMapExternalRealm.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2AddressMapExternalRealm.setStatus(_A)
_Natv2AddressMapExternalAddressType_Type=InetAddressType
_Natv2AddressMapExternalAddressType_Object=MibTableColumn
natv2AddressMapExternalAddressType=_Natv2AddressMapExternalAddressType_Object((1,3,6,1,2,1,234,2,5,1,9),_Natv2AddressMapExternalAddressType_Type())
natv2AddressMapExternalAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2AddressMapExternalAddressType.setStatus(_A)
_Natv2AddressMapExternalAddress_Type=InetAddress
_Natv2AddressMapExternalAddress_Object=MibTableColumn
natv2AddressMapExternalAddress=_Natv2AddressMapExternalAddress_Object((1,3,6,1,2,1,234,2,5,1,10),_Natv2AddressMapExternalAddress_Type())
natv2AddressMapExternalAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2AddressMapExternalAddress.setStatus(_A)
_Natv2AddressMapExternalPoolIndex_Type=Natv2PoolIndexOrZero
_Natv2AddressMapExternalPoolIndex_Object=MibTableColumn
natv2AddressMapExternalPoolIndex=_Natv2AddressMapExternalPoolIndex_Object((1,3,6,1,2,1,234,2,5,1,11),_Natv2AddressMapExternalPoolIndex_Type())
natv2AddressMapExternalPoolIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2AddressMapExternalPoolIndex.setStatus(_A)
_Natv2AddressMapSubscriberIndex_Type=Natv2SubscriberIndexOrZero
_Natv2AddressMapSubscriberIndex_Object=MibTableColumn
natv2AddressMapSubscriberIndex=_Natv2AddressMapSubscriberIndex_Object((1,3,6,1,2,1,234,2,5,1,12),_Natv2AddressMapSubscriberIndex_Type())
natv2AddressMapSubscriberIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2AddressMapSubscriberIndex.setStatus(_A)
_Natv2PortMapTable_Object=MibTable
natv2PortMapTable=_Natv2PortMapTable_Object((1,3,6,1,2,1,234,2,6))
if mibBuilder.loadTexts:natv2PortMapTable.setStatus(_A)
_Natv2PortMapEntry_Object=MibTableRow
natv2PortMapEntry=_Natv2PortMapEntry_Object((1,3,6,1,2,1,234,2,6,1))
natv2PortMapEntry.setIndexNames((0,_B,_q),(0,_B,_r),(0,_B,_s),(0,_B,_t),(0,_B,_u),(0,_B,_v))
if mibBuilder.loadTexts:natv2PortMapEntry.setStatus(_A)
_Natv2PortMapInstanceIndex_Type=Natv2InstanceIndex
_Natv2PortMapInstanceIndex_Object=MibTableColumn
natv2PortMapInstanceIndex=_Natv2PortMapInstanceIndex_Object((1,3,6,1,2,1,234,2,6,1,1),_Natv2PortMapInstanceIndex_Type())
natv2PortMapInstanceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:natv2PortMapInstanceIndex.setStatus(_A)
_Natv2PortMapProtocol_Type=ProtocolNumber
_Natv2PortMapProtocol_Object=MibTableColumn
natv2PortMapProtocol=_Natv2PortMapProtocol_Object((1,3,6,1,2,1,234,2,6,1,2),_Natv2PortMapProtocol_Type())
natv2PortMapProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:natv2PortMapProtocol.setStatus(_A)
class _Natv2PortMapExternalRealm_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Natv2PortMapExternalRealm_Type.__name__=_H
_Natv2PortMapExternalRealm_Object=MibTableColumn
natv2PortMapExternalRealm=_Natv2PortMapExternalRealm_Object((1,3,6,1,2,1,234,2,6,1,3),_Natv2PortMapExternalRealm_Type())
natv2PortMapExternalRealm.setMaxAccess(_D)
if mibBuilder.loadTexts:natv2PortMapExternalRealm.setStatus(_A)
_Natv2PortMapExternalAddressType_Type=InetAddressType
_Natv2PortMapExternalAddressType_Object=MibTableColumn
natv2PortMapExternalAddressType=_Natv2PortMapExternalAddressType_Object((1,3,6,1,2,1,234,2,6,1,4),_Natv2PortMapExternalAddressType_Type())
natv2PortMapExternalAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:natv2PortMapExternalAddressType.setStatus(_A)
class _Natv2PortMapExternalAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_Natv2PortMapExternalAddress_Type.__name__=_M
_Natv2PortMapExternalAddress_Object=MibTableColumn
natv2PortMapExternalAddress=_Natv2PortMapExternalAddress_Object((1,3,6,1,2,1,234,2,6,1,5),_Natv2PortMapExternalAddress_Type())
natv2PortMapExternalAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:natv2PortMapExternalAddress.setStatus(_A)
_Natv2PortMapExternalPort_Type=InetPortNumber
_Natv2PortMapExternalPort_Object=MibTableColumn
natv2PortMapExternalPort=_Natv2PortMapExternalPort_Object((1,3,6,1,2,1,234,2,6,1,6),_Natv2PortMapExternalPort_Type())
natv2PortMapExternalPort.setMaxAccess(_D)
if mibBuilder.loadTexts:natv2PortMapExternalPort.setStatus(_A)
class _Natv2PortMapInternalRealm_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Natv2PortMapInternalRealm_Type.__name__=_H
_Natv2PortMapInternalRealm_Object=MibTableColumn
natv2PortMapInternalRealm=_Natv2PortMapInternalRealm_Object((1,3,6,1,2,1,234,2,6,1,7),_Natv2PortMapInternalRealm_Type())
natv2PortMapInternalRealm.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2PortMapInternalRealm.setStatus(_A)
_Natv2PortMapInternalAddressType_Type=InetAddressType
_Natv2PortMapInternalAddressType_Object=MibTableColumn
natv2PortMapInternalAddressType=_Natv2PortMapInternalAddressType_Object((1,3,6,1,2,1,234,2,6,1,8),_Natv2PortMapInternalAddressType_Type())
natv2PortMapInternalAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2PortMapInternalAddressType.setStatus(_A)
_Natv2PortMapInternalAddress_Type=InetAddress
_Natv2PortMapInternalAddress_Object=MibTableColumn
natv2PortMapInternalAddress=_Natv2PortMapInternalAddress_Object((1,3,6,1,2,1,234,2,6,1,9),_Natv2PortMapInternalAddress_Type())
natv2PortMapInternalAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2PortMapInternalAddress.setStatus(_A)
_Natv2PortMapInternalMappedAddressType_Type=InetAddressType
_Natv2PortMapInternalMappedAddressType_Object=MibTableColumn
natv2PortMapInternalMappedAddressType=_Natv2PortMapInternalMappedAddressType_Object((1,3,6,1,2,1,234,2,6,1,10),_Natv2PortMapInternalMappedAddressType_Type())
natv2PortMapInternalMappedAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2PortMapInternalMappedAddressType.setStatus(_A)
_Natv2PortMapInternalMappedAddress_Type=InetAddress
_Natv2PortMapInternalMappedAddress_Object=MibTableColumn
natv2PortMapInternalMappedAddress=_Natv2PortMapInternalMappedAddress_Object((1,3,6,1,2,1,234,2,6,1,11),_Natv2PortMapInternalMappedAddress_Type())
natv2PortMapInternalMappedAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2PortMapInternalMappedAddress.setStatus(_A)
_Natv2PortMapInternalPort_Type=InetPortNumber
_Natv2PortMapInternalPort_Object=MibTableColumn
natv2PortMapInternalPort=_Natv2PortMapInternalPort_Object((1,3,6,1,2,1,234,2,6,1,12),_Natv2PortMapInternalPort_Type())
natv2PortMapInternalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2PortMapInternalPort.setStatus(_A)
_Natv2PortMapExternalPoolIndex_Type=Natv2PoolIndexOrZero
_Natv2PortMapExternalPoolIndex_Object=MibTableColumn
natv2PortMapExternalPoolIndex=_Natv2PortMapExternalPoolIndex_Object((1,3,6,1,2,1,234,2,6,1,13),_Natv2PortMapExternalPoolIndex_Type())
natv2PortMapExternalPoolIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2PortMapExternalPoolIndex.setStatus(_A)
_Natv2PortMapSubscriberIndex_Type=Natv2SubscriberIndexOrZero
_Natv2PortMapSubscriberIndex_Object=MibTableColumn
natv2PortMapSubscriberIndex=_Natv2PortMapSubscriberIndex_Object((1,3,6,1,2,1,234,2,6,1,14),_Natv2PortMapSubscriberIndex_Type())
natv2PortMapSubscriberIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:natv2PortMapSubscriberIndex.setStatus(_A)
_Natv2MIBConformance_ObjectIdentity=ObjectIdentity
natv2MIBConformance=_Natv2MIBConformance_ObjectIdentity((1,3,6,1,2,1,234,3))
_Natv2MIBCompliances_ObjectIdentity=ObjectIdentity
natv2MIBCompliances=_Natv2MIBCompliances_ObjectIdentity((1,3,6,1,2,1,234,3,1))
_Natv2MIBGroups_ObjectIdentity=ObjectIdentity
natv2MIBGroups=_Natv2MIBGroups_ObjectIdentity((1,3,6,1,2,1,234,3,2))
natv2BasicInstanceLevelGroup=ObjectGroup((1,3,6,1,2,1,234,3,2,2))
natv2BasicInstanceLevelGroup.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_O),(_B,_P),(_B,_A0),(_B,_Q),(_B,_A1),(_B,_A2),(_B,_R),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO)))
if mibBuilder.loadTexts:natv2BasicInstanceLevelGroup.setStatus(_A)
natv2PooledInstanceLevelGroup=ObjectGroup((1,3,6,1,2,1,234,3,2,4))
natv2PooledInstanceLevelGroup.setObjects(*((_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_I),(_B,_J),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah)))
if mibBuilder.loadTexts:natv2PooledInstanceLevelGroup.setStatus(_A)
natv2CGNDeviceLevelGroup=ObjectGroup((1,3,6,1,2,1,234,3,2,6))
natv2CGNDeviceLevelGroup.setObjects(*((_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_S),(_B,_An),(_B,_Ao),(_B,_T),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au)))
if mibBuilder.loadTexts:natv2CGNDeviceLevelGroup.setStatus(_A)
natv2CGNInstanceLevelGroup=ObjectGroup((1,3,6,1,2,1,234,3,2,7))
natv2CGNInstanceLevelGroup.setObjects(*((_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1)))
if mibBuilder.loadTexts:natv2CGNInstanceLevelGroup.setStatus(_A)
natv2NotificationPoolUsageLow=NotificationType((1,3,6,1,2,1,234,0,1))
natv2NotificationPoolUsageLow.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:natv2NotificationPoolUsageLow.setStatus(_A)
natv2NotificationPoolUsageHigh=NotificationType((1,3,6,1,2,1,234,0,2))
natv2NotificationPoolUsageHigh.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:natv2NotificationPoolUsageHigh.setStatus(_A)
natv2NotificationInstanceAddressMapEntriesHigh=NotificationType((1,3,6,1,2,1,234,0,3))
natv2NotificationInstanceAddressMapEntriesHigh.setObjects(*((_B,_O),(_B,_Q)))
if mibBuilder.loadTexts:natv2NotificationInstanceAddressMapEntriesHigh.setStatus(_A)
natv2NotificationInstancePortMapEntriesHigh=NotificationType((1,3,6,1,2,1,234,0,4))
natv2NotificationInstancePortMapEntriesHigh.setObjects(*((_B,_P),(_B,_R)))
if mibBuilder.loadTexts:natv2NotificationInstancePortMapEntriesHigh.setStatus(_A)
natv2NotificationSubscriberPortMappingEntriesHigh=NotificationType((1,3,6,1,2,1,234,0,5))
natv2NotificationSubscriberPortMappingEntriesHigh.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:natv2NotificationSubscriberPortMappingEntriesHigh.setStatus(_A)
natv2BasicNotificationGroup=NotificationGroup((1,3,6,1,2,1,234,3,2,1))
natv2BasicNotificationGroup.setObjects(*((_B,_B2),(_B,_B3)))
if mibBuilder.loadTexts:natv2BasicNotificationGroup.setStatus(_A)
natv2PooledNotificationGroup=NotificationGroup((1,3,6,1,2,1,234,3,2,3))
natv2PooledNotificationGroup.setObjects(*((_B,_B4),(_B,_B5)))
if mibBuilder.loadTexts:natv2PooledNotificationGroup.setStatus(_A)
natv2CGNNotificationGroup=NotificationGroup((1,3,6,1,2,1,234,3,2,5))
natv2CGNNotificationGroup.setObjects((_B,_B6))
if mibBuilder.loadTexts:natv2CGNNotificationGroup.setStatus(_A)
natv2MIBBasicCompliance=ModuleCompliance((1,3,6,1,2,1,234,3,1,1))
natv2MIBBasicCompliance.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:natv2MIBBasicCompliance.setStatus(_A)
natv2MIBPooledNATCompliance=ModuleCompliance((1,3,6,1,2,1,234,3,1,2))
natv2MIBPooledNATCompliance.setObjects(*((_B,_K),(_B,_L),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:natv2MIBPooledNATCompliance.setStatus(_A)
natv2MIBCGNCompliance=ModuleCompliance((1,3,6,1,2,1,234,3,1,3))
natv2MIBCGNCompliance.setObjects(*((_B,_K),(_B,_L),(_B,_U),(_B,_V),(_B,_B7),(_B,_B8),(_B,_B9)))
if mibBuilder.loadTexts:natv2MIBCGNCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ProtocolNumber':ProtocolNumber,'Natv2SubscriberIndex':Natv2SubscriberIndex,'Natv2SubscriberIndexOrZero':Natv2SubscriberIndexOrZero,'Natv2InstanceIndex':Natv2InstanceIndex,'Natv2PoolIndex':Natv2PoolIndex,'Natv2PoolIndexOrZero':Natv2PoolIndexOrZero,'natv2MIB':natv2MIB,'natv2MIBNotifications':natv2MIBNotifications,_B4:natv2NotificationPoolUsageLow,_B5:natv2NotificationPoolUsageHigh,_B2:natv2NotificationInstanceAddressMapEntriesHigh,_B3:natv2NotificationInstancePortMapEntriesHigh,_B6:natv2NotificationSubscriberPortMappingEntriesHigh,'natv2MIBDeviceObjects':natv2MIBDeviceObjects,'natv2SubscriberTable':natv2SubscriberTable,'natv2SubscriberEntry':natv2SubscriberEntry,_X:natv2SubscriberIndex,_Ai:natv2SubscriberInternalRealm,_Aj:natv2SubscriberInternalPrefixType,_Ak:natv2SubscriberInternalPrefix,_Al:natv2SubscriberInternalPrefixLength,_Am:natv2SubscriberAddressMapEntries,_S:natv2SubscriberPortMapEntries,_An:natv2SubscriberTranslations,_Ao:natv2SubscriberAddressMapCreations,_T:natv2SubscriberPortMapCreations,_Ap:natv2SubscriberAddressMapFailureDrops,_Aq:natv2SubscriberPortMapFailureDrops,_Ar:natv2SubscriberDiscontinuityTime,_As:natv2SubscriberLimitPortMapEntries,_At:natv2SubscriberThresholdPortMapEntriesHigh,_Au:natv2SubscriberNotificationInterval,'natv2MIBInstanceObjects':natv2MIBInstanceObjects,'natv2InstanceTable':natv2InstanceTable,'natv2InstanceEntry':natv2InstanceEntry,_Y:natv2InstanceIndex,_w:natv2InstanceAlias,_x:natv2InstancePortMappingBehavior,_y:natv2InstanceFilteringBehavior,_AP:natv2InstancePoolingBehavior,_z:natv2InstanceFragmentBehavior,_O:natv2InstanceAddressMapEntries,_P:natv2InstancePortMapEntries,_A0:natv2InstanceTranslations,_Q:natv2InstanceAddressMapCreations,_R:natv2InstancePortMapCreations,_A1:natv2InstanceAddressMapEntryLimitDrops,_A3:natv2InstancePortMapEntryLimitDrops,_Av:natv2InstanceSubscriberActiveLimitDrops,_A2:natv2InstanceAddressMapFailureDrops,_A4:natv2InstancePortMapFailureDrops,_A5:natv2InstanceFragmentDrops,_A6:natv2InstanceOtherResourceFailureDrops,_A7:natv2InstanceDiscontinuityTime,_A8:natv2InstanceThresholdAddressMapEntriesHigh,_A9:natv2InstanceThresholdPortMapEntriesHigh,_AA:natv2InstanceNotificationInterval,_AB:natv2InstanceLimitAddressMapEntries,_AC:natv2InstanceLimitPortMapEntries,_AD:natv2InstanceLimitPendingFragments,_Aw:natv2InstanceLimitSubscriberActives,'natv2ProtocolTable':natv2ProtocolTable,'natv2ProtocolEntry':natv2ProtocolEntry,_c:natv2ProtocolInstanceIndex,_d:natv2ProtocolNumber,_AE:natv2ProtocolPortMapEntries,_AF:natv2ProtocolTranslations,_AG:natv2ProtocolPortMapCreations,_AH:natv2ProtocolPortMapFailureDrops,'natv2PoolTable':natv2PoolTable,'natv2PoolEntry':natv2PoolEntry,_e:natv2PoolInstanceIndex,_f:natv2PoolIndex,_AQ:natv2PoolRealm,_AR:natv2PoolAddressType,_AS:natv2PoolMinimumPort,_AT:natv2PoolMaximumPort,_AU:natv2PoolAddressMapEntries,_AV:natv2PoolPortMapEntries,_AW:natv2PoolAddressMapCreations,_AX:natv2PoolPortMapCreations,_AY:natv2PoolAddressMapFailureDrops,_AZ:natv2PoolPortMapFailureDrops,_Aa:natv2PoolDiscontinuityTime,_Ab:natv2PoolThresholdUsageLow,_Ac:natv2PoolThresholdUsageHigh,_I:natv2PoolNotifiedPortMapEntries,_J:natv2PoolNotifiedPortMapProtocol,_Ad:natv2PoolNotificationInterval,'natv2PoolRangeTable':natv2PoolRangeTable,'natv2PoolRangeEntry':natv2PoolRangeEntry,_i:natv2PoolRangeInstanceIndex,_j:natv2PoolRangePoolIndex,_k:natv2PoolRangeRowIndex,_Ae:natv2PoolRangeBegin,_Af:natv2PoolRangeEnd,'natv2AddressMapTable':natv2AddressMapTable,'natv2AddressMapEntry':natv2AddressMapEntry,_l:natv2AddressMapInstanceIndex,_m:natv2AddressMapInternalRealm,_n:natv2AddressMapInternalAddressType,_o:natv2AddressMapInternalAddress,_p:natv2AddressMapRowIndex,_Ax:natv2AddressMapInternalMappedAddressType,_Ay:natv2AddressMapInternalMappedAddress,_AI:natv2AddressMapExternalRealm,_AJ:natv2AddressMapExternalAddressType,_AK:natv2AddressMapExternalAddress,_Ag:natv2AddressMapExternalPoolIndex,_Az:natv2AddressMapSubscriberIndex,'natv2PortMapTable':natv2PortMapTable,'natv2PortMapEntry':natv2PortMapEntry,_q:natv2PortMapInstanceIndex,_r:natv2PortMapProtocol,_s:natv2PortMapExternalRealm,_t:natv2PortMapExternalAddressType,_u:natv2PortMapExternalAddress,_v:natv2PortMapExternalPort,_AL:natv2PortMapInternalRealm,_AM:natv2PortMapInternalAddressType,_AN:natv2PortMapInternalAddress,_A_:natv2PortMapInternalMappedAddressType,_B0:natv2PortMapInternalMappedAddress,_AO:natv2PortMapInternalPort,_Ah:natv2PortMapExternalPoolIndex,_B1:natv2PortMapSubscriberIndex,'natv2MIBConformance':natv2MIBConformance,'natv2MIBCompliances':natv2MIBCompliances,'natv2MIBBasicCompliance':natv2MIBBasicCompliance,'natv2MIBPooledNATCompliance':natv2MIBPooledNATCompliance,'natv2MIBCGNCompliance':natv2MIBCGNCompliance,'natv2MIBGroups':natv2MIBGroups,_K:natv2BasicNotificationGroup,_L:natv2BasicInstanceLevelGroup,_U:natv2PooledNotificationGroup,_V:natv2PooledInstanceLevelGroup,_B7:natv2CGNNotificationGroup,_B8:natv2CGNDeviceLevelGroup,_B9:natv2CGNInstanceLevelGroup})