_H='rbtwsPortConfigGroup'
_G='rbtwsPortConfigTrunkMaster'
_F='rbtwsPortConfigPoeMode'
_E='rbtwsPortConfigPortMode'
_D='rbtwsPortConfigPortNumber'
_C='read-only'
_B='RBTWS-PORT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rbtwsMibs,=mibBuilder.importSymbols('RBTWS-ROOT-MIB','rbtwsMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rbtwsPortMib=ModuleIdentity((1,3,6,1,4,1,52,4,15,1,4,6))
if mibBuilder.loadTexts:rbtwsPortMib.setRevisions(('2008-05-19 00:04','2006-11-09 00:01','2006-04-06 00:00'))
class RbtwsPhysPortNumber(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
class RbtwsPortMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('directAttachAP',1),('networkPort',2),('wired',3)))
class RbtwsPortPoeMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('poeEnable',1),('poeDisable',2)))
_RbtwsPortObjects_ObjectIdentity=ObjectIdentity
rbtwsPortObjects=_RbtwsPortObjects_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,6,1))
_RbtwsPortDataObjects_ObjectIdentity=ObjectIdentity
rbtwsPortDataObjects=_RbtwsPortDataObjects_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,6,1,1))
_RbtwsPortConfigTable_Object=MibTable
rbtwsPortConfigTable=_RbtwsPortConfigTable_Object((1,3,6,1,4,1,52,4,15,1,4,6,1,1,1))
if mibBuilder.loadTexts:rbtwsPortConfigTable.setStatus(_A)
_RbtwsPortConfigEntry_Object=MibTableRow
rbtwsPortConfigEntry=_RbtwsPortConfigEntry_Object((1,3,6,1,4,1,52,4,15,1,4,6,1,1,1,1))
rbtwsPortConfigEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:rbtwsPortConfigEntry.setStatus(_A)
_RbtwsPortConfigPortNumber_Type=RbtwsPhysPortNumber
_RbtwsPortConfigPortNumber_Object=MibTableColumn
rbtwsPortConfigPortNumber=_RbtwsPortConfigPortNumber_Object((1,3,6,1,4,1,52,4,15,1,4,6,1,1,1,1,1),_RbtwsPortConfigPortNumber_Type())
rbtwsPortConfigPortNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rbtwsPortConfigPortNumber.setStatus(_A)
_RbtwsPortConfigPortMode_Type=RbtwsPortMode
_RbtwsPortConfigPortMode_Object=MibTableColumn
rbtwsPortConfigPortMode=_RbtwsPortConfigPortMode_Object((1,3,6,1,4,1,52,4,15,1,4,6,1,1,1,1,2),_RbtwsPortConfigPortMode_Type())
rbtwsPortConfigPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsPortConfigPortMode.setStatus(_A)
_RbtwsPortConfigPoeMode_Type=RbtwsPortPoeMode
_RbtwsPortConfigPoeMode_Object=MibTableColumn
rbtwsPortConfigPoeMode=_RbtwsPortConfigPoeMode_Object((1,3,6,1,4,1,52,4,15,1,4,6,1,1,1,1,3),_RbtwsPortConfigPoeMode_Type())
rbtwsPortConfigPoeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsPortConfigPoeMode.setStatus(_A)
_RbtwsPortConfigTrunkMaster_Type=RbtwsPhysPortNumber
_RbtwsPortConfigTrunkMaster_Object=MibTableColumn
rbtwsPortConfigTrunkMaster=_RbtwsPortConfigTrunkMaster_Object((1,3,6,1,4,1,52,4,15,1,4,6,1,1,1,1,4),_RbtwsPortConfigTrunkMaster_Type())
rbtwsPortConfigTrunkMaster.setMaxAccess(_C)
if mibBuilder.loadTexts:rbtwsPortConfigTrunkMaster.setStatus(_A)
_RbtwsPortConformance_ObjectIdentity=ObjectIdentity
rbtwsPortConformance=_RbtwsPortConformance_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,6,1,2))
_RbtwsPortCompliances_ObjectIdentity=ObjectIdentity
rbtwsPortCompliances=_RbtwsPortCompliances_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,6,1,2,1))
_RbtwsPortGroups_ObjectIdentity=ObjectIdentity
rbtwsPortGroups=_RbtwsPortGroups_ObjectIdentity((1,3,6,1,4,1,52,4,15,1,4,6,1,2,2))
rbtwsPortConfigGroup=ObjectGroup((1,3,6,1,4,1,52,4,15,1,4,6,1,2,2,1))
rbtwsPortConfigGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:rbtwsPortConfigGroup.setStatus(_A)
rbtwsPortCompliance=ModuleCompliance((1,3,6,1,4,1,52,4,15,1,4,6,1,2,1,1))
rbtwsPortCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:rbtwsPortCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'RbtwsPhysPortNumber':RbtwsPhysPortNumber,'RbtwsPortMode':RbtwsPortMode,'RbtwsPortPoeMode':RbtwsPortPoeMode,'rbtwsPortMib':rbtwsPortMib,'rbtwsPortObjects':rbtwsPortObjects,'rbtwsPortDataObjects':rbtwsPortDataObjects,'rbtwsPortConfigTable':rbtwsPortConfigTable,'rbtwsPortConfigEntry':rbtwsPortConfigEntry,_D:rbtwsPortConfigPortNumber,_E:rbtwsPortConfigPortMode,_F:rbtwsPortConfigPoeMode,_G:rbtwsPortConfigTrunkMaster,'rbtwsPortConformance':rbtwsPortConformance,'rbtwsPortCompliances':rbtwsPortCompliances,'rbtwsPortCompliance':rbtwsPortCompliance,'rbtwsPortGroups':rbtwsPortGroups,_H:rbtwsPortConfigGroup})