_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alcatelNGOAWBaseMIB=ModuleIdentity((1,3,6,1,4,1,6486,802))
if mibBuilder.loadTexts:alcatelNGOAWBaseMIB.setRevisions(('2016-09-01 00:00',))
_Alcatel_ObjectIdentity=ObjectIdentity
alcatel=_Alcatel_ObjectIdentity((1,3,6,1,4,1,6486))
if mibBuilder.loadTexts:alcatel.setStatus(_A)
_AlcatelNGOAWManagement_ObjectIdentity=ObjectIdentity
alcatelNGOAWManagement=_AlcatelNGOAWManagement_ObjectIdentity((1,3,6,1,4,1,6486,802,1))
if mibBuilder.loadTexts:alcatelNGOAWManagement.setStatus(_A)
_ManagementNGOAWHardware_ObjectIdentity=ObjectIdentity
managementNGOAWHardware=_ManagementNGOAWHardware_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1))
if mibBuilder.loadTexts:managementNGOAWHardware.setStatus(_A)
_HardwareNGOAWEntities_ObjectIdentity=ObjectIdentity
hardwareNGOAWEntities=_HardwareNGOAWEntities_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,1))
if mibBuilder.loadTexts:hardwareNGOAWEntities.setStatus(_A)
_HardwareNGOAWDevices_ObjectIdentity=ObjectIdentity
hardwareNGOAWDevices=_HardwareNGOAWDevices_ObjectIdentity((1,3,6,1,4,1,6486,802,1,1,2))
if mibBuilder.loadTexts:hardwareNGOAWDevices.setStatus(_A)
_ManagementNGOAWSoftware_ObjectIdentity=ObjectIdentity
managementNGOAWSoftware=_ManagementNGOAWSoftware_ObjectIdentity((1,3,6,1,4,1,6486,802,1,2))
if mibBuilder.loadTexts:managementNGOAWSoftware.setStatus(_A)
_SoftwareNGOAWEntities_ObjectIdentity=ObjectIdentity
softwareNGOAWEntities=_SoftwareNGOAWEntities_ObjectIdentity((1,3,6,1,4,1,6486,802,1,2,1))
if mibBuilder.loadTexts:softwareNGOAWEntities.setStatus(_A)
_SoftwareNGOAWServices_ObjectIdentity=ObjectIdentity
softwareNGOAWServices=_SoftwareNGOAWServices_ObjectIdentity((1,3,6,1,4,1,6486,802,1,2,2))
if mibBuilder.loadTexts:softwareNGOAWServices.setStatus(_A)
_ManagementNGOAWAgentCapabilities_ObjectIdentity=ObjectIdentity
managementNGOAWAgentCapabilities=_ManagementNGOAWAgentCapabilities_ObjectIdentity((1,3,6,1,4,1,6486,802,1,4))
if mibBuilder.loadTexts:managementNGOAWAgentCapabilities.setStatus(_A)
mibBuilder.exportSymbols('ALCATEL-NGOAW-BASE-MIB',**{'alcatel':alcatel,'alcatelNGOAWBaseMIB':alcatelNGOAWBaseMIB,'alcatelNGOAWManagement':alcatelNGOAWManagement,'managementNGOAWHardware':managementNGOAWHardware,'hardwareNGOAWEntities':hardwareNGOAWEntities,'hardwareNGOAWDevices':hardwareNGOAWDevices,'managementNGOAWSoftware':managementNGOAWSoftware,'softwareNGOAWEntities':softwareNGOAWEntities,'softwareNGOAWServices':softwareNGOAWServices,'managementNGOAWAgentCapabilities':managementNGOAWAgentCapabilities})