_Q='qmGroup'
_P='qmHtbSystemDrop'
_O='qmHtbMaxQL'
_N='qmHtbCurrentQL'
_M='qmBytesDropped'
_L='qmBytes'
_K='qmPacketsDropped'
_J='qmPackets'
_I='qmCurPps'
_H='qmMaxPps'
_G='qmClass'
_F='qmPriority'
_E='qmChannel'
_D='Integer32'
_C='read-only'
_B='AQUAQM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wanflex,=mibBuilder.importSymbols('INFINET-MIB','wanflex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
aquaqmMIB=ModuleIdentity((1,3,6,1,4,1,3942,1,1,4))
if mibBuilder.loadTexts:aquaqmMIB.setRevisions(('2011-02-16 08:26','2007-11-08 12:55','2004-08-16 19:10'))
_QmTable_Object=MibTable
qmTable=_QmTable_Object((1,3,6,1,4,1,3942,1,1,4,1))
if mibBuilder.loadTexts:qmTable.setStatus(_A)
_QmEntry_Object=MibTableRow
qmEntry=_QmEntry_Object((1,3,6,1,4,1,3942,1,1,4,1,1))
qmEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:qmEntry.setStatus(_A)
class _QmChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_QmChannel_Type.__name__=_D
_QmChannel_Object=MibTableColumn
qmChannel=_QmChannel_Object((1,3,6,1,4,1,3942,1,1,4,1,1,1),_QmChannel_Type())
qmChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:qmChannel.setStatus(_A)
class _QmPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_QmPriority_Type.__name__=_D
_QmPriority_Object=MibTableColumn
qmPriority=_QmPriority_Object((1,3,6,1,4,1,3942,1,1,4,1,1,2),_QmPriority_Type())
qmPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:qmPriority.setStatus(_A)
class _QmClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_QmClass_Type.__name__=_D
_QmClass_Object=MibTableColumn
qmClass=_QmClass_Object((1,3,6,1,4,1,3942,1,1,4,1,1,3),_QmClass_Type())
qmClass.setMaxAccess(_C)
if mibBuilder.loadTexts:qmClass.setStatus(_A)
_QmTo_Type=IpAddress
_QmTo_Object=MibTableColumn
qmTo=_QmTo_Object((1,3,6,1,4,1,3942,1,1,4,1,1,4),_QmTo_Type())
qmTo.setMaxAccess(_C)
if mibBuilder.loadTexts:qmTo.setStatus(_A)
class _QmMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_QmMax_Type.__name__=_D
_QmMax_Object=MibTableColumn
qmMax=_QmMax_Object((1,3,6,1,4,1,3942,1,1,4,1,1,5),_QmMax_Type())
qmMax.setMaxAccess(_C)
if mibBuilder.loadTexts:qmMax.setStatus(_A)
class _QmMaxPps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_QmMaxPps_Type.__name__=_D
_QmMaxPps_Object=MibTableColumn
qmMaxPps=_QmMaxPps_Object((1,3,6,1,4,1,3942,1,1,4,1,1,6),_QmMaxPps_Type())
qmMaxPps.setMaxAccess(_C)
if mibBuilder.loadTexts:qmMaxPps.setStatus(_A)
_QmCur_Type=Integer32
_QmCur_Object=MibTableColumn
qmCur=_QmCur_Object((1,3,6,1,4,1,3942,1,1,4,1,1,7),_QmCur_Type())
qmCur.setMaxAccess(_C)
if mibBuilder.loadTexts:qmCur.setStatus(_A)
_QmCurPps_Type=Integer32
_QmCurPps_Object=MibTableColumn
qmCurPps=_QmCurPps_Object((1,3,6,1,4,1,3942,1,1,4,1,1,8),_QmCurPps_Type())
qmCurPps.setMaxAccess(_C)
if mibBuilder.loadTexts:qmCurPps.setStatus(_A)
_QmPackets_Type=Counter32
_QmPackets_Object=MibTableColumn
qmPackets=_QmPackets_Object((1,3,6,1,4,1,3942,1,1,4,1,1,9),_QmPackets_Type())
qmPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:qmPackets.setStatus(_A)
_QmPacketsDropped_Type=Counter32
_QmPacketsDropped_Object=MibTableColumn
qmPacketsDropped=_QmPacketsDropped_Object((1,3,6,1,4,1,3942,1,1,4,1,1,10),_QmPacketsDropped_Type())
qmPacketsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:qmPacketsDropped.setStatus(_A)
_QmBytes_Type=Counter32
_QmBytes_Object=MibTableColumn
qmBytes=_QmBytes_Object((1,3,6,1,4,1,3942,1,1,4,1,1,11),_QmBytes_Type())
qmBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:qmBytes.setStatus(_A)
_QmBytesDropped_Type=Counter32
_QmBytesDropped_Object=MibTableColumn
qmBytesDropped=_QmBytesDropped_Object((1,3,6,1,4,1,3942,1,1,4,1,1,12),_QmBytesDropped_Type())
qmBytesDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:qmBytesDropped.setStatus(_A)
_QmHTB_ObjectIdentity=ObjectIdentity
qmHTB=_QmHTB_ObjectIdentity((1,3,6,1,4,1,3942,1,1,4,2))
_QmHtbCurrentQL_Type=Gauge32
_QmHtbCurrentQL_Object=MibScalar
qmHtbCurrentQL=_QmHtbCurrentQL_Object((1,3,6,1,4,1,3942,1,1,4,2,1),_QmHtbCurrentQL_Type())
qmHtbCurrentQL.setMaxAccess(_C)
if mibBuilder.loadTexts:qmHtbCurrentQL.setStatus(_A)
_QmHtbMaxQL_Type=Gauge32
_QmHtbMaxQL_Object=MibScalar
qmHtbMaxQL=_QmHtbMaxQL_Object((1,3,6,1,4,1,3942,1,1,4,2,2),_QmHtbMaxQL_Type())
qmHtbMaxQL.setMaxAccess(_C)
if mibBuilder.loadTexts:qmHtbMaxQL.setStatus(_A)
_QmHtbSystemDrop_Type=Gauge32
_QmHtbSystemDrop_Object=MibScalar
qmHtbSystemDrop=_QmHtbSystemDrop_Object((1,3,6,1,4,1,3942,1,1,4,2,3),_QmHtbSystemDrop_Type())
qmHtbSystemDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:qmHtbSystemDrop.setStatus(_A)
_AquaqmMIBConformance_ObjectIdentity=ObjectIdentity
aquaqmMIBConformance=_AquaqmMIBConformance_ObjectIdentity((1,3,6,1,4,1,3942,1,1,4,3))
_AquaqmMIBCompliances_ObjectIdentity=ObjectIdentity
aquaqmMIBCompliances=_AquaqmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,3942,1,1,4,3,1))
_AquaqmMIBGroups_ObjectIdentity=ObjectIdentity
aquaqmMIBGroups=_AquaqmMIBGroups_ObjectIdentity((1,3,6,1,4,1,3942,1,1,4,3,2))
qmGroup=ObjectGroup((1,3,6,1,4,1,3942,1,1,4,3,2,1))
qmGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,'qmTo'),(_B,'qmMax'),(_B,_H),(_B,'qmCur'),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:qmGroup.setStatus(_A)
aquaqmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,3942,1,1,4,3,1,1))
aquaqmMIBCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:aquaqmMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'aquaqmMIB':aquaqmMIB,'qmTable':qmTable,'qmEntry':qmEntry,_E:qmChannel,_F:qmPriority,_G:qmClass,'qmTo':qmTo,'qmMax':qmMax,_H:qmMaxPps,'qmCur':qmCur,_I:qmCurPps,_J:qmPackets,_K:qmPacketsDropped,_L:qmBytes,_M:qmBytesDropped,'qmHTB':qmHTB,_N:qmHtbCurrentQL,_O:qmHtbMaxQL,_P:qmHtbSystemDrop,'aquaqmMIBConformance':aquaqmMIBConformance,'aquaqmMIBCompliances':aquaqmMIBCompliances,'aquaqmMIBCompliance':aquaqmMIBCompliance,'aquaqmMIBGroups':aquaqmMIBGroups,_Q:qmGroup})