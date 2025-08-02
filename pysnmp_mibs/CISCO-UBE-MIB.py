_H='ciscoUbeMIBGroup'
_G='cubeTotalSessionAllowed'
_F='cubeVersion'
_E='cubeEnabled'
_D='read-write'
_C='Unsigned32'
_B='CISCO-UBE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoUbeMIB=ModuleIdentity((1,3,6,1,4,1,9,9,764))
if mibBuilder.loadTexts:ciscoUbeMIB.setRevisions(('2010-11-29 00:00',))
_CiscoUbeMIBObjects_ObjectIdentity=ObjectIdentity
ciscoUbeMIBObjects=_CiscoUbeMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,764,0))
_CubeEnabled_Type=TruthValue
_CubeEnabled_Object=MibScalar
cubeEnabled=_CubeEnabled_Object((1,3,6,1,4,1,9,9,764,0,1),_CubeEnabled_Type())
cubeEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:cubeEnabled.setStatus(_A)
_CubeVersion_Type=SnmpAdminString
_CubeVersion_Object=MibScalar
cubeVersion=_CubeVersion_Object((1,3,6,1,4,1,9,9,764,0,2),_CubeVersion_Type())
cubeVersion.setMaxAccess('read-only')
if mibBuilder.loadTexts:cubeVersion.setStatus(_A)
class _CubeTotalSessionAllowed_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999999))
_CubeTotalSessionAllowed_Type.__name__=_C
_CubeTotalSessionAllowed_Object=MibScalar
cubeTotalSessionAllowed=_CubeTotalSessionAllowed_Object((1,3,6,1,4,1,9,9,764,0,3),_CubeTotalSessionAllowed_Type())
cubeTotalSessionAllowed.setMaxAccess(_D)
if mibBuilder.loadTexts:cubeTotalSessionAllowed.setStatus(_A)
if mibBuilder.loadTexts:cubeTotalSessionAllowed.setUnits('session')
_CiscoUbeMIBConform_ObjectIdentity=ObjectIdentity
ciscoUbeMIBConform=_CiscoUbeMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,764,1))
_CiscoUbeMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoUbeMIBCompliances=_CiscoUbeMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,764,1,1))
_CiscoUbeMIBGroups_ObjectIdentity=ObjectIdentity
ciscoUbeMIBGroups=_CiscoUbeMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,764,1,2))
ciscoUbeMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,764,1,2,1))
ciscoUbeMIBGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:ciscoUbeMIBGroup.setStatus(_A)
ciscoCubeMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,764,1,1,1))
ciscoCubeMIBCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:ciscoCubeMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoUbeMIB':ciscoUbeMIB,'ciscoUbeMIBObjects':ciscoUbeMIBObjects,_E:cubeEnabled,_F:cubeVersion,_G:cubeTotalSessionAllowed,'ciscoUbeMIBConform':ciscoUbeMIBConform,'ciscoUbeMIBCompliances':ciscoUbeMIBCompliances,'ciscoCubeMIBCompliance':ciscoCubeMIBCompliance,'ciscoUbeMIBGroups':ciscoUbeMIBGroups,_H:ciscoUbeMIBGroup})