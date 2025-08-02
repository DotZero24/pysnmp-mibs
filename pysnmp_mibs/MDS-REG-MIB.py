_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mdsGlobalRegModule=ModuleIdentity((1,3,6,1,4,1,4130,4))
if mibBuilder.loadTexts:mdsGlobalRegModule.setRevisions(('2006-02-08 00:00',))
_MdsRoot_ObjectIdentity=ObjectIdentity
mdsRoot=_MdsRoot_ObjectIdentity((1,3,6,1,4,1,4130))
if mibBuilder.loadTexts:mdsRoot.setStatus(_A)
_MdsWideband_ObjectIdentity=ObjectIdentity
mdsWideband=_MdsWideband_ObjectIdentity((1,3,6,1,4,1,4130,1))
if mibBuilder.loadTexts:mdsWideband.setStatus(_A)
_MdsPointToPoint_ObjectIdentity=ObjectIdentity
mdsPointToPoint=_MdsPointToPoint_ObjectIdentity((1,3,6,1,4,1,4130,1,1))
if mibBuilder.loadTexts:mdsPointToPoint.setStatus(_A)
_MdsNarrowband_ObjectIdentity=ObjectIdentity
mdsNarrowband=_MdsNarrowband_ObjectIdentity((1,3,6,1,4,1,4130,2))
if mibBuilder.loadTexts:mdsNarrowband.setStatus(_A)
_MdsPointToMultiPoint_ObjectIdentity=ObjectIdentity
mdsPointToMultiPoint=_MdsPointToMultiPoint_ObjectIdentity((1,3,6,1,4,1,4130,2,1))
if mibBuilder.loadTexts:mdsPointToMultiPoint.setStatus(_A)
_MdsBroadband_ObjectIdentity=ObjectIdentity
mdsBroadband=_MdsBroadband_ObjectIdentity((1,3,6,1,4,1,4130,3))
if mibBuilder.loadTexts:mdsBroadband.setStatus(_A)
_MdsSoftware_ObjectIdentity=ObjectIdentity
mdsSoftware=_MdsSoftware_ObjectIdentity((1,3,6,1,4,1,4130,9))
if mibBuilder.loadTexts:mdsSoftware.setStatus(_A)
mibBuilder.exportSymbols('MDS-REG-MIB',**{'mdsRoot':mdsRoot,'mdsWideband':mdsWideband,'mdsPointToPoint':mdsPointToPoint,'mdsNarrowband':mdsNarrowband,'mdsPointToMultiPoint':mdsPointToMultiPoint,'mdsBroadband':mdsBroadband,'mdsGlobalRegModule':mdsGlobalRegModule,'mdsSoftware':mdsSoftware})