if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adComplianceShared,adIdentityShared,adShared=mibBuilder.importSymbols('ADTRAN-MIB','adComplianceShared','adIdentityShared','adShared')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenErpsModuleIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,79))
_AdGenErpsModule_ObjectIdentity=ObjectIdentity
adGenErpsModule=_AdGenErpsModule_ObjectIdentity((1,3,6,1,4,1,664,5,79))
_AdGenErps_ObjectIdentity=ObjectIdentity
adGenErps=_AdGenErps_ObjectIdentity((1,3,6,1,4,1,664,5,79,1))
_AdGenErpsID_ObjectIdentity=ObjectIdentity
adGenErpsID=_AdGenErpsID_ObjectIdentity((1,3,6,1,4,1,664,6,10000,79,1))
_AdGenErpsCompliance_ObjectIdentity=ObjectIdentity
adGenErpsCompliance=_AdGenErpsCompliance_ObjectIdentity((1,3,6,1,4,1,664,99,10000,79))
mibBuilder.exportSymbols('ADTRAN-ERPS-CONTAINER-MIB',**{'adGenErpsModule':adGenErpsModule,'adGenErps':adGenErps,'adGenErpsModuleIdentity':adGenErpsModuleIdentity,'adGenErpsID':adGenErpsID,'adGenErpsCompliance':adGenErpsCompliance})