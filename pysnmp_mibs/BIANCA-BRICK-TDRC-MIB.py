_I='ipTdrcServiceIfIndex'
_H='delete'
_G='disabled'
_F='ipTdrcIfIndex'
_E='DisplayString'
_D='BIANCA-BRICK-TDRC-MIB'
_C='read-write'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bibo_ObjectIdentity=ObjectIdentity
bibo=_Bibo_ObjectIdentity((1,3,6,1,4,1,272,4))
_Biboip_ObjectIdentity=ObjectIdentity
biboip=_Biboip_ObjectIdentity((1,3,6,1,4,1,272,4,5))
_IpTdrcTable_Object=MibTable
ipTdrcTable=_IpTdrcTable_Object((1,3,6,1,4,1,272,4,5,43))
if mibBuilder.loadTexts:ipTdrcTable.setStatus(_A)
_IpTdrcEntry_Object=MibTableRow
ipTdrcEntry=_IpTdrcEntry_Object((1,3,6,1,4,1,272,4,5,43,1))
ipTdrcEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:ipTdrcEntry.setStatus(_A)
class _IpTdrcIfIndex_Type(Integer32):defaultValue=0
_IpTdrcIfIndex_Type.__name__=_B
_IpTdrcIfIndex_Object=MibTableColumn
ipTdrcIfIndex=_IpTdrcIfIndex_Object((1,3,6,1,4,1,272,4,5,43,1,1),_IpTdrcIfIndex_Type())
ipTdrcIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipTdrcIfIndex.setStatus(_A)
class _IpTdrcMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),('ack-prioritisation',2),('static',3),('dynamic',4),(_H,5)))
_IpTdrcMode_Type.__name__=_B
_IpTdrcMode_Object=MibTableColumn
ipTdrcMode=_IpTdrcMode_Object((1,3,6,1,4,1,272,4,5,43,1,2),_IpTdrcMode_Type())
ipTdrcMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ipTdrcMode.setStatus(_A)
class _IpTdrcMaxRate_Type(Integer32):defaultValue=1024000
_IpTdrcMaxRate_Type.__name__=_B
_IpTdrcMaxRate_Object=MibTableColumn
ipTdrcMaxRate=_IpTdrcMaxRate_Object((1,3,6,1,4,1,272,4,5,43,1,3),_IpTdrcMaxRate_Type())
ipTdrcMaxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ipTdrcMaxRate.setStatus(_A)
class _IpTdrcWindowScaling_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_IpTdrcWindowScaling_Type.__name__=_B
_IpTdrcWindowScaling_Object=MibTableColumn
ipTdrcWindowScaling=_IpTdrcWindowScaling_Object((1,3,6,1,4,1,272,4,5,43,1,4),_IpTdrcWindowScaling_Type())
ipTdrcWindowScaling.setMaxAccess(_C)
if mibBuilder.loadTexts:ipTdrcWindowScaling.setStatus(_A)
class _IpTdrcMss_Type(Integer32):defaultValue=1452;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4056))
_IpTdrcMss_Type.__name__=_B
_IpTdrcMss_Object=MibTableColumn
ipTdrcMss=_IpTdrcMss_Object((1,3,6,1,4,1,272,4,5,43,1,5),_IpTdrcMss_Type())
ipTdrcMss.setMaxAccess(_C)
if mibBuilder.loadTexts:ipTdrcMss.setStatus(_A)
class _IpTdrcServices_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('listed-only',1),('all',2)))
_IpTdrcServices_Type.__name__=_B
_IpTdrcServices_Object=MibTableColumn
ipTdrcServices=_IpTdrcServices_Object((1,3,6,1,4,1,272,4,5,43,1,6),_IpTdrcServices_Type())
ipTdrcServices.setMaxAccess(_C)
if mibBuilder.loadTexts:ipTdrcServices.setStatus(_A)
_IpTdrcServiceTable_Object=MibTable
ipTdrcServiceTable=_IpTdrcServiceTable_Object((1,3,6,1,4,1,272,4,5,44))
if mibBuilder.loadTexts:ipTdrcServiceTable.setStatus(_A)
_IpTdrcServiceEntry_Object=MibTableRow
ipTdrcServiceEntry=_IpTdrcServiceEntry_Object((1,3,6,1,4,1,272,4,5,44,1))
ipTdrcServiceEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:ipTdrcServiceEntry.setStatus(_A)
class _IpTdrcServiceIfIndex_Type(Integer32):defaultValue=0
_IpTdrcServiceIfIndex_Type.__name__=_B
_IpTdrcServiceIfIndex_Object=MibTableColumn
ipTdrcServiceIfIndex=_IpTdrcServiceIfIndex_Object((1,3,6,1,4,1,272,4,5,44,1,1),_IpTdrcServiceIfIndex_Type())
ipTdrcServiceIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipTdrcServiceIfIndex.setStatus(_A)
class _IpTdrcServicePort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpTdrcServicePort_Type.__name__=_B
_IpTdrcServicePort_Object=MibTableColumn
ipTdrcServicePort=_IpTdrcServicePort_Object((1,3,6,1,4,1,272,4,5,44,1,2),_IpTdrcServicePort_Type())
ipTdrcServicePort.setMaxAccess(_C)
if mibBuilder.loadTexts:ipTdrcServicePort.setStatus(_A)
class _IpTdrcServiceStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5)));namedValues=NamedValues(*(('enabled',1),(_G,2),(_H,5)))
_IpTdrcServiceStatus_Type.__name__=_B
_IpTdrcServiceStatus_Object=MibTableColumn
ipTdrcServiceStatus=_IpTdrcServiceStatus_Object((1,3,6,1,4,1,272,4,5,44,1,3),_IpTdrcServiceStatus_Type())
ipTdrcServiceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ipTdrcServiceStatus.setStatus(_A)
class _IpTdrcServiceAlias_Type(DisplayString):defaultValue=OctetString('')
_IpTdrcServiceAlias_Type.__name__=_E
_IpTdrcServiceAlias_Object=MibTableColumn
ipTdrcServiceAlias=_IpTdrcServiceAlias_Object((1,3,6,1,4,1,272,4,5,44,1,4),_IpTdrcServiceAlias_Type())
ipTdrcServiceAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:ipTdrcServiceAlias.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'bintec':bintec,'bibo':bibo,'biboip':biboip,'ipTdrcTable':ipTdrcTable,'ipTdrcEntry':ipTdrcEntry,_F:ipTdrcIfIndex,'ipTdrcMode':ipTdrcMode,'ipTdrcMaxRate':ipTdrcMaxRate,'ipTdrcWindowScaling':ipTdrcWindowScaling,'ipTdrcMss':ipTdrcMss,'ipTdrcServices':ipTdrcServices,'ipTdrcServiceTable':ipTdrcServiceTable,'ipTdrcServiceEntry':ipTdrcServiceEntry,_I:ipTdrcServiceIfIndex,'ipTdrcServicePort':ipTdrcServicePort,'ipTdrcServiceStatus':ipTdrcServiceStatus,'ipTdrcServiceAlias':ipTdrcServiceAlias})