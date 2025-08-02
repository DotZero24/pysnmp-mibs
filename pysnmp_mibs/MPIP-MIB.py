_I='read-only'
_H='mpIpTMask'
_G='mpIpTAddress'
_F='mpIpTIfName'
_E='DisplayString'
_D='not-accessible'
_C='Integer32'
_B='MPIP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,ObjectName,ObjectSyntax,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','ObjectName','ObjectSyntax','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_E,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
mpIpMib=ModuleIdentity((1,3,6,1,4,1,5651,3,700))
_MpIpTable_Object=MibTable
mpIpTable=_MpIpTable_Object((1,3,6,1,4,1,5651,3,700,1))
if mibBuilder.loadTexts:mpIpTable.setStatus(_A)
_MpIpEntry_Object=MibTableRow
mpIpEntry=_MpIpEntry_Object((1,3,6,1,4,1,5651,3,700,1,1))
mpIpEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:mpIpEntry.setStatus(_A)
class _MpIpTIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_MpIpTIfName_Type.__name__=_E
_MpIpTIfName_Object=MibTableColumn
mpIpTIfName=_MpIpTIfName_Object((1,3,6,1,4,1,5651,3,700,1,1,1),_MpIpTIfName_Type())
mpIpTIfName.setMaxAccess(_D)
if mibBuilder.loadTexts:mpIpTIfName.setStatus(_A)
_MpIpTAddress_Type=IpAddress
_MpIpTAddress_Object=MibTableColumn
mpIpTAddress=_MpIpTAddress_Object((1,3,6,1,4,1,5651,3,700,1,1,2),_MpIpTAddress_Type())
mpIpTAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:mpIpTAddress.setStatus(_A)
_MpIpTMask_Type=IpAddress
_MpIpTMask_Object=MibTableColumn
mpIpTMask=_MpIpTMask_Object((1,3,6,1,4,1,5651,3,700,1,1,3),_MpIpTMask_Type())
mpIpTMask.setMaxAccess(_D)
if mibBuilder.loadTexts:mpIpTMask.setStatus(_A)
_MpIpTBPAddress_Type=IpAddress
_MpIpTBPAddress_Object=MibTableColumn
mpIpTBPAddress=_MpIpTBPAddress_Object((1,3,6,1,4,1,5651,3,700,1,1,4),_MpIpTBPAddress_Type())
mpIpTBPAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:mpIpTBPAddress.setStatus(_A)
class _MpIpTType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('secondary',2)))
_MpIpTType_Type.__name__=_C
_MpIpTType_Object=MibTableColumn
mpIpTType=_MpIpTType_Object((1,3,6,1,4,1,5651,3,700,1,1,5),_MpIpTType_Type())
mpIpTType.setMaxAccess('read-write')
if mibBuilder.loadTexts:mpIpTType.setStatus(_A)
class _MpIpTWay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('manual',1),('dhcp',2),('negotiated',3),('unnumbered',4),('virtual',5)))
_MpIpTWay_Type.__name__=_C
_MpIpTWay_Object=MibTableColumn
mpIpTWay=_MpIpTWay_Object((1,3,6,1,4,1,5651,3,700,1,1,6),_MpIpTWay_Type())
mpIpTWay.setMaxAccess(_I)
if mibBuilder.loadTexts:mpIpTWay.setStatus(_A)
_MpIpTRowStatus_Type=RowStatus
_MpIpTRowStatus_Object=MibTableColumn
mpIpTRowStatus=_MpIpTRowStatus_Object((1,3,6,1,4,1,5651,3,700,1,1,7),_MpIpTRowStatus_Type())
mpIpTRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:mpIpTRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mpIpMib':mpIpMib,'mpIpTable':mpIpTable,'mpIpEntry':mpIpEntry,_F:mpIpTIfName,_G:mpIpTAddress,_H:mpIpTMask,'mpIpTBPAddress':mpIpTBPAddress,'mpIpTType':mpIpTType,'mpIpTWay':mpIpTWay,'mpIpTRowStatus':mpIpTRowStatus})