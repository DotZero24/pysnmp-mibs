_G='NotificationType'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='DisplayString'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso,mgmt=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier',_G,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_G,'TimeTicks','Unsigned32','enterprises','iso','mgmt')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','RowStatus','TextualConvention')
class DisplayString(OctetString):0
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_Zxr10_ObjectIdentity=ObjectIdentity
zxr10=_Zxr10_ObjectIdentity((1,3,6,1,4,1,3902,3))
_Zxr10X25_ObjectIdentity=ObjectIdentity
zxr10X25=_Zxr10X25_ObjectIdentity((1,3,6,1,4,1,3902,3,4000))
_Zxr10X25OprTable_Object=MibTable
zxr10X25OprTable=_Zxr10X25OprTable_Object((1,3,6,1,4,1,3902,3,4000,1))
if mibBuilder.loadTexts:zxr10X25OprTable.setStatus(_A)
_Zxr10X25OprEntry_Object=MibTableRow
zxr10X25OprEntry=_Zxr10X25OprEntry_Object((1,3,6,1,4,1,3902,3,4000,1,1))
zxr10X25OprEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxr10X25OprEntry.setStatus(_A)
class _Zxr10X25OprXconnenctIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10X25OprXconnenctIfName_Type.__name__=_C
_Zxr10X25OprXconnenctIfName_Object=MibTableColumn
zxr10X25OprXconnenctIfName=_Zxr10X25OprXconnenctIfName_Object((1,3,6,1,4,1,3902,3,4000,1,1,1),_Zxr10X25OprXconnenctIfName_Type())
zxr10X25OprXconnenctIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25OprXconnenctIfName.setStatus(_A)
class _Zxr10X25OprLocalswitchIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Zxr10X25OprLocalswitchIfName_Type.__name__=_C
_Zxr10X25OprLocalswitchIfName_Object=MibTableColumn
zxr10X25OprLocalswitchIfName=_Zxr10X25OprLocalswitchIfName_Object((1,3,6,1,4,1,3902,3,4000,1,1,2),_Zxr10X25OprLocalswitchIfName_Type())
zxr10X25OprLocalswitchIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25OprLocalswitchIfName.setStatus(_A)
_Zxr10X25OprDLCI_Type=Integer32
_Zxr10X25OprDLCI_Object=MibTableColumn
zxr10X25OprDLCI=_Zxr10X25OprDLCI_Object((1,3,6,1,4,1,3902,3,4000,1,1,3),_Zxr10X25OprDLCI_Type())
zxr10X25OprDLCI.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25OprDLCI.setStatus(_A)
class _Zxr10X25OprType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('localswitch',1),('xconnect',2),('both',3)))
_Zxr10X25OprType_Type.__name__=_F
_Zxr10X25OprType_Object=MibTableColumn
zxr10X25OprType=_Zxr10X25OprType_Object((1,3,6,1,4,1,3902,3,4000,1,1,4),_Zxr10X25OprType_Type())
zxr10X25OprType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25OprType.setStatus(_A)
_Zxr10X25OprStatus_Type=RowStatus
_Zxr10X25OprStatus_Object=MibTableColumn
zxr10X25OprStatus=_Zxr10X25OprStatus_Object((1,3,6,1,4,1,3902,3,4000,1,1,5),_Zxr10X25OprStatus_Type())
zxr10X25OprStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10X25OprStatus.setStatus(_A)
mibBuilder.exportSymbols('ZXR10-X25-MIB',**{_C:DisplayString,'zte':zte,'zxr10':zxr10,'zxr10X25':zxr10X25,'zxr10X25OprTable':zxr10X25OprTable,'zxr10X25OprEntry':zxr10X25OprEntry,'zxr10X25OprXconnenctIfName':zxr10X25OprXconnenctIfName,'zxr10X25OprLocalswitchIfName':zxr10X25OprLocalswitchIfName,'zxr10X25OprDLCI':zxr10X25OprDLCI,'zxr10X25OprType':zxr10X25OprType,'zxr10X25OprStatus':zxr10X25OprStatus})