_K='oacExpIMDot11GeneralGroup'
_J='oacExpIMDot11AssociatedStations'
_I='oacExpIMDot11SSID'
_H='oacExpIMDot11MACAddress'
_G='oacExpIMDot11EntryType'
_F='ifIndex'
_E='IF-MIB'
_D='OctetString'
_C='read-only'
_B='ONEACCESS-DOT11-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
oacExpIMDot11,oacMIBModules,oacRequirements=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMDot11','oacMIBModules','oacRequirements')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
oacDot11MIBModule=ModuleIdentity((1,3,6,1,4,1,13191,1,100,900))
if mibBuilder.loadTexts:oacDot11MIBModule.setRevisions(('2011-10-27 00:00','2010-07-08 00:01'))
class InterfaceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mainInterface',1),('subInterface',2)))
_OacExpIMDot11Conformance_ObjectIdentity=ObjectIdentity
oacExpIMDot11Conformance=_OacExpIMDot11Conformance_ObjectIdentity((1,3,6,1,4,1,13191,5,900))
_OacExpIMDot11Groups_ObjectIdentity=ObjectIdentity
oacExpIMDot11Groups=_OacExpIMDot11Groups_ObjectIdentity((1,3,6,1,4,1,13191,5,900,1))
_OacExpIMDot11Compliances_ObjectIdentity=ObjectIdentity
oacExpIMDot11Compliances=_OacExpIMDot11Compliances_ObjectIdentity((1,3,6,1,4,1,13191,5,900,2))
_OacExpIMDot11Objects_ObjectIdentity=ObjectIdentity
oacExpIMDot11Objects=_OacExpIMDot11Objects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,8,1))
_OacExpIMDot11InterfaceTable_Object=MibTable
oacExpIMDot11InterfaceTable=_OacExpIMDot11InterfaceTable_Object((1,3,6,1,4,1,13191,10,3,8,1,1))
if mibBuilder.loadTexts:oacExpIMDot11InterfaceTable.setStatus(_A)
_OacExpIMDot11InterfaceEntry_Object=MibTableRow
oacExpIMDot11InterfaceEntry=_OacExpIMDot11InterfaceEntry_Object((1,3,6,1,4,1,13191,10,3,8,1,1,1))
oacExpIMDot11InterfaceEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:oacExpIMDot11InterfaceEntry.setStatus(_A)
_OacExpIMDot11EntryType_Type=InterfaceType
_OacExpIMDot11EntryType_Object=MibTableColumn
oacExpIMDot11EntryType=_OacExpIMDot11EntryType_Object((1,3,6,1,4,1,13191,10,3,8,1,1,1,1),_OacExpIMDot11EntryType_Type())
oacExpIMDot11EntryType.setMaxAccess(_C)
if mibBuilder.loadTexts:oacExpIMDot11EntryType.setStatus(_A)
_OacExpIMDot11MACAddress_Type=MacAddress
_OacExpIMDot11MACAddress_Object=MibTableColumn
oacExpIMDot11MACAddress=_OacExpIMDot11MACAddress_Object((1,3,6,1,4,1,13191,10,3,8,1,1,1,2),_OacExpIMDot11MACAddress_Type())
oacExpIMDot11MACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:oacExpIMDot11MACAddress.setStatus(_A)
class _OacExpIMDot11SSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_OacExpIMDot11SSID_Type.__name__=_D
_OacExpIMDot11SSID_Object=MibTableColumn
oacExpIMDot11SSID=_OacExpIMDot11SSID_Object((1,3,6,1,4,1,13191,10,3,8,1,1,1,3),_OacExpIMDot11SSID_Type())
oacExpIMDot11SSID.setMaxAccess(_C)
if mibBuilder.loadTexts:oacExpIMDot11SSID.setStatus(_A)
_OacExpIMDot11AssociatedStations_Type=Counter32
_OacExpIMDot11AssociatedStations_Object=MibTableColumn
oacExpIMDot11AssociatedStations=_OacExpIMDot11AssociatedStations_Object((1,3,6,1,4,1,13191,10,3,8,1,1,1,4),_OacExpIMDot11AssociatedStations_Type())
oacExpIMDot11AssociatedStations.setMaxAccess(_C)
if mibBuilder.loadTexts:oacExpIMDot11AssociatedStations.setStatus(_A)
oacExpIMDot11GeneralGroup=ObjectGroup((1,3,6,1,4,1,13191,5,900,1,1))
oacExpIMDot11GeneralGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:oacExpIMDot11GeneralGroup.setStatus(_A)
oacExpIMDot11Compliance=ModuleCompliance((1,3,6,1,4,1,13191,5,900,2,1))
oacExpIMDot11Compliance.setObjects((_B,_K))
if mibBuilder.loadTexts:oacExpIMDot11Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'InterfaceType':InterfaceType,'oacDot11MIBModule':oacDot11MIBModule,'oacExpIMDot11Conformance':oacExpIMDot11Conformance,'oacExpIMDot11Groups':oacExpIMDot11Groups,_K:oacExpIMDot11GeneralGroup,'oacExpIMDot11Compliances':oacExpIMDot11Compliances,'oacExpIMDot11Compliance':oacExpIMDot11Compliance,'oacExpIMDot11Objects':oacExpIMDot11Objects,'oacExpIMDot11InterfaceTable':oacExpIMDot11InterfaceTable,'oacExpIMDot11InterfaceEntry':oacExpIMDot11InterfaceEntry,_G:oacExpIMDot11EntryType,_H:oacExpIMDot11MACAddress,_I:oacExpIMDot11SSID,_J:oacExpIMDot11AssociatedStations})