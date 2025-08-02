_D='current'
_C='rndErrorSeverity'
_B='rndErrorDesc'
_A='RADLAN-DEVICEPARAMS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
elt,=mibBuilder.importSymbols('ELTEX-MIB','elt')
rldot1dStpTrapVrblVID,rldot1dStpTrapVrblifIndex=mibBuilder.importSymbols('RADLAN-BRIDGEMIBOBJECTS-MIB','rldot1dStpTrapVrblVID','rldot1dStpTrapVrblifIndex')
rndErrorDesc,rndErrorSeverity=mibBuilder.importSymbols(_A,_B,_C)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
eltNotifications=ModuleIdentity((1,3,6,1,4,1,35265,0))
if mibBuilder.loadTexts:eltNotifications.setRevisions(('2012-07-13 00:00',))
i2cBusFailure=NotificationType((1,3,6,1,4,1,35265,0,3))
i2cBusFailure.setObjects(*((_A,_B),(_A,_C)))
if mibBuilder.loadTexts:i2cBusFailure.setStatus(_D)
i2cBusOperational=NotificationType((1,3,6,1,4,1,35265,0,4))
i2cBusOperational.setObjects(*((_A,_B),(_A,_C)))
if mibBuilder.loadTexts:i2cBusOperational.setStatus(_D)
mibBuilder.exportSymbols('ELTEX-TRAPS-MIB',**{'eltNotifications':eltNotifications,'i2cBusFailure':i2cBusFailure,'i2cBusOperational':i2cBusOperational})