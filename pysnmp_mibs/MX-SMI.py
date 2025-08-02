_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mediatrix=ModuleIdentity((1,3,6,1,4,1,4935))
if mibBuilder.loadTexts:mediatrix.setRevisions(('1901-08-07 00:00',))
_MediatrixProducts_ObjectIdentity=ObjectIdentity
mediatrixProducts=_MediatrixProducts_ObjectIdentity((1,3,6,1,4,1,4935,1))
if mibBuilder.loadTexts:mediatrixProducts.setStatus(_A)
_MediatrixAdmin_ObjectIdentity=ObjectIdentity
mediatrixAdmin=_MediatrixAdmin_ObjectIdentity((1,3,6,1,4,1,4935,5))
if mibBuilder.loadTexts:mediatrixAdmin.setStatus(_A)
_MediatrixMgmt_ObjectIdentity=ObjectIdentity
mediatrixMgmt=_MediatrixMgmt_ObjectIdentity((1,3,6,1,4,1,4935,10))
if mibBuilder.loadTexts:mediatrixMgmt.setStatus(_A)
_IpAddressStatus_ObjectIdentity=ObjectIdentity
ipAddressStatus=_IpAddressStatus_ObjectIdentity((1,3,6,1,4,1,4935,10,1))
if mibBuilder.loadTexts:ipAddressStatus.setStatus(_A)
_MediatrixConfig_ObjectIdentity=ObjectIdentity
mediatrixConfig=_MediatrixConfig_ObjectIdentity((1,3,6,1,4,1,4935,15))
if mibBuilder.loadTexts:mediatrixConfig.setStatus(_A)
_IpAddressConfig_ObjectIdentity=ObjectIdentity
ipAddressConfig=_IpAddressConfig_ObjectIdentity((1,3,6,1,4,1,4935,15,1))
if mibBuilder.loadTexts:ipAddressConfig.setStatus(_A)
_MediatrixIpTelephonySignaling_ObjectIdentity=ObjectIdentity
mediatrixIpTelephonySignaling=_MediatrixIpTelephonySignaling_ObjectIdentity((1,3,6,1,4,1,4935,20))
if mibBuilder.loadTexts:mediatrixIpTelephonySignaling.setStatus(_A)
_MediatrixModules_ObjectIdentity=ObjectIdentity
mediatrixModules=_MediatrixModules_ObjectIdentity((1,3,6,1,4,1,4935,90))
if mibBuilder.loadTexts:mediatrixModules.setStatus(_A)
_MediatrixExperimental_ObjectIdentity=ObjectIdentity
mediatrixExperimental=_MediatrixExperimental_ObjectIdentity((1,3,6,1,4,1,4935,99))
if mibBuilder.loadTexts:mediatrixExperimental.setStatus(_A)
mibBuilder.exportSymbols('MX-SMI',**{'mediatrix':mediatrix,'mediatrixProducts':mediatrixProducts,'mediatrixAdmin':mediatrixAdmin,'mediatrixMgmt':mediatrixMgmt,'ipAddressStatus':ipAddressStatus,'mediatrixConfig':mediatrixConfig,'ipAddressConfig':ipAddressConfig,'mediatrixIpTelephonySignaling':mediatrixIpTelephonySignaling,'mediatrixModules':mediatrixModules,'mediatrixExperimental':mediatrixExperimental})