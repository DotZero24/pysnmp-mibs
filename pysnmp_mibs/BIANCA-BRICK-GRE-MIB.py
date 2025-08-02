_F='greDstIpAddr'
_E='BIANCA-BRICK-GRE-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
_Bintec_ObjectIdentity=ObjectIdentity
bintec=_Bintec_ObjectIdentity((1,3,6,1,4,1,272))
_Bibo_ObjectIdentity=ObjectIdentity
bibo=_Bibo_ObjectIdentity((1,3,6,1,4,1,272,4))
_Vpn_ObjectIdentity=ObjectIdentity
vpn=_Vpn_ObjectIdentity((1,3,6,1,4,1,272,4,23))
_GreIfTable_Object=MibTable
greIfTable=_GreIfTable_Object((1,3,6,1,4,1,272,4,23,5))
if mibBuilder.loadTexts:greIfTable.setStatus(_A)
_GreIfEntry_Object=MibTableRow
greIfEntry=_GreIfEntry_Object((1,3,6,1,4,1,272,4,23,5,1))
greIfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:greIfEntry.setStatus(_A)
class _GreIfIndex_Type(Integer32):defaultValue=0
_GreIfIndex_Type.__name__=_C
_GreIfIndex_Object=MibTableColumn
greIfIndex=_GreIfIndex_Object((1,3,6,1,4,1,272,4,23,5,1,1),_GreIfIndex_Type())
greIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:greIfIndex.setStatus(_A)
class _GreIfDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_GreIfDescr_Type.__name__=_D
_GreIfDescr_Object=MibTableColumn
greIfDescr=_GreIfDescr_Object((1,3,6,1,4,1,272,4,23,5,1,2),_GreIfDescr_Type())
greIfDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:greIfDescr.setStatus(_A)
class _GreIfMtu_Type(Integer32):defaultValue=1500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8192))
_GreIfMtu_Type.__name__=_C
_GreIfMtu_Object=MibTableColumn
greIfMtu=_GreIfMtu_Object((1,3,6,1,4,1,272,4,23,5,1,3),_GreIfMtu_Type())
greIfMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:greIfMtu.setStatus(_A)
_GreDstIpAddr_Type=IpAddress
_GreDstIpAddr_Object=MibTableColumn
greDstIpAddr=_GreDstIpAddr_Object((1,3,6,1,4,1,272,4,23,5,1,4),_GreDstIpAddr_Type())
greDstIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:greDstIpAddr.setStatus(_A)
class _GreKey_Type(Integer32):defaultValue=0
_GreKey_Type.__name__=_C
_GreKey_Object=MibTableColumn
greKey=_GreKey_Object((1,3,6,1,4,1,272,4,23,5,1,5),_GreKey_Type())
greKey.setMaxAccess(_B)
if mibBuilder.loadTexts:greKey.setStatus(_A)
class _GreUseKey_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('delete',1),('yes',2),('no',3)))
_GreUseKey_Type.__name__=_C
_GreUseKey_Object=MibTableColumn
greUseKey=_GreUseKey_Object((1,3,6,1,4,1,272,4,23,5,1,6),_GreUseKey_Type())
greUseKey.setMaxAccess(_B)
if mibBuilder.loadTexts:greUseKey.setStatus(_A)
_GreSrcIpAddr_Type=IpAddress
_GreSrcIpAddr_Object=MibTableColumn
greSrcIpAddr=_GreSrcIpAddr_Object((1,3,6,1,4,1,272,4,23,5,1,7),_GreSrcIpAddr_Type())
greSrcIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:greSrcIpAddr.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'bintec':bintec,'bibo':bibo,'vpn':vpn,'greIfTable':greIfTable,'greIfEntry':greIfEntry,'greIfIndex':greIfIndex,'greIfDescr':greIfDescr,'greIfMtu':greIfMtu,_F:greDstIpAddr,'greKey':greKey,'greUseKey':greUseKey,'greSrcIpAddr':greSrcIpAddr})