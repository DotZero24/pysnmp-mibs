_P='hpnicfFtmNotificationGroup'
_O='hpnicfFtmConfigGroup'
_N='hpnicfFtmUnitNameChange'
_M='hpnicfFtmUnitIDChange'
_L='hpnicfFtmFabricType'
_K='hpnicfFtmFabricVlanID'
_J='hpnicfFtmAuthValue'
_I='hpnicfFtmAuthMode'
_H='hpnicfFtmUnitName'
_G='hpnicfFtmUnitID'
_F='read-only'
_E='hpnicfFtmIndex'
_D='read-write'
_C='Integer32'
_B='HPN-ICF-FTM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfFtmManMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,1,1))
_HpnicfFtm_ObjectIdentity=ObjectIdentity
hpnicfFtm=_HpnicfFtm_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,1))
_HpnicfFtmManMIBObjects_ObjectIdentity=ObjectIdentity
hpnicfFtmManMIBObjects=_HpnicfFtmManMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,1,1,1))
_HpnicfFtmUnitTable_Object=MibTable
hpnicfFtmUnitTable=_HpnicfFtmUnitTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,1,1,1,1))
if mibBuilder.loadTexts:hpnicfFtmUnitTable.setStatus(_A)
_HpnicfFtmUnitEntry_Object=MibTableRow
hpnicfFtmUnitEntry=_HpnicfFtmUnitEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,1,1,1,1,1))
hpnicfFtmUnitEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:hpnicfFtmUnitEntry.setStatus(_A)
_HpnicfFtmIndex_Type=Integer32
_HpnicfFtmIndex_Object=MibTableColumn
hpnicfFtmIndex=_HpnicfFtmIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,1,1,1,1,1,1),_HpnicfFtmIndex_Type())
hpnicfFtmIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:hpnicfFtmIndex.setStatus(_A)
_HpnicfFtmUnitID_Type=Integer32
_HpnicfFtmUnitID_Object=MibTableColumn
hpnicfFtmUnitID=_HpnicfFtmUnitID_Object((1,3,6,1,4,1,11,2,14,11,15,2,1,1,1,1,1,2),_HpnicfFtmUnitID_Type())
hpnicfFtmUnitID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfFtmUnitID.setStatus(_A)
_HpnicfFtmUnitName_Type=OctetString
_HpnicfFtmUnitName_Object=MibTableColumn
hpnicfFtmUnitName=_HpnicfFtmUnitName_Object((1,3,6,1,4,1,11,2,14,11,15,2,1,1,1,1,1,3),_HpnicfFtmUnitName_Type())
hpnicfFtmUnitName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfFtmUnitName.setStatus(_A)
class _HpnicfFtmUnitRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('master',0),('slave',1)))
_HpnicfFtmUnitRole_Type.__name__=_C
_HpnicfFtmUnitRole_Object=MibTableColumn
hpnicfFtmUnitRole=_HpnicfFtmUnitRole_Object((1,3,6,1,4,1,11,2,14,11,15,2,1,1,1,1,1,4),_HpnicfFtmUnitRole_Type())
hpnicfFtmUnitRole.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfFtmUnitRole.setStatus(_A)
class _HpnicfFtmNumberMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('automatic',0),('manual',1)))
_HpnicfFtmNumberMode_Type.__name__=_C
_HpnicfFtmNumberMode_Object=MibTableColumn
hpnicfFtmNumberMode=_HpnicfFtmNumberMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,1,1,1,1,1,5),_HpnicfFtmNumberMode_Type())
hpnicfFtmNumberMode.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfFtmNumberMode.setStatus(_A)
class _HpnicfFtmAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ftm-none',0),('ftm-simple',1),('ftm-md5',2)))
_HpnicfFtmAuthMode_Type.__name__=_C
_HpnicfFtmAuthMode_Object=MibScalar
hpnicfFtmAuthMode=_HpnicfFtmAuthMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,1,1,1,2),_HpnicfFtmAuthMode_Type())
hpnicfFtmAuthMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfFtmAuthMode.setStatus(_A)
_HpnicfFtmAuthValue_Type=OctetString
_HpnicfFtmAuthValue_Object=MibScalar
hpnicfFtmAuthValue=_HpnicfFtmAuthValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,1,1,1,3),_HpnicfFtmAuthValue_Type())
hpnicfFtmAuthValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfFtmAuthValue.setStatus(_A)
class _HpnicfFtmFabricVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_HpnicfFtmFabricVlanID_Type.__name__=_C
_HpnicfFtmFabricVlanID_Object=MibScalar
hpnicfFtmFabricVlanID=_HpnicfFtmFabricVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,1,1,1,4),_HpnicfFtmFabricVlanID_Type())
hpnicfFtmFabricVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfFtmFabricVlanID.setStatus(_A)
class _HpnicfFtmFabricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('outofStack',1),('line',2),('ring',3),('mesh',4)))
_HpnicfFtmFabricType_Type.__name__=_C
_HpnicfFtmFabricType_Object=MibScalar
hpnicfFtmFabricType=_HpnicfFtmFabricType_Object((1,3,6,1,4,1,11,2,14,11,15,2,1,1,1,5),_HpnicfFtmFabricType_Type())
hpnicfFtmFabricType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfFtmFabricType.setStatus(_A)
_HpnicfFtmManMIBComformance_ObjectIdentity=ObjectIdentity
hpnicfFtmManMIBComformance=_HpnicfFtmManMIBComformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,1,1,2))
_HpnicfFtmMIBCompliances_ObjectIdentity=ObjectIdentity
hpnicfFtmMIBCompliances=_HpnicfFtmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,1,1,2,1))
_HpnicfFtmMIBGroups_ObjectIdentity=ObjectIdentity
hpnicfFtmMIBGroups=_HpnicfFtmMIBGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,1,1,2,2))
_HpnicfFtmManMIBNotification_ObjectIdentity=ObjectIdentity
hpnicfFtmManMIBNotification=_HpnicfFtmManMIBNotification_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,1,1,3))
hpnicfFtmConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,1,1,2,2,1))
hpnicfFtmConfigGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:hpnicfFtmConfigGroup.setStatus(_A)
hpnicfFtmUnitIDChange=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,1,1,3,1))
hpnicfFtmUnitIDChange.setObjects(*((_B,_E),(_B,_G)))
if mibBuilder.loadTexts:hpnicfFtmUnitIDChange.setStatus(_A)
hpnicfFtmUnitNameChange=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,1,1,3,2))
hpnicfFtmUnitNameChange.setObjects(*((_B,_E),(_B,_H)))
if mibBuilder.loadTexts:hpnicfFtmUnitNameChange.setStatus(_A)
hpnicfFtmNotificationGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,15,2,1,1,2,2,2))
hpnicfFtmNotificationGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:hpnicfFtmNotificationGroup.setStatus(_A)
hpnicfFtmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,2,1,1,2,1,1))
hpnicfFtmMIBCompliance.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:hpnicfFtmMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfFtm':hpnicfFtm,'hpnicfFtmManMIB':hpnicfFtmManMIB,'hpnicfFtmManMIBObjects':hpnicfFtmManMIBObjects,'hpnicfFtmUnitTable':hpnicfFtmUnitTable,'hpnicfFtmUnitEntry':hpnicfFtmUnitEntry,_E:hpnicfFtmIndex,_G:hpnicfFtmUnitID,_H:hpnicfFtmUnitName,'hpnicfFtmUnitRole':hpnicfFtmUnitRole,'hpnicfFtmNumberMode':hpnicfFtmNumberMode,_I:hpnicfFtmAuthMode,_J:hpnicfFtmAuthValue,_K:hpnicfFtmFabricVlanID,_L:hpnicfFtmFabricType,'hpnicfFtmManMIBComformance':hpnicfFtmManMIBComformance,'hpnicfFtmMIBCompliances':hpnicfFtmMIBCompliances,'hpnicfFtmMIBCompliance':hpnicfFtmMIBCompliance,'hpnicfFtmMIBGroups':hpnicfFtmMIBGroups,_O:hpnicfFtmConfigGroup,_P:hpnicfFtmNotificationGroup,'hpnicfFtmManMIBNotification':hpnicfFtmManMIBNotification,_M:hpnicfFtmUnitIDChange,_N:hpnicfFtmUnitNameChange})