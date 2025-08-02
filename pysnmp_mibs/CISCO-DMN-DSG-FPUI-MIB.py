_C='current'
_B='read-write'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoDSGFPUI=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,24))
if mibBuilder.loadTexts:ciscoDSGFPUI.setRevisions(('2010-08-30 11:00','2010-03-22 05:00','2009-12-20 12:00'))
class _FpuiKBLock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_FpuiKBLock_Type.__name__=_A
_FpuiKBLock_Object=MibScalar
fpuiKBLock=_FpuiKBLock_Object((1,3,6,1,4,1,1429,2,2,5,24,1),_FpuiKBLock_Type())
fpuiKBLock.setMaxAccess(_B)
if mibBuilder.loadTexts:fpuiKBLock.setStatus(_C)
class _FpuiKBLockTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1800))
_FpuiKBLockTimeout_Type.__name__=_A
_FpuiKBLockTimeout_Object=MibScalar
fpuiKBLockTimeout=_FpuiKBLockTimeout_Object((1,3,6,1,4,1,1429,2,2,5,24,2),_FpuiKBLockTimeout_Type())
fpuiKBLockTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:fpuiKBLockTimeout.setStatus(_C)
class _FpuiLCDContrast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_FpuiLCDContrast_Type.__name__=_A
_FpuiLCDContrast_Object=MibScalar
fpuiLCDContrast=_FpuiLCDContrast_Object((1,3,6,1,4,1,1429,2,2,5,24,3),_FpuiLCDContrast_Type())
fpuiLCDContrast.setMaxAccess(_B)
if mibBuilder.loadTexts:fpuiLCDContrast.setStatus(_C)
class _FpuiAWReminder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_FpuiAWReminder_Type.__name__=_A
_FpuiAWReminder_Object=MibScalar
fpuiAWReminder=_FpuiAWReminder_Object((1,3,6,1,4,1,1429,2,2,5,24,4),_FpuiAWReminder_Type())
fpuiAWReminder.setMaxAccess(_B)
if mibBuilder.loadTexts:fpuiAWReminder.setStatus(_C)
mibBuilder.exportSymbols('CISCO-DMN-DSG-FPUI-MIB',**{'ciscoDSGFPUI':ciscoDSGFPUI,'fpuiKBLock':fpuiKBLock,'fpuiKBLockTimeout':fpuiKBLockTimeout,'fpuiLCDContrast':fpuiLCDContrast,'fpuiAWReminder':fpuiAWReminder})