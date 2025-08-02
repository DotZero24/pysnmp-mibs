_L='a3ComMipSmdsGroupIpAddr'
_K='a3ComMipLocalGroupIpAddr'
_J='a3ComMipLocalGroupPort'
_I='a3ComMipPortIndex'
_H='disabled'
_G='enabled'
_F='OctetString'
_E='A3Com-Mip-r1-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class RowStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('active',1),('notInService',2),('notReady',3),('createAndGo',4),('createAndWait',5),('destroy',6)))
_A3Com_ObjectIdentity=ObjectIdentity
a3Com=_A3Com_ObjectIdentity((1,3,6,1,4,1,43))
_BrouterMIB_ObjectIdentity=ObjectIdentity
brouterMIB=_BrouterMIB_ObjectIdentity((1,3,6,1,4,1,43,2))
_A3ComMIP_ObjectIdentity=ObjectIdentity
a3ComMIP=_A3ComMIP_ObjectIdentity((1,3,6,1,4,1,43,2,27))
_A3ComMipSConfig_ObjectIdentity=ObjectIdentity
a3ComMipSConfig=_A3ComMipSConfig_ObjectIdentity((1,3,6,1,4,1,43,2,27,1))
class _A3ComMipControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_A3ComMipControl_Type.__name__=_B
_A3ComMipControl_Object=MibScalar
a3ComMipControl=_A3ComMipControl_Object((1,3,6,1,4,1,43,2,27,1,1),_A3ComMipControl_Type())
a3ComMipControl.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComMipControl.setStatus(_A)
_A3ComMipCConfig_ObjectIdentity=ObjectIdentity
a3ComMipCConfig=_A3ComMipCConfig_ObjectIdentity((1,3,6,1,4,1,43,2,27,2))
_A3ComMipPortTable_Object=MibTable
a3ComMipPortTable=_A3ComMipPortTable_Object((1,3,6,1,4,1,43,2,27,2,1))
if mibBuilder.loadTexts:a3ComMipPortTable.setStatus(_A)
_A3ComMipPortEntry_Object=MibTableRow
a3ComMipPortEntry=_A3ComMipPortEntry_Object((1,3,6,1,4,1,43,2,27,2,1,1))
a3ComMipPortEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:a3ComMipPortEntry.setStatus(_A)
_A3ComMipPortIndex_Type=Integer32
_A3ComMipPortIndex_Object=MibTableColumn
a3ComMipPortIndex=_A3ComMipPortIndex_Object((1,3,6,1,4,1,43,2,27,2,1,1,1),_A3ComMipPortIndex_Type())
a3ComMipPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComMipPortIndex.setStatus(_A)
class _A3ComMipPortQueryInterval_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,5400))
_A3ComMipPortQueryInterval_Type.__name__=_B
_A3ComMipPortQueryInterval_Object=MibTableColumn
a3ComMipPortQueryInterval=_A3ComMipPortQueryInterval_Object((1,3,6,1,4,1,43,2,27,2,1,1,2),_A3ComMipPortQueryInterval_Type())
a3ComMipPortQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComMipPortQueryInterval.setStatus(_A)
class _A3ComMipPortThreshold_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_A3ComMipPortThreshold_Type.__name__=_B
_A3ComMipPortThreshold_Object=MibTableColumn
a3ComMipPortThreshold=_A3ComMipPortThreshold_Object((1,3,6,1,4,1,43,2,27,2,1,1,3),_A3ComMipPortThreshold_Type())
a3ComMipPortThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComMipPortThreshold.setStatus(_A)
class _A3ComMipPortQuerier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_A3ComMipPortQuerier_Type.__name__=_B
_A3ComMipPortQuerier_Object=MibTableColumn
a3ComMipPortQuerier=_A3ComMipPortQuerier_Object((1,3,6,1,4,1,43,2,27,2,1,1,4),_A3ComMipPortQuerier_Type())
a3ComMipPortQuerier.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComMipPortQuerier.setStatus(_A)
class _A3ComMipPortPaceMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_A3ComMipPortPaceMode_Type.__name__=_B
_A3ComMipPortPaceMode_Object=MibTableColumn
a3ComMipPortPaceMode=_A3ComMipPortPaceMode_Object((1,3,6,1,4,1,43,2,27,2,1,1,5),_A3ComMipPortPaceMode_Type())
a3ComMipPortPaceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComMipPortPaceMode.setStatus(_A)
_A3ComMipLocalGroupTable_Object=MibTable
a3ComMipLocalGroupTable=_A3ComMipLocalGroupTable_Object((1,3,6,1,4,1,43,2,27,2,2))
if mibBuilder.loadTexts:a3ComMipLocalGroupTable.setStatus(_A)
_A3ComMipLocalGroupEntry_Object=MibTableRow
a3ComMipLocalGroupEntry=_A3ComMipLocalGroupEntry_Object((1,3,6,1,4,1,43,2,27,2,2,1))
a3ComMipLocalGroupEntry.setIndexNames((0,_E,_J),(0,_E,_K))
if mibBuilder.loadTexts:a3ComMipLocalGroupEntry.setStatus(_A)
_A3ComMipLocalGroupPort_Type=Integer32
_A3ComMipLocalGroupPort_Object=MibTableColumn
a3ComMipLocalGroupPort=_A3ComMipLocalGroupPort_Object((1,3,6,1,4,1,43,2,27,2,2,1,1),_A3ComMipLocalGroupPort_Type())
a3ComMipLocalGroupPort.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComMipLocalGroupPort.setStatus(_A)
_A3ComMipLocalGroupIpAddr_Type=IpAddress
_A3ComMipLocalGroupIpAddr_Object=MibTableColumn
a3ComMipLocalGroupIpAddr=_A3ComMipLocalGroupIpAddr_Object((1,3,6,1,4,1,43,2,27,2,2,1,2),_A3ComMipLocalGroupIpAddr_Type())
a3ComMipLocalGroupIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComMipLocalGroupIpAddr.setStatus(_A)
class _A3ComMipLocalGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('igmp',2)))
_A3ComMipLocalGroupType_Type.__name__=_B
_A3ComMipLocalGroupType_Object=MibTableColumn
a3ComMipLocalGroupType=_A3ComMipLocalGroupType_Object((1,3,6,1,4,1,43,2,27,2,2,1,3),_A3ComMipLocalGroupType_Type())
a3ComMipLocalGroupType.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComMipLocalGroupType.setStatus(_A)
_A3ComMipLocalGroupStatus_Type=RowStatus
_A3ComMipLocalGroupStatus_Object=MibTableColumn
a3ComMipLocalGroupStatus=_A3ComMipLocalGroupStatus_Object((1,3,6,1,4,1,43,2,27,2,2,1,4),_A3ComMipLocalGroupStatus_Type())
a3ComMipLocalGroupStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComMipLocalGroupStatus.setStatus(_A)
_A3ComMipSmdsGroupTable_Object=MibTable
a3ComMipSmdsGroupTable=_A3ComMipSmdsGroupTable_Object((1,3,6,1,4,1,43,2,27,2,3))
if mibBuilder.loadTexts:a3ComMipSmdsGroupTable.setStatus(_A)
_A3ComMipSmdsGroupEntry_Object=MibTableRow
a3ComMipSmdsGroupEntry=_A3ComMipSmdsGroupEntry_Object((1,3,6,1,4,1,43,2,27,2,3,1))
a3ComMipSmdsGroupEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:a3ComMipSmdsGroupEntry.setStatus(_A)
_A3ComMipSmdsGroupIpAddr_Type=IpAddress
_A3ComMipSmdsGroupIpAddr_Object=MibTableColumn
a3ComMipSmdsGroupIpAddr=_A3ComMipSmdsGroupIpAddr_Object((1,3,6,1,4,1,43,2,27,2,3,1,1),_A3ComMipSmdsGroupIpAddr_Type())
a3ComMipSmdsGroupIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:a3ComMipSmdsGroupIpAddr.setStatus(_A)
class _A3ComMipSmdsGroupMediaAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_A3ComMipSmdsGroupMediaAddr_Type.__name__=_F
_A3ComMipSmdsGroupMediaAddr_Object=MibTableColumn
a3ComMipSmdsGroupMediaAddr=_A3ComMipSmdsGroupMediaAddr_Object((1,3,6,1,4,1,43,2,27,2,3,1,2),_A3ComMipSmdsGroupMediaAddr_Type())
a3ComMipSmdsGroupMediaAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComMipSmdsGroupMediaAddr.setStatus(_A)
_A3ComMipSmdsGroupStatus_Type=RowStatus
_A3ComMipSmdsGroupStatus_Object=MibTableColumn
a3ComMipSmdsGroupStatus=_A3ComMipSmdsGroupStatus_Object((1,3,6,1,4,1,43,2,27,2,3,1,3),_A3ComMipSmdsGroupStatus_Type())
a3ComMipSmdsGroupStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:a3ComMipSmdsGroupStatus.setStatus(_A)
_A3ComMipData_ObjectIdentity=ObjectIdentity
a3ComMipData=_A3ComMipData_ObjectIdentity((1,3,6,1,4,1,43,2,27,3))
mibBuilder.exportSymbols(_E,**{'RowStatus':RowStatus,'a3Com':a3Com,'brouterMIB':brouterMIB,'a3ComMIP':a3ComMIP,'a3ComMipSConfig':a3ComMipSConfig,'a3ComMipControl':a3ComMipControl,'a3ComMipCConfig':a3ComMipCConfig,'a3ComMipPortTable':a3ComMipPortTable,'a3ComMipPortEntry':a3ComMipPortEntry,_I:a3ComMipPortIndex,'a3ComMipPortQueryInterval':a3ComMipPortQueryInterval,'a3ComMipPortThreshold':a3ComMipPortThreshold,'a3ComMipPortQuerier':a3ComMipPortQuerier,'a3ComMipPortPaceMode':a3ComMipPortPaceMode,'a3ComMipLocalGroupTable':a3ComMipLocalGroupTable,'a3ComMipLocalGroupEntry':a3ComMipLocalGroupEntry,_J:a3ComMipLocalGroupPort,_K:a3ComMipLocalGroupIpAddr,'a3ComMipLocalGroupType':a3ComMipLocalGroupType,'a3ComMipLocalGroupStatus':a3ComMipLocalGroupStatus,'a3ComMipSmdsGroupTable':a3ComMipSmdsGroupTable,'a3ComMipSmdsGroupEntry':a3ComMipSmdsGroupEntry,_L:a3ComMipSmdsGroupIpAddr,'a3ComMipSmdsGroupMediaAddr':a3ComMipSmdsGroupMediaAddr,'a3ComMipSmdsGroupStatus':a3ComMipSmdsGroupStatus,'a3ComMipData':a3ComMipData})