_R='colubrisCdpMIBGroup'
_Q='coCdpGlobalHoldTime'
_P='coCdpGlobalMessageInterval'
_O='coCdpCachePortId'
_N='coCdpCachePlatform'
_M='coCdpCacheVersion'
_L='coCdpCacheCapabilities'
_K='coCdpCacheTimeToLive'
_J='coCdpCacheDeviceId'
_I='coCdpCacheAddress'
_H='coCdpCacheLocalInterface'
_G='seconds'
_F='read-write'
_E='coCdpCacheDeviceIndex'
_D='Integer32'
_C='read-only'
_B='COLUBRIS-CDP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
colubrisMgmtV2,=mibBuilder.importSymbols('COLUBRIS-SMI','colubrisMgmtV2')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
colubrisCdpMIB=ModuleIdentity((1,3,6,1,4,1,8744,5,9))
_ColubrisCdpMIBObjects_ObjectIdentity=ObjectIdentity
colubrisCdpMIBObjects=_ColubrisCdpMIBObjects_ObjectIdentity((1,3,6,1,4,1,8744,5,9,1))
_CoCdpCache_ObjectIdentity=ObjectIdentity
coCdpCache=_CoCdpCache_ObjectIdentity((1,3,6,1,4,1,8744,5,9,1,1))
_CoCdpCacheTable_Object=MibTable
coCdpCacheTable=_CoCdpCacheTable_Object((1,3,6,1,4,1,8744,5,9,1,1,1))
if mibBuilder.loadTexts:coCdpCacheTable.setStatus(_A)
_CoCdpCacheEntry_Object=MibTableRow
coCdpCacheEntry=_CoCdpCacheEntry_Object((1,3,6,1,4,1,8744,5,9,1,1,1,1))
coCdpCacheEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:coCdpCacheEntry.setStatus(_A)
class _CoCdpCacheDeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CoCdpCacheDeviceIndex_Type.__name__=_D
_CoCdpCacheDeviceIndex_Object=MibTableColumn
coCdpCacheDeviceIndex=_CoCdpCacheDeviceIndex_Object((1,3,6,1,4,1,8744,5,9,1,1,1,1,1),_CoCdpCacheDeviceIndex_Type())
coCdpCacheDeviceIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:coCdpCacheDeviceIndex.setStatus(_A)
_CoCdpCacheLocalInterface_Type=DisplayString
_CoCdpCacheLocalInterface_Object=MibTableColumn
coCdpCacheLocalInterface=_CoCdpCacheLocalInterface_Object((1,3,6,1,4,1,8744,5,9,1,1,1,1,2),_CoCdpCacheLocalInterface_Type())
coCdpCacheLocalInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdpCacheLocalInterface.setStatus(_A)
_CoCdpCacheAddress_Type=IpAddress
_CoCdpCacheAddress_Object=MibTableColumn
coCdpCacheAddress=_CoCdpCacheAddress_Object((1,3,6,1,4,1,8744,5,9,1,1,1,1,3),_CoCdpCacheAddress_Type())
coCdpCacheAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdpCacheAddress.setStatus(_A)
_CoCdpCacheDeviceId_Type=DisplayString
_CoCdpCacheDeviceId_Object=MibTableColumn
coCdpCacheDeviceId=_CoCdpCacheDeviceId_Object((1,3,6,1,4,1,8744,5,9,1,1,1,1,4),_CoCdpCacheDeviceId_Type())
coCdpCacheDeviceId.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdpCacheDeviceId.setStatus(_A)
_CoCdpCacheTimeToLive_Type=Unsigned32
_CoCdpCacheTimeToLive_Object=MibTableColumn
coCdpCacheTimeToLive=_CoCdpCacheTimeToLive_Object((1,3,6,1,4,1,8744,5,9,1,1,1,1,5),_CoCdpCacheTimeToLive_Type())
coCdpCacheTimeToLive.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdpCacheTimeToLive.setStatus(_A)
_CoCdpCacheCapabilities_Type=DisplayString
_CoCdpCacheCapabilities_Object=MibTableColumn
coCdpCacheCapabilities=_CoCdpCacheCapabilities_Object((1,3,6,1,4,1,8744,5,9,1,1,1,1,6),_CoCdpCacheCapabilities_Type())
coCdpCacheCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdpCacheCapabilities.setStatus(_A)
_CoCdpCacheVersion_Type=DisplayString
_CoCdpCacheVersion_Object=MibTableColumn
coCdpCacheVersion=_CoCdpCacheVersion_Object((1,3,6,1,4,1,8744,5,9,1,1,1,1,7),_CoCdpCacheVersion_Type())
coCdpCacheVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdpCacheVersion.setStatus(_A)
_CoCdpCachePlatform_Type=DisplayString
_CoCdpCachePlatform_Object=MibTableColumn
coCdpCachePlatform=_CoCdpCachePlatform_Object((1,3,6,1,4,1,8744,5,9,1,1,1,1,8),_CoCdpCachePlatform_Type())
coCdpCachePlatform.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdpCachePlatform.setStatus(_A)
_CoCdpCachePortId_Type=DisplayString
_CoCdpCachePortId_Object=MibTableColumn
coCdpCachePortId=_CoCdpCachePortId_Object((1,3,6,1,4,1,8744,5,9,1,1,1,1,9),_CoCdpCachePortId_Type())
coCdpCachePortId.setMaxAccess(_C)
if mibBuilder.loadTexts:coCdpCachePortId.setStatus(_A)
_CoCdpGlobal_ObjectIdentity=ObjectIdentity
coCdpGlobal=_CoCdpGlobal_ObjectIdentity((1,3,6,1,4,1,8744,5,9,1,2))
class _CoCdpGlobalMessageInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,254))
_CoCdpGlobalMessageInterval_Type.__name__=_D
_CoCdpGlobalMessageInterval_Object=MibScalar
coCdpGlobalMessageInterval=_CoCdpGlobalMessageInterval_Object((1,3,6,1,4,1,8744,5,9,1,2,1),_CoCdpGlobalMessageInterval_Type())
coCdpGlobalMessageInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:coCdpGlobalMessageInterval.setStatus(_A)
if mibBuilder.loadTexts:coCdpGlobalMessageInterval.setUnits(_G)
class _CoCdpGlobalHoldTime_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,255))
_CoCdpGlobalHoldTime_Type.__name__=_D
_CoCdpGlobalHoldTime_Object=MibScalar
coCdpGlobalHoldTime=_CoCdpGlobalHoldTime_Object((1,3,6,1,4,1,8744,5,9,1,2,2),_CoCdpGlobalHoldTime_Type())
coCdpGlobalHoldTime.setMaxAccess(_F)
if mibBuilder.loadTexts:coCdpGlobalHoldTime.setStatus(_A)
if mibBuilder.loadTexts:coCdpGlobalHoldTime.setUnits(_G)
_ColubrisCdpMIBConformance_ObjectIdentity=ObjectIdentity
colubrisCdpMIBConformance=_ColubrisCdpMIBConformance_ObjectIdentity((1,3,6,1,4,1,8744,5,9,2))
_ColubrisCdpMIBCompliances_ObjectIdentity=ObjectIdentity
colubrisCdpMIBCompliances=_ColubrisCdpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,8744,5,9,2,1))
_ColubrisCdpMIBGroups_ObjectIdentity=ObjectIdentity
colubrisCdpMIBGroups=_ColubrisCdpMIBGroups_ObjectIdentity((1,3,6,1,4,1,8744,5,9,2,2))
colubrisCdpMIBGroup=ObjectGroup((1,3,6,1,4,1,8744,5,9,2,2,1))
colubrisCdpMIBGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:colubrisCdpMIBGroup.setStatus(_A)
colubrisCdpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,8744,5,9,2,1,1))
colubrisCdpMIBCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:colubrisCdpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'colubrisCdpMIB':colubrisCdpMIB,'colubrisCdpMIBObjects':colubrisCdpMIBObjects,'coCdpCache':coCdpCache,'coCdpCacheTable':coCdpCacheTable,'coCdpCacheEntry':coCdpCacheEntry,_E:coCdpCacheDeviceIndex,_H:coCdpCacheLocalInterface,_I:coCdpCacheAddress,_J:coCdpCacheDeviceId,_K:coCdpCacheTimeToLive,_L:coCdpCacheCapabilities,_M:coCdpCacheVersion,_N:coCdpCachePlatform,_O:coCdpCachePortId,'coCdpGlobal':coCdpGlobal,_P:coCdpGlobalMessageInterval,_Q:coCdpGlobalHoldTime,'colubrisCdpMIBConformance':colubrisCdpMIBConformance,'colubrisCdpMIBCompliances':colubrisCdpMIBCompliances,'colubrisCdpMIBCompliance':colubrisCdpMIBCompliance,'colubrisCdpMIBGroups':colubrisCdpMIBGroups,_R:colubrisCdpMIBGroup})