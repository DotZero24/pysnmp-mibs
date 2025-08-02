_B='mandatory'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nmsEPONGroup,=mibBuilder.importSymbols('NMS-SMI','nmsEPONGroup')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_NmsEponOltMat_ObjectIdentity=ObjectIdentity
nmsEponOltMat=_NmsEponOltMat_ObjectIdentity((1,3,6,1,4,1,3320,101,200))
_OltFtpServerIpAddr_Type=IpAddress
_OltFtpServerIpAddr_Object=MibScalar
oltFtpServerIpAddr=_OltFtpServerIpAddr_Object((1,3,6,1,4,1,3320,101,200,1),_OltFtpServerIpAddr_Type())
oltFtpServerIpAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:oltFtpServerIpAddr.setStatus(_B)
_OltFtpServerPort_Type=Integer32
_OltFtpServerPort_Object=MibScalar
oltFtpServerPort=_OltFtpServerPort_Object((1,3,6,1,4,1,3320,101,200,2),_OltFtpServerPort_Type())
oltFtpServerPort.setMaxAccess(_A)
if mibBuilder.loadTexts:oltFtpServerPort.setStatus(_B)
_OltMatInsideIpAddr_Type=IpAddress
_OltMatInsideIpAddr_Object=MibScalar
oltMatInsideIpAddr=_OltMatInsideIpAddr_Object((1,3,6,1,4,1,3320,101,200,3),_OltMatInsideIpAddr_Type())
oltMatInsideIpAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:oltMatInsideIpAddr.setStatus(_B)
mibBuilder.exportSymbols('NMS-EPON-OLT-MAT-MIB',**{'nmsEponOltMat':nmsEponOltMat,'oltFtpServerIpAddr':oltFtpServerIpAddr,'oltFtpServerPort':oltFtpServerPort,'oltMatInsideIpAddr':oltMatInsideIpAddr})