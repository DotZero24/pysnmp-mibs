_D='bsIfExtIfIndex'
_C='BAY-STACK-IF-EXT-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackIfExtMib=ModuleIdentity((1,3,6,1,4,1,45,5,40))
if mibBuilder.loadTexts:bayStackIfExtMib.setRevisions(('2012-05-31 00:00','2010-11-03 00:00'))
_BsIfExtNotifications_ObjectIdentity=ObjectIdentity
bsIfExtNotifications=_BsIfExtNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,40,0))
_BsIfExtObjects_ObjectIdentity=ObjectIdentity
bsIfExtObjects=_BsIfExtObjects_ObjectIdentity((1,3,6,1,4,1,45,5,40,1))
_BsIfExtScalars_ObjectIdentity=ObjectIdentity
bsIfExtScalars=_BsIfExtScalars_ObjectIdentity((1,3,6,1,4,1,45,5,40,1,1))
_BsIfExtDirectedBroadcast_Type=TruthValue
_BsIfExtDirectedBroadcast_Object=MibScalar
bsIfExtDirectedBroadcast=_BsIfExtDirectedBroadcast_Object((1,3,6,1,4,1,45,5,40,1,1,1),_BsIfExtDirectedBroadcast_Type())
bsIfExtDirectedBroadcast.setMaxAccess(_B)
if mibBuilder.loadTexts:bsIfExtDirectedBroadcast.setStatus(_A)
_BsIfExtIfTable_Object=MibTable
bsIfExtIfTable=_BsIfExtIfTable_Object((1,3,6,1,4,1,45,5,40,1,2))
if mibBuilder.loadTexts:bsIfExtIfTable.setStatus(_A)
_BsIfExtIfEntry_Object=MibTableRow
bsIfExtIfEntry=_BsIfExtIfEntry_Object((1,3,6,1,4,1,45,5,40,1,2,1))
bsIfExtIfEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:bsIfExtIfEntry.setStatus(_A)
_BsIfExtIfIndex_Type=InterfaceIndex
_BsIfExtIfIndex_Object=MibTableColumn
bsIfExtIfIndex=_BsIfExtIfIndex_Object((1,3,6,1,4,1,45,5,40,1,2,1,1),_BsIfExtIfIndex_Type())
bsIfExtIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:bsIfExtIfIndex.setStatus(_A)
_BsIfExtIfDirectedBroadcast_Type=TruthValue
_BsIfExtIfDirectedBroadcast_Object=MibTableColumn
bsIfExtIfDirectedBroadcast=_BsIfExtIfDirectedBroadcast_Object((1,3,6,1,4,1,45,5,40,1,2,1,2),_BsIfExtIfDirectedBroadcast_Type())
bsIfExtIfDirectedBroadcast.setMaxAccess(_B)
if mibBuilder.loadTexts:bsIfExtIfDirectedBroadcast.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'bayStackIfExtMib':bayStackIfExtMib,'bsIfExtNotifications':bsIfExtNotifications,'bsIfExtObjects':bsIfExtObjects,'bsIfExtScalars':bsIfExtScalars,'bsIfExtDirectedBroadcast':bsIfExtDirectedBroadcast,'bsIfExtIfTable':bsIfExtIfTable,'bsIfExtIfEntry':bsIfExtIfEntry,_D:bsIfExtIfIndex,'bsIfExtIfDirectedBroadcast':bsIfExtIfDirectedBroadcast})