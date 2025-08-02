_P='h3cFtmNotificationGroup'
_O='h3cFtmConfigGroup'
_N='h3cFtmUnitNameChange'
_M='h3cFtmUnitIDChange'
_L='h3cFtmFabricType'
_K='h3cFtmFabricVlanID'
_J='h3cFtmAuthValue'
_I='h3cFtmAuthMode'
_H='h3cFtmUnitName'
_G='h3cFtmUnitID'
_F='read-only'
_E='h3cFtmIndex'
_D='read-write'
_C='Integer32'
_B='H3C-FTM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cFtmManMIB=ModuleIdentity((1,3,6,1,4,1,2011,10,2,1,1))
_H3cFtm_ObjectIdentity=ObjectIdentity
h3cFtm=_H3cFtm_ObjectIdentity((1,3,6,1,4,1,2011,10,2,1))
_H3cFtmManMIBObjects_ObjectIdentity=ObjectIdentity
h3cFtmManMIBObjects=_H3cFtmManMIBObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,1,1,1))
_H3cFtmUnitTable_Object=MibTable
h3cFtmUnitTable=_H3cFtmUnitTable_Object((1,3,6,1,4,1,2011,10,2,1,1,1,1))
if mibBuilder.loadTexts:h3cFtmUnitTable.setStatus(_A)
_H3cFtmUnitEntry_Object=MibTableRow
h3cFtmUnitEntry=_H3cFtmUnitEntry_Object((1,3,6,1,4,1,2011,10,2,1,1,1,1,1))
h3cFtmUnitEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:h3cFtmUnitEntry.setStatus(_A)
_H3cFtmIndex_Type=Integer32
_H3cFtmIndex_Object=MibTableColumn
h3cFtmIndex=_H3cFtmIndex_Object((1,3,6,1,4,1,2011,10,2,1,1,1,1,1,1),_H3cFtmIndex_Type())
h3cFtmIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:h3cFtmIndex.setStatus(_A)
_H3cFtmUnitID_Type=Integer32
_H3cFtmUnitID_Object=MibTableColumn
h3cFtmUnitID=_H3cFtmUnitID_Object((1,3,6,1,4,1,2011,10,2,1,1,1,1,1,2),_H3cFtmUnitID_Type())
h3cFtmUnitID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFtmUnitID.setStatus(_A)
_H3cFtmUnitName_Type=OctetString
_H3cFtmUnitName_Object=MibTableColumn
h3cFtmUnitName=_H3cFtmUnitName_Object((1,3,6,1,4,1,2011,10,2,1,1,1,1,1,3),_H3cFtmUnitName_Type())
h3cFtmUnitName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFtmUnitName.setStatus(_A)
class _H3cFtmUnitRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('master',0),('slave',1)))
_H3cFtmUnitRole_Type.__name__=_C
_H3cFtmUnitRole_Object=MibTableColumn
h3cFtmUnitRole=_H3cFtmUnitRole_Object((1,3,6,1,4,1,2011,10,2,1,1,1,1,1,4),_H3cFtmUnitRole_Type())
h3cFtmUnitRole.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cFtmUnitRole.setStatus(_A)
class _H3cFtmNumberMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('automatic',0),('manual',1)))
_H3cFtmNumberMode_Type.__name__=_C
_H3cFtmNumberMode_Object=MibTableColumn
h3cFtmNumberMode=_H3cFtmNumberMode_Object((1,3,6,1,4,1,2011,10,2,1,1,1,1,1,5),_H3cFtmNumberMode_Type())
h3cFtmNumberMode.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cFtmNumberMode.setStatus(_A)
class _H3cFtmAuthMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ftm-none',0),('ftm-simple',1),('ftm-md5',2)))
_H3cFtmAuthMode_Type.__name__=_C
_H3cFtmAuthMode_Object=MibScalar
h3cFtmAuthMode=_H3cFtmAuthMode_Object((1,3,6,1,4,1,2011,10,2,1,1,1,2),_H3cFtmAuthMode_Type())
h3cFtmAuthMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFtmAuthMode.setStatus(_A)
_H3cFtmAuthValue_Type=OctetString
_H3cFtmAuthValue_Object=MibScalar
h3cFtmAuthValue=_H3cFtmAuthValue_Object((1,3,6,1,4,1,2011,10,2,1,1,1,3),_H3cFtmAuthValue_Type())
h3cFtmAuthValue.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFtmAuthValue.setStatus(_A)
class _H3cFtmFabricVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094))
_H3cFtmFabricVlanID_Type.__name__=_C
_H3cFtmFabricVlanID_Object=MibScalar
h3cFtmFabricVlanID=_H3cFtmFabricVlanID_Object((1,3,6,1,4,1,2011,10,2,1,1,1,4),_H3cFtmFabricVlanID_Type())
h3cFtmFabricVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cFtmFabricVlanID.setStatus(_A)
class _H3cFtmFabricType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('outofStack',1),('line',2),('ring',3),('mesh',4)))
_H3cFtmFabricType_Type.__name__=_C
_H3cFtmFabricType_Object=MibScalar
h3cFtmFabricType=_H3cFtmFabricType_Object((1,3,6,1,4,1,2011,10,2,1,1,1,5),_H3cFtmFabricType_Type())
h3cFtmFabricType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cFtmFabricType.setStatus(_A)
_H3cFtmManMIBComformance_ObjectIdentity=ObjectIdentity
h3cFtmManMIBComformance=_H3cFtmManMIBComformance_ObjectIdentity((1,3,6,1,4,1,2011,10,2,1,1,2))
_H3cFtmMIBCompliances_ObjectIdentity=ObjectIdentity
h3cFtmMIBCompliances=_H3cFtmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2011,10,2,1,1,2,1))
_H3cFtmMIBGroups_ObjectIdentity=ObjectIdentity
h3cFtmMIBGroups=_H3cFtmMIBGroups_ObjectIdentity((1,3,6,1,4,1,2011,10,2,1,1,2,2))
_H3cFtmManMIBNotification_ObjectIdentity=ObjectIdentity
h3cFtmManMIBNotification=_H3cFtmManMIBNotification_ObjectIdentity((1,3,6,1,4,1,2011,10,2,1,1,3))
h3cFtmConfigGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,1,1,2,2,1))
h3cFtmConfigGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:h3cFtmConfigGroup.setStatus(_A)
h3cFtmUnitIDChange=NotificationType((1,3,6,1,4,1,2011,10,2,1,1,3,1))
h3cFtmUnitIDChange.setObjects(*((_B,_E),(_B,_G)))
if mibBuilder.loadTexts:h3cFtmUnitIDChange.setStatus(_A)
h3cFtmUnitNameChange=NotificationType((1,3,6,1,4,1,2011,10,2,1,1,3,2))
h3cFtmUnitNameChange.setObjects(*((_B,_E),(_B,_H)))
if mibBuilder.loadTexts:h3cFtmUnitNameChange.setStatus(_A)
h3cFtmNotificationGroup=NotificationGroup((1,3,6,1,4,1,2011,10,2,1,1,2,2,2))
h3cFtmNotificationGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:h3cFtmNotificationGroup.setStatus(_A)
h3cFtmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,2011,10,2,1,1,2,1,1))
h3cFtmMIBCompliance.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:h3cFtmMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cFtm':h3cFtm,'h3cFtmManMIB':h3cFtmManMIB,'h3cFtmManMIBObjects':h3cFtmManMIBObjects,'h3cFtmUnitTable':h3cFtmUnitTable,'h3cFtmUnitEntry':h3cFtmUnitEntry,_E:h3cFtmIndex,_G:h3cFtmUnitID,_H:h3cFtmUnitName,'h3cFtmUnitRole':h3cFtmUnitRole,'h3cFtmNumberMode':h3cFtmNumberMode,_I:h3cFtmAuthMode,_J:h3cFtmAuthValue,_K:h3cFtmFabricVlanID,_L:h3cFtmFabricType,'h3cFtmManMIBComformance':h3cFtmManMIBComformance,'h3cFtmMIBCompliances':h3cFtmMIBCompliances,'h3cFtmMIBCompliance':h3cFtmMIBCompliance,'h3cFtmMIBGroups':h3cFtmMIBGroups,_O:h3cFtmConfigGroup,_P:h3cFtmNotificationGroup,'h3cFtmManMIBNotification':h3cFtmManMIBNotification,_M:h3cFtmUnitIDChange,_N:h3cFtmUnitNameChange})