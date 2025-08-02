_I='hmITIpTMask'
_H='hmITIpTAddress'
_G='hmITIpTIfName'
_F='DisplayString'
_E='read-only'
_D='not-accessible'
_C='Integer32'
_B='HMIT-IP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmITMgmt,=mibBuilder.importSymbols('HMIT-SMI','hmITMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
hmITIpMib=ModuleIdentity((1,3,6,1,4,1,248,100,1,3,700))
if mibBuilder.loadTexts:hmITIpMib.setRevisions(('2010-01-08 17:00',))
_HmITIpTable_Object=MibTable
hmITIpTable=_HmITIpTable_Object((1,3,6,1,4,1,248,100,1,3,700,1))
if mibBuilder.loadTexts:hmITIpTable.setStatus(_A)
_HmITIpEntry_Object=MibTableRow
hmITIpEntry=_HmITIpEntry_Object((1,3,6,1,4,1,248,100,1,3,700,1,1))
hmITIpEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:hmITIpEntry.setStatus(_A)
class _HmITIpTIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_HmITIpTIfName_Type.__name__=_F
_HmITIpTIfName_Object=MibTableColumn
hmITIpTIfName=_HmITIpTIfName_Object((1,3,6,1,4,1,248,100,1,3,700,1,1,1),_HmITIpTIfName_Type())
hmITIpTIfName.setMaxAccess(_D)
if mibBuilder.loadTexts:hmITIpTIfName.setStatus(_A)
_HmITIpTAddress_Type=IpAddress
_HmITIpTAddress_Object=MibTableColumn
hmITIpTAddress=_HmITIpTAddress_Object((1,3,6,1,4,1,248,100,1,3,700,1,1,2),_HmITIpTAddress_Type())
hmITIpTAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hmITIpTAddress.setStatus(_A)
_HmITIpTMask_Type=IpAddress
_HmITIpTMask_Object=MibTableColumn
hmITIpTMask=_HmITIpTMask_Object((1,3,6,1,4,1,248,100,1,3,700,1,1,3),_HmITIpTMask_Type())
hmITIpTMask.setMaxAccess(_D)
if mibBuilder.loadTexts:hmITIpTMask.setStatus(_A)
_HmITIpTBPAddress_Type=IpAddress
_HmITIpTBPAddress_Object=MibTableColumn
hmITIpTBPAddress=_HmITIpTBPAddress_Object((1,3,6,1,4,1,248,100,1,3,700,1,1,4),_HmITIpTBPAddress_Type())
hmITIpTBPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hmITIpTBPAddress.setStatus(_A)
class _HmITIpTType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('secondary',2)))
_HmITIpTType_Type.__name__=_C
_HmITIpTType_Object=MibTableColumn
hmITIpTType=_HmITIpTType_Object((1,3,6,1,4,1,248,100,1,3,700,1,1,5),_HmITIpTType_Type())
hmITIpTType.setMaxAccess(_E)
if mibBuilder.loadTexts:hmITIpTType.setStatus(_A)
class _HmITIpTWay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('manual',1),('dhcp',2),('negotiated',3),('unnumbered',4),('virtual',5)))
_HmITIpTWay_Type.__name__=_C
_HmITIpTWay_Object=MibTableColumn
hmITIpTWay=_HmITIpTWay_Object((1,3,6,1,4,1,248,100,1,3,700,1,1,6),_HmITIpTWay_Type())
hmITIpTWay.setMaxAccess(_E)
if mibBuilder.loadTexts:hmITIpTWay.setStatus(_A)
_HmITIpTRowStatus_Type=RowStatus
_HmITIpTRowStatus_Object=MibTableColumn
hmITIpTRowStatus=_HmITIpTRowStatus_Object((1,3,6,1,4,1,248,100,1,3,700,1,1,7),_HmITIpTRowStatus_Type())
hmITIpTRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:hmITIpTRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hmITIpMib':hmITIpMib,'hmITIpTable':hmITIpTable,'hmITIpEntry':hmITIpEntry,_G:hmITIpTIfName,_H:hmITIpTAddress,_I:hmITIpTMask,'hmITIpTBPAddress':hmITIpTBPAddress,'hmITIpTType':hmITIpTType,'hmITIpTWay':hmITIpTWay,'hmITIpTRowStatus':hmITIpTRowStatus})