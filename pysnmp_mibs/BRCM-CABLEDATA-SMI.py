_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
broadcom,=mibBuilder.importSymbols('BRCM-SMI','broadcom')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cableData=ModuleIdentity((1,3,6,1,4,1,4413,2))
if mibBuilder.loadTexts:cableData.setRevisions(('2007-05-21 00:00','2007-02-05 00:00','2002-07-31 00:00'))
_CableDataProducts_ObjectIdentity=ObjectIdentity
cableDataProducts=_CableDataProducts_ObjectIdentity((1,3,6,1,4,1,4413,2,1))
if mibBuilder.loadTexts:cableDataProducts.setStatus(_A)
_CableDataMgmt_ObjectIdentity=ObjectIdentity
cableDataMgmt=_CableDataMgmt_ObjectIdentity((1,3,6,1,4,1,4413,2,2))
if mibBuilder.loadTexts:cableDataMgmt.setStatus(_A)
_CableDataAgentCapability_ObjectIdentity=ObjectIdentity
cableDataAgentCapability=_CableDataAgentCapability_ObjectIdentity((1,3,6,1,4,1,4413,2,3))
if mibBuilder.loadTexts:cableDataAgentCapability.setStatus(_A)
_CableDataExperimental_ObjectIdentity=ObjectIdentity
cableDataExperimental=_CableDataExperimental_ObjectIdentity((1,3,6,1,4,1,4413,2,4))
if mibBuilder.loadTexts:cableDataExperimental.setStatus(_A)
_CableDataPrivate_ObjectIdentity=ObjectIdentity
cableDataPrivate=_CableDataPrivate_ObjectIdentity((1,3,6,1,4,1,4413,2,99))
if mibBuilder.loadTexts:cableDataPrivate.setStatus(_A)
mibBuilder.exportSymbols('BRCM-CABLEDATA-SMI',**{'cableData':cableData,'cableDataProducts':cableDataProducts,'cableDataMgmt':cableDataMgmt,'cableDataAgentCapability':cableDataAgentCapability,'cableDataExperimental':cableDataExperimental,'cableDataPrivate':cableDataPrivate})