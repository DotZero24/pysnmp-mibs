if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rdnDefinitions,=mibBuilder.importSymbols('RDN-DEFINITIONS-MIB','rdnDefinitions')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rdnSensorTypes=ModuleIdentity((1,3,6,1,4,1,4981,4,6))
if mibBuilder.loadTexts:rdnSensorTypes.setRevisions(('2008-08-08 00:00','2003-11-05 00:00','2001-08-07 00:00'))
_RdnSensorsUnknown_ObjectIdentity=ObjectIdentity
rdnSensorsUnknown=_RdnSensorsUnknown_ObjectIdentity((1,3,6,1,4,1,4981,4,6,0))
_RdnSensorsSRM750_ObjectIdentity=ObjectIdentity
rdnSensorsSRM750=_RdnSensorsSRM750_ObjectIdentity((1,3,6,1,4,1,4981,4,6,1))
_RdnSensorsSRMDIMM_ObjectIdentity=ObjectIdentity
rdnSensorsSRMDIMM=_RdnSensorsSRMDIMM_ObjectIdentity((1,3,6,1,4,1,4981,4,6,2))
_RdnSensorsSRMDC2DC_ObjectIdentity=ObjectIdentity
rdnSensorsSRMDC2DC=_RdnSensorsSRMDC2DC_ObjectIdentity((1,3,6,1,4,1,4981,4,6,3))
_RdnSensorsSRMXFAB_ObjectIdentity=ObjectIdentity
rdnSensorsSRMXFAB=_RdnSensorsSRMXFAB_ObjectIdentity((1,3,6,1,4,1,4981,4,6,4))
_RdnSensorsFan_ObjectIdentity=ObjectIdentity
rdnSensorsFan=_RdnSensorsFan_ObjectIdentity((1,3,6,1,4,1,4981,4,6,5))
mibBuilder.exportSymbols('RDN-SENSOR-TYPE-MIB',**{'rdnSensorTypes':rdnSensorTypes,'rdnSensorsUnknown':rdnSensorsUnknown,'rdnSensorsSRM750':rdnSensorsSRM750,'rdnSensorsSRMDIMM':rdnSensorsSRMDIMM,'rdnSensorsSRMDC2DC':rdnSensorsSRMDC2DC,'rdnSensorsSRMXFAB':rdnSensorsSRMXFAB,'rdnSensorsFan':rdnSensorsFan})