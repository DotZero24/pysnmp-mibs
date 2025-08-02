_G='zyQueuingMethodPortQueue'
_F='ZYXEL-QUEUING-METHOD-MIB'
_E='read-write'
_D='Integer32'
_C='dot1dBasePort'
_B='BRIDGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_B,_C)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelQueuingMethod=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,70))
_ZyxelQueuingMethodSetup_ObjectIdentity=ObjectIdentity
zyxelQueuingMethodSetup=_ZyxelQueuingMethodSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,70,1))
_ZyxelQueuingMethodPortTable_Object=MibTable
zyxelQueuingMethodPortTable=_ZyxelQueuingMethodPortTable_Object((1,3,6,1,4,1,890,1,15,3,70,1,1))
if mibBuilder.loadTexts:zyxelQueuingMethodPortTable.setStatus(_A)
_ZyxelQueuingMethodPortEntry_Object=MibTableRow
zyxelQueuingMethodPortEntry=_ZyxelQueuingMethodPortEntry_Object((1,3,6,1,4,1,890,1,15,3,70,1,1,1))
zyxelQueuingMethodPortEntry.setIndexNames((0,_B,_C),(0,_F,_G))
if mibBuilder.loadTexts:zyxelQueuingMethodPortEntry.setStatus(_A)
_ZyQueuingMethodPortQueue_Type=Integer32
_ZyQueuingMethodPortQueue_Object=MibTableColumn
zyQueuingMethodPortQueue=_ZyQueuingMethodPortQueue_Object((1,3,6,1,4,1,890,1,15,3,70,1,1,1,1),_ZyQueuingMethodPortQueue_Type())
zyQueuingMethodPortQueue.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zyQueuingMethodPortQueue.setStatus(_A)
_ZyQueuingMethodPortWeight_Type=Integer32
_ZyQueuingMethodPortWeight_Object=MibTableColumn
zyQueuingMethodPortWeight=_ZyQueuingMethodPortWeight_Object((1,3,6,1,4,1,890,1,15,3,70,1,1,1,2),_ZyQueuingMethodPortWeight_Type())
zyQueuingMethodPortWeight.setMaxAccess(_E)
if mibBuilder.loadTexts:zyQueuingMethodPortWeight.setStatus(_A)
class _ZyQueuingMethodPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('strictlyPriority',0),('weightedFairScheduling',1),('weightedRoundRobin',2)))
_ZyQueuingMethodPortMode_Type.__name__=_D
_ZyQueuingMethodPortMode_Object=MibTableColumn
zyQueuingMethodPortMode=_ZyQueuingMethodPortMode_Object((1,3,6,1,4,1,890,1,15,3,70,1,1,1,3),_ZyQueuingMethodPortMode_Type())
zyQueuingMethodPortMode.setMaxAccess(_E)
if mibBuilder.loadTexts:zyQueuingMethodPortMode.setStatus(_A)
_ZyxelQueuingMethodHybridSpqPortTable_Object=MibTable
zyxelQueuingMethodHybridSpqPortTable=_ZyxelQueuingMethodHybridSpqPortTable_Object((1,3,6,1,4,1,890,1,15,3,70,1,2))
if mibBuilder.loadTexts:zyxelQueuingMethodHybridSpqPortTable.setStatus(_A)
_ZyxelQueuingMethodHybridSpqPortEntry_Object=MibTableRow
zyxelQueuingMethodHybridSpqPortEntry=_ZyxelQueuingMethodHybridSpqPortEntry_Object((1,3,6,1,4,1,890,1,15,3,70,1,2,1))
zyxelQueuingMethodHybridSpqPortEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:zyxelQueuingMethodHybridSpqPortEntry.setStatus(_A)
class _ZyQueuingMethodHybridSpqPortQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('none',0),('q0',1),('q1',2),('q2',3),('q3',4),('q4',5),('q5',6),('q6',7),('q7',8)))
_ZyQueuingMethodHybridSpqPortQueue_Type.__name__=_D
_ZyQueuingMethodHybridSpqPortQueue_Object=MibTableColumn
zyQueuingMethodHybridSpqPortQueue=_ZyQueuingMethodHybridSpqPortQueue_Object((1,3,6,1,4,1,890,1,15,3,70,1,2,1,1),_ZyQueuingMethodHybridSpqPortQueue_Type())
zyQueuingMethodHybridSpqPortQueue.setMaxAccess(_E)
if mibBuilder.loadTexts:zyQueuingMethodHybridSpqPortQueue.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'zyxelQueuingMethod':zyxelQueuingMethod,'zyxelQueuingMethodSetup':zyxelQueuingMethodSetup,'zyxelQueuingMethodPortTable':zyxelQueuingMethodPortTable,'zyxelQueuingMethodPortEntry':zyxelQueuingMethodPortEntry,_G:zyQueuingMethodPortQueue,'zyQueuingMethodPortWeight':zyQueuingMethodPortWeight,'zyQueuingMethodPortMode':zyQueuingMethodPortMode,'zyxelQueuingMethodHybridSpqPortTable':zyxelQueuingMethodHybridSpqPortTable,'zyxelQueuingMethodHybridSpqPortEntry':zyxelQueuingMethodHybridSpqPortEntry,'zyQueuingMethodHybridSpqPortQueue':zyQueuingMethodHybridSpqPortQueue})