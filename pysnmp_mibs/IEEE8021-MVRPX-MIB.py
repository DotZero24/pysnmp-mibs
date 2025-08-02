_K='ieee8021MvrpxReqdGroup'
_J='ieee8021MvrpxPortXmitZero'
_I='ieee8021MvrpxPortMvrpNewPropagated'
_H='ieee8021MvrpxPortNewOnly'
_G='ieee8021MvrpxPortEntry'
_F='systemGroup'
_E='SNMPv2-MIB'
_D='read-create'
_C='TruthValue'
_B='IEEE8021-MVRPX-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ieee8021BridgeBasePortEntry,=mibBuilder.importSymbols('IEEE8021-BRIDGE-MIB','ieee8021BridgeBasePortEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
systemGroup,=mibBuilder.importSymbols(_E,_F)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_C)
ieee8021MvrpxMib=ModuleIdentity((1,3,111,2,802,1,1,22))
if mibBuilder.loadTexts:ieee8021MvrpxMib.setRevisions(('2018-06-28 00:00','2014-12-15 00:00','2011-04-05 00:00'))
_Ieee8021MvrpxMIBObjects_ObjectIdentity=ObjectIdentity
ieee8021MvrpxMIBObjects=_Ieee8021MvrpxMIBObjects_ObjectIdentity((1,3,111,2,802,1,1,22,1))
_Ieee8021MvrpxPortTable_Object=MibTable
ieee8021MvrpxPortTable=_Ieee8021MvrpxPortTable_Object((1,3,111,2,802,1,1,22,1,1))
if mibBuilder.loadTexts:ieee8021MvrpxPortTable.setStatus(_A)
_Ieee8021MvrpxPortEntry_Object=MibTableRow
ieee8021MvrpxPortEntry=_Ieee8021MvrpxPortEntry_Object((1,3,111,2,802,1,1,22,1,1,1))
if mibBuilder.loadTexts:ieee8021MvrpxPortEntry.setStatus(_A)
class _Ieee8021MvrpxPortNewOnly_Type(TruthValue):defaultValue=2
_Ieee8021MvrpxPortNewOnly_Type.__name__=_C
_Ieee8021MvrpxPortNewOnly_Object=MibTableColumn
ieee8021MvrpxPortNewOnly=_Ieee8021MvrpxPortNewOnly_Object((1,3,111,2,802,1,1,22,1,1,1,1),_Ieee8021MvrpxPortNewOnly_Type())
ieee8021MvrpxPortNewOnly.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021MvrpxPortNewOnly.setStatus(_A)
class _Ieee8021MvrpxPortMvrpNewPropagated_Type(TruthValue):defaultValue=2
_Ieee8021MvrpxPortMvrpNewPropagated_Type.__name__=_C
_Ieee8021MvrpxPortMvrpNewPropagated_Object=MibTableColumn
ieee8021MvrpxPortMvrpNewPropagated=_Ieee8021MvrpxPortMvrpNewPropagated_Object((1,3,111,2,802,1,1,22,1,1,1,2),_Ieee8021MvrpxPortMvrpNewPropagated_Type())
ieee8021MvrpxPortMvrpNewPropagated.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021MvrpxPortMvrpNewPropagated.setStatus(_A)
class _Ieee8021MvrpxPortXmitZero_Type(TruthValue):defaultValue=2
_Ieee8021MvrpxPortXmitZero_Type.__name__=_C
_Ieee8021MvrpxPortXmitZero_Object=MibTableColumn
ieee8021MvrpxPortXmitZero=_Ieee8021MvrpxPortXmitZero_Object((1,3,111,2,802,1,1,22,1,1,1,3),_Ieee8021MvrpxPortXmitZero_Type())
ieee8021MvrpxPortXmitZero.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021MvrpxPortXmitZero.setStatus(_A)
_Ieee8021MvrpxConformance_ObjectIdentity=ObjectIdentity
ieee8021MvrpxConformance=_Ieee8021MvrpxConformance_ObjectIdentity((1,3,111,2,802,1,1,22,2))
_Ieee8021MvrpxCompliances_ObjectIdentity=ObjectIdentity
ieee8021MvrpxCompliances=_Ieee8021MvrpxCompliances_ObjectIdentity((1,3,111,2,802,1,1,22,2,1))
_Ieee8021MvrpxGroups_ObjectIdentity=ObjectIdentity
ieee8021MvrpxGroups=_Ieee8021MvrpxGroups_ObjectIdentity((1,3,111,2,802,1,1,22,2,2))
ieee8021BridgeBasePortEntry.registerAugmentions((_B,_G))
ieee8021MvrpxPortEntry.setIndexNames(*ieee8021BridgeBasePortEntry.getIndexNames())
ieee8021MvrpxReqdGroup=ObjectGroup((1,3,111,2,802,1,1,22,2,2,1))
ieee8021MvrpxReqdGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:ieee8021MvrpxReqdGroup.setStatus(_A)
ieee8021MvrpxCompliance=ModuleCompliance((1,3,111,2,802,1,1,22,2,1,1))
ieee8021MvrpxCompliance.setObjects(*((_E,_F),(_B,_K)))
if mibBuilder.loadTexts:ieee8021MvrpxCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ieee8021MvrpxMib':ieee8021MvrpxMib,'ieee8021MvrpxMIBObjects':ieee8021MvrpxMIBObjects,'ieee8021MvrpxPortTable':ieee8021MvrpxPortTable,_G:ieee8021MvrpxPortEntry,_H:ieee8021MvrpxPortNewOnly,_I:ieee8021MvrpxPortMvrpNewPropagated,_J:ieee8021MvrpxPortXmitZero,'ieee8021MvrpxConformance':ieee8021MvrpxConformance,'ieee8021MvrpxCompliances':ieee8021MvrpxCompliances,'ieee8021MvrpxCompliance':ieee8021MvrpxCompliance,'ieee8021MvrpxGroups':ieee8021MvrpxGroups,_K:ieee8021MvrpxReqdGroup})