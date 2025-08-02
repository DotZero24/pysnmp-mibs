_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hwSecSessStatMIB=ModuleIdentity((1,3,6,1,4,1,2011,6,122,69))
_Huawei_ObjectIdentity=ObjectIdentity
huawei=_Huawei_ObjectIdentity((1,3,6,1,4,1,2011))
_HuaweiUtility_ObjectIdentity=ObjectIdentity
huaweiUtility=_HuaweiUtility_ObjectIdentity((1,3,6,1,4,1,2011,6))
_HwSecurity_ObjectIdentity=ObjectIdentity
hwSecurity=_HwSecurity_ObjectIdentity((1,3,6,1,4,1,2011,6,122))
_HwSecSessStatTable_ObjectIdentity=ObjectIdentity
hwSecSessStatTable=_HwSecSessStatTable_ObjectIdentity((1,3,6,1,4,1,2011,6,122,69,1))
_HwSecSessStatEntry_ObjectIdentity=ObjectIdentity
hwSecSessStatEntry=_HwSecSessStatEntry_ObjectIdentity((1,3,6,1,4,1,2011,6,122,69,1,1))
_HwSecCurrSessThreshold_Type=Integer32
_HwSecCurrSessThreshold_Object=MibScalar
hwSecCurrSessThreshold=_HwSecCurrSessThreshold_Object((1,3,6,1,4,1,2011,6,122,69,1,1,1),_HwSecCurrSessThreshold_Type())
hwSecCurrSessThreshold.setMaxAccess(_A)
if mibBuilder.loadTexts:hwSecCurrSessThreshold.setStatus(_B)
_HwSecCurrSessNum_Type=Integer32
_HwSecCurrSessNum_Object=MibScalar
hwSecCurrSessNum=_HwSecCurrSessNum_Object((1,3,6,1,4,1,2011,6,122,69,1,1,2),_HwSecCurrSessNum_Type())
hwSecCurrSessNum.setMaxAccess(_A)
if mibBuilder.loadTexts:hwSecCurrSessNum.setStatus(_B)
_HwSecConSessThreshold_Type=Integer32
_HwSecConSessThreshold_Object=MibScalar
hwSecConSessThreshold=_HwSecConSessThreshold_Object((1,3,6,1,4,1,2011,6,122,69,1,1,3),_HwSecConSessThreshold_Type())
hwSecConSessThreshold.setMaxAccess(_A)
if mibBuilder.loadTexts:hwSecConSessThreshold.setStatus(_B)
_HwSecConSessNum_Type=Integer32
_HwSecConSessNum_Object=MibScalar
hwSecConSessNum=_HwSecConSessNum_Object((1,3,6,1,4,1,2011,6,122,69,1,1,4),_HwSecConSessNum_Type())
hwSecConSessNum.setMaxAccess(_A)
if mibBuilder.loadTexts:hwSecConSessNum.setStatus(_B)
mibBuilder.exportSymbols('HUAWEI-SECURITY-SESSION-STAT-MIB',**{'huawei':huawei,'huaweiUtility':huaweiUtility,'hwSecurity':hwSecurity,'hwSecSessStatMIB':hwSecSessStatMIB,'hwSecSessStatTable':hwSecSessStatTable,'hwSecSessStatEntry':hwSecSessStatEntry,'hwSecCurrSessThreshold':hwSecCurrSessThreshold,'hwSecCurrSessNum':hwSecCurrSessNum,'hwSecConSessThreshold':hwSecConSessThreshold,'hwSecConSessNum':hwSecConSessNum})