_G='eltQosClassStatsClassIndex'
_F='eltQosPolicyStatsPolicyIndex'
_E='ELTEX-QOS-MIB'
_D='Integer32'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltexLtd,=mibBuilder.importSymbols('ELTEX-SMI-ACTUAL','eltexLtd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
eltQos=ModuleIdentity((1,3,6,1,4,1,35265,20))
if mibBuilder.loadTexts:eltQos.setRevisions(('2015-04-23 00:00',))
_EltQosPolicyStats_ObjectIdentity=ObjectIdentity
eltQosPolicyStats=_EltQosPolicyStats_ObjectIdentity((1,3,6,1,4,1,35265,20,1))
_EltQosPolicyStatsTable_Object=MibTable
eltQosPolicyStatsTable=_EltQosPolicyStatsTable_Object((1,3,6,1,4,1,35265,20,1,1))
if mibBuilder.loadTexts:eltQosPolicyStatsTable.setStatus(_A)
_EltQosPolicyStatsEntry_Object=MibTableRow
eltQosPolicyStatsEntry=_EltQosPolicyStatsEntry_Object((1,3,6,1,4,1,35265,20,1,1,1))
eltQosPolicyStatsEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:eltQosPolicyStatsEntry.setStatus(_A)
class _EltQosPolicyStatsPolicyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EltQosPolicyStatsPolicyIndex_Type.__name__=_D
_EltQosPolicyStatsPolicyIndex_Object=MibTableColumn
eltQosPolicyStatsPolicyIndex=_EltQosPolicyStatsPolicyIndex_Object((1,3,6,1,4,1,35265,20,1,1,1,1),_EltQosPolicyStatsPolicyIndex_Type())
eltQosPolicyStatsPolicyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosPolicyStatsPolicyIndex.setStatus(_A)
class _EltQosPolicyStatsifDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EltQosPolicyStatsifDescr_Type.__name__=_C
_EltQosPolicyStatsifDescr_Object=MibTableColumn
eltQosPolicyStatsifDescr=_EltQosPolicyStatsifDescr_Object((1,3,6,1,4,1,35265,20,1,1,1,2),_EltQosPolicyStatsifDescr_Type())
eltQosPolicyStatsifDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosPolicyStatsifDescr.setStatus(_A)
class _EltQosPolicyStatsPolicy_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EltQosPolicyStatsPolicy_Type.__name__=_C
_EltQosPolicyStatsPolicy_Object=MibTableColumn
eltQosPolicyStatsPolicy=_EltQosPolicyStatsPolicy_Object((1,3,6,1,4,1,35265,20,1,1,1,3),_EltQosPolicyStatsPolicy_Type())
eltQosPolicyStatsPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosPolicyStatsPolicy.setStatus(_A)
_EltQosPolicyStatsBytes_Type=Counter64
_EltQosPolicyStatsBytes_Object=MibTableColumn
eltQosPolicyStatsBytes=_EltQosPolicyStatsBytes_Object((1,3,6,1,4,1,35265,20,1,1,1,4),_EltQosPolicyStatsBytes_Type())
eltQosPolicyStatsBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosPolicyStatsBytes.setStatus(_A)
_EltQosPolicyStatsPkts_Type=Counter64
_EltQosPolicyStatsPkts_Object=MibTableColumn
eltQosPolicyStatsPkts=_EltQosPolicyStatsPkts_Object((1,3,6,1,4,1,35265,20,1,1,1,5),_EltQosPolicyStatsPkts_Type())
eltQosPolicyStatsPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosPolicyStatsPkts.setStatus(_A)
_EltQosPolicyStatsDrops_Type=Counter64
_EltQosPolicyStatsDrops_Object=MibTableColumn
eltQosPolicyStatsDrops=_EltQosPolicyStatsDrops_Object((1,3,6,1,4,1,35265,20,1,1,1,6),_EltQosPolicyStatsDrops_Type())
eltQosPolicyStatsDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosPolicyStatsDrops.setStatus(_A)
_EltQosClassStats_ObjectIdentity=ObjectIdentity
eltQosClassStats=_EltQosClassStats_ObjectIdentity((1,3,6,1,4,1,35265,20,2))
_EltQosClassStatsTable_Object=MibTable
eltQosClassStatsTable=_EltQosClassStatsTable_Object((1,3,6,1,4,1,35265,20,2,1))
if mibBuilder.loadTexts:eltQosClassStatsTable.setStatus(_A)
_EltQosClassStatsEntry_Object=MibTableRow
eltQosClassStatsEntry=_EltQosClassStatsEntry_Object((1,3,6,1,4,1,35265,20,2,1,1))
eltQosClassStatsEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:eltQosClassStatsEntry.setStatus(_A)
class _EltQosClassStatsClassIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EltQosClassStatsClassIndex_Type.__name__=_D
_EltQosClassStatsClassIndex_Object=MibTableColumn
eltQosClassStatsClassIndex=_EltQosClassStatsClassIndex_Object((1,3,6,1,4,1,35265,20,2,1,1,1),_EltQosClassStatsClassIndex_Type())
eltQosClassStatsClassIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosClassStatsClassIndex.setStatus(_A)
class _EltQosClassStatsifDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EltQosClassStatsifDescr_Type.__name__=_C
_EltQosClassStatsifDescr_Object=MibTableColumn
eltQosClassStatsifDescr=_EltQosClassStatsifDescr_Object((1,3,6,1,4,1,35265,20,2,1,1,2),_EltQosClassStatsifDescr_Type())
eltQosClassStatsifDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosClassStatsifDescr.setStatus(_A)
class _EltQosClassStatsClass_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EltQosClassStatsClass_Type.__name__=_C
_EltQosClassStatsClass_Object=MibTableColumn
eltQosClassStatsClass=_EltQosClassStatsClass_Object((1,3,6,1,4,1,35265,20,2,1,1,3),_EltQosClassStatsClass_Type())
eltQosClassStatsClass.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosClassStatsClass.setStatus(_A)
class _EltQosClassStatsPolicy_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_EltQosClassStatsPolicy_Type.__name__=_C
_EltQosClassStatsPolicy_Object=MibTableColumn
eltQosClassStatsPolicy=_EltQosClassStatsPolicy_Object((1,3,6,1,4,1,35265,20,2,1,1,4),_EltQosClassStatsPolicy_Type())
eltQosClassStatsPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosClassStatsPolicy.setStatus(_A)
_EltQosClassStatsBytes_Type=Counter64
_EltQosClassStatsBytes_Object=MibTableColumn
eltQosClassStatsBytes=_EltQosClassStatsBytes_Object((1,3,6,1,4,1,35265,20,2,1,1,5),_EltQosClassStatsBytes_Type())
eltQosClassStatsBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosClassStatsBytes.setStatus(_A)
_EltQosClassStatsPkts_Type=Counter64
_EltQosClassStatsPkts_Object=MibTableColumn
eltQosClassStatsPkts=_EltQosClassStatsPkts_Object((1,3,6,1,4,1,35265,20,2,1,1,6),_EltQosClassStatsPkts_Type())
eltQosClassStatsPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosClassStatsPkts.setStatus(_A)
_EltQosClassStatsDrops_Type=Counter64
_EltQosClassStatsDrops_Object=MibTableColumn
eltQosClassStatsDrops=_EltQosClassStatsDrops_Object((1,3,6,1,4,1,35265,20,2,1,1,7),_EltQosClassStatsDrops_Type())
eltQosClassStatsDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:eltQosClassStatsDrops.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'eltQos':eltQos,'eltQosPolicyStats':eltQosPolicyStats,'eltQosPolicyStatsTable':eltQosPolicyStatsTable,'eltQosPolicyStatsEntry':eltQosPolicyStatsEntry,_F:eltQosPolicyStatsPolicyIndex,'eltQosPolicyStatsifDescr':eltQosPolicyStatsifDescr,'eltQosPolicyStatsPolicy':eltQosPolicyStatsPolicy,'eltQosPolicyStatsBytes':eltQosPolicyStatsBytes,'eltQosPolicyStatsPkts':eltQosPolicyStatsPkts,'eltQosPolicyStatsDrops':eltQosPolicyStatsDrops,'eltQosClassStats':eltQosClassStats,'eltQosClassStatsTable':eltQosClassStatsTable,'eltQosClassStatsEntry':eltQosClassStatsEntry,_G:eltQosClassStatsClassIndex,'eltQosClassStatsifDescr':eltQosClassStatsifDescr,'eltQosClassStatsClass':eltQosClassStatsClass,'eltQosClassStatsPolicy':eltQosClassStatsPolicy,'eltQosClassStatsBytes':eltQosClassStatsBytes,'eltQosClassStatsPkts':eltQosClassStatsPkts,'eltQosClassStatsDrops':eltQosClassStatsDrops})