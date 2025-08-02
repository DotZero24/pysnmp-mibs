_G='alaAUTOCONFIGNotificationGroup'
_F='alaAutoConfigTrap'
_E='alaAutoConfigAbort'
_D='alaAutoConfigAutoFabricEnableTrap'
_C='Integer32'
_B='ALCATEL-ENT1-AUTO-CONFIG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1AutoConfig,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1AutoConfig')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
alaAUTOCONFIGMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,83,1))
if mibBuilder.loadTexts:alaAUTOCONFIGMIB.setRevisions(('2012-05-04 00:00',))
_AlaAUTOCONFIGMIBNotifications_ObjectIdentity=ObjectIdentity
alaAUTOCONFIGMIBNotifications=_AlaAUTOCONFIGMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,83,1,0))
_AlaAUTOCONFIGMIBObjects_ObjectIdentity=ObjectIdentity
alaAUTOCONFIGMIBObjects=_AlaAUTOCONFIGMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,83,1,1))
if mibBuilder.loadTexts:alaAUTOCONFIGMIBObjects.setStatus(_A)
_AlaAUTOCONFIGGlobal_ObjectIdentity=ObjectIdentity
alaAUTOCONFIGGlobal=_AlaAUTOCONFIGGlobal_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,83,1,1,1))
class _AlaAutoConfigAbort_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_AlaAutoConfigAbort_Type.__name__=_C
_AlaAutoConfigAbort_Object=MibScalar
alaAutoConfigAbort=_AlaAutoConfigAbort_Object((1,3,6,1,4,1,6486,801,1,2,1,83,1,1,1,1),_AlaAutoConfigAbort_Type())
alaAutoConfigAbort.setMaxAccess('read-write')
if mibBuilder.loadTexts:alaAutoConfigAbort.setStatus(_A)
_AlaAUTOCONFIGNotificationObjects_ObjectIdentity=ObjectIdentity
alaAUTOCONFIGNotificationObjects=_AlaAUTOCONFIGNotificationObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,83,1,1,2))
_AlaAutoConfigTrapsObj_ObjectIdentity=ObjectIdentity
alaAutoConfigTrapsObj=_AlaAutoConfigTrapsObj_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,83,1,1,3))
class _AlaAutoConfigAutoFabricEnableTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_AlaAutoConfigAutoFabricEnableTrap_Type.__name__=_C
_AlaAutoConfigAutoFabricEnableTrap_Object=MibScalar
alaAutoConfigAutoFabricEnableTrap=_AlaAutoConfigAutoFabricEnableTrap_Object((1,3,6,1,4,1,6486,801,1,2,1,83,1,1,3,1),_AlaAutoConfigAutoFabricEnableTrap_Type())
alaAutoConfigAutoFabricEnableTrap.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:alaAutoConfigAutoFabricEnableTrap.setStatus(_A)
_AlaAUTOCONFIGMIBConformance_ObjectIdentity=ObjectIdentity
alaAUTOCONFIGMIBConformance=_AlaAUTOCONFIGMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,83,1,2))
if mibBuilder.loadTexts:alaAUTOCONFIGMIBConformance.setStatus(_A)
_AlaAUTOCONFIGMIBGroups_ObjectIdentity=ObjectIdentity
alaAUTOCONFIGMIBGroups=_AlaAUTOCONFIGMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,83,1,2,1))
if mibBuilder.loadTexts:alaAUTOCONFIGMIBGroups.setStatus(_A)
_AlaAUTOCONFIGMIBCompliances_ObjectIdentity=ObjectIdentity
alaAUTOCONFIGMIBCompliances=_AlaAUTOCONFIGMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,83,1,2,2))
if mibBuilder.loadTexts:alaAUTOCONFIGMIBCompliances.setStatus(_A)
alaAutoConfigGlobalGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,83,1,2,1,2))
alaAutoConfigGlobalGroup.setObjects(*((_B,_E),(_B,_D)))
if mibBuilder.loadTexts:alaAutoConfigGlobalGroup.setStatus(_A)
alaAutoConfigTrap=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,83,1,0,1))
alaAutoConfigTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:alaAutoConfigTrap.setStatus(_A)
alaAUTOCONFIGNotificationGroup=NotificationGroup((1,3,6,1,4,1,6486,801,1,2,1,83,1,2,1,1))
alaAUTOCONFIGNotificationGroup.setObjects((_B,_F))
if mibBuilder.loadTexts:alaAUTOCONFIGNotificationGroup.setStatus(_A)
alaAUTOCONFIGMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,83,1,2,2,1))
alaAUTOCONFIGMIBCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:alaAUTOCONFIGMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alaAUTOCONFIGMIB':alaAUTOCONFIGMIB,'alaAUTOCONFIGMIBNotifications':alaAUTOCONFIGMIBNotifications,_F:alaAutoConfigTrap,'alaAUTOCONFIGMIBObjects':alaAUTOCONFIGMIBObjects,'alaAUTOCONFIGGlobal':alaAUTOCONFIGGlobal,_E:alaAutoConfigAbort,'alaAUTOCONFIGNotificationObjects':alaAUTOCONFIGNotificationObjects,'alaAutoConfigTrapsObj':alaAutoConfigTrapsObj,_D:alaAutoConfigAutoFabricEnableTrap,'alaAUTOCONFIGMIBConformance':alaAUTOCONFIGMIBConformance,'alaAUTOCONFIGMIBGroups':alaAUTOCONFIGMIBGroups,_G:alaAUTOCONFIGNotificationGroup,'alaAutoConfigGlobalGroup':alaAutoConfigGlobalGroup,'alaAUTOCONFIGMIBCompliances':alaAUTOCONFIGMIBCompliances,'alaAUTOCONFIGMIBCompliance':alaAUTOCONFIGMIBCompliance})