_G='hwSecDiskSN'
_F='hwSecDiskAscq'
_E='hwSecDiskAsc'
_D='hwSecDiskSlotNumber'
_C='accessible-for-notify'
_B='HUAWEI-SECURITY-DISK-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hwDiskMib=ModuleIdentity((1,3,6,1,4,1,2011,6,122,66))
if mibBuilder.loadTexts:hwDiskMib.setRevisions(('2013-12-19 09:00',))
_Huawei_ObjectIdentity=ObjectIdentity
huawei=_Huawei_ObjectIdentity((1,3,6,1,4,1,2011))
_HuaweiUtility_ObjectIdentity=ObjectIdentity
huaweiUtility=_HuaweiUtility_ObjectIdentity((1,3,6,1,4,1,2011,6))
_HwSecurity_ObjectIdentity=ObjectIdentity
hwSecurity=_HwSecurity_ObjectIdentity((1,3,6,1,4,1,2011,6,122))
_HwSecDiskMibNotification_ObjectIdentity=ObjectIdentity
hwSecDiskMibNotification=_HwSecDiskMibNotification_ObjectIdentity((1,3,6,1,4,1,2011,6,122,66,1))
_HwSecDiskMibTrapObject_ObjectIdentity=ObjectIdentity
hwSecDiskMibTrapObject=_HwSecDiskMibTrapObject_ObjectIdentity((1,3,6,1,4,1,2011,6,122,66,1,1))
_HwSecDiskSlotNumber_Type=Integer32
_HwSecDiskSlotNumber_Object=MibScalar
hwSecDiskSlotNumber=_HwSecDiskSlotNumber_Object((1,3,6,1,4,1,2011,6,122,66,1,1,1),_HwSecDiskSlotNumber_Type())
hwSecDiskSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSecDiskSlotNumber.setStatus(_A)
_HwSecDiskAsc_Type=Integer32
_HwSecDiskAsc_Object=MibScalar
hwSecDiskAsc=_HwSecDiskAsc_Object((1,3,6,1,4,1,2011,6,122,66,1,1,2),_HwSecDiskAsc_Type())
hwSecDiskAsc.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSecDiskAsc.setStatus(_A)
_HwSecDiskAscq_Type=Integer32
_HwSecDiskAscq_Object=MibScalar
hwSecDiskAscq=_HwSecDiskAscq_Object((1,3,6,1,4,1,2011,6,122,66,1,1,3),_HwSecDiskAscq_Type())
hwSecDiskAscq.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSecDiskAscq.setStatus(_A)
_HwSecDiskSN_Type=OctetString
_HwSecDiskSN_Object=MibScalar
hwSecDiskSN=_HwSecDiskSN_Object((1,3,6,1,4,1,2011,6,122,66,1,1,4),_HwSecDiskSN_Type())
hwSecDiskSN.setMaxAccess(_C)
if mibBuilder.loadTexts:hwSecDiskSN.setStatus(_A)
_HwSecDiskMibTraps_ObjectIdentity=ObjectIdentity
hwSecDiskMibTraps=_HwSecDiskMibTraps_ObjectIdentity((1,3,6,1,4,1,2011,6,122,66,1,2))
hwSecDiskPredictionError=NotificationType((1,3,6,1,4,1,2011,6,122,66,1,2,1))
hwSecDiskPredictionError.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:hwSecDiskPredictionError.setStatus(_A)
hwSecDiskOffline=NotificationType((1,3,6,1,4,1,2011,6,122,66,1,2,2))
hwSecDiskOffline.setObjects((_B,_D))
if mibBuilder.loadTexts:hwSecDiskOffline.setStatus(_A)
hwSecDiskOnline=NotificationType((1,3,6,1,4,1,2011,6,122,66,1,2,3))
hwSecDiskOnline.setObjects((_B,_D))
if mibBuilder.loadTexts:hwSecDiskOnline.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'huawei':huawei,'huaweiUtility':huaweiUtility,'hwSecurity':hwSecurity,'hwDiskMib':hwDiskMib,'hwSecDiskMibNotification':hwSecDiskMibNotification,'hwSecDiskMibTrapObject':hwSecDiskMibTrapObject,_D:hwSecDiskSlotNumber,_E:hwSecDiskAsc,_F:hwSecDiskAscq,_G:hwSecDiskSN,'hwSecDiskMibTraps':hwSecDiskMibTraps,'hwSecDiskPredictionError':hwSecDiskPredictionError,'hwSecDiskOffline':hwSecDiskOffline,'hwSecDiskOnline':hwSecDiskOnline})