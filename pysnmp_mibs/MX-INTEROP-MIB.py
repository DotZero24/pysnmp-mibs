_E='mxInteropGroupVer1'
_D='mxInteropHttpUAHeaderConfig'
_C='OctetString'
_B='MX-INTEROP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixExperimental,=mibBuilder.importSymbols('MX-SMI','mediatrixExperimental')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mxInteropMIB=ModuleIdentity((1,3,6,1,4,1,4935,99,3))
if mibBuilder.loadTexts:mxInteropMIB.setRevisions(('1911-01-21 00:00',))
_MxInteropMIBObjects_ObjectIdentity=ObjectIdentity
mxInteropMIBObjects=_MxInteropMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,99,3,1))
class _MxInteropHttpUAHeaderConfig_Type(OctetString):defaultValue=OctetString('%product%');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MxInteropHttpUAHeaderConfig_Type.__name__=_C
_MxInteropHttpUAHeaderConfig_Object=MibScalar
mxInteropHttpUAHeaderConfig=_MxInteropHttpUAHeaderConfig_Object((1,3,6,1,4,1,4935,99,3,1,10),_MxInteropHttpUAHeaderConfig_Type())
mxInteropHttpUAHeaderConfig.setMaxAccess('read-write')
if mibBuilder.loadTexts:mxInteropHttpUAHeaderConfig.setStatus(_A)
_MxInteropConformance_ObjectIdentity=ObjectIdentity
mxInteropConformance=_MxInteropConformance_ObjectIdentity((1,3,6,1,4,1,4935,99,3,2))
_MxInteropCompliances_ObjectIdentity=ObjectIdentity
mxInteropCompliances=_MxInteropCompliances_ObjectIdentity((1,3,6,1,4,1,4935,99,3,2,1))
_MxInteropGroups_ObjectIdentity=ObjectIdentity
mxInteropGroups=_MxInteropGroups_ObjectIdentity((1,3,6,1,4,1,4935,99,3,2,2))
mxInteropGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,99,3,2,2,5))
mxInteropGroupVer1.setObjects((_B,_D))
if mibBuilder.loadTexts:mxInteropGroupVer1.setStatus(_A)
mxInteropBasicComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,99,3,2,1,1))
mxInteropBasicComplVer1.setObjects((_B,_E))
if mibBuilder.loadTexts:mxInteropBasicComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mxInteropMIB':mxInteropMIB,'mxInteropMIBObjects':mxInteropMIBObjects,_D:mxInteropHttpUAHeaderConfig,'mxInteropConformance':mxInteropConformance,'mxInteropCompliances':mxInteropCompliances,'mxInteropBasicComplVer1':mxInteropBasicComplVer1,'mxInteropGroups':mxInteropGroups,_E:mxInteropGroupVer1})