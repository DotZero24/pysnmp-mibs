_Y='colubrisVirtualApMIBGroup'
_X='coVirtualApOperState'
_W='coVirtualApDefaultUserBandwidthLevel'
_V='coVirtualApDefaultUserMaxReceiveRate'
_U='coVirtualApDefaultUserMaxTransmitRate'
_T='coVirtualApDefaultUserRateLimitationEnabled'
_S='coVirtualApUserAccountingProfileIndex'
_R='coVirtualApUserAccountingEnabled'
_Q='coVirtualApAuthenProfileIndex'
_P='coVirtualApAuthenMode'
_O='coVirtualApSecurity'
_N='coVirtualApDefaultVLAN'
_M='coVirtualApMaximumNumberOfUsers'
_L='coVirtualApBroadcastSSID'
_K='coVirtualApSSID'
_J='disable'
_I='enable'
_H='coVirtualApWlanProfileIndex'
_G='ifIndex'
_F='IF-MIB'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='COLUBRIS-VIRTUAL-AP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
colubrisMgmtV2,=mibBuilder.importSymbols('COLUBRIS-SMI','colubrisMgmtV2')
ColubrisPriorityQueue,ColubrisProfileIndexOrZero,ColubrisSSID,ColubrisSecurity,ColubrisUsersAuthenticationMode=mibBuilder.importSymbols('COLUBRIS-TC','ColubrisPriorityQueue','ColubrisProfileIndexOrZero','ColubrisSSID','ColubrisSecurity','ColubrisUsersAuthenticationMode')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
colubrisVirtualApMIB=ModuleIdentity((1,3,6,1,4,1,8744,5,11))
_ColubrisVirtualApMIBObjects_ObjectIdentity=ObjectIdentity
colubrisVirtualApMIBObjects=_ColubrisVirtualApMIBObjects_ObjectIdentity((1,3,6,1,4,1,8744,5,11,1))
_CoVirtualApConfig_ObjectIdentity=ObjectIdentity
coVirtualApConfig=_CoVirtualApConfig_ObjectIdentity((1,3,6,1,4,1,8744,5,11,1,1))
_CoVirtualAccessPointConfigTable_Object=MibTable
coVirtualAccessPointConfigTable=_CoVirtualAccessPointConfigTable_Object((1,3,6,1,4,1,8744,5,11,1,1,1))
if mibBuilder.loadTexts:coVirtualAccessPointConfigTable.setStatus(_A)
_CoVirtualAccessPointConfigEntry_Object=MibTableRow
coVirtualAccessPointConfigEntry=_CoVirtualAccessPointConfigEntry_Object((1,3,6,1,4,1,8744,5,11,1,1,1,1))
coVirtualAccessPointConfigEntry.setIndexNames((0,_F,_G),(0,_B,_H))
if mibBuilder.loadTexts:coVirtualAccessPointConfigEntry.setStatus(_A)
class _CoVirtualApWlanProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CoVirtualApWlanProfileIndex_Type.__name__=_D
_CoVirtualApWlanProfileIndex_Object=MibTableColumn
coVirtualApWlanProfileIndex=_CoVirtualApWlanProfileIndex_Object((1,3,6,1,4,1,8744,5,11,1,1,1,1,1),_CoVirtualApWlanProfileIndex_Type())
coVirtualApWlanProfileIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:coVirtualApWlanProfileIndex.setStatus(_A)
_CoVirtualApSSID_Type=ColubrisSSID
_CoVirtualApSSID_Object=MibTableColumn
coVirtualApSSID=_CoVirtualApSSID_Object((1,3,6,1,4,1,8744,5,11,1,1,1,1,2),_CoVirtualApSSID_Type())
coVirtualApSSID.setMaxAccess(_E)
if mibBuilder.loadTexts:coVirtualApSSID.setStatus(_A)
_CoVirtualApBroadcastSSID_Type=TruthValue
_CoVirtualApBroadcastSSID_Object=MibTableColumn
coVirtualApBroadcastSSID=_CoVirtualApBroadcastSSID_Object((1,3,6,1,4,1,8744,5,11,1,1,1,1,3),_CoVirtualApBroadcastSSID_Type())
coVirtualApBroadcastSSID.setMaxAccess(_E)
if mibBuilder.loadTexts:coVirtualApBroadcastSSID.setStatus(_A)
class _CoVirtualApMaximumNumberOfUsers_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CoVirtualApMaximumNumberOfUsers_Type.__name__=_D
_CoVirtualApMaximumNumberOfUsers_Object=MibTableColumn
coVirtualApMaximumNumberOfUsers=_CoVirtualApMaximumNumberOfUsers_Object((1,3,6,1,4,1,8744,5,11,1,1,1,1,4),_CoVirtualApMaximumNumberOfUsers_Type())
coVirtualApMaximumNumberOfUsers.setMaxAccess(_E)
if mibBuilder.loadTexts:coVirtualApMaximumNumberOfUsers.setStatus(_A)
class _CoVirtualApDefaultVLAN_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_CoVirtualApDefaultVLAN_Type.__name__=_D
_CoVirtualApDefaultVLAN_Object=MibTableColumn
coVirtualApDefaultVLAN=_CoVirtualApDefaultVLAN_Object((1,3,6,1,4,1,8744,5,11,1,1,1,1,5),_CoVirtualApDefaultVLAN_Type())
coVirtualApDefaultVLAN.setMaxAccess(_E)
if mibBuilder.loadTexts:coVirtualApDefaultVLAN.setStatus(_A)
_CoVirtualApSecurity_Type=ColubrisSecurity
_CoVirtualApSecurity_Object=MibTableColumn
coVirtualApSecurity=_CoVirtualApSecurity_Object((1,3,6,1,4,1,8744,5,11,1,1,1,1,6),_CoVirtualApSecurity_Type())
coVirtualApSecurity.setMaxAccess(_C)
if mibBuilder.loadTexts:coVirtualApSecurity.setStatus(_A)
_CoVirtualApAuthenMode_Type=ColubrisUsersAuthenticationMode
_CoVirtualApAuthenMode_Object=MibTableColumn
coVirtualApAuthenMode=_CoVirtualApAuthenMode_Object((1,3,6,1,4,1,8744,5,11,1,1,1,1,7),_CoVirtualApAuthenMode_Type())
coVirtualApAuthenMode.setMaxAccess(_C)
if mibBuilder.loadTexts:coVirtualApAuthenMode.setStatus(_A)
_CoVirtualApAuthenProfileIndex_Type=ColubrisProfileIndexOrZero
_CoVirtualApAuthenProfileIndex_Object=MibTableColumn
coVirtualApAuthenProfileIndex=_CoVirtualApAuthenProfileIndex_Object((1,3,6,1,4,1,8744,5,11,1,1,1,1,8),_CoVirtualApAuthenProfileIndex_Type())
coVirtualApAuthenProfileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:coVirtualApAuthenProfileIndex.setStatus(_A)
class _CoVirtualApUserAccountingEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_CoVirtualApUserAccountingEnabled_Type.__name__=_D
_CoVirtualApUserAccountingEnabled_Object=MibTableColumn
coVirtualApUserAccountingEnabled=_CoVirtualApUserAccountingEnabled_Object((1,3,6,1,4,1,8744,5,11,1,1,1,1,9),_CoVirtualApUserAccountingEnabled_Type())
coVirtualApUserAccountingEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:coVirtualApUserAccountingEnabled.setStatus(_A)
_CoVirtualApUserAccountingProfileIndex_Type=ColubrisProfileIndexOrZero
_CoVirtualApUserAccountingProfileIndex_Object=MibTableColumn
coVirtualApUserAccountingProfileIndex=_CoVirtualApUserAccountingProfileIndex_Object((1,3,6,1,4,1,8744,5,11,1,1,1,1,10),_CoVirtualApUserAccountingProfileIndex_Type())
coVirtualApUserAccountingProfileIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:coVirtualApUserAccountingProfileIndex.setStatus(_A)
_CoVirtualApDefaultUserRateLimitationEnabled_Type=TruthValue
_CoVirtualApDefaultUserRateLimitationEnabled_Object=MibTableColumn
coVirtualApDefaultUserRateLimitationEnabled=_CoVirtualApDefaultUserRateLimitationEnabled_Object((1,3,6,1,4,1,8744,5,11,1,1,1,1,11),_CoVirtualApDefaultUserRateLimitationEnabled_Type())
coVirtualApDefaultUserRateLimitationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:coVirtualApDefaultUserRateLimitationEnabled.setStatus(_A)
_CoVirtualApDefaultUserMaxTransmitRate_Type=Integer32
_CoVirtualApDefaultUserMaxTransmitRate_Object=MibTableColumn
coVirtualApDefaultUserMaxTransmitRate=_CoVirtualApDefaultUserMaxTransmitRate_Object((1,3,6,1,4,1,8744,5,11,1,1,1,1,12),_CoVirtualApDefaultUserMaxTransmitRate_Type())
coVirtualApDefaultUserMaxTransmitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:coVirtualApDefaultUserMaxTransmitRate.setStatus(_A)
_CoVirtualApDefaultUserMaxReceiveRate_Type=Integer32
_CoVirtualApDefaultUserMaxReceiveRate_Object=MibTableColumn
coVirtualApDefaultUserMaxReceiveRate=_CoVirtualApDefaultUserMaxReceiveRate_Object((1,3,6,1,4,1,8744,5,11,1,1,1,1,13),_CoVirtualApDefaultUserMaxReceiveRate_Type())
coVirtualApDefaultUserMaxReceiveRate.setMaxAccess(_C)
if mibBuilder.loadTexts:coVirtualApDefaultUserMaxReceiveRate.setStatus(_A)
_CoVirtualApDefaultUserBandwidthLevel_Type=ColubrisPriorityQueue
_CoVirtualApDefaultUserBandwidthLevel_Object=MibTableColumn
coVirtualApDefaultUserBandwidthLevel=_CoVirtualApDefaultUserBandwidthLevel_Object((1,3,6,1,4,1,8744,5,11,1,1,1,1,14),_CoVirtualApDefaultUserBandwidthLevel_Type())
coVirtualApDefaultUserBandwidthLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:coVirtualApDefaultUserBandwidthLevel.setStatus(_A)
class _CoVirtualApOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_CoVirtualApOperState_Type.__name__=_D
_CoVirtualApOperState_Object=MibTableColumn
coVirtualApOperState=_CoVirtualApOperState_Object((1,3,6,1,4,1,8744,5,11,1,1,1,1,15),_CoVirtualApOperState_Type())
coVirtualApOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:coVirtualApOperState.setStatus(_A)
_ColubrisVirtualApMIBConformance_ObjectIdentity=ObjectIdentity
colubrisVirtualApMIBConformance=_ColubrisVirtualApMIBConformance_ObjectIdentity((1,3,6,1,4,1,8744,5,11,2))
_ColubrisVirtualApMIBCompliances_ObjectIdentity=ObjectIdentity
colubrisVirtualApMIBCompliances=_ColubrisVirtualApMIBCompliances_ObjectIdentity((1,3,6,1,4,1,8744,5,11,2,1))
_ColubrisVirtualApMIBGroups_ObjectIdentity=ObjectIdentity
colubrisVirtualApMIBGroups=_ColubrisVirtualApMIBGroups_ObjectIdentity((1,3,6,1,4,1,8744,5,11,2,2))
colubrisVirtualApMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,11,2,2,1))
colubrisVirtualApMIBGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:colubrisVirtualApMIBGroup.setStatus(_A)
colubrisVirtualApMIBCompliance=ModuleCompliance((1,3,6,1,4,1,8744,5,11,2,1,1))
colubrisVirtualApMIBCompliance.setObjects((_B,_Y))
if mibBuilder.loadTexts:colubrisVirtualApMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'colubrisVirtualApMIB':colubrisVirtualApMIB,'colubrisVirtualApMIBObjects':colubrisVirtualApMIBObjects,'coVirtualApConfig':coVirtualApConfig,'coVirtualAccessPointConfigTable':coVirtualAccessPointConfigTable,'coVirtualAccessPointConfigEntry':coVirtualAccessPointConfigEntry,_H:coVirtualApWlanProfileIndex,_K:coVirtualApSSID,_L:coVirtualApBroadcastSSID,_M:coVirtualApMaximumNumberOfUsers,_N:coVirtualApDefaultVLAN,_O:coVirtualApSecurity,_P:coVirtualApAuthenMode,_Q:coVirtualApAuthenProfileIndex,_R:coVirtualApUserAccountingEnabled,_S:coVirtualApUserAccountingProfileIndex,_T:coVirtualApDefaultUserRateLimitationEnabled,_U:coVirtualApDefaultUserMaxTransmitRate,_V:coVirtualApDefaultUserMaxReceiveRate,_W:coVirtualApDefaultUserBandwidthLevel,_X:coVirtualApOperState,'colubrisVirtualApMIBConformance':colubrisVirtualApMIBConformance,'colubrisVirtualApMIBCompliances':colubrisVirtualApMIBCompliances,'colubrisVirtualApMIBCompliance':colubrisVirtualApMIBCompliance,'colubrisVirtualApMIBGroups':colubrisVirtualApMIBGroups,_Y:colubrisVirtualApMIBGroup})