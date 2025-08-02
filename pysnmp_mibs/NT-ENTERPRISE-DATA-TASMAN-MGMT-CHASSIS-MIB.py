_C='current'
_B='read-only'
_A='DisplayString'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntEnterpriseDataTasmanMgmt,=mibBuilder.importSymbols('NT-ENTERPRISE-DATA-MIB','ntEnterpriseDataTasmanMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_A,'PhysAddress','TextualConvention')
nnchassisMib=ModuleIdentity((1,3,6,1,4,1,562,73,1,1,1,2))
if mibBuilder.loadTexts:nnchassisMib.setRevisions(('1999-07-01 00:00',))
class _NnchassisType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NnchassisType_Type.__name__=_A
_NnchassisType_Object=MibScalar
nnchassisType=_NnchassisType_Object((1,3,6,1,4,1,562,73,1,1,1,2,1),_NnchassisType_Type())
nnchassisType.setMaxAccess(_B)
if mibBuilder.loadTexts:nnchassisType.setStatus(_C)
class _NnchassisSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_NnchassisSerialNumber_Type.__name__=_A
_NnchassisSerialNumber_Object=MibScalar
nnchassisSerialNumber=_NnchassisSerialNumber_Object((1,3,6,1,4,1,562,73,1,1,1,2,2),_NnchassisSerialNumber_Type())
nnchassisSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nnchassisSerialNumber.setStatus(_C)
mibBuilder.exportSymbols('NT-ENTERPRISE-DATA-TASMAN-MGMT-CHASSIS-MIB',**{'nnchassisMib':nnchassisMib,'nnchassisType':nnchassisType,'nnchassisSerialNumber':nnchassisSerialNumber})