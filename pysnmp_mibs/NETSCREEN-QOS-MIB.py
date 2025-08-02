_I='nsQosPlyId'
_H='NETSCREEN-QOS-MIB'
_G='off-on'
_F='on-off'
_E='on'
_D='off'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenQos,=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenQos')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
netscreenQosMibModule=ModuleIdentity((1,3,6,1,4,1,3224,5,0))
if mibBuilder.loadTexts:netscreenQosMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2001-09-28 00:00','2001-05-15 00:00'))
class _NsQosUsrShapingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_D,0),(_E,1),(_F,2),(_G,3),('auto',4)))
_NsQosUsrShapingMode_Type.__name__=_C
_NsQosUsrShapingMode_Object=MibScalar
nsQosUsrShapingMode=_NsQosUsrShapingMode_Object((1,3,6,1,4,1,3224,5,1),_NsQosUsrShapingMode_Type())
nsQosUsrShapingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nsQosUsrShapingMode.setStatus(_A)
class _NsQosSysShapingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_D,0),(_E,1),(_F,2),(_G,3),('auto',4)))
_NsQosSysShapingMode_Type.__name__=_C
_NsQosSysShapingMode_Object=MibScalar
nsQosSysShapingMode=_NsQosSysShapingMode_Object((1,3,6,1,4,1,3224,5,2),_NsQosSysShapingMode_Type())
nsQosSysShapingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:nsQosSysShapingMode.setStatus(_A)
_NsQosPly_ObjectIdentity=ObjectIdentity
nsQosPly=_NsQosPly_ObjectIdentity((1,3,6,1,4,1,3224,5,3))
_NsQosPlyTable_Object=MibTable
nsQosPlyTable=_NsQosPlyTable_Object((1,3,6,1,4,1,3224,5,3,1))
if mibBuilder.loadTexts:nsQosPlyTable.setStatus(_A)
_NsQosPlyEntry_Object=MibTableRow
nsQosPlyEntry=_NsQosPlyEntry_Object((1,3,6,1,4,1,3224,5,3,1,1))
nsQosPlyEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:nsQosPlyEntry.setStatus(_A)
class _NsQosPlyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsQosPlyId_Type.__name__=_C
_NsQosPlyId_Object=MibTableColumn
nsQosPlyId=_NsQosPlyId_Object((1,3,6,1,4,1,3224,5,3,1,1,1),_NsQosPlyId_Type())
nsQosPlyId.setMaxAccess(_B)
if mibBuilder.loadTexts:nsQosPlyId.setStatus(_A)
_NsQosPlyVsys_Type=Integer32
_NsQosPlyVsys_Object=MibTableColumn
nsQosPlyVsys=_NsQosPlyVsys_Object((1,3,6,1,4,1,3224,5,3,1,1,2),_NsQosPlyVsys_Type())
nsQosPlyVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsQosPlyVsys.setStatus(_A)
class _NsQosPlyQosEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsQosPlyQosEnable_Type.__name__=_C
_NsQosPlyQosEnable_Object=MibTableColumn
nsQosPlyQosEnable=_NsQosPlyQosEnable_Object((1,3,6,1,4,1,3224,5,3,1,1,3),_NsQosPlyQosEnable_Type())
nsQosPlyQosEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:nsQosPlyQosEnable.setStatus(_A)
_NsQosPlyGanBW_Type=Integer32
_NsQosPlyGanBW_Object=MibTableColumn
nsQosPlyGanBW=_NsQosPlyGanBW_Object((1,3,6,1,4,1,3224,5,3,1,1,4),_NsQosPlyGanBW_Type())
nsQosPlyGanBW.setMaxAccess(_B)
if mibBuilder.loadTexts:nsQosPlyGanBW.setStatus(_A)
_NsQosPlyMaxBW_Type=Integer32
_NsQosPlyMaxBW_Object=MibTableColumn
nsQosPlyMaxBW=_NsQosPlyMaxBW_Object((1,3,6,1,4,1,3224,5,3,1,1,5),_NsQosPlyMaxBW_Type())
nsQosPlyMaxBW.setMaxAccess(_B)
if mibBuilder.loadTexts:nsQosPlyMaxBW.setStatus(_A)
_NsQosPlyTraffPriority_Type=Integer32
_NsQosPlyTraffPriority_Object=MibTableColumn
nsQosPlyTraffPriority=_NsQosPlyTraffPriority_Object((1,3,6,1,4,1,3224,5,3,1,1,6),_NsQosPlyTraffPriority_Type())
nsQosPlyTraffPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:nsQosPlyTraffPriority.setStatus(_A)
class _NsQosPlyDSEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsQosPlyDSEnable_Type.__name__=_C
_NsQosPlyDSEnable_Object=MibTableColumn
nsQosPlyDSEnable=_NsQosPlyDSEnable_Object((1,3,6,1,4,1,3224,5,3,1,1,7),_NsQosPlyDSEnable_Type())
nsQosPlyDSEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:nsQosPlyDSEnable.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'netscreenQosMibModule':netscreenQosMibModule,'nsQosUsrShapingMode':nsQosUsrShapingMode,'nsQosSysShapingMode':nsQosSysShapingMode,'nsQosPly':nsQosPly,'nsQosPlyTable':nsQosPlyTable,'nsQosPlyEntry':nsQosPlyEntry,_I:nsQosPlyId,'nsQosPlyVsys':nsQosPlyVsys,'nsQosPlyQosEnable':nsQosPlyQosEnable,'nsQosPlyGanBW':nsQosPlyGanBW,'nsQosPlyMaxBW':nsQosPlyMaxBW,'nsQosPlyTraffPriority':nsQosPlyTraffPriority,'nsQosPlyDSEnable':nsQosPlyDSEnable})